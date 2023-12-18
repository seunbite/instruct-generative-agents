def a(i):
    return 3/(i)

for i in range(3):
    try:
        print(a(i))
        break
    except:
        continue