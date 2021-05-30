def GuestList():
    #declare a list of six friends
    friends = ["Ross","Rachel","Chandler","Monica","Joey","Phoebe"]
    guestList = []
    #loop through the list
    for friend in friends:
        #ask the user to enter guest in each list
        print("Enter guest list for ",friend,":")
        lst = input().split(" ")
        #append the lists in guestList as a set
        guestList.append(set(lst))
    #declare a list to store all the friends
    unified_list = []
    #extract each set, take each of its element and put them into list
    for guests in guestList:
        for i in range(len(guests)):
            unified_list.append(list(guests)[i])
    #make a set of that list
    unified_set = set(unified_list)
    #remove the first element because the first element will be an empty string
    
    #return the set
    return unified_set
if __name__ == "__main__":
    #call and print the set
    print("The unified set of guest is:\n",GuestList())
