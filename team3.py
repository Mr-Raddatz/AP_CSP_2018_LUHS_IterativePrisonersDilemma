import random

team_name = 'Ur m0m g4y'
strategy_name = 'Betray, then Collude until Betrayed, Unless they start colluding again, then collude until betrayed'
strategy_description = 'Your Mom = "G" + "A" + "Y"'
    
def move(my_history, their_history, my_score, their_score):
    # tit for tat, until betrayed twice in a row, then always betray
    #collude twice, then spiteful
    # winner12: c, c then pavlov, then if betrayed twice, betray
    #pavlov: c on the first move, then betrays only if the players did not agree
    # gradual: c on first move, betray n times after nth bertayal, after two colludes, start colluding again
   
    betrayed = False
    
    if 'b' in their_history:
        betrayed = True
    else:
        betrayed = False
        
    if len(their_history) > 2:
        if their_history[-2:-1]+their_history[-1] == 'cc':
            betrayed = False

    
    if len(my_history) == 0:
        return 'b'
    elif not betrayed:
        return 'c'
    elif betrayed:
        return 'b'
    else:
        return random.choice('b', 'c')
    
