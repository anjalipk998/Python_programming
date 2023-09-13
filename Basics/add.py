try:
    add =[]
    while(True):
        userchoice = int(input("enter ur choice"))
        if userchoice==1:
            add.append(str(input("enter the data")))
        elif userchoice==2:
            for a in add:
                print(a)
        elif userchoice==3:
            itemnumber =int(input("enter the index to be replaced"))
            addLength=len(add)
            if(addLength<itemnumber):
                print("out of index")
                break
        elif userchoice==4:
            exit
        else :
            print("enter a valid choice")
    
except KeyboardInterrupt:
    print("bye")