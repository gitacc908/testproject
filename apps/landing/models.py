from django.db import models


class Scheme(models.Model):
    """
    Contains Portfolio projects
    """
    title = models.CharField(
        max_length=255, verbose_name='title'
    )
    client = models.CharField(
        max_length=255, verbose_name='client'
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
