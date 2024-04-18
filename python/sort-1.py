import heapq

n = int(input())
nheap = []

for i in range(n):
    nheap.append(int(input()))
    
heapq.heapify(nheap)
for nn in nheap:
    print(nn)