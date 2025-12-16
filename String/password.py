s = input()
ans = ''
for ch in s:
    if ch != ' ':
        ans += chr(ord(ch) + 5)
    else:
        ans += ' '
print(ans)