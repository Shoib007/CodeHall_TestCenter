from django.contrib import admin
from .models import TestCenter, Registration
# Register your models here.
admin.site.register([TestCenter, Registration])