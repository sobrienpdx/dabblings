import random
# number guesser
secret_number_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secret_number = (random.choice(secret_number_set))
print
print "Number Guesser"
print 
print"I'm thinking of a number between 1 and 10. Guess what number I'm thinking of.",
guess = int(raw_input())
while guess != secret_number:
    while guess < secret_number:
        print "too low. Guess again?"
        guess = int(raw_input())
    while guess > secret_number:
     print "that's too high. new guess?"
     guess = int(raw_input())
if guess == secret_number:
    print "that's it!"