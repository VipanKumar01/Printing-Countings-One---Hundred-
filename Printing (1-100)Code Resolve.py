a = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
b = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
c = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety','One Hundred']
n=int(input('Enter no.'))
for i in range(n+1):
    temp1 , temp2  = i%10 , i//10
    if i<=9:                    print(a[i])
    if i>=10 and i<=19:         print(b[temp1])
    if i>=20 and i<=100:         print(c[temp2-2],a[temp1])
# if n<=100: print('One Hundred')