import functions
import time

now = time.strftime("%b %d, %Y %H:%m:%S")
print('it is ' + now)

while True:
    intro = input('Please type - add, show, edit, complete or exit: ')
    intro = intro.strip()
    
    match intro:
        case 'add':
            todos = functions.get_todos()
            user_input = input('Please type a todo to add: ')
            todos.append(user_input + '\n')
            functions.commit_todos(todos)
        case 'show':
            todos = functions.get_todos()
            for idx, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{idx +1} - {item}"
                print (row)
        case 'edit':
            todos = functions.get_todos()
            num = int(input('Please type a todo number to edit: '))
            user_input = input('Please type a new todo: ')
            todos[num -1] = user_input + '\n'
            functions.commit_todos(todos)
        case 'complete':
            todos = functions.get_todos()
            num = int(input('Please type a todo number to mark as completed: '))
            todos.pop(num - 1)
            functions.commit_todos(todos)
        case 'exit':
            print('Bye bye!')
            break
        case any:
            print('Your option is invalid')


