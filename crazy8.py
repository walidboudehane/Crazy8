import math
import random
import copy
class LinkedList:
    class _Node:
        def __init__(self, v, n):
            self.value = v
            self.next = n

    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self):
        result ='['
        if self._size==0:
            return ''
        current=self._head
        while current:
            result+=str(current.value) 
            if current.next!=None :
                result+=', '
            current=current.next
        return result + ']'

    def __len__(self):
        return self._size

    def isEmpty(self):
        if self._size==0:
            return True
        return False

    # Adds a node of value v to the beginning of the list
    def add(self,v):
        if self._size==0:
            self._head=self._Node(v,None)
            self._tail = self._head

        else:
            current = self._head
            newNode = self._Node(v, current)
            self._head=newNode
        self._size+=1
            

        

    # Adds a node of value v to the end of the list
    def append(self,v): 
        if self._size == 0:
            self._head = self._Node(v,None)
            self._tail = self._head
        
        else:
            self._tail.next = self._Node(v,None)
            self._tail = self._tail.next
        
        self._size += 1

    # Removes and returns the first node of the list
    def pop(self):
        if self._size !=0:
            result = self._head.value
            self._head=self._head.next
            self._size -=1
        return result 
    # Returns the value of the first node of the list
    def peek(self):
        return self._head.value

    # Removes the first node of the list with value v and return v
    def remove(self, v):
        find=False
        if self._head.value ==v:
            result = self._head.value
            self._head = self._head.next
            find=True
        else:
            current = self._head
            while current.next!=None:
                if current.next.value==v:  

                    result = current.next.value
                    current.next = current.next.next
                    find=True
            
                else:
                    current=current.next
            if current.next==self._tail:
                self._tail = current
        if find:        
            self._size -= 1
        else:
            result=None
        
        return result 

class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        result ='['
        if self._size==0:
            return ''
        current=self._head
        compteur=0
        while compteur==0:
            result+=str(current.value) 
            if current.next!=self._head :
                result+=', '
            else:
                compteur+=1

            current=current.next
        return result +"]"
        
    def __iter__(self):
        current = self._head
        for i in range(self._size):
            yield current.value
            current = current.next

    # Moves head pointer to next node in list
    def next(self):
        self._head=self._head.next
        self._tail=self._tail.next

        
        


    # Adds a node of value v to the end of the list
    def append(self, v):
        if self._size == 0:
            self._head = self._Node(v,None)
            self._tail = self._head
        
        else:
            self._tail.next = self._Node(v,None)
            self._tail = self._tail.next
            self._tail.next=self._head
        
        self._size += 1

    # Reverses the next pointers of all nodes to previous node
    def reverse(self):
        reversedList=CircularLinkedList()
        size=self._size
        if size>2:
            valHead=self._head.value
            self.pop()
            for i in range(size-1):
                for j in range(size-2):
                    self.next()
                reversedList.append(self._tail.value)
            
            for i in range(size-2):
                reversedList.next()
    
            
            reversedList.append(valHead)
    
            for i in range(size-1):
                reversedList.next()
            
            self._head=reversedList._head
            self._tail=reversedList._tail
        
        else:
            self
            print(self)
        


    # Removes head node and returns its value
    def pop(self):
        if self._size !=0:
            result = self._head.value
            self._tail.next=self._head.next
            self._head=self._head.next
            self._size -=1
        return result 
                

class Card:
    def __init__(self, r, s):
        self._rank = r
        self._suit = s

    suits = {'s': '\U00002660', 'h': '\U00002661', 'd': '\U00002662', 'c': '\U00002663'}

    def __str__(self):
        return self._rank + self.suits[self._suit]

    # returns True if self and other cards are the same rank or the same suit
    def __eq__(self, other):
        return self._rank == other._rank or self._suit == other._suit

class Hand:
    def __init__(self):
        self.cards = {'s': LinkedList(), 'h': LinkedList(), 'd': LinkedList(), 'c': LinkedList()}

    def __str__(self):
        result = ''
        for suit in self.cards.values():
            result += str(suit)
        return result

    def __getitem__(self, item):
        return self.cards[item]

    def __len__(self):
        result = 0
        for suit in list(self.cards):
            result += len(self.cards[suit])

        return result

    def add(self, card):
        self.cards[card._suit].add(card)

    def get_most_common_suit(self):
        return max(list(self.cards), key = lambda x: len(self[x]))

    # Returns a card included in the hand according to
    # the criteria contained in *args and None if the card
    # isn't in the hand. The tests show how *args must be used.
    def play(self, *args):
        
        suitsList = ['s','h','c','d']
        nbrArgs = len(args)
        for i in range(len(suitsList)):
            if (suitsList[i]==args[0]):
                suitTemp=args[0]
                if suitTemp in self.cards:

                    if nbrArgs >= 2:
                            
                        rank = args[1]
                        card=Card(rank,suitTemp)
                        self.cards[suitTemp].remove(card)
                        return card
                    return self.cards[suitTemp].pop()
                else:
                    return None
        else:
            rank = args[0]
            
            if nbrArgs >= 2:

                suitTemp = args[1]

                if suitTemp in self.cards:

                    card=Card(rank,suitTemp)
                 
                    self.cards[suitTemp].remove(card)
                    return card
                return None
            else:
                for suitTemp in list(self.cards):
                    
                    suitSize=len(self.cards[suitTemp])

                    for i in range(suitSize):

                        card=Card(rank,suitTemp)

                        self.cards[suitTemp].remove(card)

                        return card

                return None
        return None


