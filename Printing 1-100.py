a = ['','one','two','three','four','five','six','seven','eight','nine']
b = ['ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
n=int(input('Enter no: '))

count = 0
for i in a:
    if count==n+1:
        break
    print(i)
    count = count+1

for i in b:
    if count == n+1:
        break
    print(i)
    count = count+1

for i in c:
    for j in a:
        if count == n+1:
            break
        print(i,j)
        count = count+1

if count == 100:
    print("one hundred")