from django.shortcuts import render
Public_url="http://127.0.0.1:8000/"
# Create your views here.
def homepage(request):
    return render(request,template_name="index.html",context={"url":Public_url})