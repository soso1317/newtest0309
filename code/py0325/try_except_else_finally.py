
try:
   x = int(input("숫자를 입력하세요"))
   y = 10 / x
except ZeroDivisionError:
    print("0으로 나누기 오류")
else :
    print(y)
finally:
    print('코드 실행을 종료합니다')

