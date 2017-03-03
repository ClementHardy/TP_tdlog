# -*- coding: utf-8 -*-
"""
Ce programme permet l'intéraction avec le jeu
"""
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from TP2game import *


class Button(QtGui.QPushButton) :
    def __init__(self,text,coords):
        super().__init__(text)
        self.coords = coords

def addButton(window,coords,text):
    button = Button(text,coords)
    window.addWidget(button,button.coords.x,button.coords.y)    

class WindowGame(QtGui.QWidget):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.positionClicked = None
        self.source = None      
        self.windowGame = QtGui.QGridLayout()
        self.init_WindowGame()
       
        
    def init_WindowGame(self):       
        
        self.setLayout(self.windowGame)   
        for i in range(self.game.grid.length):
            for j in range(self.game.grid.length) :
                button = Button(str(self.game.grid[Coords(i,j)]),Coords(i,j))
                self.windowGame.addWidget(button,button.coords.x\
                ,button.coords.y)       
                button.setCheckable(True)
                button.clicked[bool].connect(self.buttonClicked)
        
        self.setWindowTitle('Jeu des pièces')        
        self.show()
    def play(self):
        if self.game.player_2.name == 'computer':
            var, lastPosition = self.game.play(self.positionClicked)
            if var :
                addButton(self.windowGame,lastPosition,'0')
                addButton(self.windowGame,self.game.position,'king')
                self.game.changeTurn()
                if not self.game.end_game():
                    lastPosition = self.game.play(self.positionClicked)[1]
                    addButton(self.windowGame,lastPosition,'0')
                    addButton(self.windowGame,self.game.position,'king')
                    self.game.changeTurn()
                
        else :
            var, lastPosition = self.game.play(self.positionClicked)
            if var :
                addButton(self.windowGame,lastPosition,'0')
                addButton(self.windowGame,self.game.position,'king')
                self.game.changeTurn()
        
   
    def buttonClicked(self,pressed):      
        self.source = self.sender()
        if pressed:
            self.source.toggle() #permet de changer l'état du bouton
            self.positionClicked = self.source.coords #attention l'axe des x n'est pas l'axe habituel
            if not(self.game.end_game()):
                self.play()
                addButton(self.windowGame,Coords(10,self.game.grid.length + 10)\
                ,str(self.game.player_1.name)+'  '+str(self.game.player_1.score))
                addButton(self.windowGame,Coords(50,self.game.grid.length + 10)\
                ,str(self.game.player_2.name)+'  '+str(self.game.player_2.score))
            else:
                self.game.winner()
            
    


