import os

heading = "Welcome To KBC"
print(heading.center(50))
count_money = 0

name = input("Enter your name: ")

print(f"Hi, {name}")       #use of f-string

answer = input("Are you ready to start? ")
#1
if answer.lower() == "yes":
    print("Your First Question for 10000(Ten Thousand Rupees)")
    print("Who is the current prime minister Of Republic Of India?")
    print("a) Lal Bahadur Shastri    b) Narendra Modi")
    print("c) Rajnath Singh          d) Rahul Gandhi")
    answer = input("Enter your answer: ")

    if answer.lower() == "b":
        print("Correct Answer")
        print("Congratulations, you have won Ten Thousand Rupees")
        count_money = 10000
    elif answer.lower() in ["a", "c", "d"]:
        print("Wrong Answer")
        print("Thank You for playing")
        print("You have won", count_money)
        exit()
    else:
        print("Invalid Input")

    print("\n")

    answer = input("Are you ready for your next question? ")
    print("\n")
    # 2
    if answer.lower() == "yes":
        print("Your second question for 20000(Twenty Thousand Rupees)")
        print("What is the capital of India?")
        print("a) Delhi    b) Mumbai")
        print("c) Kolkata  d) Goa")
        answer = input("Enter your answer: ")

        if answer.lower() == "a":
            print("Correct Answer")
            print("Congratulations, you have won Twenty Thousand rupees")
            count_money = 20000
        elif answer.lower() in ["b", "c", "d"]:
            print("Wrong Answer")
            print("Thank You for playing")
            print("You have won", count_money)
            exit()
        else:
            print("Invalid Input")
    else:
        print("Thank You for playing")
        print("You have won", count_money)
        exit()

    print("\n")

    answer = input("Are you ready for your next question? ")
    print("\n")
    # 3
    if answer.lower() == "yes":
        print("Your third question for 30000(Thirty Thousand Rupees)")
        print("Which city is known as 'The city of joy'?")
        print("a) Delhi    b) Mumbai")
        print("c) Kolkata  d) Goa")
        answer = input("Enter your answer: ")

        if answer.lower() == "c":
            print("Correct Answer")
            print("Congratulations, you have won Thirty Thousand rupees")
            count_money = 30000
        elif answer.lower() in ["b", "a", "d"]:
            print("Wrong Answer")
            print("Thank You for playing")
            print("You have won", count_money)
            exit()
        else:
            print("Invalid Input")
    else:
        print("Thank You for playing")
        print("You have won", count_money)
        exit()

    print("\n")

    answer = input("Are you ready for your next question? ")
    print("\n")
    # 4
    if answer.lower() == "yes":
        print("Your third question for 40000(Forty Thousand Rupees)")
        print("Which year did India achived its Independece?")
        print("a) 1950    b) 1947")
        print("c) 1946  d) 1948")
        answer = input("Enter your answer: ")

        if answer.lower() == "b":
            print("Correct Answer")
            print("Congratulations, you have won Forty Thousand rupees")
            count_money = 40000
        elif answer.lower() in ["c", "a", "d"]:
            print("Wrong Answer")
            print("Thank You for playing")
            print("You have won", count_money)
            exit()
        else:
            print("Invalid Input")
    else:
        print("Thank You for playing")
        print("You have won", count_money)
        exit()

    print("\n")

    answer = input("Are you ready for your next question? ")
    print("\n")
    # 5
    if answer.lower() == "yes":
        print("Your third question for 50000(Fifty Thousand Rupees)")
        print("What was the british capital of India?")
        print("a) Delhi    b) Mumbai")
        print("c) Kolkata  d) Goa")
        answer = input("Enter your answer: ")

        if answer.lower() == "c":
            print("Correct Answer")
            print("Congratulations, you have won Fifty Thousand rupees")
            print("Thank You for Playing the game")
            count_money = 50000
        elif answer.lower() in ["b", "a", "d"]:
            print("Wrong Answer")
            print("Thank You for playing")
            print("You have won", count_money)
            exit()
        else:
            print("Invalid Input")
    else:
        print("Thank You for playing")
        print("You have won", count_money)
        exit()
else:
    print("Thank You")
    print("You have earned:", count_money)
    exit()






