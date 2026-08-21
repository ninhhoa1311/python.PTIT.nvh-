test = int(input())

for _ in range(test):

    s = input()

    print("YES" if s[0]+s[1] == s[-2]+s[-1] else "NO")