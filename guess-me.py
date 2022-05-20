from random import randint


# generated random number to be guessed by player
random_num = randint(1, 101)

print('#'*20)
print('#'*20)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
print('#'*20)
print('#'*20)
print('\n')

# list to save player guesses
guesses = [0]

while True:
    player_guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? - "))

    # checking guess number should be within limit
    if player_guess < 1 or player_guess > 100:
        print("OUT OF BOUNDS! Please guess it again.")
        continue
    
    # here we compare the player's guess to our number
    if player_guess == random_num:
        print(f'CONGRATULATIONS !!, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    
    # if guess is incorrect, then add it to guess list
    guesses.append(player_guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(random_num - player_guess) < abs(random_num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    
    else:
        if abs(random_num - player_guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')


print('*'*20)
print("THANKS FOR PLAYING!")
print('*'*20)
