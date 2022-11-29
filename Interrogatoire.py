
import sys
import os
from os import path

chemin_fichier='./mots.txt'
lines=[]
print(f"Controle surprise....avec le fichier {chemin_fichier}")
try:
    if(os.path.exists(chemin_fichier)):
        f=open(chemin_fichier,'r')
        
        lines = f.readlines() 
     
        f.close()
    else:
        print(f"Fichier {chemin_fichier} non trouvé")
except Exception as e:
    print("problème de lecture")
    print(e)

dictionnaire=[]
for mot in lines:
    dictionnaire.append(mot.strip())
    
dictionnaire_pourri=dict()
for mot in dictionnaire:
    print(mot)
    mot_temp=mot.replace('au','o')
    mot_temp=mot_temp.replace('ant','ent')

    dictionnaire_pourri[mot]=mot_temp

for mot in dictionnaire_pourri:
    print(f"{mot} {dictionnaire_pourri[mot]}")
