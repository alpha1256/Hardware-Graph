from cpu_temp import plotCPUTemp

def main():
	userIn =input('Enter filename: ')
	userIn = userIn +".csv"
	plotCPUTemp(userIn)

if __name__ == '__main__':
	main()
