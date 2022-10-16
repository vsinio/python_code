# 1
def rectangle_area(a, b):
    """площадь прямоуг"""
    return a * b


print("def variant", end=" ")
print(rectangle_area(10, 11))

print((lambda a, b: a * b)(10, 12))  # та же самая функция но через лямбду


# 2
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


print("def variant", end=" ")
print(maximum(5, 9))
print((lambda a, b: a if a > a else b)(5, 9))
