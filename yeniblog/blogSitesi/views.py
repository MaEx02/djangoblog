from django.shortcuts import render
from django.utils import timezone
from  .models import Gonderi

def gonderi_listesi(request):
    gonderiler=Gonderi.objects.filter(y_tarihi__lte=timezone.now()).order_by('y_tarihi')
    return render(request, 'blog/gonderi_listesi.html', {'gonderiler':gonderiler})
def gonderi_getir(request,pk):
    gonderi=Gonderi.objects.get(id=pk)

    context = {'gonderi':gonderi}
    return render(request,'blog/generic.html',context)
def anasayfa(request):
    return render(request,'blog/index.html')