n=3
new=[]
for i in range(1,n+1):
    if i % 15==0:
        new.append('FizzBuzz')
    elif i%3==0:
        new.append("Fizz")
    elif i%5==0:
        new.append('BUZZ')
    else:
        new.append(str(i))

print(new)