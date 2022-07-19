from django.contrib import admin
from .models import UploadFiles,XmlToDict,RegStore

admin.site.register(UploadFiles)
admin.site.register(RegStore)
admin.site.register(XmlToDict)