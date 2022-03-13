# Sequence
# Container vs Flat
# Container: 서로 다른 자료형을 담을 수 있는 자료 구조 [list, tuple, collections.deque]
# Flat: 단일 자료형만 담을 수 있는 자료 구조 [str, bytes, bytearray, array.array, memoryview]
# 가변 vs 불변
# 가변: list, bytearray, array.array, memoryview, collections.deque
# 불변: tuple ,str, bytes

# list 및 tuple 고급
# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!)'
code_list1 = []

# ord: str -> unicode
# chr: unicode -> str
for s in chars:
    # unicode list
    code_list1.append(ord(s))

print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 x)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())

print()
print()

# Generator example
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# List 주의
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# **증명**
print([id(i) for i in marks1])
print([id(i) for i in marks2])
