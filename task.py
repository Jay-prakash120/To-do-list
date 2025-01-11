import json

# Create an empty list for store data 
task_list = []
c = 0

# Load the data avilable in 'plan.json' file
with open("plan.json", "r") as f:
    task_list = json.load(f)

# Store data in 'plan.json' file to keep it non-volatile        
def save_task(task_list):
    with open("plan.json", "w") as file:
        return json.dump(task_list, file)

# showing only pending task
def view_pending():
    print("\nPending Task:\n")
    for index,item in enumerate(task_list):
        if (item["status"]=="Not complete"):
            print(f"{index + 1}. {item["Task"]}\n")
            if item["Roadmap"]!="Not Avilable":
                roadmap(index)
            else:
                print("\n\nRoadmap not avilable!\n\n")    
    print("\n")

def roadmap(index):
    road_data = task_list[index]
    if road_data["Roadmap"] != "Not Avilable":
        print(f"\n\nRoadmap to complete '{road_data["Task"]}' :\n\n{road_data["Roadmap"]}")
    print("\n\n")    

# Show only completed task
def view_completed():
    c = 0
    print("Completed Tasks✅ :\n")
    for index, item in enumerate(task_list):
        if item["status"] == "Completed":
            print(f"{index + 1}. {item['Task']}\n")
            if item["Roadmap"]!="Not Avilable":
                roadmap(index)
            else:
                print("\n\nRoadmap not avilable!\n\n")  
            c = c + 1
    if c == 0:
        print("\nNothing to show in completed task !")        
    print("\n")
          
while True:

    print("1. ➕ Add Task")
    print("2. 📋 View pending Task")
    print("3. ✅ Mark As Complete")
    print("4. 📌 Add Roadmap To Complete Task")
    print("5. 🔍 View Roadmap")
    print("6. 📊 Report")
    print("7. 🗑️ Delete any task")
    print("8. 🔙 Exit")
    choice = input("Enter Choice: ")

    # choice '1' is responsible for add new task and store it in List
    if choice =="1":
        task = input("\n\nEnter Task: ")
        #view_pending()
        roadmap_choice = input("Do you want to add a roadmap for this task(Y/n):  ")
        if roadmap_choice == "y" or "Y":
            add_roadmap = input("Enter roadmap: ")
            task_list.append({"Task" : task, "status": "Not complete", "Roadmap" : add_roadmap})
        else:
            task_list.append({"Task" : task, "status": "Not complete", "Roadmap" : "Not Avilable"})
        print("\nTask Added succesfully!")    
            
    # Choice '2' is for view the incomplete task
    if choice =="2":
        view_pending()
            
    # Choice '3' is for mark any task as complete
    if choice == "3":
        index = task_list[int(input("\n\nEnter Task Number To Mark As Complete: ")) - 1]
        mark = index["status"] = "Completed"
        print(f"\nTask: '{index["Task"]}'  Marked As Completed!\n\n")
        view_pending()

    # Choice '4' is responsible for add a roadmap for a task
    if choice == "4":
        task_data = task_list[int(input("\n\nEnter Task number to add Roadmap: ")) - 1]
        task_data["Roadmap"] = input(f"\nEnter Roadmap For {task_data["Task"]}: \n\n")
        print("\nRoadmap added succesfully!\n\n")
        view_pending()

    # Choice '5' is for view avilable roadmap of a task
    if choice == "5":
        index = int(input("\n\nEnter Task Number To View it's Roadmap: ")) - 1
        roadmap(index)

    # Choice '6' is responsible for view all the task and their status, and roadmap
    if choice == "6":
        print("\n\nReport:")
        view_pending()
        view_completed()
        print("\n")

    if choice == "7":
        del_task = int(input("\nEnter task number to delete: ")) - 1
        item_in_list = task_list[del_task]
        task_in_item = item_in_list["Task"]
        del task_list[del_task]
        print(f"\nTask: '{task_in_item}' deleted!\n\n")
        view_pending()

    save_task(task_list)
    
    # The last option is responsible for end the execution 
    if choice == "8":
        print("\n\nT H A N K  Y O U 😊\n\nP R O G R A M  E N D E D !\n\n")
        break