# views.py
# gestion des requêtes HTTP
# seule la première fonction sera expliqué car toutes ont la même structure

from django.shortcuts import render
from .td import *

# partie traitement des données


# partie requêtes

def index(request):
    return render(request, "index.html")

def cour_prem_arbre(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']): # la requête est de type GET et a des éléments ?
        cdt = request.GET['condition'] # prendre le contenu de la variable condition
        day = request.GET['jour'] # prendre le conenu de la variable jour
        ctx = search_data("La cour des premières près des arbres",cdt,day) # on cherche les données dans les fichiers csv
        return render(request,'cour_prem_arbre.html',context=ctx) # on retourne la page avec le dictionnaire. Dans les pages HTML elles sont indiqué entre deux acolades
    return render(request,'cour_prem_arbre.html') # s'il n'y a pas d'éléments alors on affiche juste la page

def cour_prem_casier(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La cour des premières près des casiers",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'cour_prem_casier.html',context=ctx)
    return render(request,'cour_prem_casier.html')

def espace_fumeur(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("L'espace \"fumeurs\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'espace_fumeur.html',context=ctx)
    return render(request,'espace_fumeur.html')

def toilettes_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Les toilettes des premières",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'toilettes_prem.html',context=ctx)
    return render(request,'toilettes_prem.html')

def salle_cours(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Une salle de cours",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'salle_cours.html',context=ctx)
    return render(request,'salle_cours.html')

def chapelle(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle de devoirs \"La chapelle\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'chapelle.html',context=ctx)
    return render(request,'chapelle.html')

def salle_devoir_t(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle de devoirs \"T301\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'salle_devoir_t.html',context=ctx)
    return render(request,'salle_devoir_t.html')

def salle_devoir_p(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle de devoirs \"P302\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'salle_devoir_p.html',context=ctx)
    return render(request,'salle_devoir_p.html')

def couloir_prem(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Un couloir du batiment 1ères",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'couloir_prem.html',context=ctx)
    return render(request,'couloir_prem.html')

def couloir_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Un couloir du batiment 2ndes",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'couloir_sd.html',context=ctx)
    return render(request,'couloir_sd.html')

def couloir_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Un couloir du batiment terminales",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'couloir_ter.html',context=ctx)
    return render(request,'couloir_ter.html')

def foyer(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le foyer",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'foyer.html',context=ctx)
    return render(request,'foyer.html')

def cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le CDI",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'cdi.html',context=ctx)
    return render(request,'cdi.html')

def rest_cdi(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Dans la file d'attente pour la restauration près du CDI",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'rest_cdi.html',context=ctx)
    return render(request,'rest_cdi.html')

def rest_aquarium(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Dans la file d'attente pour la restauration \"Aquarium\"",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'rest_aquarium.html',context=ctx)
    return render(request,'rest_aquarium.html')

def refectoire(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le réfectoire des élèves",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'refectoire.html',context=ctx)
    return render(request,'refectoire.html')

def sport(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le complexe sportif",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'sport.html',context=ctx)
    return render(request,'sport.html')

def cour_sd(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La cour des secondes ",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'cour_sd.html',context=ctx)
    return render(request,'cour_sd.html')

def preau_ter(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Sous le préau de la cour des terminales",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'preau_ter.html',context=ctx)
    return render(request,'preau_ter.html')

def ref_prof(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("Le réfectoire des professeurs batiment P",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'ref_prof.html',context=ctx)
    return render(request,'ref_prof.html')

def sdp_pc(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle des profs (coins ordinateurs ) batiment L",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'sdp_pc.html',context=ctx)
    return render(request,'sdp_pc.html')

def sdp_distrib(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle des profs (coin distributeur) batiment L",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'sdp_distrib.html',context=ctx)
    return render(request,'sdp_distrib.html')

def sdp_ref(request):
    if request.method == 'GET' and all(q in request.GET for q in ['condition','jour']):
        cdt = request.GET['condition']
        day = request.GET['jour']
        mini,moy,maxi = search_data("La salle des profs (réfectoire) batiment L",cdt,day)
        ctx = {'mini':mini,'moy':moy,'maxi':maxi}
        return render(request,'sdp_ref.html',context=ctx)
    return render(request,'sdp_ref.html')
