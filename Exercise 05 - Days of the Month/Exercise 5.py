Day={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,  # Creating a dictionary
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

answer="yes"
Month_Days=int(input("Chose a mouth number from (1-12):"))

if 1 <= Month_Days <= 12: # mantioning the dictionary in order for it to work in the following statements
 if Month_Days == 2: #creating a statement for the second line of the dictionary
    year = int(input("Enter the year: "))
        
       #This line was inpired in Copilot Ai
    if (year / 4 == 0 and year / 100 != 0) or (year / 400 == 0):

        print("It's a leep year February has 29 days")

    else:
        print("February has 28 days")

 else:  
    print(f"Month number {Month_Days} has {Day} days.")

else:   #creating a statement for the input numbers that are outside the dictionary
   print("invalid Month number")
















    
