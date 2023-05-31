from LabeLiT import info
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.contrib import messages
from django.core.mail import send_mail
from .tokens import generate_token
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile




def signup(request):
    context = {}
    if request.method == "POST":
        full_name = request.POST['full_name']
        name_parts = full_name.split()
        first_name = name_parts[0] if len(name_parts) > 0 else full_name
        try:
            last_name = name_parts[1]
        except IndexError:
            last_name = ""
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered! Please sign in.')
            return redirect('signin')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already in use!')
            return redirect('signin')
        
        if len(username) >20:
            messages.error(request, "Username must be less than 20 character")
            return render(request, 'signup.html')

        # if username.isalnum():
        #     messages.error(request, 'Username should not contain special characters!')
        #     return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, "Passwords does not match")
            return render(request, 'signup.html')
        
        # Image Upload and Resize
        if request.FILES:
            profile_picture = request.FILES['profile_picture']
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)
            uploaded_file_url = fs.url(filename)
            img = Image.open(profile_picture)
            img.thumbnail((500, 500))
            img.save(fs.path(filename))

        else:
            uploaded_file_url = None

        user = User.objects.create_user(username=username, email=email, password=password1)

        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        user.profile_picture = uploaded_file_url  # save uploaded file url to user's profile_picture field
        user.save()

        messages.success(request, "Account has been successfully created! We have sent you an email confirmation letter. confirm your email address to activate your account.")

        # Welcome Email

        subject = "Welcome to LabeLiT"
        message = f"Hello {full_name}! \n\nWe are pleased to welcome you as part of us. \nCongratulations on your way to being part of this great innovation.\n\nRegards\LabeLit Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)


        # Email verification and account activation

        current_site = info.CURRENT_SITE
        email_subject = "Email Address Verification"
        message2 = render_to_string(
            "emailing/email_verification.html",
            {
                "name": full_name,
                "domain": current_site,
                "site_protocol": settings.SITE_PROTOCOL,
                "userId": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": generate_token.make_token(user),
            }
        )

        # prepare verification email

        send_email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        # send_email.fail_silently = True
        send_email.send()

        return redirect("signin")
    return render(request, "signup.html", context)


def activate(request, userIdb64, token):
    try:
        userId = force_str(urlsafe_base64_decode(userIdb64))
        user = User.objects.get(pk=userId)
        
    except(ValueError, TypeError,OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, "Your Emmail address has being successfully verified.")
        return redirect("creators-dashboard")
    else:
        return render(request, "emailing/email_activation_failed.html")


def signin(request):
    context = {}
    if request.method == "POST":
        username_or_email = request.POST["username_or_email"]
        password_ = request.POST["password"]

        if request.user.is_authenticated:
            if request.user.email==username_or_email or request.user.email==username_or_email:
                return redirect('creators-dashboard')

        user = authenticate(email=username_or_email, password=password_)
        if user is not None:
            login(request, user)
            return redirect('creators-dashboard')
        else:
            user = authenticate(username=username_or_email, password=password_)
            if user is not None:
                login(request, user)
            return redirect('creators-dashboard')
            messages.error(request, "Invalid Credentials")
    return render(request, "signin.html", context)


def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('index')


def index(request):
    context = {}
    return render(request, "index.html", context)


def creatorsDashboard(request):
    context = {}
    annotator = request.user.annotator
    
    annotating = Project.objects.filter(annotators=annotator)
    my_projects = Project.objects.filter(creator=request.user).order_by('-created_date')
    projects = Project.objects.filter(creator=request.user)
    my_images = Image.objects.filter(uploaded_by=request.user)
    context['my_images'] = my_images
    # context['annotators_of_last_project'] = annotators_of_last_project
    context['annotating'] = annotating
    context['my_projects'] = my_projects
    context['my_annotators'] = Annotator.objects.filter(project__creator=request.user).distinct()
    return render(request, 'creator-dashboard.html', context)


def creatorsProjects(request):
    context = {}

    if request.method=="POST":
        project_title = request.POST['title']
        project_description = request.POST['description']
        Project.objects.create(creator=request.user, title=project_title, description=project_description)
    
    my_projects = Project.objects.filter(creator=request.user)
    context['my_projects'] = my_projects
    return render(request, 'creator-projects.html', context)



def projectPage(request, slug):
    project = get_object_or_404(Project, pk=slug)
    project_annotators = project.annotators.all()
    context = {}
    context['project'] = project
    context['project_annotators'] = project_annotators
    return render(request, 'creator-project-page.html', context)



def creatorsAnnotators(request):
    context = {}
    projects = Project.objects.filter(creator=request.user)

    annotators = []

    # Loop through each project to get its annotators
    for project in projects:
        # Get the annotators of the project and add them to the list of annotators
        project_annotators = project.annotators.all()
        annotators += list(project_annotators)

    # Remove duplicates from the list of annotators
    annotators = list(set(annotators))
    context["my_annotators"] = annotators
    return render(request, 'creator-annotators.html', context)


def annotatorLabeling(request):
    context = {}
    my_annotators = ""
    return render(request, 'annotator-labeling-page.html', context)


def annotatorDashboard(request):
    context = {}
    return render(request, 'annotator-dashboard.html', context)







def annotatorsProjects(request):
    context = {}
    return render(request, 'annotator-projects.html', context)


def annotatingPage(request, slug):
    context = {}
    return render(request, 'annotator-labeling-page.html', context)

