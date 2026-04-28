name = input("what is ur name?")
print("hello " +name+ "!")

for i in range(1,11):
	print(i)
numbers =[10,2,8,5,30]

for num in numbers:
	if num > 20:
		print(str(num) + " is greater than 20")
	else :
		print(str(num) + " is less than 20")

def check_strength_password(password):
	if len(password) < 6:
 		print("easy password")
	elif len(password) < 10:
		print("medium password")
	else:
		print("strong password")

check_strength_password("hi")
check_strength_password("dharmi00")
check_strength_password("mystr0ngpassword")

