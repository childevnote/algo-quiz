import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coin_value = [int(read()) for _ in range(n)]
answer = 0

for i in range(n-1, -1, -1):
  if k >= coin_value[i]:
    answer += k // coin_value[i]
    k %= coin_value[i]

print(answer)