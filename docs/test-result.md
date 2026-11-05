# 기능 테스트 결과

## 테스트 환경
- Windows / WSL Ubuntu
- Python 3.14.4
- 실행 명령: `python3 main.py`

## 테스트 결과

| 테스트 항목 | 결과 |
|---|---|
| 메뉴 출력 | 정상 |
| 기본 퀴즈 7개 출력 | 정상 |
| 퀴즈 정답·오답 판정 | 정상 |
| 점수 계산 (6/7, 86점) | 정상 |
| 퀴즈 추가 및 삭제 | 정상 |
| 최고 점수 확인 | 정상 |
| 빈 입력 및 잘못된 숫자 처리 | 정상 |
| 프로그램 종료 | 정상 |

주요 기능을 실행하여 정상 동작을 확인했다.

## 실행 화면

- [개발 환경](screenshots/environment.png)
- [메인 메뉴](screenshots/menu.png)
- [퀴즈 목록](screenshots/quiz_list.png)
- [퀴즈 풀이](screenshots/play.png)
- [퀴즈 풀이 및 채점 결과](screenshots/play2.png)
- [잘못된 입력 및 Ctrl + C 예외 처리](screenshots/invalid_input.png)
- [EOF 입력 처리](screenshots/eof.png)
- [JSON 파일 누락 처리](screenshots/missing_json.png)
- [JSON 파일 손상 처리](screenshots/corrupt_json.png)
- [퀴즈 추가](screenshots/add_quiz.png)
- [퀴즈 삭제](screenshots/delete_quiz.png)
- [최고 점수 확인](screenshots/score.png)
- [프로그램 종료](screenshots/quit.png)

### 프로그램 재실행 후 데이터 유지 테스트

퀴즈를 추가하고 게임을 진행한 뒤 프로그램을 종료했다.
이후 프로그램을 다시 실행하여 추가한 퀴즈와 최고 점수가 유지되는지 확인했다.

1. [퀴즈 추가](screenshots/persistence_1.png)
2. [문제 푼 후 최고 점수 확인](screenshots/persistence_2.png)
3. [프로그램 재실행 후 퀴즈 목록 확인](screenshots/persistence_3.png)
4. [프로그램 재실행 후 최고 점수 확인](screenshots/persistence_4.png)