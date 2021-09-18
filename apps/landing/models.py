from django.db import models
from apps.api.models import User


class Scheme(models.Model):
    """
    Contains Portfolio projects
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='schemes'
    )
    title = models.CharField(
        max_length=255, verbose_name='title'
    )
    image = models.ImageField(
        upload_to="img", null=True
    )
    client = models.ForeignKey(
       'Client', on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField(
        auto_now=True, verbose_name='date'
    )
    skills = models.CharField(
        max_length=255, verbose_name='skills'
    )
    link = models.URLField(
        max_length=255, verbose_name='link'
    )
    comment = models.CharField(
        max_length=255, verbose_name='comment'
    )
    
    class Meta:
        verbose_name = 'Scheme'
        verbose_name_plural = "Scheme's"

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Contains users callback requests
    """
    name = models.CharField(
        max_length=255, verbose_name='name'
    )
    email = models.EmailField(
        max_length=255, verbose_name='email'
    )
    comment = models.CharField(
        max_length=255, verbose_name='comment'
    )

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contact's"

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    User profile
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    image = models.ImageField(
        upload_to='img'
    )
    facebook = models.URLField(
        max_length=255, verbose_name='facebook', null=True, blank=True
    )
    twitter = models.URLField(
        max_length=255, verbose_name='twitter', null=True, blank=True
    )
    linkedin = models.URLField(
        max_length=255, verbose_name='linkedin', null=True, blank=True
    )
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = "Profile's"

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clients', null=True, blank=True
    )
    name = models.CharField(
        max_length=255, verbose_name='client name'
    )
    image = models.ImageField(
        upload_to='img', null=True, blank=True
    )
    comment = models.CharField(
        max_length=255, verbose_name="client's comment"
    )
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = "Client's"

    def __str__(self):
        return self.name
