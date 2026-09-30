import sys

read = sys.stdin.readline
write = sys.stdout.writelines

def sol():
    s = read()
    dic = []
    for i in range(len(s)-1):
        tem = s[i:]
        dic.append(tem)
    write(sorted(dic))
sol()
