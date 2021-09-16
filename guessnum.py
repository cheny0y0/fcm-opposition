import os, random, sys, time

try :
    raw_input
except NameError :
    py_ver = "3.x"
else :
    py_ver = "2.x"

while 1 :
    try :
        while 1 :
            print("Whenever you press Ctrl-C to exit.")
            if py_ver == "2.x" :
                gamemode = raw_input("Select a game mode: 1. 1-player 2. 2-player")
            if py_ver == "3.x" :
                gamemode = input("Select a game mode: 1. 1-player 2. 2-player")
            if gamemode.strip() not in ["1", "2"] :
                print("Invalid choice. Choose again.")
            else :
                break
        while 1 :
            if py_ver == "2.x" :
                startnum = raw_input("Current number from:")
            if py_ver == "3.x" :
                startnum = input("Current number from:")
            try :
                startnum = int(startnum.strip())
            except (TypeError, ValueError) :
                print("Invalid start number. Input again(must be integer).")
            else :
                break
        while 1 :
            if py_ver == "2.x" :
                endnum = raw_input("Current number to:")
            if py_ver == "3.x" :
                endnum = input("Current number to:")
            try :
                endnum = int(endnum.strip())
            except (TypeError, ValueError) :
                print("Invalid end number. Input again(must be integer).")
            else :
                if endnum <= startnum :
                    print("End number must be bigger than the start number.")
                else :
                    break
        if gamemode == "1" :
            num = random.randint(startnum, endnum)
        if gamemode == "2" :
            while 1 :
                if py_ver == "2.x" :
                    num = raw_input("Current number to guess:")
                if py_ver == "3.x" :
                    num = input("Current number to guess:")
                try :
                    num = int(num.strip())
                except (TypeError, ValueError) :
                    print("Invalid number. Input again(must be integer).")
                else :
                    if startnum <= num <= endnum :
                        break
                    else :
                        print("The number must be between the start number and the end number.")
        while 1 :
            if py_ver == "2.x" :
                trial = raw_input("How many trials?")
            if py_ver == "3.x" :
                trial = input("How many trials?")
            try :
                trial = int(trial.strip())
                if trial <= 0 :
                    raise ValueError
            except (TypeError, ValieError) :
                print("Invalid argument. Input again.")
            else :
                break
        if gamemode == "2" :
            if os.name == "nt" :
                os.system("cls")
            else :
                os.system("clear")
    except (KeyboardInterrupt, EOFError) :
        sys.exit(0)
    for i in range(1, trial+1) :
        trial -= 1
        while 1 :
            try :
                if py_ver == "2.x" :
                    ans = raw_input("Remaining trials: %d  Guess a number between %s and %s. What number do you guess?"%(trial, startnum, endnum))
                if py_ver == "3.x" :
                    ans = input("Remaining trials: %d  Guess a number between %s and %s. What number do you guess?"%(trial, startnum, endnum))
                try :
                    ans = int(ans.strip())
                    if startnum > ans or endnum < ans :
                        raise ValueError
                except (TypeError, ValueError) :
                    print("Please input an integer.")
                else :
                    break
            except (KeyboardInterrupt, EOFError) :
                try :
                    if py_ver == "2.x" :
                        raw_input("If you really want to exit, please press Ctrl-C again.")
                    if py_ver == "3.x" :
                        input("If you really want to exit, please press Ctrl-C again, otherwise press enter.")
                except KeyboardInterrupt :
                    sys.exit(0)
                except EOFError :
                    pass
        if ans > num :
            print("Your answer is greater than the correct number.")
        if ans < num :
            print("Your answer is less than the correct answer.")
        if ans == num :
            print("Congratulations! You used %d trial(s)."%i)
            break
        if trial == 0 :
            print("You lose. The correct number is: %d"%num)
