 # hexagon
"""Write a Python program that prompts the user to enter a size for a hexagon, and then prints a hexagon of that size using asterisks(*). The program should handle invalid input gracefully by displaying an error message and asking the user to enter a valid input.

Example Output:
Enter a size for the hexagon: 4"""


while True:
     try:
         size = int(input("Enter a size for hexagon: "))
         if size <=0:
             raise ValueError
         break
     except ValueError:
         print("Error")
         print(f"{size} is Invalid input. Please enter a valid input")

for i in range(-size+1, size):

     space = '' * (size-abs(i) - 1)
     asterisks = '*' * (2 * (size-abs(i) - 1))
     print(space + asterisks)

     """using absolute value of i, but the correct form is not showing in the output
          Enter a size for hexagon: 7

     **
     ****
     ******
     ********
     **********
     ************
     **********
     ********
     ******
     ****
     **
     """

