import random

team_name = 'smooth criminals'
strategy_name = 'shart'
strategy_description = 'pretty self explanatory'

def move(my_history, their_history, my_score, their_score):
    
    n = random.randint(0,12)
    
    if n > 10:
        print 'b'
    elif 'bbb' in their_history:
        print 'c'
    elif 3 <= n <= 9:
        print 'bb'
    elif 0 <= n <= 2:
        print 'cccc'
