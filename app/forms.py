from django import forms
from .models import UploadFiles,XmlToDict,RegStore


class FileForm(forms.ModelForm):
	class Meta:
		model=UploadFiles
		fields=['title','description','category','file']

class XmlForm(forms.ModelForm):
	class Meta:
		model=XmlToDict
		fields=['xmlFile']
		
class RegStoreForm(forms.ModelForm):
	class Meta:
		model=RegStore
		fields=['title','expression']