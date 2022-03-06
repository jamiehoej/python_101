# def aboutme(name, age, city):
# 	howold = "if >1 "year" elif <1 "years ""
# 	return "hello my name is " + name + "I am" + age + howold=if >1 "year " elif <1 "years " + "old " + "and i live in " city 


def aboutme2(name, age, city):
	howold= ""

	if age<1:
		howold="year" 
	elif age>1:
		howold="years"

	if age<=1:
		howold="year"
	elif age>1:
		howold="years"
	else:
		howold="ohno, oopsie"

	howold="year"
	if age>1: 
		howold="years"
	
	howold="year" if age<=1 else "years"

	s="hello my name is " + name + " i am " + str(age) + howold + " i come from the land down under, called" + city
	s="hello my name is " + name + " i am " + str(age) + ("year" if age<=1 else "years") + " i come from the land down under, called" + city
	
	return s

henlo=aboutme2("fuckthisshit", 0, "getmeoutpls")
print(aboutme2("hullabulla", 2, " not australia, haha"))
print(henlo)
