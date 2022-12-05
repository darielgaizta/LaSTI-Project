from django.urls import path
from . import views

urlpatterns = [
	path('sync-session/', views.sync_session, name='sync_session'),
	path('sync-session/stream/', views.watch_stream, name='watch_stream'),
	path('sync-session/stream/comments/', views.get_comments, name='get_comments'),
	path('sync-session/stream/comments/submit/', views.submit_comment, name='submit_comment'),
]