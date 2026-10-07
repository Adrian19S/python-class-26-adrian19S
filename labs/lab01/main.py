# Starting file for LAB 1
# Include your course number, student first and last name, and date in the comment header
#CS 31 Adrian S. 10/7/26

print("My Awesome Quiz on Python Concepts")
print() # prints an empty line
print("*"*20) # print a line of 20 astericks

# Ask for the user's name
print()
username = input ("What is your name?") 
print(f"Hello, {username}!") # f-string format

#Ask if they want to take the quiz

print()
start_quiz = input("Do you want to take my awesome quiz? Y/N")
if start_quiz == "Y"or start_quiz == "y":
    print("Great! Let's get started!")
    #put ourr quiz questions here all indented sadly

    #Set our counter to 0 
    counter = 0 

    #Question 1 
    q1 = int(input("How would Python solve 3 * 3? "))
    if q1 == 9: 
        #update my counter because they got the answer right 
        counter += 1 # shorthand for counter = counter + 1 
        print("Yes! You are correct. Python would solve this as 9.") 
    else: #INCORRECT 
        print("Sorry. That is not correct.") 


        #Question 2 

        
        

    #Question 3


    #Question 4


    #Question 5




    #Output the score
    print("****YOUR FINAL SCORE****")
    print(f"Your final score is: {counter}")

    #if counter == 5: 
    print("You are a rockstar! You got them all correct!")
    #if counter == 4:
    print ("Good job!")
    #if counter ==3:
    print ("Nice")
    #if counter ==2:
    print ("Try again")
    #if counter ==1:
    print("You should probably try again lol")


 

elif start_quiz== "N":
    print("Sorry, maybe next time!")


else: #if they type anything else tell them its invalid
    print("Sorry. That is an invalid response. Try again.")