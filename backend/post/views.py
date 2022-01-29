from django.http import HttpResponse


def home(request):
    return HttpResponse(f'<h1>Home page</h1>')
