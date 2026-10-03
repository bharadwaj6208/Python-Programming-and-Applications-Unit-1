#Write a python program, in which a while loop starts at 10 and counts down +to 1, printing each value of the count and prints "Liftoff"

count = 10
while count>=1:
    print (count)
    count -= 1
print ("liftoff")

#this program also works

cnt = 10
while True:
    print(cnt)
    cnt -= 1
    if cnt ==0:
        break
print("liftoff")