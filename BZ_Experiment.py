from argparse import ArgumentParser
import sys
from random import randrange

def playerturn(p1, p2):
    """This is a experimental function for each player to input a number and see who had a higher number
    
    Args:
        p1 (str): name of the first player
        p2 (str): name of the second player

    Raise:
        ValueError: Not a number

    Side effects:
        Print out the number each player chose and who won
    """
    p1_count = 0
    p2_count = 0
    while p1_count == 0 and p2_count == 0:
        try:
            p1_input = int(input(f"Enter a number between 20-30 {p1}:"))
            if p1_input < 20 or p1_input > 30:
                print("Out of range")
            else:
                p1_num = p1_input + randrange(10)
                print(p1_num)
            p2_input = int(input(f"Enter a number between 20-30 {p2}:"))
            if p2_input < 20 or p2_input > 30:    
                print("Out of range")
            else:
                p2_num = p2_input + randrange(10)
                print(p2_num)
            if p1_num > p2_num:
                print("p1 wins")
                p1_count += 1
            elif p2_num > p1_num:
                print("p2 wins")
                p2_count += 1
            else:
                print("It's a tie")
        except ValueError:
            print("Not a number")
        if p1_count == 5:
            print("p1 wins the round")
        elif p2_count == 5:
            print("p2 wins the round")

def main(p1, p2):
    playerturn(p1, p2)

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("p1", help="name of first player")
    parser.add_argument("p2", help="name of second player")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.p1, args.p2)