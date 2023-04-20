from collections import deque

can_be_poly = lambda text: deque(text).pop() == deque(text).popleft()

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
