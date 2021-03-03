

# python program to illustrate nested If statement 
#!/usr/bin/python 
i = 10
if (i == 10): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too")
        if (i < 12):
            print("3rd level if")
        
            if (i < 12): 
                print ("i is smaller than 12 too")
                if (i < 12):
                    print("3rd level if")
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
                print ("i is greater than 15")
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
        print ("i is greater than 15")
else:
    print("First nesting")