question_file = open("questions.txt", "r")
questions_ans = [line.strip() for line in question_file.readlines()]
questions_split = [i.split("=") for i in questions_ans]
questions_dict = {item[0]: item[1] for item in questions_split}
question_file.close()

total_answers = len(questions_dict)
correct_answers = 0

def quiz():
    global correct_answers

    for key, value in questions_dict.items():
        user_ans = input(f"{key}=")
        if user_ans == value:
            correct_answers += 1

quiz()

result = open("result.txt", "w")
result.write(f"Your final score is {correct_answers}/{total_answers}.")
result.close()



