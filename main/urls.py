from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='DBLookup'),
	path('DBLookup',views.DBLookup,name='DBLookup'),
	path('DBClear',views.clear,name='clear'),
]
