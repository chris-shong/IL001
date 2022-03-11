# class 변수 vs instance 변수
class Car:
    """
    Car class
    Author: Lee
    Date: 2021.03.12
    """
    # Class 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        # instance 변수에는 under bar 사용
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Current Detail info : {} {}'.format(self._company, self._details.get('price')))


# self 의미
# self를 가지고 있는 것을 instance라 함 (instance 변수, instance method)
car1 = Car('Ferarri', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)  # 값 비교
print(car1 is car2)  # id값으로 instance 자체를 비교

# dir & __dict__ 비교
# dir: 해당 instance가 가지고 있는 모든 method들을 list의 형태로 보여줌
print(dir(car1))
print(dir(car2))

print()
print()

# __dict__: 해당 instance에서 불필요한 정보는 제거하고 내가 정의한 namespace만 보고싶을 경우
print(car1.__dict__)
print(car2.__dict__)

# Doctoring
print(Car.__doc__)
print()

# execute
car1.detail_info()  # == Car.detail_info(car1)
car2.detail_info()  # == Car.detail_info(car2)

# comparison
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))
print(id(car1.__class__) == id(car2.__class__))

# Error
# Car.detail_info() # error

# 공유 확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 동일한 이름으로 instance 변수와 class 변수 생성 가능
# instance namespace에 없을 경우 class 변수에서 검색
