from django.contrib import admin
from .models import (
    Contact, Scheme, Client
)

admin.site.register(Contact)
admin.site.register(Scheme)
admin.site.register(Client)
