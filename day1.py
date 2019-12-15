import os
ans = sum(int(l) // 3 - 2 for l in open(os.path.expanduser("~/Downloads/input.txt")))
print(ans)