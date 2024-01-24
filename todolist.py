# to do list
# enter 1,2,3 eg to choose menu option
def show_menu():
    print("1. Add a Task.")
    print("2. Mark Task Complete.")
    print("3. Edit a Task.")
    print("4. Remove a Task.")
    print("5. View All Tasks.")
    print("6. Quit.")


def main():
    todo = []

    while True:
        show_menu()

        user_choice = input("What would you like to do? (1-6): ")
        user_input = int(user_choice)
        # 1 = add a task
        if user_input == 1:
            print("You can add a task.")

        # 2 = mark task complete
        elif user_input == 2:
            print("You can mark a task complete.")

        # 3 = edit a task
        elif user_input == 3:
            print("You can edit a task.")

        # 4 = remove a task
        elif user_input == 4:
            print("You can remove a task.")

        # 5 = view tasks
        elif user_input == 5:
            print("You can view tasks.")

        # 6 break loop
        elif user_input == 6:
            print("Exiting Program.")
            break

        # if invalid repeat
        else:
            print("Invalid choice. Please between 1-6. ")


if __name__ == "__main__":
    main()
