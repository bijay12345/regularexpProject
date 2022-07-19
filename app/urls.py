from django.urls import path
from .views import FileListView,fileUp,convertor,convert,regStore,RegDetail,RegListView


urlpatterns=[
	path('',FileListView.as_view(),name="home"),
	path('fileup/',fileUp,name="fileup"),
	path('convertor/',convertor,name="converter"),
	path('converted/',convert, name="convert"),
	path('regStore/',regStore,name="regexp"),
	path('reg/<int:pk>/',RegDetail.as_view(),name="regdetail"),
	path('reglist/',RegListView.as_view(),name="regList"),
]