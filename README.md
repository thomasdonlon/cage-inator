```
██████ ▄▄ ▄▄ ▄▄▄▄▄     ▄█████  ▄▄▄   ▄▄▄▄ ▄▄▄▄▄     ▄▄ ▄▄  ▄▄  ▄▄▄ ▄▄▄▄▄▄ ▄▄▄  ▄▄▄▄  
  ██   ██▄██ ██▄▄      ██     ██▀██ ██ ▄▄ ██▄▄  ▄▄▄ ██ ███▄██ ██▀██  ██  ██▀██ ██▄█▄ 
  ██   ██ ██ ██▄▄▄     ▀█████ ██▀██ ▀█▄▄█ ██▄▄▄     ██ ██ ▀██ ██▀██  ██  ▀███▀ ██ ██ 
```
Ever find yourself exhausted, writing out a billion possible combinations for the "cage" rule variant in sudoku puzzles? Let **The Cage-inator** handle that for you. (A cage is a region of cells in a Sudoku puzzle that must sum to the given number without repeating any digits.)

Don't worry, **The Cage-inator** doesn't solve the puzzle for you. It would never deny you that fun. Instead, **The Cage-inator** provides you with the information and valid options as it **Cage-inates** one specific cage. 

### Usage:
Run the included .py file. Fill out the inputs as prompted, and watch as **The Cage-inator** works its mystifying and awesome power. 

### Example:
Consider the cage variant Sudoku puzzle below:

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/f823269f-5f75-41cc-b5f5-94f93fd80f4d" />

The cage highlighted in red has a sum of 3, and all numbers are allowed. You would go into **The Cage-inator** and enter 3, the number of cells (2), and 'x' for each cell ('x' represents all numbers in **The Cage-inator**). 

**The Cage-inator** will then return the list of all possible solutions for that cage: 
```
[1,2]
[2,1]
```

Consider a more complicated example for a partially-completed Sudoku: 

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/a2162707-8e34-4ca8-8bef-eb0a99570c16" />

The highlighted cage has a sum of 9, and some digits are ruled out in each cell. Using **The Cage-inator**, you can quickly get the answer for the allowed combinations of this cage (ordering the cells arbitrarily in this case from top right towards the bottom left). **The Cage-inator** provides several helpful utilities: 
```
Welcome to the Cage-inator!
Enter the cage sum: 9
Enter the number of cells in the cage: 3
Note: You can enter "x" to indicate all numbers 1-9 are possible for that cell.
Enter the possible valid entry numbers for cell 1 (no separation): 123678
Enter the possible valid entry numbers for cell 2 (no separation): 13678
Enter the possible valid entry numbers for cell 3 (no separation): 134678
Valid combinations found:
[2, 1, 6]
[2, 3, 4]
[2, 6, 1]
Numbers that are in all valid combinations: {2}
Numbers to remove from cell 1: {1, 3, 6, 7, 8} 
Numbers to remove from cell 2: {8, 7}
Numbers to remove from cell 3: {8, 3, 7}
```
