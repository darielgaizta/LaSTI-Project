from django.shortcuts import render

# Create your views here.
def sync_session(request):
	return render(request, 'index.html')

def watch_stream(request):
	return render(request, 'stream.html')