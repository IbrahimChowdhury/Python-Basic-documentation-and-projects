# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
i=0
while i<1000 :
    i+=1
    status= str(input(">"))
    if status=="help":
        print("start to run the car")
        print("stop to stop the car")
        print("exit to out of the game")
    elif status=="start":
        print("The car hs been started")
    elif status == "stop":
        print("the car has been stopped")
    elif status== "exit":
        break