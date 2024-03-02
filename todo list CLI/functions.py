todos_file = "todos.txt"

def get_todos():
    with open(todos_file, 'r') as f:
        todos = f.readlines()
    return todos

def commit_todos(list):
    with open(todos_file, 'w') as f:
        f.writelines(list)

    

    
    