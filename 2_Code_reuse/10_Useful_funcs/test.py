import time


for num in range(10):
    print(num)
    time.sleep(1)
print()

for num in range(10):
    print(num, end=' ', flush=False)
    time.sleep(1)
print()

for num in range(10):
    print(num, end=' ', flush=True)
    time.sleep(1)
print()




