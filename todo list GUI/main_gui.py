import functions
import PySimpleGUI as psg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

psg.theme('Black')

clock = psg.Text('', key='clock')
label = psg.Text("Type a to-do")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.get_todos(), 
                       key='todos', 
                       enable_events=True,
                       size=[45,10])
edit_button = psg.Button('Edit')
complete_button = psg.Button('Complete')
exit_button = psg.Button('Exit')

window = psg.Window('To-do app', 
                    layout=[[clock],[label], [input_box, add_button], [list_box,edit_button,complete_button],[exit_button]], 
                    font=('arial', 16))

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.commit_todos(todos)
            window['todos'].Update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                idx = todos.index(todo_to_edit)
                todos[idx] = new_todo
                functions.commit_todos(todos)
                window['todos'].Update(values=todos)
            except IndexError:
                psg.popup('Please select an item first',  font=('arial', 18))
        case 'Complete':
            try:
                todo_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.commit_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                psg.popup('Please select an item first',  font=('arial', 18))
        case 'Exit':
            break  
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WIN_CLOSED:
            break
    

window.close()