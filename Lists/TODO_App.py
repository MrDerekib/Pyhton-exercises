header = """

  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/

"""
help = """

TODO LIST HELP.
Type 'q' to quit 
To add a todo to the list type it and hit enter.
To complete a todo enter its number

"""
dots = "***********************************"
instructions = "Enter a command. Type 'h' for help: "
print(header)
print(dots)
todo = []
todo_done = []
command = ""


def show_todo():
    for idx in range(len(todo)):
        print(f"{idx +1}) {todo[idx]}")


while True:
    command = input(instructions)
    if command.lower() == "h":
        print(help)
        print(dots)
    elif command.isnumeric():
        if int(command) <= len(todo):
            done = todo.pop(int(command) - 1)
            todo_done.append(done)
            print(f"-> {done} COMPLETED!! 🥳")
            show_todo()
            print(dots)
        else:
            print("Wrong task number, try again")
    elif command.lower() == "q":
        print(f"Today you completed {len(todo_done)} TODOS:")
        for task in todo_done:
            print(f"* {task}")
        break
    else:
        todo.append(command)
        show_todo()
        print(dots)
