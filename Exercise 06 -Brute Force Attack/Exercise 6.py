max_Trys=5 
for attempt in range(1,max_Trys + 1): #Creating a finite loop for the user
      Password=int(input("Enter your password:")) #Declaring what the loop will be repeating
      correct_password=12345
      if Password == correct_password: # Creating a statemnt to exit the loop
       print("Your password is correct")
       break
      
      else:
          remmaining= max_Trys-attempt # Creating a statement to tell the user how many times will the loop continue
          if remmaining>0: # Creating a statemnt in case the user can't exit the loop
              print(f"Wrong password you have {remmaining} attempts") 

          else:
              print("maximum attempts reached")
              



    


