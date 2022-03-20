# concurrent.futures wait, as_completed
# wait

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
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

    # Futures
    futures_list = []

    # 결과 건수
    # futures.ThreadPoolExecutor
    with ProcessPoolExecutor(max_workers=worker) as executor:
        for work in WORK_LIST:
            # future 반환
            future = executor.submit(sum_generator, work)
            # scheduling
            futures_list.append(future)
            # scheduling 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # wait 결과 출력
        # result = wait(futures_list, timeout=3)
        # # 성공
        # print('Completed Tasks : ' + str(result.done))
        # # 실패
        # print('Pending ones after waiting for 3 seconds : ' + str(result.not_done))
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm
    msg = '\n Time : {:.2f}s'
    print(msg.format(end_tm))


# 실행
if __name__ == '__main__':
    main()