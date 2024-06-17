import random
keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


#from art import logo
#print(logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
keep_playing = True

# deal a random card from deck (list) of cards
def deal_card(player):
  player.append(random.choice(cards))
  return player


# Calculates score. If score is blackjack returns 0. If score is above 21 and there is an 11 replace 11 with 1.
def calculate_score(hands):
  score = sum(hands)
  if score == 21 and len(hands) == 2:
    return 0
  elif score > 21:
    for n in range(len(hands)):
      if hands[n] == 11:
        hands[n] = 1
        return sum(hands)
      else:
        return score
  else:
    return score

def compare(user_score,computer_score):
  if user_score == computer_score:
    print("It is a draw.")
  elif computer_score == 0:
    print("Sorry Computer won the Blackjack.")
  elif user_score == 0:
    print("You won the Blackjack!!")
  elif user_score > 21:
    print("Sorry your score went above 21. You lose :(")
  elif computer_score > 21:
    print("Computer's score went above 21. You win!!")
  elif computer_score > user_score:
    print("Computer's score is higher than your score. You lose :(")
  else:
    print("Your score is higher than Computer's score. You win!!")    

# Initial deal

for n in range(0,2):
  deal_card(user_cards)
  deal_card(computer_cards)


# 
while keep_playing:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  
  if computer_score == 0 or user_score == 0 or user_score > 21:
    keep_playing = False
  
  else:
    keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ")
    if keep_dealing == 'y':
      deal_card(user_cards)
      calculate_score(user_cards)
    else:
      keep_playing = False
      



while computer_score < 17 and computer_score != 0:
  deal_card(computer_cards)
  computer_score = calculate_score(computer_cards)
  
print(f"	Your final hand: {user_cards}, final_score: {user_score}")
print(f"	Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score,computer_score))


      #print(user)
#print(computer)

#if keep_playing == False and user_score < 21 and computer_score < 21:
  