while True:
	user_input = int(input("Enter an integer: "))
	if user_input % 2 != 0:
		print("this is an odd number")
		break
	print("this is an even number")