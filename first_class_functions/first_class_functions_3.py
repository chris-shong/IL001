# Closure 사용
def closure_ex1():
    # Free variable
    # Closure 영역
    series = []

    def averager(v):
        series.append(v)
        print("inner >>> {} / {}".format(series, len(series)))
        return sum(series) / len(series)
    return averager


avg_closure1 = closure_ex1()
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(avg_closure1.__closure__[0].cell_contents)


# 잘못된 Closure 사용의 예
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

# avg_closure2 = closure_ex2()
# print(avg_closure2(10)) -> error


def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager


avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))