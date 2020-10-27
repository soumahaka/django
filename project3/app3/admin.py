from django.contrib import admin
from app3.models import AccessRecord, Topic,Webpage, User

# Register your models here.

""" Ici on enregistre les differentes tables creees dans 
le fichier model.py en administration"""
admin.site.register(AccessRecord) 
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)

