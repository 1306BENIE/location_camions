from django.shortcuts import render, redirect
from .models import Camion, Client, Location
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, "location/home.html")

def camion_list(request):
    camions = Camion.objects.all()
    return render(request, 'location/camion_list.html', context={'camions': camions})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'location/client_list.html', context={'clients': clients})

def louer_camion(request, camion_id):
    camion = Camion.objects.get(id=camion_id)
    if request.method == 'POST':
        client_id = request.POST.get('client')
        if client_id:
            try:
                date_debut = request.POST.get('date_debut')
                date_fin = request.POST.get('date_fin')
                client = Client.objects.get(id=client_id)
                location = Location(camion=camion, client=client, date_debut=date_debut, date_fin=date_fin)
                location.save()
                camion.disponible = False
                camion.save()
                
                subject = 'Confirmation de location de camion'
                message = 'Votre location de camion a été confirmée.'
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [client.email]  # Remplacez par l'adresse e-mail du client
                send_mail(subject, message, from_email, to_email)
        
                return redirect('camion_list')
            except Client.DoesNotExist:
                return f"{client} n'existe pas"  
    else:
        clients = Client.objects.all()
        return render(request, 'location/louer_camion.html', context={'camion': camion, 'clients': clients})