from questionClasses import ChoiceQuestion

print("Welcome to the King of Iron Fist Quiz Bowl!")

def main():
    first = ChoiceQuestion()
    first.setText("Who is my current main in Tekken 7?")
    first.addChoice("Alisa", False)
    first.addChoice("Kazuya", False)
    first.addChoice("Heihachi", True)
    first.addChoice("Xiaoyu", False)

    second = ChoiceQuestion()
    second.setText("Which map on Tekken 7 had the most Death Combos?")
    second.addChoice("Infinite Azure", False)
    second.addChoice("Forgotten Realm", True)
    second.addChoice("Duomo di Sirio", False)
    second.addChoice("G Corp. Helipad", False)

    third = ChoiceQuestion()
    third.setText("Which input notation (on Heihachi) will induce the most rage in player Renshiro?")
    third.addChoice("b+2", False)
    third.addChoice("f,f+3", False)
    third.addChoice("EWGF", False)
    third.addChoice("db+2", True)

    fourth = ChoiceQuestion()
    fourth.setText("How many negative frames on block is considered 'punishable'?")
    fourth.addChoice("-5", False)
    fourth.addChoice("-10", True)
    fourth.addChoice("-15", False)
    fourth.addChoice("-20", False)

    fifth = ChoiceQuestion()
    fifth.setText("Which among these characters has a wavedash?")
    fifth.addChoice("Bob", True)
    fifth.addChoice("Nina", False)
    fifth.addChoice("Josie", False)
    fifth.addChoice("Eddy", False)

    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(third)
    presentQuestion(fourth)
    presentQuestion(fifth)

def presentQuestion(q):
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))

main()