from itertools import permutations

def solve_cryptarithm():
    # Unique letters in the problem
    letters = 'SENDMORY'
    digits = '0123456789'
    
    # Permutations of digits
    for perm in permutations(digits, len(letters)):
        solution = dict(zip(letters, perm))
        
        # Convert words to numbers based on current permutation
        s = int(''.join(solution[ch] for ch in 'SEND'))
        m = int(''.join(solution[ch] for ch in 'MORE'))
        r = int(''.join(solution[ch] for ch in 'MONEY'))
        
        # Check if the equation is satisfied
        if s + m == r and solution['S'] != '0' and solution['M'] != '0':
            print(f"SEND + MORE = MONEY")
            print(f"{s} + {m} = {r}")
            return solution

    print("No solution found.")
    return None

# Example usage
solve_cryptarithm()
