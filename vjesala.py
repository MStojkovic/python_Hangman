# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:24:42 2018

@author: Igor
"""

from tkinter import *
from functools import partial
import random
import time

class App:
    def __init__(self, master):
        self.frame = Frame(master, bg="gold", height = 50, width = 200)
        self.frame.pack()
        self.menu()
        
    def menu(self):
        photo = PhotoImage(file = "Uvod.gif")
        self.photoLabel = Label(self.frame, image = photo)
        self.photoLabel.image = photo
        self.photoLabel.grid(row = 0)
        
        self.newGame = Button(self.frame, text = "New Game", borderwidth = 1, width = 50, bg = "yellow", command =self.game)
        self.newGame.grid(row = 1)
        
        self.exitButton = Button(self.frame, text = "Exit", borderwidth = 1, width = 50, bg = "yellow", command = self.frame.quit)
        self.exitButton.grid(row = 2)
        
    def loadWords(self):
        file = open('parole.txt', 'r')
        rows = file.readlines()
        file.close()
        
        self.words = []
        
        for row in rows:
                self.words.append(row.strip('\n'))
                
    def loadImages(self):
        self.ImageList = []
        self.ImageList.append(PhotoImage(file = "Pocetna.gif"))
        self.ImageList.append(PhotoImage(file = "Prva.gif"))
        self.ImageList.append(PhotoImage(file = "Druga.gif"))
        self.ImageList.append(PhotoImage(file = "Treca.gif"))
        self.ImageList.append(PhotoImage(file = "Cetvrta.gif"))
        self.ImageList.append(PhotoImage(file = "Peta.gif"))
        self.ImageList.append(PhotoImage(file = "Sesta.gif"))
        self.ImageList.append(PhotoImage(file = "Kraj.gif"))
        
    def generateLetters(self):
        
        self.lblList = []
        
        for i in range (97, 123):
            label = Label (self.frame, text = chr(i), height = 1, width = 1, bg = "yellow", anchor = "center", borderwidth = "1")
            self.lblList.append(label)
            
    def getRandomInt(self, number):
        return (random.randint(0, number))
    
    def validateInputLetter(self, letter):
        hits = []
        counter = 0
        for c in self.word:
            if (c == letter):
                self.inputWord[counter] = letter
                hits.append(counter)
            counter += 1
        if (len(hits) > 0):
            return 0
        else:
            return 1
        
    def configureGrid(self):
        self.inputLabel = Label(self.frame, text = "".join(self.inputWord), height = 2, width = 50, bg = "yellow", anchor = "center")
        self.inputLabel.grid(row = 0, column = 1, columnspan = 6, sticky = 'se')
        
        self.errLabel = Label(self.frame, image = self.ImageList[0])
        self.errLabel.image = self.ImageList[0]
        self.errLabel.grid(row = 0, rowspan = 6, column = 0)
        
        self.exitGame = Button(self.frame, bg = "yellow", text = "Exit game", anchor = "center", width = 10, height = 1, command = self.exitGame)
        self.exitGame.grid(row = 9, columnspan = 7, sticky = 'se')

        self.entry = Entry(self.frame, bg = "yellow")
        self.entry.grid(row = 1, column = 1, columnspan = 6)
        
        self.enterButton = Button (self.frame, text = "ENTER", bg = "yellow", height = 1, width = 10, anchor = "center", command = self.onClick)
        self.enterButton.grid(row = 2, column = 1, columnspan = 6)
        #self.entry.insert(0,'Please insert a letter')
                
        lblRow = 3
        lblColumn = 1
        
        for lbl in self.lblList:
            lbl.grid(row = lblRow, column = lblColumn)
            lblColumn += 1
            if (lblColumn == 7):
                lblRow += 1
                lblColumn = 1
                
    def onClick(self):
        self.wait.set(1)
        
    def game(self):
        
        self.loadWords()
        self.loadImages()
        self.generateLetters()
        
        self.photoLabel.grid_remove()
        self.newGame.grid_remove()
        self.exitButton.grid_remove()
        
        self.usedLetters = []
        self.word = self.words[self.getRandomInt(len(self.words))]
        print(self.word)
        self.inputWord = []
        for i in range(len(self.word)):
            self.inputWord.append('_')
            
        self.configureGrid()
        self.wait = IntVar()
        self.wait.set(0)
        validateInput = 0
        errNumber = 0
        #print ('1')
        while errNumber < 7:
            validateInput = 1
            getErrNumber = 0
            #print ('2')
            self.enterButton.wait_variable(self.wait)
            if (self.entry.get()):
                while (validateInput):
                    letter = self.entry.get()
                    letter = letter.lower()
                    if ((ord(letter) > 96) and (ord(letter) < 123) and (letter not in self.usedLetters)):
                        validateInput = 0
                        self.entry.delete(0, END)
            #wait_variable(validateInput)
                print ("".join(self.inputWord))
                getErrNumber = self.validateInputLetter(letter)
                if (getErrNumber > 0):
                    errNumber += 1
                    self.errLabel.configure(image = self.ImageList[errNumber])
                    self.errLabel.image = self.ImageList[errNumber]
                else:
                    self.inputLabel.configure(text = "".join(self.inputWord))
                #print('4')
                self.grayOutLabel(letter)
                if (("".join(self.inputWord)) == self.word):
                    self.victory()
            
                if (errNumber > 6):
                    self.gameOver()
                
            
    def grayOutLabel(self, letter):
        self.lblList[(ord(letter) - 97)].configure(bg = "light slate gray")
                        
    def gameOver(self):
        for lbl in self.lblList:
            lbl.grid_remove()
        self.inputLabel.grid_remove()
        self.enterButton.grid_remove()
        self.entry.grid_remove()
        
    def victory(self):
        for lbl in self.lblList:
            lbl.grid_remove()
        self.errLabel.grid_remove()
        self.enterButton.grid_remove()
        self.entry.grid_remove()
        self.inputLabel.configure(text = "Congratulations, you guessed right!")
        
    def exitGame(self):
        self.wait.set(0)
        root.destroy()
 

root = Tk()

app = App(root)

root.mainloop()
root.destroy()         
            
        
        
        
