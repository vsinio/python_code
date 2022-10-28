# lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst2=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# c = [x+y for x, y in zip(lst[0], lst2[0])]
# print(c)
def solution(a, b):
    c = len(b)
    if b == a[c:3]:
        return True
    else:
        return False
print(solution("abcd", "cd"))

def high_and_low(numbers):
    s = str(max(numbers)) +" "+ str(min(numbers))
    return s

print(high_and_low([1,2,3]))