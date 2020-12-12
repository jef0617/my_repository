
file = open("input.txt",'r')
lines = file.readlines()

size = len(lines)

dic = {}

m = int(lines[-1])

for i in lines[0:-1]:
  aaa = i.split(":")
  num = int(aaa[0])
  word = aaa[1][:-1]
  if m % num == 0:
    dic[word] = num
  else:
    continue


if len(dic) == 0:
  print(m)
else:
  dic2 = sorted(dic.items(),key = lambda x:x[1],reverse=False)
  for s in dic2:
    print(s[0])

  