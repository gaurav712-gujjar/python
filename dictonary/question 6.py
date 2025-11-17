s = ")[]"
var = []
a = 0

pairs = {')': '(', ']': '[', '}': '{'}

for ch in s:
    if ch in "([{":
        var.append(ch)

    elif len(var) > 0:
        if ch in pairs and pairs[ch] == var.pop():
            a=0
        else:
            a = 1
            break
    else:
        a = 1
        break

if len(var) != 0 or a == 1:
    print("invalid")
else:
    print("valid")
