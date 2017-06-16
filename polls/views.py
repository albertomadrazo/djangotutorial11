from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello fucks, you're about to be polled out.")