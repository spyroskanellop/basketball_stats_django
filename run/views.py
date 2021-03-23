from django.http import HttpResponse


# Create your views here.
def about(request):
    return HttpResponse("Hello, world. You're at the about page.")


def home(request):
    return HttpResponse('Hello from home')
