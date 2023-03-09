from cpu_temp import plotCPUTemp
from gpu_temp import plotGPUTemp
from cpu_load import plotCPULoad
from gpu_load import plotGPULoad

def main():
	userIn =input('Enter filename to read from: ')
	nameOfGame = input('Enter the name of this game: ')

	#print("Enter 1 For CPU Temp\nEnter 2 for GPU Temp\nEnter any other key to exit: ")
	try:
		userInput = input("Enter 1 For CPU Temp\nEnter 2 for GPU Temp\nEnter 3 for CPU Load\nEnter 4 for GPU Load\nEnter any other key to exit: ")
		print(userInput)
		if userInput == '1':
			plotCPUTemp(userIn,nameOfGame)
		elif userInput == '2':
			plotGPUTemp(userIn, nameOfGame)
		elif userInput == '3':
			plotCPULoad(userIn, nameOfGame)
		elif userInput == '4':
			plotGPULoad(userIn,nameOfGame)
		else:
			print("Thank you and have a nice day")
	except:
		print("An error occured")

if __name__ == '__main__':
	main()
