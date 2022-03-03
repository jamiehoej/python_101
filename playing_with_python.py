def aboutme(name: str, age: int, city: str) -> str:
	s="hello my name is " + name + " I am " + str(age) + " old " + "i live in " + city

	return s


# now we call the function
msg=aboutme("martin",26,"odense")
print(msg)

print(aboutme("1111",23442,"dkjscanvjdkasnv"))
