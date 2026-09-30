# 231115 11:11 ~ 11:25
# n = int(input())
# p = list(map(int, input().split()))
# sorted_p = sorted(p)
# answer = 0

# def atm (total, arr):
#   for i in range(n):
#     for j in range(i+1):
#       total += arr[j]
#   return total

# print(atm(answer, sorted_p))

n = int(input())
p = list(map(int, input().split()))
sorted_p = sorted(p)
answer = 0
cumulative_sum = 0

for i in range(n):
    cumulative_sum += sorted_p[i]
    answer += cumulative_sum

print(answer)
