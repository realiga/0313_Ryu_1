import random  # 랜덤 기능을 가져와요

# 1. 컴퓨터가 1~100 사이의 비밀 숫자를 정합니다
secret_number = random.randint(1, 100)
attempts = 0  # 시도 횟수를 저장할 변수

print("어서오세요! 숫자를 맞춰보세요 (1~100)")

# 2. 맞출 때까지 계속 반복합니다 (반복문)
while True:
    # 3. 사용자에게 입력을 받습니다
    if attempts>10:
        print("10회 초과입니다. 실패")
        break
    
    guess = int(input("숫자를 입력하세요: "))
    attempts += 1  # 시도 횟수 1 증가
    
    # 4. 판독하기 (조건문)
    if guess < secret_number:
        print("더 큰 숫자예요! (UP)")
    elif guess > secret_number:
        print("더 작은 숫자예요! (DOWN)")
    else:
        print(f"정답입니다! {attempts}번 만에 맞추셨네요! 🎉")
        break  # 정답을 맞췄으니 반복을 끝냅니다