#Day 4 focused on learning Python's match-case statement (introduced in Python 3.10).

#In this program:
#- The user enters their favourite IPL team
#- The program matches the input with predefined cases
#- Based on the match, it displays the team captain
#- A default case handles invalid inputs

#Concepts practiced:
#- match-case control flow
#- Input validation using strip() and lower()
#- Writing cleaner and more readable conditional logic

This approach is an alternative to if-elif-else and helps write structured decision-based programs.
y=input("please enter your favourate ipl team:")
match y:
    case "csk":
        print("your team's  captain is mr.gaikwad")
    case "rcb":
        print("your team's captain is mr.patidar")
    case "mi":
        print("your team's captain is mr.pandya")
    case "gt":
        print("your team's captain is mr.gill")
    case "pbks": 
        print("your team's captain is mr.iyer")
    case "rr":
        print("your team's captain is mr.parag")
    case "dc":
        print("your team's captain is mr.rahul")
    case "kkr":
        print("your  team's captain is mr.khan")
    case "srh":
        print("your team's captain is mr.cummins")
    case _:
        print("please enter valid team name")
        
print("thank you")
