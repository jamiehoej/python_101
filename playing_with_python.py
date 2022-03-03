def aboutme(name: str, age: int, city: str) -> str:
	s="hello my name is " + name + " I am " + str(age) + " old " + "i live in " + city

	return s


# now we call the function
msg=aboutme("martin",26,"odense")
print(msg)

print(aboutme("1111",23442,"dkjscanvjdkasnv"))

def aboutme2(name: str, age: int, city: str) -> str:
	word=""
	if age<=1:
		word=" year"
	elif age>1:
		word=" years"
	
	s="hello my name is " + name + " I am " + str(age) + word + " old " + "i live in " + city
	return s

# we run this other function, yes hehe
print(aboutme2("boris",2,"kentucky"))