import os
from django.db import models
from django.contrib.auth.models import User
import uuid



def user_directory_path(instance, filename):
    # Generate a unique id for the image
    unique_id = uuid.uuid4().hex
    # Get the file extension
    ext = filename.split('.')[-1]
    # Prefix the filename with the unique id and save it in the 'instances' folder
    filename = f'{instance.name}_{unique_id}.{ext}'
    return os.path.join('instances', filename)


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=1000000)
    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Annotator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    # images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.user.username


class MyAnnotator(models.Model):
    annotator = models.ManyToManyField(Annotator, related_name='my_annotators')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Annotation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    annotator = models.ForeignKey(Annotator, on_delete=models.SET_NULL, null=True)
    annotation = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.annotation


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000000000, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    annotators = models.ManyToManyField(Annotator, blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(Image, blank=True)
    
    def __str__(self):
        return self.title


