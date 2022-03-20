import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading

# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장(예: 게시판성 커뮤니티)
urls = ['http://daum.net', 'http://naver.com', 'https://tistory.com']


async def fetch(url, executor):
    # thread명 출력
    print('Thread Name: ', threading.current_thread().getName(), "Start", url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)

    soup = BeautifulSoup(res.read(), 'html.parser')

    # 전체 페이지 소스 확인
    # print(soup.prettify())
    result_data = soup.title

    print('Thread Name: ', threading.current_thread().getName(), "Done", url)
    # 결과 반환
    return result_data


async def main():
    # Thread pool 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor))
        for url in urls
    ]

    # 결과 취합
    rst = await asyncio.gather(*futures)
    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)

