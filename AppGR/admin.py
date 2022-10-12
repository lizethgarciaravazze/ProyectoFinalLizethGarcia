from os import access
from django.contrib import admin
from AppGR.models import Sombras, Base, Brochas, Avatar
# Register your models here.

admin.site.register(Sombras)
admin.site.register(Base)
admin.site.register(Brochas)
admin.site.register(Avatar)