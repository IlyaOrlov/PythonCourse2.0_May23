question = input("Отгадаем загадку? (y/n) ")
maxQuestion = 3
countQuestion = 1

while question == "y" and countQuestion <= maxQuestion:

        match countQuestion:
            case 1:
                answer = input("Нет ушей, а слышит. Нету рук, а пишет. Что это?")
                trueAnswer = "магнитофон"
            case 2:
                answer = input("Стоит дуб, В нем двенадцать гнезд, В каждом гнезде gо четыре яйца, В каждом яйце - семь цыпленков.")
                trueAnswer = "год"
            case 3:
                answer = input("Пустые отдыхаем, А полные шагаем.")
                trueAnswer = "сапоги"

        if answer.lower() == trueAnswer:
            print(f"Вы молодец! {trueAnswer} - это верный ответ")
        else:
            print(f"Правильный ответ: {trueAnswer}")

        question = input("Отгадаем ещё загадку? (y/n)")
        countQuestion+=1
else:
    print("Спасибо за участие!")
