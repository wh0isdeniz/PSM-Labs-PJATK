import numpy as np
import time

def create_grid(rows, cols):
    # Creating an initial grid with random live (1) and dead (0) cells.
    return np.random.choice([0, 1], size=(rows, cols))

def count_neighbors(grid, row, col):
    # Counting the number of live neighbors with cyclic boundary conditions
    rows, cols = grid.shape
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            r = (row + i) % rows
            c = (col + j) % cols
            count += grid[r, c]
    return count

def next_generation_custom(grid, survival_rules, birth_rules):
    #Generating the next generation based on custom rules.
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)
    for row in range(rows):
        for col in range(cols):
            alive_neighbors = count_neighbors(grid, row, col)
            cell = grid[row, col]
            if cell == 1:
                if alive_neighbors in survival_rules:
                    new_grid[row, col] = 1
            else:
                if alive_neighbors in birth_rules:
                    new_grid[row, col] = 1
    return new_grid

def get_rules_from_user():
    #Safely get survival and birth rules from the user with validation.
    while True:
        try:
            survival = input("Enter survival rules (e.g. 2,3): ")
            birth = input("Enter birth rules (e.g. 3): ")

            survival_rules = [int(n) for n in survival.split(",")]
            birth_rules = [int(n) for n in birth.split(",")]

            # Validation: all numbers between 0 and 8
            if any(n < 0 or n > 8 for n in survival_rules + birth_rules):
                raise ValueError("Rules must be integers between 0 and 8.")

            return survival_rules, birth_rules

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def ask_yes_no(prompt):
    # Ask a yes/no question with input validation.
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['yes', 'no']:
            return answer
        print("Please answer with 'yes' or 'no'.")

def display_grid(grid):
    #Printing the grid in a graphical way using symbols. I thought it looks better this way than 0's and 1's.
    for row in grid:
        line = ''.join('⬛' if cell == 1 else '⬜' for cell in row)
        print(line)

def run_game():
    #Run the Game of Life with dynamic rule changing and graphical display.
    rows, cols = 10, 10
    grid = create_grid(rows, cols)
    survival_rules, birth_rules = get_rules_from_user()
    generations = 20
    change_interval = 5  # Ask every 5 generations

    for gen in range(1, generations + 1):
        print(f"Generation {gen}")
        display_grid(grid)
        grid = next_generation_custom(grid, survival_rules, birth_rules)
        time.sleep(0.5)
        print("\n" * 5)

        if gen % change_interval == 0:
            if ask_yes_no("Do you want to change the rules? (yes/no): ") == "yes":
                survival_rules, birth_rules = get_rules_from_user()

if __name__ == "__main__":
    run_game()
