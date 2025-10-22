def ranks(array):
    unique_scores = sorted(set(array), reverse=True)
    
    # Step 2: Create a map of score → rank
    rank_map = {}
    rank = 1
    for score in unique_scores:
        rank_map[score] = rank
        rank += array.count(score)  # Skip ranks for tied values

    # Step 3: Build the rank list for the original order
    ranks = [rank_map[value] for value in array]

    return ranks
