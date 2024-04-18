import heapq

sum=0;nli = []
for _ in range(5):
    n = int(input())
    sum += n
    heapq.heappush(nli,n)
    
print(int(sum/5))
print(nli[2])