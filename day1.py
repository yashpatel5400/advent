import os
cached = {}
masses = [int(l) for l in open(os.path.expanduser("~/Downloads/input.txt"))]
ans = 0

while len(masses) > 0:
    mass = masses.pop()
    if mass in cached:
        new_mass = cached[mass]
    else:
        new_mass = int(mass) // 3 - 2
    if new_mass > 0:
        cached[mass] = new_mass
        ans += new_mass
        masses.append(new_mass)
print(ans)