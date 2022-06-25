import random

def play():
    user= input(" what is your choice: 'r' for rock,'p' for paper,'s' for scissor ")
    computer=random.choice(['r','p','s'])

    if user == computer:
        return 'Its a tie'
    
    if is_win(user,computer):
        return "you won!!"
    
    return "you lost!!"


def is_win(player1,player2):#r>s,p>r,s>p
    if(player1=='r' and player2=='s')or(player1=='p' and player2=='r') or (player1=='s' and player2=='p'):
        return 'true'

print(play())