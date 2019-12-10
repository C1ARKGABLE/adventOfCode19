import sys, os
def passwds(f,t,m):
  p = 0
  for digit in range(f,t+1):
    s = digit.__str__()
    equals = {}
    for i in range(len(s)):
      if i < len(s)-1 and (int(s[i]) > int(s[i+1])): # increasing numbers
        break

      if i < len(s)-1 and int(s[i]) == int(s[i+1]): # map consecutive numbers
          if not int(s[i]) in equals:
            equals[int(s[i])] = 0
          equals[int(s[i])] += 1

    if i == len(s)-1 and len(equals) > 0:
      if m == 0: # part1
        p += 1
      else:
        if any(v==1  for v in equals.values()): # part2
          p += 1

  print("passwords:",p)

if __name__ == "__main__":
  # part1
  passwds(134792,675810,0)
  # part2 
  passwds(134792,675810,1)