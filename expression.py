m = int(input())
n = int(input())
o = int(input())

one = m + n * o
two = m * (n + o)
three = m * n * o
four = (m + n) * o
five= m + n + o

results = [one, two, three, four, five]
max_result = max(results)

print(max_result)