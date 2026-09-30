n = int(input())
arr = list(map(int, input().split()))
answer = []

def solution():
  for i in arr:
    if i==0 and arr.count(i) == len(arr):
      return -1
    if i==0:
      answer.append(-1)
    elif i!=0 and i==arr.count(i):
      answer.append(i)
    elif i!=0 and i==arr.count(i)+arr.count(0):
      answer.append(-1)
    else:
      answer.append(0)
  return max(answer)

print(solution())