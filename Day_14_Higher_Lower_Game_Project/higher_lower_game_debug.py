import random
from art import logo
from art import vs
from game_data import data
score = 0  
keep_playing = True


def create_candidate_A():
  global random_seed_A
  random_seed_A = random.randint(0,len(data) -1)
  
  candidate_A = data[random_seed_A]
  return random_seed_A, candidate_A


def create_candidate_B(): 
  random_seed_B = random.randint(0,len(data) -1)
  
  while random_seed_B == random_seed_A:
    random_seed_B = random.randint(0,len(data))
  candidate_B = data[random_seed_B]
  return random_seed_B, candidate_B

def compare(user_input):
  global score
  global keep_playing
  global candidate_A
  global candidate_B
  if candidate_A['follower_count'] > candidate_B['follower_count']:
    result = 'A'
  else:
    result = 'B'

  if user_input == result:
    score += 1
    return score
  else:
    keep_playing = False
    return keep_playing
 


while keep_playing:
  
  candidate_A = create_candidate_A()[1]
  #print(candidate_A)
  candidate_B = create_candidate_B()[1]
  #print(candidate_B)
  print(logo)
  if score == 0:
    print(f"Compare A: {candidate_A['name']}, a {candidate_A['description']}, from {candidate_A['country']}")
    print(vs)
    print(f"Against B: {candidate_B['name']}, a {candidate_B['description']}, from {candidate_B['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    compare(guess)
        
  else:
    candidate_A = create_candidate_A()[1]
    candidate_B = create_candidate_B()[1]
    print(logo)
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {candidate_A['name']}, a {candidate_A['description']}, from {candidate_A['country']}")
    print(vs)
    print(f"Against B: {candidate_B['name']}, a {candidate_B['description']}, from {candidate_B['country']}")
  # compare follower count
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    compare(guess)