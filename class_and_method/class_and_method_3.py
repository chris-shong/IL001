# class method vs instance method vs static method
class Car:
    """
    Car class
    Author: Lee
    Date: 2021.03.12
    Description: Class, Static, Instance Method
    """
    # Class 변수(모든 instance가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        # instance 변수에는 under bar 사용
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Current Detail info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_calc(self):
        return 'After Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 Or More")
            return
        cls.price_per_raise = per  # == Car.price_per_raise
        print('Succeed! price increased!.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'


car1 = Car('Ferarri', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 정보(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# 가격 정보(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# Instance로 호출(static)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# Class로 호출(static)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))