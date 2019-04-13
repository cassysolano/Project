'''
Created on Apr 13, 2019

@author: ITAUser
'''
import json
answer='yes'
while answer!='no':
    with open("birthdays_1.json","r") as f_r:
        data = json.load(f_r)
    
    print("\n\nWe have birthdays of the following people...")
    for i in data:
        print ("\n" + i)
    
    ans = input("1. Find somebody's birthday. \n2. Add birthday \n\n")
    if ans=='1':
        name = input("Enter the person's name: ")
        print ("The birthday for {} is {}".format(name, data.get(name, "not in our database")))
     
    elif ans=='2':
        n = int(input("How many birthdays do you wanna add? (max 3 at a time) "))
        i=0
        while i<n:
            print("\n Add Person ",i+1)
            new_name = input("\nEnter the name: ")
            new_birthday = input("Enter their birthday (dd/mm/yyyy):")
            data[new_name] = new_birthday
            with open("birthdays_1.json", "w") as f_w:
                json.dump(data, f_w)
            
            print ("Birthday Added!")
        
            i+=1
    
    else:
        print("\nInvalid Choice!")
    answer = input("\nDo you wanna use again (yes/no): ")