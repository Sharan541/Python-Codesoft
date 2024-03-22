tsk=[]
def addtask():
    t=str(input())
    tsk.append(t)
    print("Task is added")
def deltask():
    t=int(input())
    if t>len(tsk):
        print("Task doesn't exist")
    else:
        tsk.remove(tsk[t-1])
def listtask():
    if not tsk:
        print("The Tasklist is empty")
    else:
        for i in range(len(tsk)):
            print (i+1,tsk[i],sep=" )")

if __name__=="__main__":
    while True:
        print("============================================")
        print("This is To-Do lsit task application")
        print("============================================")
        print("please select one option from below ")
        print("1) Add a task")
        print("2) delete a task")
        print("3) List the tasks")
        print("4) Quit")
        print("choose the option you are looking for:")
        c=int(input())
        if c==1:
            print("Enter the task to be added :")
            addtask()
        elif c==2:
            print("Which task ned to be deleted :")
            deltask()
        elif c==3:
            print("The tasks are :")
            listtask()
        elif c==4:
            break
        else:
            print("Please give a valid input")
    print("Good byee")