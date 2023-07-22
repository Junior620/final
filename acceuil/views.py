from django.shortcuts import render
from .models import AcceuilContact


# Create your views here.
def acceuil(request):
    if request.method == "POST":
        nom = request.POST.get('nom', '')
        email = request.POST.get('email', '')
        telephone = request.POST.get('telephone', '')
        detail = request.POST.get('detail', '')
        myclient = AcceuilContact.objects.create(nom=nom, email=email, telephone=telephone, detail=detail)
        myclient.save()
    return render(request, 'index.html')


#def error_404(request, exception):
 #   return render(request, '404.html')
