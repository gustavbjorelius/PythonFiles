
for _ in range(5):
    print('x', end=' ')
print('    ')

for i in range(5):
    print(i, end=' ')
print('    ')

for i in range(8):
    if i % 2 == 0:
        continue
    else: 
        print(i, end='')

print('    ')

list = [1,2,4,8,16]
while list: 
    print(list.pop()**2, end=' ')
