from dice_rolls import roll_dice
from probability import calculate_exact_probability
from write_to_excel import excel_writer
import statistics

def run_simulation(num_trials, num_dice, target_sum):
    success_count = 0
    for _ in range(num_trials):
        current_sum = 0
        for _ in range(num_dice):
            current_sum += roll_dice()
            
        if current_sum == target_sum:
            success_count += 1
    return success_count

def main():
    NUM_DICE = 10
    TARGET_SUM = 32
    
    while True:
        try:
            N = int(input("Enter the max number of trials (e.g., 100000): "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input.")

    # Calculate exact probability once
    _, _, exact_prob = calculate_exact_probability(NUM_DICE, TARGET_SUM)
    print(f"\nExact Probability for Sum {TARGET_SUM} with {NUM_DICE} dice: {exact_prob:.6f} ({exact_prob*100:.4f}%)")

    milestones = [100, 1000, 10000, 100000, 1000000]
    active_milestones = [m for m in milestones if m <= N]
    if not active_milestones and N > 0:
        active_milestones = [N]

    all_data = []
    print(f"Running simulation 10 times for up to {active_milestones[-1]} trials...")

    for experiment_id in range(1, 11):
        # We need to simulate cumulatively to be efficient, or just run fresh for each milestone.
        # Running fresh is easier to implement and less error-prone for independence, 
        # though cumulative is faster. Task 1 did cumulative.
        # Let's do cumulative for performance.
        
        current_successes = 0
        current_trials = 0
        
        targets = sorted(active_milestones)
        previous_target = 0
        
        for target in targets:
            trials_needed = target - previous_target
            
            # Run additional trials
            successes_in_batch = run_simulation(trials_needed, NUM_DICE, TARGET_SUM)
            
            current_successes += successes_in_batch
            current_trials = target
            previous_target = target
            
            sim_prob = current_successes / current_trials
            
            all_data.append({
                'Experiment ID': experiment_id,
                'Total Trials': current_trials,
                'Successful Trials': current_successes,
                'Simulated Probability': sim_prob,
                'Exact Probability': exact_prob,
                'Error': abs(exact_prob - sim_prob)
            })

    # Process data for Excel
    final_records = []
    unique_trials = sorted(list(set(d['Total Trials'] for d in all_data)))

    for trials in unique_trials:
        subset = [d for d in all_data if d['Total Trials'] == trials]
        
        prob_list = [d['Simulated Probability'] for d in subset]
        success_list = [d['Successful Trials'] for d in subset]
        
        # Add individual experiments
        for d in subset:
            final_records.append({
                'Experiment ID': d['Experiment ID'],
                'Total Trials': d['Total Trials'],
                'Successful Trials': d['Successful Trials'],
                'Simulated Probability (%)': round(d['Simulated Probability'] * 100, 4),
                'Exact Probability (%)': round(d['Exact Probability'] * 100, 4),
                'Error': round(d['Error'], 6)
            })
            
        # Mean
        mean_prob = statistics.mean(prob_list)
        mean_success = statistics.mean(success_list)
        mean_error = abs(exact_prob - mean_prob)
        
        final_records.append({
            'Experiment ID': 'Mean',
            'Total Trials': trials,
            'Successful Trials': mean_success,
            'Simulated Probability (%)': round(mean_prob * 100, 4),
            'Exact Probability (%)': round(exact_prob * 100, 4),
            'Error': round(mean_error, 6)
        })
        
        # Mode
        try:
            mode_prob = statistics.mode(prob_list)
            mode_success = statistics.mode(success_list)
            mode_error = abs(exact_prob - mode_prob)
        except statistics.StatisticsError:
            mode_prob = "N/A"
            mode_success = "N/A"
            mode_error = "N/A"
            
        final_records.append({
            'Experiment ID': 'Mode',
            'Total Trials': trials,
            'Successful Trials': mode_success,
            'Simulated Probability (%)': "N/A" if mode_prob == "N/A" else round(mode_prob * 100, 4),
            'Exact Probability (%)': round(exact_prob * 100, 4),
            'Error': "N/A" if mode_error == "N/A" else round(mode_error, 6)
        })

    if final_records:
        excel_writer(final_records)
        
    # Summary
    if unique_trials:
        max_trials = unique_trials[-1]
        mean_rec = next(r for r in final_records if r['Experiment ID'] == 'Mean' and r['Total Trials'] == max_trials)
        print(f"\nSummary for {max_trials} trials (Mean of 10 experiments):")
        print(f"Mean Simulated Probability: {mean_rec['Simulated Probability (%)']}%")
        print(f"Exact Probability: {mean_rec['Exact Probability (%)']}%")
        print(f"Mean Error: {mean_rec['Error']}")

if __name__ == "__main__":
    main()

    