# Closure 기초
# 외부에서 호출된 함수의 변수값, 상태(reference) 복사 후 저장 -> 후에 접근(액세스) 가능


# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) -> error


# Ex2
b = 20


def func_v2(a):
    print(a)
    print(b)

func_v2(10)


# Ex3
# Global vs Local variable

c = 30


def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40


print('>>', c)
func_v3(10)
print('>>', c)

# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접군 -> 교착 상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# Closure는 공유하되 변경되지 않는(Immutable, Read only) 적극적으로 사용 -> 함수형 프로그래밍
# Closure는 불변자료구조 및 atom, STM -> 멀티thread(Coroutine) 프로그래밍에 강점
# 해당 영역의 상태를 기억하고 있다

a = 100
print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))


# class 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# instance 생성
averager_cls = Averager()

# 누적
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))




