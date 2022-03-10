# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

# magic method
# class의 정보를 출력
# __str__: 사용자 레벨에서 print로 정보를 확인할 떄
# __repr__: 엔지니어 레벨에서 객체의 엄격한 정보를 확인할 때
# 둘 다 존재할 때 __str__ 우선 출력

class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('Ferarri', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1))

print()
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

# 반복문에서는 __str__이 출력
# repr를 활용할 경우 __repr__이 출력
for x in car_list:
    print(repr(x))
    # print(x)