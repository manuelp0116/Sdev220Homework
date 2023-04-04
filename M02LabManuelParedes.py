"""
M02Lab StudentList selector.
Manuel paredes    

This app will ask for students last name and GPA and then decide if they go to Dean's list or honor roll, the program
decides this with the GPA ranges needed to enter in each list.    
"""


studentLast = input("Enter student last name or ZZZ to exit the program ")

while studentLast != "ZZZ": # the progream will keep running until ZZZ is input.
    studentGpa = float(input("what is " + studentLast + " GPA? "))
    
    if studentGpa >= 3.5 : # dean's list if student gpa is 3.5 or higher 
        print(studentLast + " has  made the Dean's List")
        studentLast = input("Enter student last name or ZZZ to exit the program")
        
        
    elif studentGpa >= 3.25 and studentGpa < 3.5: # honor roll list if student GPA is 3.25 or higher 
        print(studentLast + " has made the honor Roll")
        studentLast = input("Enter student last name or ZZZ to exit the program")
        
    else: # added an extra list, rest of students with a GPA lower than 3.25
        print(studentLast + "didn't make it to honor roll")
        studentLast = input("Enter student last name or ZZZ to exit the program")
        
    
