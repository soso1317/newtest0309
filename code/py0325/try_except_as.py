y = [10, 20, 30]  # 리스트 생성

try:
    index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요").split())
    print(y[index] / x )

except ZeroDivisionError as e:
    print('[MyErrMsg]', e)
except IndexError as ei:
    print('잘못된 인덱스입니다.', ei)
