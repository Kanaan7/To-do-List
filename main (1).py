import json

fileName = "todo.json"


#choice menu
def choices():
    print("")
    print("Your To Do List")
    print("(1) View List")
    print("(2) Add a To DO")
    print("(3) Delete To Do")
    print("(4) Edit To Do")
    print("(5) Exit")


#viewing data
def view_list():
    with open(fileName, 'r') as f:
        temp = json.load(f)
        for entry in temp:
            x = 0
            todo = entry["To-Do"]
            due_date = entry["Due"]
            bio = entry["description"]
            print(f"index Number {x}")
            print(f"To-Do: {todo}")
            print(f"Due: {due_date}")
            print(f"description : {bio}")
            print("\n\n")
            x = x + 1


#check system for data
def check():
    with open(fileName, 'r') as f:
        temp = json.load(f)
        for entry in temp:
            if len(temp) == 0:
                print("there is no data in the system at the moment!!")


#delete data
def delete_list():
    view_list()
    newData = []
    with open(fileName, "r") as f:
        temp = json.load(f)
        dataLen = len(temp) - 1
    print("which index number would you like to delete?")
    deleteOpt = input(f"select a number 0-{dataLen}")
    x = 0
    for entry in temp:
        if x == int(deleteOpt):
            pass
            x = x + 1
        else:
            newData.append(entry)
            x = x + 1
    with open(fileName, "w") as f:
        json.dump(newData, f, indent=4)


#adding data
def add_toList():
    list_info = {}
    with open(fileName, "r") as f:
        temp = json.load(f)
        list_info["To-Do"] = input("To-do: ")
        list_info["Due"] = input("Due by: ")
        list_info["description"] = input("notes: ")
        temp.append(list_info)
        with open(fileName, "w") as f:
            json.dump(temp, f, indent=4)


#update data
def update_list():
    view_list()
    newData = []
    with open(fileName, "r") as f:
        temp = json.load(f)
        dataLen = len(temp) - 1
    print("which todo list would you like to update  ?")
    print("")
    edit = input(f"select a number 0-{dataLen}")
    x = 0
    i = 0
    for entry in temp:
        if x == int(edit):
            todo = entry["To-Do"]
            due = entry["Due"]
            bio = entry["description"]
            print(f"current To-Do: {todo}")
            todo = input("enter new To-Do \n")
            print(f"current Due: {due}")
            due = input("enter new Due\n")
            print(f"current description: {bio}")
            bio = input("enter new description\n")
            newData.append({"To-Do": todo, "Due": due, "description": bio})
            x = x + 1
        else:
            newData.append(entry)
            i = i + 1
    with open(fileName, "w") as f:
        json.dump(newData, f, indent=4)


#main loop
while True:
    choices()
    chioce = input("\nEnter Number: ")
    if chioce == "1":
        view_list()

    elif chioce == "2":
        add_toList()
    elif chioce == "3":
        delete_list()
    elif chioce == "4":
        update_list()
    elif chioce == "5":
        break
    else:
        print("you did not enter a number, please read carefully.")
