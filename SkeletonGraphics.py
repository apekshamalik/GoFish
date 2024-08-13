from tkinter import *
from Game import Game
from Card import Card
from Hand import Hand
from Player import Player
from PIL import Image, ImageTk
from random import *
import time

COMPUTER_TEXT_ROW = 150
PLAYER_TEXT_ROW = 325   
ONE_SECOND = 1000
CARD_WIDTH = 71
CARD_HEIGHT = 96   

# intializes the data storage model at launch of application
def initialize(canvas, model, mainWindow):
    
    model.game = Game()
    deck = model.game.deck
    createDeck(deck, canvas)
    shuffle(deck)
    model.game.createPlayersAndHands(deck)
    
    card_back_img = ImageTk.PhotoImage(Image.open('cards/x1.gif'))
    model.game.back_card = card_back_img


def mousePressed(event, canvas, model):
    model.card_selected = True  # Set the flag when a card is selected
    card = event.widget['text']
    player_pair = model.game.playerTurn(canvas, model, card)
    if player_pair:
        model.card_selected = False  # Reset the flag if a pair is found
        return
    redraw(canvas, model)

    canvas.after(500, lambda: computerTurn(canvas, model))


    computer_pair = True
    c_hand = model.game.computer.hand.cards
    while(computer_pair and len(c_hand) > 0):
        computer_pair = model.game.computerTurn(canvas, model)
        redraw(canvas, model)

 
def redraw(canvas, model):
    canvas.delete(ALL)
    model.game.printCardsToCanvas(canvas)
    canvas.update()

    
    pass

def createDeck(deck, canvas):
    suits = ['d', 'c']#, 'h', 's']
    for i in range(len(suits)):
        for j in range(1, 14):
            card = Card(suits[i], j)
            card_image = ImageTk.PhotoImage(card.card_image)
            label = Label(canvas, image = card_image, text=suits[i]+str(j))
            label.image = card_image
            deck.append(label)




def run(width = 500, height = 500):

    class Struct(): pass

    
    model = Struct()
    model.width = width
    model.height = height
    
   
    mainWindow = Tk()
    canvas = Canvas(mainWindow, width = model.width, height = model.height)
    canvas.pack()

    initialize(canvas, model, mainWindow)


    def redrawWrapper(canvas, model):
        canvas.delete(ALL)  # delete the contents of the canvas
        redraw(canvas, model) # redraw the new conents
        canvas.update() # update the display

    def mousePressWrapper(event, canvas, model):
        mousePressed(event, canvas, model) 
        redrawWrapper(canvas, model) 

 

   
    mainWindow.bind("<Button-1>", lambda event:
                            mousePressWrapper(event, canvas, model))

    redrawWrapper(canvas, model)

 
    mainWindow.mainloop()

run(1250) 





