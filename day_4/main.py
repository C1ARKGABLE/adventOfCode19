from datetime import datetime

START_RANGE = 134792
END_RANGE = 675810

total = 0
length = 6

start = datetime.now()
for num in range(START_RANGE, END_RANGE+1):
  a = []
  past = 0
  broken = False
  for i in str(num):
    current = int(i)
    if (diff := current - past) >= 0:
      a.append(diff)
      past = current
    else:
      broken = True
      break
  
  if not broken and sum(a) == past and any(x==1 for x in a):
    total += 1

print(datetime.now() - start)
print(total)
