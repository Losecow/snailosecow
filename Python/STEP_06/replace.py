member = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
N = input()

for i in member:
    N = N.replace(i, "*")

print(len(N))
