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

## 5. 실습 결과

브랜치 생성 및 병합, Clone, Commit, Push, Pull을 수행하고 로컬 저장소와 원격 저장소의 변경사항이 동기화되는 것을 확인했다.