from django.shortcuts import render,redirect
from .forms import FileForm,XmlForm,RegStoreForm
from django.contrib import messages
from .models import UploadFiles,XmlToDict,StoreJson,RegStore
from django.views.generic import ListView,DetailView
import json
import xmltodict 
from django.http import HttpResponse
import os


class FileListView(ListView):
	model=UploadFiles
	template_name="app/home.html"
	context_object_name="files"


def fileUp(request):
	if request.method=="POST":
		form=FileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"File Uploaded")
			return redirect('/')
	else:
		form=FileForm()
	return render(request,"app/fileup.html",{"form":form})


def convertor(request):
	if request.method=="POST":
		file=XmlForm(request.POST,request.FILES)
		if file.is_valid():
			file.save()
			messages.info(request,"The file is converted successfully.")
			return redirect('convert')
		else:
			messages.warning(request,"Please enter the specified format only.")
	else:
		file=XmlForm()
	return render(request,'app/jsonupload.html',{'form':file})

def convert(request):
	files= XmlToDict.objects.all()
	file=files[0].xmlFile.path

	with open(file,'r') as xmlFile:
		dictData=xmltodict.parse(xmlFile.read())
		jsonData=json.dumps(dictData,sort_keys=True, indent=4)
		return HttpResponse(jsonData)

		
def regStore(request):
	if request.method=="POST":
		form=RegStoreForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"your expressions are saved successfully...")
			return redirect('/')
	else:
		form=RegStoreForm()
	return render(request,'app/regstore.html',{"form":form})

class RegListView(ListView):
	model=RegStore
	context_object_name="regs"  

class RegDetail(DetailView):
	model=RegStore