import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from random import randint


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    user_id = instance.user.id
    directory_path = os.path.join('user_{}'.format(user_id), 'instances', filename)
    full_path = os.path.join(settings.STATIC_ROOT, directory_path)

    # Create the directory if it doesn't exist
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return directory_path


class Annotator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=5000, blank=True, null=True)
    custom_anotator_id = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        while True:
            if not self.custom_anotator_id:
                self.custom_anotator_id = randint(100000, 999999)
            try:
                Annotator.objects.get(custom_anotator_id=self.custom_anotator_id)
                # unique code already exists, generate a new one
                self.custom_anotator_id = randint(100000, 999999)
            except Annotator.DoesNotExist:
                # unique code doesn't exist, save the object
                super().save(*args, **kwargs)
                break


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=1000000, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Annotations(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    annotator = models.ForeignKey(Annotator, on_delete=models.SET_NULL, null=True)
    annotation = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000000000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    annotators = models.ManyToManyField(Annotator, blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(Image, blank=True)
    project_code = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        while True:
            if not self.project_code:
                self.project_code = randint(100000, 999999)
            try:
                Project.objects.get(project_code=self.project_code)
                # unique code already exists, generate a new one
                self.project_code = randint(100000, 999999)
            except Project.DoesNotExist:
                # unique code doesn't exist, save the object
                super().save(*args, **kwargs)
                break

