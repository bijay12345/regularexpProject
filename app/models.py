from django.db import models
from django.core.validators import FileExtensionValidator
import re  
from regex_field.fields import RegexField


FILE_CHOICES=(
	('pd','pdf'),
	('jp', 'jpg'),
	('xm', 'xml'), 
	('js', 'json')
	)
class UploadFiles(models.Model):
	title=models.CharField(max_length=200)
	description=models.CharField(max_length=300)
	category=models.CharField(max_length=2,choices=FILE_CHOICES)
	file=models.FileField(upload_to='webfiles/',validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg','xml','json'])])
	def __str__(self):
		return self.title

class XmlToDict(models.Model):
	title=models.CharField(max_length=100)
	xmlFile=models.FileField(upload_to='xmlFiles/',validators=[FileExtensionValidator(allowed_extensions=['xml'])])
	date_added=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=('-date_added',)

	def __str__(self):
		return self.title

class StoreJson(models.Model):
	file=models.FileField(upload_to='jsonReady/')


class RegStore(models.Model):
	title=models.CharField(max_length=200)
	expression=RegexField(max_length=120,re_flags=re.IGNORECASE)
	date_created=models.DateTimeField(auto_now_add=True)