class Deck(LinkedList):
    def __init__(self, custom=False):
        super().__init__()
        if not custom:
            # for all suits
            for i in range(4):
                # for all ranks
                for j in range(13):
                    s = list(Card.suits)[i]
                    r = ''
                    if j == 0:
                        r = 'A'
                    elif j > 0 and j < 10:
                        r = str(j+1)
                    elif j == 10:
                        r = 'J'
                    elif j== 11:
                        r = 'Q'
                    elif j == 12:
                        r = 'K'
                    self.add(Card(r,s))

    def draw(self):
        return self.pop()

    def shuffle(self, cut_precision = 0.05):
        # Cutting the two decks in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision*len(self)))

        # other_deck must point the kth node in self
        # (starting at 0 of course)
        # other_deck = #TO DO
        current=self._head
        for i in range(k):
            current=current.next
        other_deck=current




        #TO DO: seperate both lists
        liste1=LinkedList()
        liste2=LinkedList()
        
        current=self._head
        while current.next!=other_deck:

            liste1.append(current.value)
            current=current.next

        liste1.append(current.value)

    
        while current.next!=None:
            current=current.next
            liste2.append(current.value)
        


        # Merging the two decks together
        mergedList=LinkedList()
        #switch self._head and other_deck pointers
        current1=liste1._head
        current2=liste2._head
        switch=True
        if random.uniform(0,1) < 0.5:
            #switch self._head and other_deck pointers
            
            for i in range(k*2):
                if switch:
                    
                    mergedList.append(current2.value)
                    current2=current2.next
                    switch=False
                else:
                 
                    mergedList.append(current1.value)
                    current1=current1.next
                    switch=True

        else:
            for i in range(k*2):
                if switch:
                
                    mergedList.append(current1.value)
                    current1=current1.next
                    switch=False
                else:
                    
                    mergedList.append(current2.value)
                    current2=current2.next
                    switch=True
        self._head=mergedList._head


class Player():
    def __init__(self, name, strategy='naive'):
        self.name = name
        self.score = 8
        self.hand = Hand()
        self.strategy = strategy

    def __str__(self):
        return self.name

    # This function must modify the player's hand,
    # the discard pile, and the game's declared_suit 
    # attribute. No other variables must be changed.
    # The player's strategy can ONLY be based
    # on his own cards, the discard pile, and
    # the number of cards his opponents hold.
    def play(self, game):
        if(self.strategy == 'naive'):
            top_card = game.discard_pile.peek()
            # player doesn't have a playable card
            # player draws a card
            if(self.hand.play(self, top_card) == None):
                self.hand.add(self, game.draw_from_deck(self, 1))

            # player has a playable card
            # played card gets removed from hand
            # played card becomes top card
            # played card gets added to discard pile
            else:
                playable_card = self.hand.play(self, top_card)
                self.hand.remove(self, playable_card)
                self.declared_suit = str(playable_card._suit)
                game.discard_pile.add(playable_card)

            return game

        else:
            # TO DO(?): Custom strategy (Bonus)
            pass

