class Quiz:
    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제 내용이 비어 있습니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")
        for choice in choices:
            if not isinstance(choice, str) or not choice.strip():
                raise ValueError("선택지 내용이 비어 있습니다.")
        
        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1~4여야 합니다.")

        self.question = question
        self.choices = choices.copy()
        self.answer = answer

    def displayQuiz(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def checkAnswer(self, userAnswer):
        return userAnswer == self.answer

    def getQuestion(self):
        return self.question

    def getChoices(self):
        return self.choices.copy()

    def getAnswer(self):
        return self.answer