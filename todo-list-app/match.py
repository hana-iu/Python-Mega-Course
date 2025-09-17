todos = []
while True: 
    user_action= input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()
    match user_action:
        case 'add': 
            todo = input("Enter a task: ")
            todos.append(todo)
        case 'show' | 'display':
            i = 1
            for item in todos: 
                item = item.title()
                print(f"{i}. {item}")
                i = i+1
        case 'edit':
            number = int(input("Enter the number of the task you want to edit: "))
            number = number - 1
            new_todo = input("Enter the edit: ")
            todos[number] = new_todo
        case 'exit': 
            print("Bye Bye....")
            break
        case _: 
            print("Hey, you entered an unknown command!")