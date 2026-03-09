import pytest 
from task_cli import save_tasks,load_tasks,add_task,update_task,delete_task

def test_add_tasks(tmp_path):
    """Checks if a task was added to task file"""
    test_file = tmp_path / "tasks.json"
    result = add_task("Test task",test_file)
    assert result["task_description"] == "Test task"

def test_status_new(tmp_path):
    """Checks if an added task has status 'to do' """
    test_file = tmp_path / "tasks.json"
    result = add_task("Test task",test_file)
    assert result["status"] == "to do"

def test_edit_task(tmp_path):
    """Checks if task changes are saved"""
    test_file = tmp_path / "tasks.json"
    add_task("Test task",test_file)
    update_task(1,"in progress",test_file)
    task_list = load_tasks(test_file)
    updated = next(c for c in task_list if c["status"] == "in progress")
    assert updated["status"] == "in progress"

def test_delete_task(tmp_path):
    """Checks if task are deleted"""
    test_file = tmp_path / "tasks.json"
    add_task("Test task",test_file)
    delete_task(1,test_file)
    task_list = load_tasks(test_file)
    assert len(task_list) == 0