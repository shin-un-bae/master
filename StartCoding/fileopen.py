
"""f =open("c:/jocoding/test.txt", 'w')
for i in range(1, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
"""
"""f = open("C:/jocoding/test.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()"""

f = open("C:/jocoding/test.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
