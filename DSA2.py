#Convert a queue to a list
from queue import Queue
que=Queue()
que.put(2)
que.put(20)
que.put(1)
que.put(12)
print("Initially:")
print(que.queue)
l=list(que.queue)
print("Finally: ")
print(l)