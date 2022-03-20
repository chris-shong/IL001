# 코루틴(Coroutine): 단일(싱글) thread, 스택을 기반으로 동작하는 비동기 작업
# thread: os가 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 thread
# yield, send: 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴: 메인루틴 호출 -> 서브루틴에서 수행(흐름 제어)
# 코루틴: 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴: thread에 비해 오버헤드 감소
# thread : single thread -> multi thread -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, context 스위칭 비용 발생, 자원 소비 가능성 증가
# def -> async, yield -> await

# Coroutine Ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))


# Main routine
# generator 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# cr1.send(100)

# 잘못된 사용
cr2 = coroutine1()

# cr2.send(100) -> Error

# Coroutine Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPEND : yield 대기 상태 -> 중요
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

cr3.send(100)

print()
print()


# Coroutine Ex3
# StopIteration 자동 처리(3.5 -> await)
# 중첩 coroutine 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()

print(list(t2))


def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))
