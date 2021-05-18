# 예외상황 처리
# 파이썬에서는 0으로 나누거나 배열의 인덱스를 잘못 사용하는 등
# 여러가지 경우에 오류가 발생할 수 있다
# 오류가 발생하면 프로그램이 비정상적으로 종료된다
# 이런 경우 프로그램이 정상적 종료를 유도해야 하는데
# 이때 예외상황 처리를 한다


def ten_div(x):
    try:
        return 10/x
    except:
        return "0으로 나누는 오류가 발생했습니다."

a = ten_div(0)
print(a)
