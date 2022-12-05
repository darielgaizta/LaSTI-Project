from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Comment

# Create your views here.
def sync_session(request):
	return render(request, 'index.html')

def watch_stream(request):
	return render(request, 'stream.html')

def submit_comment(request):
	username = request.POST['username']
	text = request.POST['text']
	new_comment = Comment.objects.create(username=username, text=text)
	new_message.save()
	return HttpResponse('Message is sent successfully.')

def get_comments(request):
	comments = Comment.objects.all()
	return JsonResponse({
			"messages": list(comments.values())
		})