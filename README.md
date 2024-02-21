# DS-project-Family-Tree-Python-
The family tree project is made to create, print, maintain/manipulate a family tree using Python. The program doesn't have any GUI, but CLI.
Here is the manual, on how to use the program:

Prerequisites:
  Python installed on your system (version 3.6 or higher).
  Any required Python libraries (e.g., anytree, csv) installed. You can install them using pip if not already installed.

Installation:
  Download the Python script file containing the Family Tree Program to your local machine.
  Ensure you have installed the required Python libraries (mentioned in the prerequisites section).
  Open a terminal or command prompt window.
  Navigate to the directory where the Python script file is located.

Usage:
  
  1. Creating a Family Tree:
     Launch the program by executing the Python script file in the terminal or command prompt window.
     Choose option 1 from the menu to create a tree.
     Enter the path of the CSV file containing the family tree data when prompted.
     The program will parse the CSV file and construct the family tree accordingly.
     Upon successful creation, the program will display a message confirming the creation of the tree.
  
  2. Printing the Family Tree:
     Choose option 2 from the menu to print the tree structure.
     The program will display the family tree's hierarchical structure, showing the family members' relationships.
  
  3. Adding a Member:
     Choose option 3 from the menu to add a new member to the tree.
     Enter the name of the new member and the name of their parent when prompted.
     If the parent exists in the tree, the new member will be added as their child.
     The program will display an error message if the parent does not exist.
  
  4. Removing a Member:
     Choose option 4 from the menu to remove an existing member from the tree.
     Enter the name of the member to be removed when prompted.
     If the member exists in the tree, they will be removed along with all their descendants.
     If the member does not exist, the program will display an error message.
 
  5. Showing Information about a Selected Person: 
     Choose option 5 from the menu to show information about a specific person in the family tree.
     Enter the name of the person whose information you want to display when prompted.
     The program will provide relevant information about the selected person, such as their age, address, etc. (if available).
 
  6. Exiting the Program:
     Choose option 6 from the menu to exit the program.
     The program will terminate, and you will return to the command prompt or terminal.
