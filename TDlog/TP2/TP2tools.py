# -*- coding: utf-8 -*-
"""
Ce fichier comprend un certain nombre d'outils utiles
à la création du jeu
"""
# cette fonction permet de transformer des lignes de nombres
#séparés par des virgules en un tableau

def from_csv_to_tab(path):
   tab=[]
   with open(path) as file:
       for line in file:
           tmp=[]
           number=''
           for char in line:
               if char != ',':                 
                   number = number + char
               else:                
                   tmp.append(int(number))
                   number=''
           tmp.append(int(number))
           tab.append(tmp)
   return tab
     
            
            



class Grid:
    def __init__(self,test,length):
        if not test :
            self._length=length
            self._tab=[[None for i in range(self.length)] for j in range(self.length)]
        else :
            self._tab = from_csv_to_tab(input("path : "))
            self._length=len(self._tab)
        if self._length % 2 ==0:
                raise even_size
    def __contains__(self, coords):
        return not(coords.x >= self._length or coords.y >= self._length\
        or coords.x<0 or coords.y<0)
    
    def __getitem__(self,coords):
        assert(coords in self)
        return self._tab[coords.x][coords.y]
    
    def __setitem__(self,coords,value):
        assert(coords in self)
        self._tab[coords.x][coords.y]=value
    
        
    @property
    def length(self):
        return self._length


class even_size(Exception):
    pass


class Coords:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def translate(self, dx, dy):
        self._x += dx
        self._y += dy
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x=value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        self._y=value
    
        

class Player:
    def __init__(self,name,score=0):
        self._name = name
        self._score = score
    @property
    def name(self):
        return (self._name)
    @property
    def score(self):
        return self._score

    
    def increment(self,n):
        self._score += n
        

        
        
        