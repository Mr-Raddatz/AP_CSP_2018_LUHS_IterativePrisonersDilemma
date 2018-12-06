####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'ur m0m g4y'
strategy_name = 'tft_spiteful'
strategy_description = 'Its really hard to explain'

def countB(history):
    sum = 0
    for element in history:
        if element == 'b':
            sum += 1
    return sum
    
def move(my_history, their_history, my_score, their_score):
    # tit for tat, until betrayed twice in a row, then always betray
    #collude twice, then spiteful
    # winner12: c, c then pavlov, then if betrayed twice, betray
    #pavlov: c on the first move, then betrays only if the players did not agree
    # gradual: c on first move, betray n times after nth bertayal, after two colludes, start colluding again
    
    '''tft_spiteful'''
    if strategy_name == 'tft_spiteful': 
        if 'bb' in their_history:
            return 'b'
        elif len(their_history) >= 1:
            return their_history[-1]
        else:
            return 'c'
    
    '''spiteful_cc'''
    if strategy_name == 'spiteful_cc':
        if len(my_history) <= 1:
            return 'c'
        elif 'b' not in their_history:
            return 'c'
        else:
            return 'b'
   
    '''winner12'''
    if strategy_name == 'winner12':
        betrayed = False
        
        if countB(their_history) >= 2:
            betrayed = True
        
        if len(my_history) < 2:
            return 'c'
        elif not betrayed:
            if their_history[-1] == my_history[-1]:
                return 'c'
            if their_history[-1] != my_history[-1]:
                return 'b'
        elif betrayed:
            return 'b'
        
    '''gradual'''
    if strategy_name == 'gradual':
        num = 0
        
        if len(their_history) >= 1:
            if their_history[-1] == 'b':
                num = countB(their_history)
                
        if len(their_history) >= 2:
            if their_history[-2] + their_history[-1] == 'cc':
                num = 0
                
        if num == 0:
            return 'c'
        else:
            return 'b'
            num -= 1
            
    '''spiteful'''
    if strategy_name == 'spiteful':
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
    

    

    

    
