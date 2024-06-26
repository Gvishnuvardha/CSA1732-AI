
class State:
    def __init__(self, left_m, left_c, boat, right_m, right_c):
        self.left_m = left_m  # number of missionaries on the left side
        self.left_c = left_c  # number of cannibals on the left side
        self.boat = boat      # 1 if boat is on the left side, 0 if on the right side
        self.right_m = right_m  # number of missionaries on the right side
        self.right_c = right_c  # number of cannibals on the right side

    def is_valid(self):
        # Check if any side has negative missionaries or cannibals
        if self.left_m < 0 or self.left_c < 0 or self.right_m < 0 or self.right_c < 0:
            return False
        # Check if the cannibals outnumber the missionaries on either side
        if (self.left_m != 0 and self.left_m < self.left_c) or \
           (self.right_m != 0 and self.right_m < self.right_c):
            return False
        return True

    def is_goal(self):
        return self.left_m == 0 and self.left_c == 0 and self.boat == 0

    def __eq__(self, other):
        return self.left_m == other.left_m and self.left_c == other.left_c and \
               self.boat == other.boat and self.right_m == other.right_m and \
               self.right_c == other.right_c

    def __hash__(self):
        return hash((self.left_m, self.left_c, self.boat, self.right_m, self.right_c))

    def __str__(self):
        return f"Left side: {self.left_m}M-{self.left_c}C, " \
               f"Boat: {'left' if self.boat == 1 else 'right'}, " \
               f"Right side: {self.right_m}M-{self.right_c}C"


def is_valid_move(state, m, c):
    if state.boat:  # Boat is on the left side
        new_left_m = state.left_m - m
        new_left_c = state.left_c - c
        new_right_m = state.right_m + m
        new_right_c = state.right_c + c
    else:  # Boat is on the right side
        new_left_m = state.left_m + m
        new_left_c = state.left_c + c
        new_right_m = state.right_m - m
        new_right_c = state.right_c - c

    new_state = State(new_left_m, new_left_c, 1 - state.boat, new_right_m, new_right_c)
    return new_state.is_valid()


def generate_next_states(state):
    next_states = []
    moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]
    for move in moves:
        m, c = move
        if is_valid_move(state, m, c):
            if state.boat:  # Boat is on the left side
                next_states.append(State(state.left_m - m, state.left_c - c, 0,
                                         state.right_m + m, state.right_c + c))
            else:  # Boat is on the right side
                next_states.append(State(state.left_m + m, state.left_c + c, 1,
                                         state.right_m - m, state.right_c - c))
    return next_states


def dfs(state, visited, path):
    visited.add(state)
    path.append(state)
    if state.is_goal():
        return True
    for next_state in generate_next_states(state):
        if next_state not in visited:
            if dfs(next_state, visited, path):
                return True
    path.pop()
    return False


def solve_missionaries_cannibals():
    initial_state = State(3, 3, 1, 0, 0)
    visited = set()
    path = []
    if dfs(initial_state, visited, path):
        return path
    else:
        return None


def print_solution_path(path):
    for i, state in enumerate(path):
        print(f"Step {i + 1}: {state}")
    print("Goal state reached!")


# Solve the problem
solution_path = solve_missionaries_cannibals()
if solution_path:
    print("Solution found:")
    print_solution_path(solution_path)
else:
    print("No solution exists.")
