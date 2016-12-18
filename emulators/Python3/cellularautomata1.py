while 1:
    #change me to change screen size

    x=5
    y=5

    #remove the triplequotes to do the screen yourself, it'll calulate the x and y values if you do this
    """
    screen=[
        ["A","B","A","A","B"]
        ]
    """

    #Sanik mode, goes FAST, 0=off, 1=on

    sanikmode=0
    

    #end



    """
    Ruleset.

    A always becomes B

    B becomes 0 if next to an A and A if it's not

    0 becomes A if next to an A and 0 if it's not


    000A000->000B000

    000B000->000A000, 000BA00->0000A00

    0000A00->000AA00
    """


    import time, os, random, msvcrt
    if os.name=="nt":
        import colorama

    def loopermath(number,loop,op):
        if op==0:
            number=number+1
            if number>loop:
                number=0
            return number
        else:
            number=number-1
            if number<0:
                number=loop
            return number

    def pause():
        print("\rPress any key to continue . . . ", end="")
        msvcrt.getch()
        print()

    try:
        screen
    except NameError:
        screen=[]

        chars=["A","\033[1m\033[32mB\033[22m\033[37m","\033[35m0\033[37m"]

        for i in range(y):
            row=[]
            for j in range(x):
                pixel=random.choice(chars)
                row.append(pixel)
            screen.append(row)
    else:
        y=len(screen)
        x=len(screen[0])

        for i in range(y):
            for j in range(x):
                if screen[i][j]=="A":
                    screen[i][j]="A"
                elif screen[i][j]=="B":
                    screen[i][j]="\033[1m\033[32mB\033[22m\033[37m"

    origscreen=[z[:] for z in screen]

    history=[]

    cycles=0

    while 1:
        os.system('cls' if os.name=='nt' else 'clear')
        for i in range(y):
            for j in range(x):
                print(screen[i][j], end="")
            print()

        history.append([z[:] for z in screen])

        tempscreen=[z[:] for z in screen]
        for i in range(y):
            for j in range(x):
                curchar=tempscreen[i][j]

                back=tempscreen[i][loopermath(j,x-1,1)]
                front=tempscreen[i][loopermath(j,x-1,0)]

                if y==1:

                    if curchar=="A":
                        screen[i][j]="\033[1m\033[32mB\033[22m\033[37m"

                    elif curchar=="\033[1m\033[32mB\033[22m\033[37m":
                        if back=="A" or front=="A":
                            screen[i][j]="\033[35m0\033[37m"
                        else:
                            screen[i][j]="A"

                    else:
                        if back=="A" or front=="A":
                            screen[i][j]="A"
                        else:
                            screen[i][j]="\033[35m0\033[37m"
                else:
                    top=tempscreen[loopermath(j,y-1,0)][j]
                    bottom=tempscreen[loopermath(j,y-1,1)][j]

                    if curchar=="A":
                        screen[i][j]="\033[1m\033[32mB\033[22m\033[37m"

                    elif curchar=="\033[1m\033[32mB\033[22m\033[37m":
                        if back=="A" or front=="A" or top=="A" or bottom=="A":
                            screen[i][j]="\033[35m0\033[37m"
                        else:
                            screen[i][j]="A"

                    else:
                        if back=="A" or front=="A" or top=="A" or bottom=="A":
                            screen[i][j]="A"
                        else:
                            screen[i][j]="\033[35m0\033[37m"

        cycles+=1
        if sanikmode==0: time.sleep(1)
        if screen==origscreen:
            os.system('cls' if os.name=='nt' else 'clear')
            for i in range(y):
                for j in range(x):
                    print(screen[i][j], end="")
                print()
            print("Original orientation found!")
            pause()
            break

    #history display

    print()

    for k in range(len(history)):
        for i in range(y):
            for j in range(x):
                 print(history[k][i][j], end="")
            print("\n")
    print("\nAnd of course.\n")
    for i in range(y):
        for j in range(x):
             print(origscreen[i][j], end="")
        print("\n\nCycles to complete: "+str(cycles)+"\n")

    pause()


#made for Lock#2757 on Discord, apparently an antimatter/matter thing, really just cellular automata