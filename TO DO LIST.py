todo=[]
def show_menu():
    print("1.view task")
    print("2.Add task")
    print("3.remove task")
    print('4.exit')
while True:
    show_menu()
    choice=int(input("enter your choice"))
    if (choice==1):
        if not todo:
            print("no tasks to show")
        else:
            for idx,task in enumerate(todo,1):
             print(f"{idx}.{task}")
    elif (choice==2):
        print("enter task to be added")
        t=input()
        todo.append(t)
        print("task added")
    elif (choice==3):
        if not todo:   
        print("nothing to remove")
        else:
         for idx,task in enumerate(todo,1):
            print(f"{idx}.{task}")
         try:
            task_num=int(input("enter task no to remove"))
            removed=todo.pop(task_num-1)
            print(f"removed:{removed}")
        except(ValueError,IndexError):
            print("invalid task no")
    elif(choice==4):
     print("goodbye")
     exit
    else:
       print("invalidchoice")

