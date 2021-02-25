# Assignment 1
# Program 2

def ChkNum(no):
	if no % 2 == 0:
		return True
	else:
		return False

def main():
	print("Enter the number:")
	value = int(input())
	ret = ChkNum(value)
	if ret == True:
		print("Number is Even")
	else:
		print("Number is Odd")
	
	
if __name__ == "__main__":
	main()
