###Program that turns graded NUMBERS into LETTERS
def grade_to_letter():
    while True:
        grade = (float(input("Please enter your grade: ")))
        if 0 <= grade <=10:
            break
        else:
            print("Error: Only grades from 0 to 10!")
         
    while True:
        if grade >=9: print("\nYou got an A") 
        
        elif 7<= grade <=8.99: print("\nYou got a B")
        
        elif 5<= grade <=6.99: print("\nYou got a C")
        
        elif 3<= grade <=4.99: print("\nYou got a D")
        
        elif 0.59<= grade <=2.59: print("\nYou got an E")
        
        elif grade <0.59: print("\nYou got an F")

        break

grade_to_letter()
        