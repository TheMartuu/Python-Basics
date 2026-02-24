from pathlib import Path 
import json
from datetime import datetime
import sys

file = Path('tasks.json')

def load_tasks():
    """Loads json file if exists or creates a new one if not"""
    if file.exists():
        contents = file.read_text(encoding="utf-8")
        return json.loads(contents)
    return [] 

def save_tasks(task): 
    """converts data and saves content to json file"""
    contents = json.dumps(task,indent=4,ensure_ascii=False)
    file.write_text(contents)

def add_task(description): 
    tasks_list =load_tasks()
    
    new_task = {
            "task_id" : len(tasks_list)+1,
            "task_description":description,
            "creation_date":datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "modification_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "status":'to do'
        }
    tasks_list.append(new_task)
    save_tasks(tasks_list)
    print('Task added to list!')
    

def show_tasks(): 
    tasks_list = load_tasks()
    if not tasks_list: 
        print ('Task list is empty!')
        return
    for task in tasks_list: 
        print(f'Task ID: {task["task_id"]} - Status: {task["status"]} - Description: {task["task_description"]} - Created: {task["creation_date"]} - Last modified: {task["modification_date"]}')

def update_task(task_id, new_status):
    tasks_list = load_tasks()
    if new_status.lower() not in ['to do', 'in progress','done','not done']: 
        print("Status not valid!")
        return 
    for task in tasks_list:
        if task["task_id"] == task_id: 
            task["status"] = new_status
            task["modification_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks_list)
            print(f'Changed status of Task ID #{task_id} to {new_status}')
            return
        else:
            print("Task ID not found! ")
            return 
        
def delete_task(task_id):
    tasks_list = load_tasks()
    for task in tasks_list: 
        if task_id == task["task_id"]:
            tasks_list.remove(task)
            save_tasks(tasks_list)
            print('Record deleted!')
            return
    print("Task ID not found!")

command = sys.argv[1]


if command == "add": 
    try:
        add_task(sys.argv[2])
    except IndexError:
        print("Description cannot be empty!")
elif command == "show": 
    show_tasks()
elif command == "edit": 
    try: 
        update_task(int(sys.argv[2]),sys.argv[3])
    except IndexError:
        print("Task ID or new status are missing!")
elif command == "delete": 
    try:
        delete_task(int(sys.argv[2]))
    except IndexError:
        print("Task ID missing!")