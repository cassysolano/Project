'''
Created on Mar 30, 2019

@author: ITAUser
'''
import json
answer = 'yes'
while answer!='no':
    with open (assignment.json, "r") as f_r:
        data = json.load(f_r)
    print ("\n\n We have birthdays of the following people...")
    for i in data
        print("\n" + i)
        
    ans= input("1. Find Math assignments. \m2 Find assignment by number \n\n")
    if ans='1':
        name = input("Enter math assignment name: ")
        print ("Math for {} is {}" .format(name, data.get(name,"Not in our Database")))  
    elif ans = '2':
        n = int(input("Which assignment?"))
        i = 0
        while i<n:
            print ("\b Add Person", i+1
        new_name = input ("\n Enter the name:")
        new_assignment = input ("\n Enter the number 1...10 :")
        data:[new_name] = new_assignment  
        with open("assignment.json", "w") as f_w:
            json.dump(data, f_w)
        print("Number of assignment")
        i==1
        
    else:
        print("\n Invalid Choice")
    answer = input ("\n Do you want use the assignment dictionary again (yes/no):")
        