import random 
num_range = input("Type a number: ") 
  
if num_range.isdigit(): 
    num_range = int(num_range) 
  
    if num_range <= 0: 
        print('Please type a number larger than 0 next time.') 
        quit() 
else: 
    print('Please type a number next time.') 
    quit() 
  
random_number = random.randint(0, num_range) 
guesses = 0 
  
while True: 
    guesses += 1 
    user_guess = input("Make a guess: ") 
    if user_guess.isdigit(): 
        user_guess = int(user_guess) 
    else: 
        print('Please type a number next time.') 
        continue 
  
    if user_guess == random_number: 
        print("You got it!") 
        break 
    elif user_guess > random_number: 
        print("You were above the number!") 
    else: 
        print("You were below the number!") 
  
print("You got it in", guesses, "guesses")
