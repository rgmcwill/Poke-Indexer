from django.urls import path

from . import views

urlpatterns = [
	path('',views.CurrentRanking,name='TeamStatistics'),
	path('TeamStatistics',views.TeamStatistics,name='TeamStatistics'),
]
