from django.urls import path
from . import views

urlpatterns = [
	path('sync-session/', views.sync_session, name='sync_session'),
	path('sync-session/stream/', views.watch_stream, name='watch_stream'),
]