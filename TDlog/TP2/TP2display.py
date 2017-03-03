# -*- coding: utf-8 -*-
"""
ce programme permet de réaliser l'affichage de l'interface graphique
"""
#ce TP a été réalisé en binôme à partir du code de Clément HARDY 
#par Cément HARDY et Adrien Decottignies


from TP2interaction import *


class CheckBox(QtGui.QWidget):
    
    def __init__(self,test = False):
        super().__init__()  
        self.init_CheckBox()
        self.test = test
       
    def init_CheckBox(self):      

        self.p1 = QtGui.QCheckBox('one player', self)
        self.p1.move(100, 20)        
        self.p1.stateChanged.connect(self.nb_players)
        self.p2 = QtGui.QCheckBox('two players', self)
        self.p2.move(100, 50)
        self.p2.stateChanged.connect(self.nb_players)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Players')
        self.show()
        
    def nb_players(self, state):
        source=self.sender()
      
        if state == QtCore.Qt.Checked: #l'état est 0 ou 2
            if source == self.p1:
                self.choice = 1
            else :
                self.choice = 2
            self.next_step = True
            self.close()
            self.menu = Menu(self.choice,self.test)



class Menu(QtGui.QWidget):
    
    def __init__(self,nb_players,test):
        super().__init__()  
        self.nb_players = nb_players
        self.test = test
        self.length =''
        self.level =''
        self.name1 = ''
        self.name2 = ''
        self.init_Menu()
        
        
    def init_Menu(self): 
        
        self.btn1 = QtGui.QPushButton('name', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.enter_name1)
        
        
        self.btn2 = QtGui.QPushButton('length', self)
        self.btn2.move(20, 80)
        self.btn2.clicked.connect(self.enter_length)
        
        
        if self.nb_players == 1 :          
            self.btn3 = QtGui.QPushButton('level', self)
            self.btn3.move(20, 50)
            self.btn3.clicked.connect(self.enter_level)
            
        else :
            self.btn0 = QtGui.QPushButton('name', self)
            self.btn0.move(20, 50)
            self.btn0.clicked.connect(self.enter_name2)
            
        
        self.btn4 = QtGui.QPushButton('PLAY', self)
        self.btn4.move(100, 110)
        self.btn4.clicked.connect(self.btn_close)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Menu - Jeu des pièces')
        self.show()
        
    
    def enter_name1(self):   
        text, ok = QtGui.QInputDialog.getText(self, 'name', 
            'Enter your name:')     
        if ok:
            self.name1 = str(text)
    def enter_name2(self):   
        text, ok = QtGui.QInputDialog.getText(self, 'name', 
            'Enter your name:')     
        if ok:
            self.name2 = str(text)
    def enter_length(self):    
        text, ok = QtGui.QInputDialog.getText(self, 'length', 
            'Enter the size of the grid:')       
        if ok:
            self.length = str(text)
    def enter_level(self):    
        text, ok = QtGui.QInputDialog.getText(self, 'level', 
            'Enter a level:')       
        if ok:
            self.level = str(text)
    def btn_close(self): 
        self.close()     
        try :
            if (self.nb_players == 2):
                game = Game(self.test,int(self.length),\
                self.name1,self.name2)
            else :
                game = Game_VS_Computer(int(self.level),\
                self.test,int(self.length),self.name1)
        except even_size:
            print("length must be an odd number")
            checkBox = CheckBox()
        except :
            print("try again")
            checkBox = CheckBox()
        
        if not self.test:
            game.fill_grid()
        self.windowGame = WindowGame(game)
        


def main():
    app = QtGui.QApplication(sys.argv)  
    checkBox = CheckBox()
    sys.exit(app.exec_())

main()   


