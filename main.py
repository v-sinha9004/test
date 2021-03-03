

# python program to illustrate nested If statement 
#!/usr/bin/python 
i = 10
if (i == 10):
    print("1st level if") 
    if (i < 15): 
        print ("2nd level if") 
    if (i < 12): 
        print ("2nd level if")
        if (i < 12):
            print("3rd level if")
            if (i < 12): 
                print ("4th level if")
                if (i < 12):
                    print("5rd level if")
                else:
                    print("5rd level else")
                    if (i < 12):
                        print("6th level if")
                        if (i < 12):
                            print("7th level if")
                        else:
                            print("7th level else")
                    else:
                        print("6th level else")
            else: 
                print ("4th level else")
        else:
            print("3rd level else")
            if (i < 12):
                print("4th level if")
                if (i < 12):
                    print("5th level if")
                else:
                    print("5th level else")
            else:
                print("4th level else")
    else: 
        print ("2nd level else")
else:
    print("1st level else")