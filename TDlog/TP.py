# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:52:26 2016

@author: Asus
"""

import data
import operator

#cette fonction retourne la taille du mot le plus long 
#cette fonction permet d'aligner les points à droite
def longueur_max(tab,indice):
    maxi=0
    for k in range(len(tab)):
        if len(tab[k][indice])>maxi:
            maxi=len(tab[k][indice])

    return(maxi)
        
    
    
    

    
    
    
def classement(groupe):
    score=[]
    for equipe in data.groups.get(str(groupe)):
        temp=[equipe,0,0]#comptabilise les points pour une équipe et le goal average
        for match in data.matches:
            if (equipe==match[0]):
                if match[1]>match[2]:
                    temp[1]+=2
                if match[1]==match[2]:
                    temp[1]+=1
                temp[2]=match[1]-match[2]
            if (equipe==match[3]):
                if match[2]>match[1]:
                    temp[1]+=2
                if match[1]==match[2]:
                    temp[1]+=1
                temp[2]=match[2]-match[1]
        score.append(temp)
    return score
#cette fonction permet de trier le tableau score
    #obtenu à l'aide de classement en prenant en compte le goal average
def trier(tab):
    n=len(tab)
    for k in range (n):
        min=k
        for j in range(k+1,n):
            if tab[min][1]>tab[j][1]:
                min=j
            else:
                if tab[min][1]==tab[j][1] and tab[min][2]>tab[j][2]:
                    min=j
                    
        a=tab[k]
        tab[k]=tab[min]
        tab[min]=a




# la fonction suivante doit trier le tableau avant de l'afficher
def affichage_classement(classement):
    trier(classement)
    longueur=longueur_max(classement,0)
    
    classement.reverse()
    for k in range(len(classement)):
        print(str(classement[k][0]),end='')
        for i in range(longueur-len(classement[k][0])):
            print(".",end='')
        print("....",str(classement[k][1]),"pts",str(classement[k][2]))
        
    return ''
            


def affichage_match_joue(groupe):
    tab=[]
    for match in data.matches:
        tab.append([match[0],match[1],match[2],match[3]])
        
        longueur=longueur_max(tab,0)
    for k in range(len(tab)):
        if tab[k][0] in data.groups.get(str(groupe)):
            print(str(tab[k][0]),end='')
            for i in range(longueur-len(tab[k][0])):
                print(" ",end='')
            print(tab[k][1],'-',tab[k][2],tab[k][3])
    return ''
          

def prochains_matchs(groupe):
    tab=[]# ce tableau permet de savoir quelles équipes ont déjà été visitées
    jouer=[]
    # cette partie du programme permet de mettre dans le tableau match
    #les match à jouer
    for equipe1 in data.groups.get(str(groupe)):
        tab.append([equipe1])
        
        for equipe2 in data.groups.get(str(groupe)):
            var = True
            for match in data.matches:
                if (match[0]==equipe1 or match[3]==equipe1)and(match[0]==equipe2 or match[3]==equipe2):
                    var=False
            if var:
            #cette boucle permet d'éviter les doublons
            #on élimine les équipes déjà visitées
                var2=True
                for k in range(len(tab)):
                    if (tab[k]==[str(equipe2)]):
                        var2=False
                        
                if var2:
                    jouer.append([equipe1,equipe2])
    #cette partie permet d'afficher les matchs à jouer
    longueur=longueur_max(jouer,0)
    for k in range(len(jouer)):
        print(jouer[k][0],'',end='')
        for i in range(longueur-len(jouer[k][0])):
            print(" ",end='')
        print('VS',' ',jouer[k][1])
    return ''
    
 
      
            
def affichage_complet():
    print('Group1')
    print('-------')
    print(affichage_classement(classement(1)))
    print(affichage_match_joue(1))
    print(prochains_matchs(1))
    print('Group2')
    print('-------')
    print(affichage_classement(classement(2)))
    print(affichage_match_joue(2))
    print(prochains_matchs(2))
    return ''
    

print(affichage_complet())
      
                
                

                
            
        
    
    
                
                
        
    
    











