team_name = 'Smooth Criminals'
strategy_name = 'Shart'
strategy_description = 'pretty self explanatory'

import random
def move(my_history, their_history, my_score, their_score):
    
    while 1 == 1:
       n = random.randint(0, 9)
       if 'cc' in their_history:
           return 'b'
       elif 0 <= n <= 4:
             return 'b'
       elif 5 <= n <= 9:
             return 'c'
       elif 'bbb' in their_history:
           return 'c'
       elif 'ccc' in my_history:
           return 'b'
               
