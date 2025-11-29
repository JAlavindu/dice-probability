from dice_rolls import roll_dice
from probability import calc_probability

if __name__ == "__main__":
    count = 0
    for i in range(10):
        rolled_number = roll_dice()
        count += rolled_number
        print(f"You rolled a {rolled_number}")
        
    probability_result = calc_probability(count)
    print(f"Total count: {count}")