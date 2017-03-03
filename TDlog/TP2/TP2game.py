# -*- coding: utf-8 -*-
"""
Ce programme comprend deux classes dont l'une hérite de l'autre
L'une permet de jouer à 2
l'autre permet de jouer contre un ordinateur
"""

import random as rd 
from TP2tools import *

moves={"7":(-1,-1),"8":(-1,0),"9":(-1,1),"4":(0,-1),"6":(0,1),"1":(1,-1),"2":(1,0),"3":(1,1)}

infini = float('inf')

class Game:
    def __init__(self,test,length,name1,name2):
        self.grid=Grid(test,length)
        self.player_1=Player(name1)
        self.player_2=Player(name2)
        self.turn=self.player_1
        self.position=Coords(self.grid.length//2,self.grid.length//2)
        self.test=test
        
    def end_game(self):
        var = True
        count = 1
        while count < 10 and var:
            if count != 5:
                coords=Coords(self.position.x+moves.get(str(count))[0],\
                self.position.y+moves.get(str(count))[1])
                if ((coords in self.grid) and (self.grid[coords] != 0)):
                    var=False       
            count+=1
        return var
        
        
    def fill_grid(self):
        coins=[5,10,20,50,100,200]
        if not self.test :
            for i in range (self.grid.length):
                for j in range(self.grid.length):
                    if not(i==self.position.x and j==self.position.y):
                        self.grid[Coords(i,j)]=coins[rd.randint(0,5)]
                    else :
                        self.grid[Coords(i,j)]=0

    def changeTurn(self):
        if (self.turn == self.player_1):
            self.turn = self.player_2
        else :
            self.turn = self.player_1
        
        
        
    def winner(self):
        if (self.player_2.score == self.player_1.score):
            print("equality") 
        else:
            print("winner : ",end='')
            if (self.player_1.score > self.player_2.score):
                print(str(self.player_1.name))
            else :
                print(str(self.player_2.name))
            
    
    def display(self):
        for i in range(self.grid.length):
            for j in range(self.grid.length):
                if self.position.x == i and self.position.y == j:
                    print('###','   ',end='')
                else:
                    print(" "* (3-len(str(self.grid[Coords(i,j)]))),end='')
                    print(self.grid[Coords(i,j)],'   ',end='')
            print('')

# cette méthode permet de jouer un coup                      
    def play(self,coords):
        
        var = False # permet de savoir si le coup choisi a pu être joué
        if ((coords in self.grid) and (self.grid[coords] != 0))\
        and (abs(coords.x-self.position.x) <=1)\
        and (abs(coords.y-self.position.y) <=1):
            var = True
            lastPosition = Coords(self.position.x, self.position.y)
            self.turn.increment(self.grid[coords])
            self.grid[coords] = 0       
            self.position.x = coords.x
            self.position.y = coords.y
        else :
            print("wrong direction")
            lastPosition = Coords(self.position.x,self.position.y)
        return var,lastPosition           
            

class Game_VS_Computer(Game):
    def __init__(self,level,test,length,name):
       self.player_1 = Player(name) 
       self.player_2 = Player('computer')
       self.grid = Grid(test,length)
       self.turn=self.player_1
       self.position = Coords(self.grid.length//2,self.grid.length//2)
       self.level = level
       self.test = test
       
#cette fonction permet de jouer un coup    
    def play(self,positionClicked):
        if self.turn == self.player_1 :
            var,lastPosition = super().play(positionClicked)     
        else: 
            choice=self.min_max(self.level,True)[1]
            lastPosition = Coords(self.position.x,self.position.y)
            self.position.translate(moves.get(choice)[0],moves.get(choice)[1])
            self.player_2.increment(self.grid[self.position])
            self.grid[self.position] = 0
            var = True
        return var,lastPosition

#la fonction d'évaluation prend en compte l'écart entre les scores
    def evaluation(self):
        return self.player_2.score-self.player_1.score


    def min_max(self,level,is_max):
        choice = -1
        if self.end_game() or level <= 0:
            return self.evaluation(),choice
        else :
            if is_max:
                val=-infini
                player = self.player_2
            else :
                val = infini
                player = self.player_1
            for direction in moves :
                self.position.translate(moves.get(direction)[0],\
                moves.get(direction)[1])
                if self.position in self.grid and self.grid[self.position] != 0:
                    tmp = self.grid[self.position]                       
                    player.increment(tmp)
                    self.grid[self.position] = 0
                    tmp2 = self.min_max(level-1,not is_max)[0]                      
                    if ((tmp2 > val) and is_max) or ((tmp2 < val) and  not is_max):
                        val = tmp2
                        choice=direction                  
                    player.increment(-tmp)
                    self.grid[self.position] = tmp
                self.position.translate(-moves.get(direction)[0],\
                -moves.get(direction)[1])       
            return val,choice
            
        



