import random

# vairables
# user_points = 0
# computer_points = 0
options = ["rock", "paper", "scissors"]


# functions
def compute_legit_winner(user_points, computer_points):
    print "what is your move?"
    computer_move= (random.choice(options))
    user_move = (raw_input()) 
    # global user_points
    # global computer_points
    if computer_move == "rock":
        if user_move == "rock":
            print "we both chose rock. do over!"
        if user_move == "paper":
            print "Mine was rock. Paper covers rock, you win that one!"
            user_points = user_points + 1
        if user_move == "scissors":
            print "Mine was rock. Rock smashes scissors, my point!" 
            computer_points = computer_points + 1
        
    if computer_move == "paper":
        if user_move == "rock":
            print "Mine was paper. Paper covers rock, so it's all me!"
            computer_points = computer_points + 1
        if user_move == "paper":
            print "We both chose paper. do over!"
        if user_move == "scissors":
            print "I picked paper. Your scissors beat me."
            user_points = user_points + 1
        
    if computer_move == "scissors":
        if user_move == "rock":
            print "mine was scissors. Your rock squishes me."
            user_points = user_points + 1
        if user_move == "paper":
            print "I'm scissors. I cut you, paper!"
            computer_points = computer_points + 1
        if user_move == "scissors":
            print "we both chose scissors. go again!"
            
    print "The current score is %r you, %r me." % (user_points, computer_points)
    return user_points, computer_points
        
def offer_play_again():
    global answer
    print "want to go again?",
    answer = raw_input()
    
def cheat_shamelessly(user_points, computer_points):
    print "what is your next move?"
    user_move = (raw_input()) 
    if user_move == "rock":
        print "I chose paper, yay me!"
    if user_move == "paper":  
        print "my scissors make confetti out of your paper!"
    if user_move == "scissors":
        print "me rock. you scissor. smash good."
    computer_points = computer_points + 1
    print "The current score is %r you, %r me." % (user_points, computer_points)
    return user_points, computer_points
    
# play   
print "let's play rock, paper, scissors. I have my choice."
computer_points = 0
user_points = 0
user_points, computer_points = compute_legit_winner(user_points, computer_points)
offer_play_again()
while answer == "yes":
    if computer_points > user_points:
        user_points, computer_points = compute_legit_winner(user_points, computer_points)
        offer_play_again()
    if computer_points < user_points or computer_points == user_points:
        user_points, computer_points = cheat_shamelessly(user_points, computer_points)
        offer_play_again()
    
if answer == "no":
    print "ok, thanks for playing!"

