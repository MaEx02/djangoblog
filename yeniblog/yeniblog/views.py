from django.shortcuts import render
from django.shortcuts import render

def gonderi_listesi(request):
    return render(request, 'blog/gonderi_listesi.html', {})
# Create your views here.
