import random

def get_card_value(card, hand_sum = None):
  """Get the value of the passed in card."""
  if card == "A":
    if hand_sum and hand_sum <= 10: return 11
    return 1
  elif card == "K" or card == "Q" or card == "J": return 10
  else: return int(card)

def get_hand_value(cards):
  """
  Get the value of the passed in hand. If we are over 21 and we have
  aces in our hand, then we can set at least one ace to equal 1 instead
  of 11.
  """
  total = 0
  aces = cards.count("A")

  for card in cards:
    # we force our aces to have value 11 
    total += get_card_value(card, 1) 

  # adjust ace values so we don't bust if we're over 21
  while total > 21 and aces:
    total -= 10
    aces -= 1

  return total

def blackjack_game():
  """
  Runs blackjack game between a player and a dealer until someone hits
  blackjack, someone busts, or both players stand. 
  """
  deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4

  # get two cards for hand, get the hand sum, and remove cards from the deck
  dealer_hand = random.sample(deck, 2)
  dealer_1, dealer_2 = dealer_hand
  dealer_sum = get_card_value(dealer_1)
  dealer_sum += get_card_value(dealer_2, dealer_sum)
  deck.remove(dealer_1)
  deck.remove(dealer_2)

  player_hand = random.sample(deck, 2)
  player_1, player_2 = player_hand
  player_sum = get_card_value(player_1)
  player_sum += get_card_value(player_2, player_sum)
  deck.remove(player_1)
  deck.remove(player_2)

  print(f"Dealer has: {dealer_1} ? = ?")
  print(f"Player has: {player_1} {player_2} = {player_sum}")

  # Check if blackjack exists
  if dealer_sum == 21 and player_sum == 21: 
    print("It's a tie!")
    return
  elif dealer_sum == 21:
    print("Dealer wins!")
    print("Blackjack!")
    return
  elif player_sum == 21: 
    print("Player wins!")
    print("Blackjack!")
    return

  # Player moves
  while True:
    move = input("Would you like to (H)it or (S)tand? ")

    if move == "H":
      hit = random.choice(deck)
      deck.remove(hit)
      player_sum += get_card_value(hit, player_sum)
      player_hand.append(hit)
      player_hand_string = " ".join(player_hand)

      if player_sum == 21: 
        print(f"Player has: {player_hand_string} = {player_sum}")
        print("Player wins!")
        print("Blackjack!") 
        return
      elif player_sum > 21:
        # see if we can go under 21 by updating an ace value (or more) so we don't bust
        if get_hand_value(player_hand) <= 21: 
          player_sum = get_hand_value(player_hand) 
          print(f"Dealer has: {dealer_1} ? = ?")
          print(f"Player has: {player_hand_string} = {player_sum}")
        else:
          print(f"Player has: {player_hand_string} = {player_sum}")
          print(f"Player busts with {player_sum}")
          print("Dealer wins!")
          return

      print(f"Dealer has: {dealer_1} ? = ?")
      print(f"Player has: {player_hand_string} = {player_sum}")
    elif move == "S": 
      player_hand_string = " ".join(player_hand)
      print(f"Player stands with: {player_hand_string} = {player_sum}")
      break
    else: 
      print("Let's try that again")
      continue
  
  # Dealer moves
  print(f"Dealer has: {dealer_1} {dealer_2} = {dealer_sum}")
  while True:
    if dealer_sum < 17:
      hit = random.choice(deck)
      deck.remove(hit)
      dealer_sum += get_card_value(hit, dealer_sum)
      dealer_hand.append(hit)
      dealer_hand_string = " ".join(dealer_hand)
      print("Dealer hits")

      if dealer_sum == 21:
        print(f"Dealer has: {dealer_hand_string} = {dealer_sum}")
        print("Dealer wins!")
        print("Blackjack!") 
        return
      elif dealer_sum > 21:
        # see if we can go under 21 by updating an ace value (or more) so we don't bust
        if get_hand_value(dealer_hand) <= 21: 
          dealer_sum = get_hand_value(dealer_hand) 
          print(f"Dealer has: {dealer_hand_string} = {dealer_sum}")
        else:
          print(f"Dealer has: {dealer_hand_string} = {dealer_sum}")
          print(f"Dealer busts with {dealer_sum}")
          print("Player wins!")
          return

      print(f"Dealer has: {dealer_hand_string} = {dealer_sum}")
    else: 
      print("Dealer stands")
      break

  dealer_hand_string = " ".join(dealer_hand)
  player_hand_string = " ".join(player_hand)

  # Results
  if player_sum > dealer_sum:
    print("Player wins!")
    print(f"{player_hand_string} = {player_sum} to Dealer's {dealer_hand_string} = {dealer_sum}")
  elif dealer_sum > player_sum:
    print("Dealer wins!")
    print(f"{dealer_hand_string} = {dealer_sum} to Players's {player_hand_string} = {player_sum}")
  else: 
    print("It's a tie!")

blackjack_game()