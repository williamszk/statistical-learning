# p.62
# about Heaps
#%%
import time
import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self._q = []
    
    def add(self, value, priority=0):
        heapq.heappush(self._q, (priority, time.time(), value))
    
    def pop(self):
        return heapq.heappop(self._q)[-1]

#%%
def f1(): print("Hello from f1()")
def f2(): print("Hello from f2()")

#%%
pri_queue = PriorityQueue()
pri_queue.add(f1, priority=1)
pri_queue.add(f2, priority=1)

popped_obj = pri_queue.pop()
popped_obj() # Hello from f1()

popped_obj_2 = pri_queue.pop()
popped_obj_2() # Hello from f2()

#%%
pri_queue_2 = PriorityQueue()

pri_queue_2.add(f2, priority=1)
pri_queue_2.add(f1, priority=0) # this should pop before, given the priority 0


pop1 = pri_queue_2.pop()
pop1() # hello from f1()

pop2 = pri_queue_2.pop()
pop2() # Hello from f2()

