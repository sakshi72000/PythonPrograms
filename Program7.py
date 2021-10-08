# Assignment 1
# Program 7 : Program to find the number is divisible by 5

def Divisible(no):
	if no % 5 == 0:
		return True
	else:
		return False
def main():
	print("Enter the number:")
	value = int(input())
	ret = Divisible(value)
	if ret == True:
		print("True")
	else:
		print("False")
if __name__ == "__main__":
	main()
