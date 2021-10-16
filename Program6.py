# Assignment 1
# Problem 6 : Program to display the number is possitive negative or zero

def ChkNum(no):
	if no < 0:
		print("Number is Negative")
	elif no > 0:
		print("Number is Positive")
	else:
		print("Number is Zero")
def main():
	print("Enter the number:")
	value = int(input())
	
	ChkNum(value)

if __name__ == "__main__":
	main()
