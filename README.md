Task Manager

Task Manager is a Python-based CLI (Command Line Interface) application designed to help you organize and manage your tasks effectively. It allows you to add tasks, mark them as complete, associate roadmaps, and view reports of pending and completed tasks.

Features

Add Tasks: Add new tasks with an optional roadmap.

View Pending Tasks: Display tasks that are not yet completed.

Mark as Complete: Mark tasks as completed when finished.

Add Roadmap: Add a step-by-step roadmap to guide the completion of a task.

View Roadmap: View the roadmap associated with a task.

Generate Report: Display a summary of all pending and completed tasks along with their roadmaps.

Delete Tasks: Remove tasks that are no longer needed.

Persistent Storage: All tasks are saved in a plan.json file for future access.


Installation

1. Clone this repository:

https://github.com/Jay-prakash120/To-do-list

2. Navigate to the project directory:

cd task-manager


3. Install Python (if not already installed). Ensure you have Python 3.x installed.



Usage

1. Run the script:

python task.py


2. Follow the on-screen prompts to manage your tasks.



Menu Options

1. ➕ Add Task
Add a new task to the list. Optionally, you can include a roadmap for the task.


2. 📋 View Pending Task
Display a list of tasks that are not yet completed.


3. ✅ Mark As Complete
Mark a specific task as completed.


4. 📌 Add Roadmap To Complete Task
Add or update a roadmap for a specific task.


5. 🔍 View Roadmap
View the roadmap for a particular task.


6. 📊 Report
View a detailed report of all tasks categorized as pending or completed.


7. 🗑️ Delete any Task
Remove a task permanently from the list.


8. 🔙 Exit
Exit the application. All changes are saved to plan.json.



File Structure

task.py: Main script to run the task manager.

plan.json: JSON file that stores task data persistently.


JSON Structure

Tasks are stored in plan.json with the following format:

[
    {
        "Task": "Task description",
        "status": "Not complete",
        "Roadmap": "Roadmap description"
    },
    {
        "Task": "Another task description",
        "status": "Completed",
        "Roadmap": "Roadmap description"
    }
]

Example Workflow

1. Add a task:

Enter Task: Complete Python project
Do you want to add a roadmap for this task(Y/n): Y
Enter roadmap: Plan the modules, write code, test the application
Task Added successfully!


2. View pending tasks:

Pending Task:
1. Complete Python project
Roadmap to complete 'Complete Python project':
Plan the modules, write code, test the application


3. Mark the task as complete:

Enter Task Number To Mark As Complete: 1
Task: 'Complete Python project' Marked As Completed!



License

This project does not have a license yet.
If you'd like others to contribute or use your code, consider adding a license. For more information, visit the Choose a License website.

Acknowledgments

Thanks to all Python developers and contributors for making programming accessible and enjoyable.
