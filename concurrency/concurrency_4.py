# Futures(동시성)
# 비동기 작업 실행
# 지연 시간(Block) CPU 및 리소스 낭비 방지 -> (File) Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. multithreading/multiprocessing API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, timeout 옵션, callback 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# GIL: Global Interpreter Lock, 2개 이상의 thread가 동시에 실행 될 때, 하나의 자원을 액세스 하는 경우 생기는 문제점을 방지하기 위해 GIL 실행
#       -> 리소스 전체에 락이 걸린다.
# multiprocessing 사용, CPython 사용을 통해 GIL 우회

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2

import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수(generator)
def sum_generator(n):
    return sum(n for n in range(1, n+1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # futures.ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as executor:
        # map -> 작업 순서 유지, 즉시 실행
        result = executor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_tm = time.time() - start_tm
    msg = '\n Result -> {} Time : {:.2f}s'
    print(msg.format(list(result), end_tm))


# 실행
if __name__ == '__main__':
    main()