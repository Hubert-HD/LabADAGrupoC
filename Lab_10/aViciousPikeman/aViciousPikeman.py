# Ejercicio 4
# https://open.kattis.com/problems/pikemaneasy

def aViciousPikerman(n, time, array):
  total= 0
  penalty=0
  for i, t in enumerate(array):
    if total + t > time:
        return i, penalty
    total += t
    penalty = (penalty + total) % 1000000007
  return n, penalty

n, t = map(int, input().split())
a, b, c, t0 = map(int, input().split())
array = [t0]
for _ in range(1,n):
  array.append(((a * array[-1] + b) % c) + 1)

res = aViciousPikerman(n,t,sorted(array))
print(*res)