# Traitement des données de type CSV
# Nathan BIZON
# Le 14/03/2022

import csv
import os

def import_data(): # importe les données depuis les fichiers CSV | Crée par Nathan
    out = [] # on crée la liste qui contiendra toutes les valeurs
    for i in range(4,11): # pour chaque fichiers csv
        path = f'niveausonore/data/Releve_Per0{i}.csv' # path prend la valeur du chemin du fichier
        with open(path,'r',encoding='utf-8-sig') as f: # on ouvre le fichier
            out.append(list(csv.DictReader(f,delimiter=';'))) # on met les valeurs dans la liste
    return out # on retourne la liste de listes sous la forme [[{},{}],[{},{}]]

def format_data(D): # les valeurs sont de type str et on veut les convertir en int D = la liste de import_data(), on veut aussi empêcher les valeurs vides | Crée par Nathan
    out = [] # on crée la nouvelle liste
    for i in D: # pour chaque liste de liste
        for j in i: # pour chaque liste
            if j['Valeur minimale'] == '' or j['Valeur maximale'] == '' or j['Valeur moyenne'] == '': # s'il n'y a pas toutes les valeurs demandées
                pass # alors on ne l'insert pas dans la liste
            else:
                j['Valeur minimale'] = int(j['Valeur minimale']) # sinon on convertit les valeurs str en valeur int
                j['Valeur moyenne'] = int(j['Valeur moyenne'])
                j['Valeur maximale'] = int(j['Valeur maximale'])
                j['Id'] = int(j['Id'])
                out.append(j) # et on met chaque dictionnaire dans une liste
    return out # on retourne une liste de dictionnaire. La nouvelle liste est donc plus facile à traiter

def search_data(place,ctx,day): #fct
    D = format_data(import_data())
    moymin,moymoy,moymax,eff,maxtemp=0,0,0,0,0 #Initialisation des variables
    mintemp=999 #Initialisation d'une variable pour avoir le minimum temporaire
    med,fati,dang=[],[],[] #Initialisation de listes
    for x in D: #recherche dans le data
         if x["Lieu"]==place: #correspondance avec le lieu
             if x["Conditions "]==ctx: #correspondance avec la condition
                 if x["Jour"]==day: #correspondance avec le jour
                     moymin,moymoy,moymax=moymin+x["Valeur minimale"],moymoy+x["Valeur moyenne"],moymax+x["Valeur maximale"] #accumulation des valeurs dans les moyennes
                     eff+=1 #compteur d'effectif
                     if mintemp>x["Valeur minimale"]:
                         mintemp=x["Valeur minimale"] #calcul de la valeur minimale
                     med.append(x["Valeur minimale"]),med.append(x["Valeur moyenne"]),med.append(x["Valeur maximale"]),med.sort() #Création d'un tableau de toutes les valeurs puis trié
                     if maxtemp<x["Valeur maximale"]:
                         maxtemp=x["Valeur maximale"] #calcul de la valeur maximale
                     fati.append([med[i] for i in range(len(med)) if med[i]>=80 and med[i]<=90]) #Création d'un tableau de valeurs au dessus de 80
                     dang.append([med[i] for i in range(len(med)) if med[i]>=90]) #Création d'un tableau de valeurs au dessus de 90
    if eff != 0:
        out = {
            "moymin":round(moymin/eff,1),
            "moymoy":round(moymoy/eff,1),
            "moymax":round(moymax/eff,1),
            "mintemp":mintemp,
            "med":med[int((len(med)/2)-1)],
            "maxtemp":maxtemp,
            "p_fatiguant":round((len(fati[-1])*100)/(len(med)),1),
            "p_dangereux":round((len(dang[-1])*100)/(len(med)),1)
            }
    else:
        r = 'Pas de valeurs disponibles'
        out = {
        "moymin":r,
        "moymoy":r,
        "moymax":r,
        "mintemp":r,
        "med":r,
        "maxtemp":r,
        "p_fatiguant":r,
        "p_dangereux":r
        }
    return out #Arrondi à 10^-1 de la moyenne des valeurs minimales,Arrondi à 10^-1 de la moyenne des valeurs moyennes,Arrondi à 10^-1 de la moyenne des valeurs maximales,Renvoi de la valeur minimale,Renvoi de la valeur médiane, Renvoi de la valeur maximale,Arrondi à 10^-1 de la proportion de valeurs au dessus de 80,Arrondi à 10^-1 de la proportion de valeurs au dessus de 90
