################################
# Card Class:
################################


from PIL import Image
class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image_file = str('cards/'+str(suit) + str(rank)+'.gif')
        self.card_image = Image.open(self.image_file)

    def getCardSuit(card_suit):
        if card_suit == 's':
            return 'Spades'
        elif card_suit == 'd':
            return 'Diamonds'
        elif card_suit == 'h':
            return 'Hearts'
        else:
            return 'Clubs'

    def getCardNum(card_num):
        card_name = str(card_num)
        if card_num == '11':
            card_name = 'Jack'
        elif card_num == '12':
            card_name = 'Queen'
        elif card_num == '13':
            card_name = 'King'
        elif card_num == '1':
            card_name = 'Ace'
        return card_name
    pass

