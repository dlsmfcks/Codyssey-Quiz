# Git 버전 관리 실습

## 1. 브랜치 생성 및 병합

`feature/test` 브랜치를 생성하여 기능 테스트 결과와 실행 화면을 기록했다.

작업 완료 후 `main` 브랜치로 이동하고, 다음 명령어로 병합했다.

```bash
git merge --no-ff feature/test -m "테스트 작업 병합"
```

## 2. Git Clone

GitHub 저장소를 별도의 `codyssey-quiz-clone` 폴더로 복제했다.

```bash
git clone https://github.com/dlsmfcks/Codyssey-Quiz.git codyssey-quiz-clone
```

## 3. Commit 및 Push

복제한 저장소의 README에서 기능 테스트 완료 항목을 수정했다.

변경사항을 커밋하고 GitHub에 Push했다.

## 4. Git Pull

기존 프로젝트 폴더에서 다음 명령어를 실행했다.

```bash
git pull origin main
```

`Fast-forward` 메시지와 함께 README 변경사항이 반영되는 것을 확인했다.

## 5. Git Checkout

git checkout 명령어로 feature/test 브랜치로 이동한 후,
다시 main 브랜치로 돌아오는 실습을 진행했다.

## 6. 커밋 관리 기준

커밋은 기능 구현, 테스트, 문서 수정 등 작업 내용을
기준으로 구분하여 관리했다.

커밋 메시지에는 변경한 내용을 간결하게 작성했다.

향후에는 다음과 같은 메시지 규칙을 적용할 수 있다.

- Feat: 새로운 기능 추가
- Fix: 오류 수정
- Docs: 문서 수정
- Refactor: 코드 구조 개선

## 7. 실습 결과

브랜치 생성 및 병합, Clone, Commit, Push, Pull을 수행하고 로컬 저장소와 원격 저장소의 변경사항이 동기화되는 것을 확인했다.