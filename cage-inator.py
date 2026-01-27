#The Cage-inator
# Solver for the "cage" rule on sudoku puzzles
# Input the cage sum, the number of cells, and the possible valid entry numbers within each cell in the cage
# Then test all combinations of numbers to find valid solutions

print("Welcome to the Cage-inator!")
cage_sum = int(input("Enter the cage sum: "))
num_cells = int(input("Enter the number of cells in the cage: "))

cell_options_list = []
print('Note: You can enter "x" to indicate all numbers 1-9 are possible for that cell.')
for i in range(num_cells):
    cell_options_input = input(f"Enter the possible valid entry numbers for cell {i+1} (comma-separated): ")

    #allow user to input 'x' for all numbers 1-9
    if cell_options_input.strip().lower() == 'x':
        cell_options_input = '1,2,3,4,5,6,7,8,9'
    else:
        cell_options_input = list(map(int, cell_options_input.split(',')))
    cell_options_list.append(cell_options_input)

#build the combination tree
tree = [[]]
for cell_options in cell_options_list:
    new_tree = []
    for combination in tree:
        for option in cell_options:
            if option not in combination:
                new_combination = combination + [option]
                new_tree.append(new_combination)
    tree = new_tree

#filter valid combinations
valid_combinations = []
for combination in tree:
    if sum(combination) == cage_sum:
        valid_combinations.append(combination)

#output results
if valid_combinations:
    print("Valid combinations found:")
    for combo in valid_combinations:
        print(combo)

    #print out numbers that are in all combinations
    common_numbers = set(valid_combinations[0])
    for combo in valid_combinations[1:]:
        common_numbers.intersection_update(set(combo))
    if common_numbers:
        print("Numbers that are in all valid combinations:", common_numbers)

    #print out numbers to remove from each cell
    for i in range(num_cells):
        all_options = set(cell_options_list[i])
        used_options = set(combo[i] for combo in valid_combinations)
        to_remove = all_options - used_options
        if to_remove:
            print(f"Numbers to remove from cell {i+1}: {to_remove}")
else:
    print("No valid combinations found.")

