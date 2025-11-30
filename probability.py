def calc_probability(value):
    count = 0
    if value == 32:
        count += 1
        return count
    else: 
        return 0

def count_combinations_dp(num_dice, target_sum):
    # dp[i][j] stores the number of ways to get sum j with i dice
    # Initialize with 0
    # Max sum for num_dice is num_dice * 6
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(num_dice + 1)]
    
    # Base case: 0 dice, sum 0 is 1 way (doing nothing)
    dp[0][0] = 1
    
    for i in range(1, num_dice + 1):
        for j in range(1, target_sum + 1):
            for k in range(1, 7):
                if j - k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    
    return dp[num_dice][target_sum]

def calculate_exact_probability(num_dice, target_sum):
    total_combinations = 6 ** num_dice
    favorable_combinations = count_combinations_dp(num_dice, target_sum)
    probability = favorable_combinations / total_combinations
    return favorable_combinations, total_combinations, probability
    