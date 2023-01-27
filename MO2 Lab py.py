students = int(input('Enter number of students: ')) #input for user to enter the amount of times to loop the program for the number of students

for i in range (students): # loop for previous input
    Lname = str(input('Enter student\'s last name or ZZZ to exit: ')) # input for last name or if user wants to exit

    while Lname != 'ZZZ': # while loop to make sure user does not want to quit the program
        Fname = str(input('Enter student\'s first name: ')) # input for the first name
        gpa = float(input('Enter the students GPA: ')) # input for gpa

        if gpa >= 3.5: # if statement to check if students made it deans list
            print(Fname, Lname, 'made it onto the Dean\'s') # printing if students made it
            break # break to end the loop so next user can be entered

        elif gpa >= 3.25: # elif statement to check for honor roll
            print(Fname, Lname, 'made it onto the Honor Roll')
            break
        
        else: # final else statement to tell user they made it on neither
            print(Fname, Lname, 'did not make it onto the Honor Roll or Dean\'s list ')
            break