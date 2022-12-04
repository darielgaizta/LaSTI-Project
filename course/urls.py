from django.urls import path
from . import views

urlpatterns = [
	path('sync-session/', views.sync_session, name='sync_session'),
]