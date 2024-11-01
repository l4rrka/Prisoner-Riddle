from random import randint

prisoners = [None] * 100
boxes = [None] * 100
wins = 0
loses = 0

repeats = int(input("How many times to repeat: "))

""" Search the prisoner's number in boxes """
def searchboxes(num, box, left):
  if left == 0:
    #print(f"Prisoner {num} never found his box.")
    return False
  if boxes[box] == num:
    #print(f"Prisoner {num} found his box in {50-left} tries.")
    return True
  else:
    return searchboxes(num, boxes[box], left-1)

""" Repeat experiment """
for exp in range(repeats): 
  prisoners = [None] * 100
  boxes = [None] * 100

  for b in range(100):
    while True:
      number = randint(0, 99)
      if number not in boxes:
        break
  
    boxes[b] = number

  # Search first for the box with the prisoner's number on it
  for p in range(100):
    prisoners[p] = searchboxes(p, p, 50)
    if prisoners[p] == False:
      #print("Prisoners lost.")
      loses += 1
      break

  if False not in prisoners:
    wins += 1
    #print("Prisoners won.")


probability = round(wins / repeats * 100, 2)
print(f"Total amount of wins: {wins}")
print(f"Total amount of loses: {loses}")
print(f"Probability of a Win: {probability}%")