def aboutme(name: str, age: int, city: str)-> str:

	howold="year"
	if age>1: 
		howold="years"
	oiyes="Hello, dis my name you see right here: " + name + " I am old. this is my age right here as you see i am " + str(age) + howold + "old" + " i come from a city known as " + city + "its ok"

	return oiyes

s=aboutme("cjnadsjva", 34, "ugggabugga")
print(s)
print(aboutme("martini",26,"odense"))


l=[2, 4, 3, 5]
print(l)

a=l[3]
print(a)
print(l[-1])
len(l)
print(len(l))

print(l[0:3])

li=l[0:3]
# print(l[0])
# print(l[1])
# print(l[2])

for element in li:
	print(element)
	if element==4:
		break

o=range(11)
for element in o:
	print(element)

for element in range(10):
	print(element)

for i in range(len(l)):
	print(i)

print("----")
for i in range(len(l)):
	print("i: ", i, "l[i]: ", l[i])
	# print(l[i])

