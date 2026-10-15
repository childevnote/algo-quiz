# 개념 정리 — 스택(Stack)과 큐(Queue) 기초

이 문제는 스택 자료구조의 가장 기본적인 성질을 이용한다.

## 스택(Stack)

- **LIFO**(Last In, First Out): 마지막에 들어온 원소가 가장 먼저 나간다.
- 접시 쌓기에 비유된다. 가장 위에 있는 접시(마지막에 쌓은 것)부터 꺼낸다.
- 지원 연산: `push`(삽입), `pop`(꺼내기), `top`/`peek`(가장 위 원소 조회).
- Python의 리스트(`append`/`pop`), Java의 `Deque`(`addLast`/`pollLast`)로 구현할 수 있다.

```python
# 일반 예시: 뒤집기
stack = []
for c in "abc":
    stack.append(c)      # a -> b -> c 순서로 쌓임
result = []
while stack:
    result.append(stack.pop())  # c -> b -> a 순서로 나옴
print(result)  # ['c', 'b', 'a']
```

## 스택을 이용한 연속 중복 제거

- 원소를 하나씩 순회하면서, 스택의 가장 위 값과 비교해 같지 않을 때만 `push`한다.
- 이렇게 하면 연속된 중복 원소가 자연스럽게 하나로 남는다.
- 중요한 점: 비교 대상은 스택의 top(결과 리스트의 마지막 원소) 하나뿐이다. 전체를 다시 살필 필요가 없으므로 한 번의 순회(O(n))로 끝난다.
