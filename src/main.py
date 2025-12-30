from cpu_temp import plotCPUTemp
from gpu_temp import plotGPUTemp
from cpu_load import plotCPULoad
from gpu_load import plotGPULoad
from ram_load import plotRAMLoad
from fan_speed import fanSpeedPlot
import logging

def main():
	userIn =input('Enter filename to read from: ')
	nameOfGame = input("Enter the name of this game: ")
	print("\nName of game: " + nameOfGame)
	#nameOfGameList = list(map(int, input('Enter the name of this game: ').split()))
	#nameOfGame = ""
	#for counter in range(len(nameOfGameList)):
	#	nameOfGame += nameOfGameList[counter] + " " 


	#print("Enter 1 For CPU Temp\nEnter 2 for GPU Temp\nEnter any other key to exit: ")
	try:
		userInput = input("Enter 1 For CPU Temp\nEnter 2 for GPU Temp\nEnter 3 for CPU Load\nEnter 4 for GPU Load\nEnter 5 for RAM Load\nEnter 6 for Fan Speed\nEnter any other key to exit: ")
		print(userInput)
		if userInput == '1':
			plotCPUTemp(userIn,nameOfGame)
		elif userInput == '2':
			plotGPUTemp(userIn, nameOfGame)
		elif userInput == '3':
			plotCPULoad(userIn, nameOfGame)
		elif userInput == '4':
			plotGPULoad(userIn,nameOfGame)
		elif userInput == '5':
			plotRAMLoad(userIn, nameOfGame)
		elif userInput == '6':
			fanSpeedPlot(userIn, nameOfGame) 
		else:
			print("Thank you and have a nice day")
	except Exception as Argument: 
		logging.exception("An Error has occured") 

if __name__ == '__main__':
	main()
