
# for comment ctrl+/

print(list(range(1,8,2)))

#while
i=1
while i<10:
    print(i,end=" ")
    i=i+1
print("done")
i=10
while i>=1:
    print(i,end="  ")
    i=i-1
print()
#for loop

for i in range(10):
    print("given 10",i,end="  ")
print()
for i in range(1,10):
    print("given 1,10",i,end="  ")
print()
for i in range(1,10,2):
    print("given 1,10,2",i,end="  ")


print()
for i in range(1,10):
    if i==5:
        break           #jumping statement
    print(i,end="  ")

print()
for i in range(1,10):
    if i==5 or i==7:    #jumping statement
        continue
    print(i,end="  ")
print()


#numbering
num=4
num1=9.9
print(type(num))
print(type(num1))

print(max(9,7,5,90,60))
print(min(9,7,5,90,60))

#ways of string
s="sai"
s='sai'
s=str('sai')
s=str("sai")
s=''        #empty string
s=str()

#mutable - can not change value of variable
#immutable - can change value of variable
#strings are immutable

str='sai'
print(id(str))  #2471770914416

str2= str+"jrv"
print(id(str2))     #2092884457904

#string +  *
str="jai"
print(str+" hai")
print(str*3)

 #slicing  ====    starting index=0  and ending index=1
str="welcome"
print(str[1:4])
print(str[:5])
print(str[2:])






