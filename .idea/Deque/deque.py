from collections import deque

deque = deque([1, 2, 3, 3, 4, 2, 4])

print(deque.index(2,0,5))

deque.insert(3,10)
print(deque)

print(deque.count(2))

deque.remove(3)
print(deque)

deque.remove(3)
print(deque)