from pathlib import Path 
import json
from datetime import datetime
import sys

file = Path('tasks.json')

def load_tasks(filepath=file):
    """Loads json file if exists or creates a new one if not"""
    if filepath.exists():
        contents = filepath.read_text(encoding="utf-8")
        return json.loads(contents)
    return [] 

def save_tasks(task,filepath=file): 
    """converts data and saves content to json file"""
    contents = json.dumps(task,indent=4,ensure_ascii=False)
    filepath.write_text(contents)

def add_task(description,filepath=file): 
    """Creates a new task and adds it ti the json file"""
    tasks_list =load_tasks(filepath)
    
    new_task = {
            "task_id" : len(tasks_list)+1,
            "task_description":description,
            "creation_date":datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "modification_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "status":'to do'
        }
    tasks_list.append(new_task)
    save_tasks(tasks_list,filepath)
    print('Task added to list!')
    return new_task
    

def show_tasks(filepath=file): 
    """Displays current task list"""
    tasks_list = load_tasks(filepath)
    if not tasks_list: 
        print ('Task list is empty!')
        return
    for task in tasks_list: 
        print(f'Task ID: {task["task_id"]} - Status: {task["status"]} - Description: {task["task_description"]} - Created: {task["creation_date"]} - Last modified: {task["modification_date"]}')

def update_task(task_id, new_status,filepath=file):
    """Updates a new status fue an existing task"""
    tasks_list = load_tasks(filepath)
    if new_status.lower() not in ['to do', 'in progress','done','not done']: 
        print("Status not valid!")
        return 
    for task in tasks_list:
        if task["task_id"] == task_id: 
            task["status"] = new_status
            task["modification_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks_list,filepath)
            print(f'Changed status of Task ID #{task_id} to {new_status}')
            return
        else:
            print("Task ID not found! ")
            return 
        
def delete_task(task_id,filepath=file):
    """Deletes selected task list from json file"""
    tasks_list = load_tasks(filepath)
    for task in tasks_list: 
        if task_id == task["task_id"]:
            tasks_list.remove(task)
            save_tasks(tasks_list,filepath)
            print('Record deleted!')
            return
    print("Task ID not found!")




if __name__ == "__main__":

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
    else: 
        print("Command not found!")