# Part B — Shopping List Manager

shopping_list = []

while True:
    action = input("\nChoose an action (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to the list.")

    elif action == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check membership with 'in' before attempting to remove
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\n--- Shopping List ---")
            for item in shopping_list:
                print(item)

    elif action == "done":
        print("Goodbye! Thanks for using the Shopping List Manager.")
        break

    else:
        print("Invalid choice. Please enter 'add', 'remove', 'show', or 'done'.")