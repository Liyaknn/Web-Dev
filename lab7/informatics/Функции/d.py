def election(x, y, z):
    return 1 if (x + y + z) >= 2 else 0

x, y, z = map(int, input().split())
print(election(x, y, z))
