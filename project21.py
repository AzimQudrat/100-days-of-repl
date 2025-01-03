"""Test your family and friends on their multiplication knowledge (or just be really mean to people you know and ask them to work out their multiplication tables for 5,474,000,000....)

Prompt the user by asking for a multiplication table for the number of their choice.
Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
Why not give users an emoji if they get all 10 math facts correct?"""

print("Math Game!")

multiples = int(input("Name your multiples: "))

points = 0

for x in range(1, 11):
    question = f"{x} X {multiples} = "
    answer = int(input(question))

    if(answer == x * multiples):
        print("Nice")
        points += 1
    else:
        print("Wrong the answer is:", x * multiples)

if points == 10:
    print("\nOMG YOU GOT THEM ALL RIGHT!!")
else:
    print("\nYou scored", points, "out of 10.")