class Game:
    def __init__(self):
        self.players = CircularLinkedList()

        for i in range(1,5):
            self.players.append(Player('Player '+ str(i)))

        self.deck = Deck()
        self.discard_pile = LinkedList()

        self.draw_count = 0
        self.declared_suit = ''

    def __str__(self):
        result = '--------------------------------------------------\n'
        result += 'Deck: ' + str(self.deck) + '\n'
        result += 'Declared Suit: ' + str(self.declared_suit) + ', '
        result += 'Draw Count: ' + str(self.draw_count) + ', '
        result += 'Top Card: ' + str(self.discard_pile.peek()) + '\n'

        for player in self.players:
            result += str(player) + ': '
            result += 'Score: ' + str(player.score) + ', '
            result += str(player.hand) + '\n'
        return result


    # Puts all cards from discard pile except the 
    # top card back into the deck in reverse order
    # and shuffles it 7 times
    def reset_deck(self):
        
        if self.discard_pile._size > 1:
            tempCard=self.discard_pile.pop()

            while (not self.discard_pile.isEmpty()):
                self.deck.add(self.discard_pile.pop())
            self.discard_pile.append(tempCard)

        if ( not self.deck.isEmpty()):
            for i in range (0,7):
                self.deck.shuffle()


    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):

        deckSize=self.deck._size

        if (deckSize > 1):
            return self.deck.pop()

        elif (deckSize == 1):
            
            tempCard = self.deck.pop()
            self.reset_deck()
            return tempCard
                
            

    def start(self, debug=False):
        # Ordre dans lequel les joeurs gagnent la partie
        result = LinkedList()

        self.reset_deck()

        # Each player draws 8 cards
        for player in self.players:
            for i in range(8):
                player.hand.add(self.deck.draw())

        self.discard_pile.add(self.deck.draw())

        transcript = open('result.txt','w',encoding='utf-8')
        if debug:
            transcript = open('result_debug.txt','w',encoding='utf-8')

        while(not self.players.isEmpty()):
            if debug:
                transcript.write(str(self))

            # player plays turn
            player = self.players.peek()

            old_top_card = self.discard_pile.peek()

            self = player.play(self)

            new_top_card = self.discard_pile.peek()

            # Player didn't play a card => must draw from pile
            if new_top_card == old_top_card:
                self.player.draw_from_deck(self, 1)
            # Player played a card
            else:
                self.player.remove(self, new_top_card)
            # Handling player change
            # Player has finished the game
            if len(player.hand) == 0 and player.score == 1:
                player.score += 1
            else:
                # Player is out of cards to play
                if len(player.hand) == 0:
                    player.score += 1
                # Player has a single card left to play
                elif len(player.hand) == 1:
                    result += str(player) + 'frappe sur la table pour avertir les autres joueurs'
                self.players.next()
        return result

if __name__ == '__main__':
    '''
    random.seed(420)
    game = Game()
    print(game.start(debug=True))

    # TESTS
    # LinkedList
    l = LinkedList()
    l.append('b')
    l.append('c')
    l.add('a')

    assert(str(l) == '[a, b, c]')
    assert(l.pop() == 'a')
    assert(len(l) == 2)
    assert(str(l.remove('c')) == 'c')
    assert(l.remove('d') == None)
    assert(str(l) == '[b]')
    assert(l.peek() == 'b')
    assert(l.pop() == 'b')
    assert(len(l) == 0)
    assert(l.isEmpty())

    # CircularLinkedList
    l = CircularLinkedList()
    l.append('a')
    l.append('b')
    l.append('c')

    assert(str(l) == '[a, b, c]')
    l.next()
    assert(str(l) == '[b, c, a]')
    l.next()
    assert(str(l) == '[c, a, b]')
    l.next()
    assert(str(l) == '[a, b, c]')
    l.reverse()
    assert(str(l) == '[a, c, b]')
    assert(l.pop() == 'a')
    assert(str(l) == '[c, b]')

    # Card
    c1 = Card('A','s')
    c2 = Card('A','s')
    # Il est pertinent de traiter le rang 1
    # comme étant l'ace
    c3 = Card('1','s')
    assert(c1 == c2)
    assert(c1 == c3)
    assert(c3 == c2)

    # Hand
    h = Hand()
    h.add(Card('A','s'))
    h.add(Card('8','s'))
    h.add(Card('8','h'))
    h.add(Card('Q','d'))
    h.add(Card('3','d'))
    h.add(Card('3','c'))

    assert(str(h) == '[8♠, A♠][8♡][3♢, Q♢][3♣]')
    assert(str(h['d']) == '[3♢, Q♢]')
    assert(h.play('3','d') == Card('3','d'))
    assert(str(h) == '[8♠, A♠][8♡][Q♢][3♣]')
    assert(str(h.play('8')) == '8♠')
    assert(str(h.play('c')) == '3♣')
    assert(str(h) == '[A♠][8♡][Q♢][]')
    assert(h.play('d','Q') == Card('Q','d'))
    assert(h.play('1') == Card('A','s'))
    assert(h.play('J') == None)

    # Deck
    d = Deck(custom=True)
    d.append(Card('A','s'))
    d.append(Card('2','s'))
    d.append(Card('3','s'))
    d.append(Card('A','h'))
    d.append(Card('2','h'))
    d.append(Card('3','h'))

    random.seed(15)

    temp = copy.deepcopy(d)
    assert(str(temp) == '[A♠, 2♠, 3♠, A♡, 2♡, 3♡]')
    temp.shuffle()
    assert(str(temp) == '[A♠, A♡, 2♠, 2♡, 3♠, 3♡]')
    temp = copy.deepcopy(d)
    temp.shuffle()
    assert(str(temp) == '[A♡, A♠, 2♡, 2♠, 3♡, 3♠]')
    assert(d.draw() == Card('A','s'))
    '''