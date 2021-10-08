# Assignment 1
# Program 9 : Program to Display the even numbers in between 0 to 20
 
def Even():
	iCnt = 0
	for iCnt in range(0,21):
		if iCnt % 2 == 0:
			print(iCnt)
def main():
	Even()
if __name__ == "__main__":
	main()
