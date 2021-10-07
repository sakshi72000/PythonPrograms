# Assignment 1
# Program 3 :Program to Add two numbers and display the Addition

def Add(no1,no2):
	return no1 + no2

def main():
	print("Enter the first number:")
	value1 = int(input())
	
	print("Enter second number:")
	value2 = int(input())
	
	ret = Add(value1,value2)
	print("The Addition is:",ret)

if __name__ == "__main__":
	main()
