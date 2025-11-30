from dice_rolls import roll_dice
from probability import calculate_exact_probability

def run_simulation(num_trials, num_dice, target_sum):
    success_count = 0
    print(f"\nStarting simulation of {num_trials} trials...")
    
    for trial in range(1, num_trials + 1):
        current_sum = 0
        # Roll num_dice dice
        for _ in range(num_dice):
            current_sum += roll_dice()
            
        if current_sum == target_sum:
            success_count += 1
            
        # Optional: Print progress every 100 trials
        if trial % 100 == 0:
            print(f"Completed {trial} trials. Successes so far: {success_count}")

    return success_count

if __name__ == "__main__":
    NUM_DICE = 10
    TARGET_SUM = 32
    NUM_TRIALS = 500

    # Task 1: Calculate exact probability using Dynamic Programming
    print("--- Task 1: Exact Probability Calculation (DP) ---")
    favorable, total, exact_prob = calculate_exact_probability(NUM_DICE, TARGET_SUM)
    print(f"Number of dice: {NUM_DICE}")
    print(f"Target sum: {TARGET_SUM}")
    print(f"Total combinations (6^{NUM_DICE}): {total}")
    print(f"Favorable combinations: {favorable}")
    print(f"Exact Probability: {exact_prob:.6f} ({exact_prob*100:.4f}%)")

    # Task 2: Simulation
    print("\n--- Task 2: Simulation (500 trials) ---")
    successes = run_simulation(NUM_TRIALS, NUM_DICE, TARGET_SUM)
    simulated_prob = successes / NUM_TRIALS
    
    print("\n--- Simulation Results ---")
    print(f"Total Trials: {NUM_TRIALS}")
    print(f"Successful Trials (Sum == {TARGET_SUM}): {successes}")
    print(f"Simulated Probability: {simulated_prob:.6f} ({simulated_prob*100:.4f}%)")
    
    # Comparison
    error = abs(exact_prob - simulated_prob)
    print(f"\nDifference between Exact and Simulated: {error:.6f}")

    