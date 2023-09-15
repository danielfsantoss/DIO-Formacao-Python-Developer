N = int(input())
loop = N
while(loop > 0):
  a, b = input().split()
  if a.endswith(b):
    print("encaixa")
  else:
    print("nao encaixa")
  loop-=1
