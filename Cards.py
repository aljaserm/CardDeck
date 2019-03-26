# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:00:25 2019

@author: aljaser

Playing Cards deck
"""

import random

cards=[]
sets=["Hearts","Diamonds","Clubs","Spades"]
royals=["King","Queen","Prince","Ace"]
deck=[]
for i in range(2,11):
    cards.append(str(i))

for j in range(4):
    cards.append(royals[j])
    
#print(cards)

for k in range(4):
    for l in range(13):
        card=(cards[l]+" of "+ sets[k])
        deck.append(card)
        
 #shuffle 
random.shuffle(deck)      
        
        
for m in range(52):
    print(deck[m])
        