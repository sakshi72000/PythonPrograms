# Assignment 1
# Program 8

def Print(no):
	iCnt = 0
	for iCnt in range(0,no):
		print("*")

def main():
	print("Enter the number:")
	value = int(input())
	
	Print(value)
if __name__ == "__main__":
	main()
