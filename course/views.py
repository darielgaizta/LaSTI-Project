from django.shortcuts import render

# Create your views here.
def sync_session(request):
	return render(request, 'index.html')