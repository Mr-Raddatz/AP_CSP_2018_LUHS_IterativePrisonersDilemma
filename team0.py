####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'

team_name = 'Fortnight' # Only 10 chars displayed.
strategy_name = 'Random random'
strategy_description = 'Random^2'
    
import random


def move(my_history, their_history, my_score, their_score):
    a = random.randint(0,1)
    if a == 0:
       return 'b'
    if a == 1:
       return 'c'
