from django.db import models

# Create your models here.
from django.forms import ModelForm


class Profile(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=50)

    def save_Profile(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

    class Meta:
        ordering = ['name']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
