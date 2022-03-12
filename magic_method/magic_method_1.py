# Special Method (Magic Method)
# Python Core: Data Model -> Sequence, Iterator, Functions, Class
# Magic method: 클래스 안에 정의할 수 있는 특별한 Built-in method

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10
print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()


# Class example 1
class Fruit:
    def __init__(self, name, price):
        self._name=name
        self._price = price

    def __str__(self):
        return 'Fruit Classs Info: {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False


# instance 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)

# 일반적인 계산
# print(s1._price + s2._price)

# Magic method
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)