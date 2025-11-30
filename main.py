from dice_rolls import roll_dice
from probability import calc_probability

if __name__ == "__main__":
    
    probability_count = 0

    while probability_count >= 0 and probability_count <= 10:
        value = 0
        for i in range(10):
          rolled_number = roll_dice()
          value += rolled_number
          print(f"You rolled a {rolled_number}")
        probability_count += calc_probability(value)
        print(f"Total count: {value}")
        print(f"Probability count: {probability_count}")
        

    