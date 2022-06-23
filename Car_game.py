print("""
start --> to start the car
fast --> to speed up the car
veryfast --> to speed up to the top speed car
nitro--> exausting nitro and speed up
slow --> to slow down the car
brake--> to handbrake the car 
stop --> to stop the car
quit --> to quit the game
        """)

command = ""
while command != "quit":

    command=input(">")
    if command=="start":
        print("The car is starting")
    elif command=="fast":
        print("The car is running fast")
    elif command=="veryfast":
        print("The car is running on top speed")
    elif command=="nitro":
        print("The car is exhausting nitro and running on super speed")
        
    elif command=="slow":
        print("The car speed is slowing down")
    elif command=="brake":
        print("The car is drifting for handbraking")
    elif command=="stop":
        print("The car is stopped")
   
    else:
        print("Please enter a valid input")

   