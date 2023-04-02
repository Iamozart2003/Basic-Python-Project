print("welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay Welcome :)")
score = 0

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    print("Correct Handsome!")
    score += 1
else:
    print("Wrong you Duffer")

answer = input("Who is Prime Minister of India?")
if answer.lower() == "narendra modi":
    print("Correct Handsome!")
    score += 1
else:
    print("Wrong you Duffer")

answer = input("What is Capital of India?")
if answer.lower() == "new delhi":
    print("Correct Handsome!")
    score += 1
else:
    print("Wrong you Duffer")

answer = input("What was lord krishna's father name?")
if answer.lower() == "Vasudev":
    print("Correct Handsome!")
    score += 1
else:
    print("Wrong you Duffer")

print("You got" +str(score)+ "questions correct. ")