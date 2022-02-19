'''Program to check perfect number'''
n=int(input())
def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return "Perfect"
    else:
        return "Not Perfect"
print(perfect(n))