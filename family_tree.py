from anytree import Node as TreeNode, RenderTree
import csv


def create_tree(file_path):
    root = None
    parent_dict = {}

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                parent = row['Parent']
                node = TreeNode(name)
                if parent == "":
                    root = node
                    parent_dict[root.name] = root
                else:
                    parent_node = parent_dict.get(parent)
                    if parent_node is None:
                        # If the parent node doesn't exist, create it
                        parent_node = TreeNode(parent)
                        parent_dict[parent] = parent_node
                    node.parent = parent_node
                parent_dict[name] = node

        print("Tree created.")
        return root

    except FileNotFoundError:
        print(f"Failed to create tree. File '{file_path}' not found.")
        return None



def print_tree(root):
    if root is not None:
        for pre, fill, node in RenderTree(root):
            print("%s%s" % (pre, node.name))


def add_member(root, new_member_name, parent_name):
    # Trim leading and trailing whitespace from member and parent names
    new_member_name = new_member_name.strip()
    parent_name = parent_name.strip()

    # Check if the tree is empty
    if root is None:
        print("Tree is empty. Cannot add member.")
        return root

    # Check if the parent is the root
    if parent_name == root.name:
        parent_node = root
    else:
        parent_node = search_node(root, parent_name)

    if parent_node:
        # Create a new node for the new member
        new_node = TreeNode(new_member_name)
        new_node.parent = parent_node

        print("Member added to the tree.")
    else:
        print("Parent node not found.")

    return root


def remove_member(root, member_name):
    node_to_remove = search_node(root, member_name)
    if node_to_remove:
        node_to_remove.parent = None
        print("Member removed from the tree.")
    else:
        print("Member not found in the tree.")


def search_node(root, node_name):
    if root is None:
        return None
    for node in root.descendants:
        if node.name == node_name:
            return node
    return None


def show_person_info(root, name):
    node = search_node(root, name)
    if node:
        print(f"Name: {node.name}")
        if node.parent:
            print(f"Parent: {node.parent.name}")
        children = [child.name for child in node.children]
        if children:
            print(f"Children: {', '.join(children)}")
    else:
        print(f"Person with name '{name}' not found.")


def display_menu():
    print("Menu:")
    print("1. Create the tree")
    print("2. Print the tree")
    print("3. Add member to the tree")
    print("4. Remove member from the tree")
    print("5. Show information about a selected person")
    print("6. Exit")


def main():
    print(" _____________________________________________________________")
    print("|                                                             |")
    print("|                 PROJECT FAMILY TREE                         |")
    print("|           Author: Muhammad Muhtasim Akhtab                  |")
    print("|                &  Asaduzzaman Sifat                         |")
    print("|             ID: B210102006 & B210102007                     |")
    print("|  Department of Information And Communication Technology     |")
    print("|_____________________________________________________________|")

    choice = None
    tree = None

    while choice != '6':
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path of the tree CSV file: ")
            tree = create_tree(file_path)

        elif choice == '2':
            if tree:
                print("     ")
                print("     ")
                print("Tree:")
                print("     ")
                print_tree(tree)
                print("     ")
                print("     ")

            else:
                print("Tree is empty.")

        elif choice == '3':
            if tree:
                name = input("Enter member name: ")
                parent = input("Enter parent name: ")
                add_member(tree, name, parent)
            else:
                print("Tree is empty.")

        elif choice == '4':
            if tree:
                name = input("Enter member name to remove: ")
                remove_member(tree, name)
            else:
                print("Tree is empty.")

        elif choice == '5':
            if tree:
                name = input("Enter name of person to show information: ")
                show_person_info(tree, name)
            else:
                print("Tree is empty.")

        elif choice == '6':
            print("Exiting program.")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
