import random
def rolling(sides):
    r = random.randint(1,sides)
    return r
def main():
    roll=True
    while roll :
     choice = input ("press enter to roll THE DICE and q to quiet ")
     if choice.lower() != "q":
         dice_no= rolling (6)
         print("you rolled face :",dice_no)
     else:
         roll=False
    print("thanks for playing.")
main()
