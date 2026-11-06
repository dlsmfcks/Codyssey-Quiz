import json
import random
import shutil
from pathlib import Path

from quiz import Quiz


class QuizGame:
    
    STATE_FILE = Path(__file__).resolve().parent / "state.json"

    BACKUP_FILE = Path(__file__).resolve().parent / "state.backup.json"

    def __init__(self):
        self.quizList= []

        self.presentScore = 0
        self.highScore = 0

        self.hasPlayed = False

        self.loadData()

    def showMenu(self):
        print("\n===========================================================")
        print("                      📖 상식 퀴즈 게임 🎯                    ")
        print("===========================================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료")
        print("===========================================================")

    def startGame(self):
        try:
            while True:
                self.showMenu()
                inputNumber = self.readNumber("선택: ", 1, 6)

                if inputNumber == 1:
                    self.playQuiz()
                elif inputNumber == 2:
                    self.addQuiz()
                elif inputNumber == 3:
                    self.showQuizList()
                elif inputNumber == 4:
                    self.showScore()
                elif inputNumber == 5:
                    self.deleteQuiz()
                elif inputNumber == 6:
                    print("게임을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 데이터를 저장하고 종료합니다.")
        
        finally:
            self.saveData()

    def playQuiz(self):
        if not self.quizList:
            print("등록된 퀴즈가 없습니다.")
            return

        correctCount = 0
        total = len(self.quizList)

        randomQuizList = self.quizList.copy()

        random.shuffle(randomQuizList)

        for i, quiz in enumerate(randomQuizList, start=1):
            print(f"\n[문제 {i}/{total}]")
            quiz.displayQuiz()
            print("===========================================================")

            userAnswer = self.readNumber("정답 입력: ", 1, 4)

            if quiz.checkAnswer(userAnswer):
                print("✅ 정답입니다!")
                correctCount += 1
                print()
            else:
                print("❌ 오답입니다.")
                print(f"\n 정답은 {quiz.getAnswer()}번입니다.")
        self.presentScore = int(100 * correctCount /total + 0.5)
        print("\n===========================================================")
        print(f"\n🏆 결과: {total}문제 중 {correctCount}문제 정답! ({self.presentScore}점)")
        
        if not self.hasPlayed or self.presentScore > self.highScore:
            self.highScore = self.presentScore
            print("🎉 새로운 최고 점수입니다! 🎉")
        
        self.hasPlayed = True
        self.saveData()


    def readNumber(self, prompt, minNumber, maxNumber):
        while True:
            text = input(prompt).strip()
        
            if not text:
                print("빈 입력 입니다. 다시 입력하세요.")
                continue

            try:
                number = int(text)
            except ValueError:
                print("숫자를 입력하세요.")
                continue

            if minNumber <= number <= maxNumber:
                return number
        
            print(f"{minNumber}~{maxNumber} 사이의 숫자를 입력하세요.")


    def addQuiz(self):
        print("----- 퀴즈 추가 -----")
        question = self.readText("문제: ")
        choices = []

        for i in range(1, 5):
            choices.append(self.readText(f"선택지 {i}: "))

        answer = self.readNumber("정답 번호: ", 1, 4)
        self.quizList.append(Quiz(question, choices, answer))
        self.saveData()
        print("\n✅ 퀴즈가 추가되었습니다!")

    def deleteQuiz(self):
        if not self.quizList:
            print("삭제할 퀴즈가 없습니다.")
            return
        
        self.showQuizList()

        number = self.readNumber("삭제할 문제 번호(0은 취소): ", 0, len(self.quizList))

        if number == 0:
            print("삭제를 취소했습니다.")
            return

        self.quizList.pop(number - 1)

        self.saveData()

        print("퀴즈가 삭제되었습니다.")

    def showQuizList(self):
        if not self.quizList:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n----- 퀴즈 목록 (총 {len(self.quizList)}개) -----")
        for i, quiz in enumerate(self.quizList, start=1):
            print(f"{i}. {quiz.getQuestion()}")

    
    def showScore(self):
        if not self.hasPlayed:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.highScore}점")

    def readText(self, prompt):
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("빈 입력은 허용되지 않습니다. 다시 입력하세요")

        
    def saveData(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.getQuestion(),
                    "choices": quiz.getChoices(),
                    "answer": quiz.getAnswer(),
                }
                for quiz in self.quizList
            ],
            "best_score": self.highScore,
            "has_played": self.hasPlayed,
        }

    
        tempFile = self.STATE_FILE.with_name("state.tmp.json")

    
        backupTempFile = self.BACKUP_FILE.with_name("state.backup.tmp.json")

        try:
        
            with tempFile.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            tempFile.replace(self.STATE_FILE)

        except (OSError, TypeError, ValueError) as error:
            print(f"저장 실패: {error}")
            return

        finally:
        
            tempFile.unlink(missing_ok=True)

        try:
        
            shutil.copy2(self.STATE_FILE, backupTempFile)

        
            backupTempFile.replace(self.BACKUP_FILE)

        except OSError as error:
            print(f"백업 실패: {error}")

        finally:
            backupTempFile.unlink(missing_ok=True)

    def loadData(self, fromBackup=False):

        filePath = self.BACKUP_FILE if fromBackup else self.STATE_FILE

        try:
            with filePath.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("JSON 최상위 값은 객체여야 합니다.")

            if not isinstance(data.get("quizzes"), list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            score = data.get("best_score")

            if type(score) is not int or not 0 <= score <= 100:
                raise ValueError("최고 점수가 잘못되었습니다.")

            played = data.get("has_played", score > 0)

            if type(played) is not bool:
                raise ValueError("게임 기록 정보가 잘못되었습니다.")

            loaded = []

            for item in data["quizzes"]:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 데이터 형식이 잘못되었습니다.")

                loaded.append(
                    Quiz(
                        item["question"],
                        item["choices"],
                        item["answer"]
                    )
                )

            self.quizList = loaded
            self.highScore = score
            self.hasPlayed = played

            if fromBackup:
                print("백업 파일에서 데이터를 불러왔습니다.")
                self.saveData()
            else:
                print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizList)}개)")

        except (
            OSError,
            UnicodeError,
            json.JSONDecodeError,
            ValueError,
            TypeError,
            KeyError
        ) as error:

            if not fromBackup:
                print(f"저장 파일을 읽을 수 없어 백업을 확인합니다: {error}")

                self.loadData(fromBackup=True)

            else:
                print(f"백업 파일도 사용할 수 없어 기본 퀴즈로 초기화합니다: {error}")

                self.setDefaultQuizzes()
                self.saveData()


    def setDefaultQuizzes(self):
        self.quizList = [
            Quiz("대한민국의 국화는 무엇일까?", ["장미", "무궁화", "개나리", "진달래"], 2),
            Quiz("주식에서 배당금을 받는다는 것은 무엇을 의미할까?",
            ["기업이 주주에게 이익의 일부를 환원하는 것", "주주가 기업에 돈을 빌려주는 것",
            "주식 가격을 강제로 올리는 것", "세금을 면제받는 것"], 1),
            Quiz("인류 최초로 달 표면에 발을 디딘 사람은?", ["닐 암스트롱", "루이 암스트롱", "버즈 올드린", "크리스티아누 호날두"], 1),
            Quiz("데이터를 통해 패턴을 학습하는 인공지능의 한 분야는?", ["딥러닝", "디자인 패턴", "머신러닝", "운영체제"], 3),
            Quiz("컴퓨터의 작업 데이터를 일시적으로 저장하는 장치는?", ["OS", "SSD", "CPU", "RAM"], 4),
            Quiz("사람의 정상 체세포에 있는 염색체는 몇 개일까?", ["44", "45", "46", "47"], 3),
            Quiz("조선이 건국된 해는?", ["1592년", "1392년", "1450년", "1398년"], 2),
        ]
        self.presentScore = 0
        self.highScore = 0
        self.hasPlayed = False
    