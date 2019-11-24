
''' This is a solution for 0-1 knapsack problem using GAs'''



''' We are using numpy.random to generate random children'''
from numpy.random import randint
from random import randint	as RandomInt
from random import choice
from itertools import chain
Population = []

''' Getting the problem's detail ''' 

KnapsackCap = int(input('how much is the Knapsack capacity ?  \n'))
NumberOfObjects = int(input('How many Objects do we have?  \n'))


ObjectsDetail = []
print('Please enter the required information \n')

for i in range(NumberOfObjects):
	weight = int(input('Weight [%s] : '%i))
	profit = int(input('Profit [%s] : '%i))
	print('\n')
	ObjectsDetail.append([weight,profit])
print('Knapsack Contains : \n',ObjectsDetail,'\n')


''' Generating First Offsprings '''
NumberOfOffsprings = int(input('How many Offspring do you want to create ?  '))
Offspring = randint(2, size=(NumberOfOffsprings,NumberOfObjects))

''' fitness function''' 

''' 
How we do it?
The fitness function will multiplies the Offsprings to each weight
and then sum the values.
if the summation of values is more than knapsack capacity the fitness
will be 0 and if its less than that, it will put the summation of Profits 
into the Fitness.

'''
Fitness = []

for i in range (NumberOfOffsprings):
	WeightSum = 0
	ProfitSum = 0
	for j in range(NumberOfObjects):
		WeightSum = WeightSum + (Offspring[i][j] * ObjectsDetail[j][0])
	for j in range(NumberOfObjects):
		if (WeightSum <= KnapsackCap):
			ProfitSum = ProfitSum + Offspring[i][j] * ObjectsDetail[j][1]
		else:
			ProfitSum = 0
	Fitness.append(ProfitSum)

''' First Selection'''

SelectionItems = []
SelectionFitness = []
for i in range (len(Fitness)):
	if (Fitness[i] >= (KnapsackCap/10) ):
		SelectionItems.append(list(Offspring[i]))
SelectionItems1 = []
end = True
counter = 0


''' The Ultimate proccess to find the best answer'''

'''
 Here we select items with random one point random
 cross over.
 then the fitness function will evaluate the fitness
 of our population and then we select the ones that
 are 10% up of our population.
 the cut point is looping 1000 time, this means
 after 1000 time the result will be choose by
 maxmimum Profit.
'''
while (end):
	for i in range(int(NumberOfOffsprings)):
		S1 = choice(SelectionItems)
		S2 = choice(SelectionItems)
		CrossOverPoint = RandomInt(1,NumberOfObjects)
		NextGen = list(chain(S1[0:CrossOverPoint],S2[CrossOverPoint:]))
		SelectionItems1.append(NextGen)
	
	''' Fitness func'''
	Fitness = []
	for i in range (NumberOfOffsprings):
		WeightSum = 0
		ProfitSum = 0
		for j in range(NumberOfObjects):
			WeightSum = WeightSum + (SelectionItems1[i][j] * ObjectsDetail[j][0])
		for j in range(NumberOfObjects):
			if (WeightSum <= KnapsackCap):
				ProfitSum = ProfitSum + SelectionItems1[i][j] * ObjectsDetail[j][1]
			else:
				ProfitSum = 0
	Fitness.append(ProfitSum)
	
	if (counter == 1000):
		print('No way')
		fitesst = max(Fitness)
		print(fitesst)
		a = Fitness.index(fitesst)
		print(SelectionItems1[a])
		
		#GoalIndex = max(Fitness).index
		#Goal = SelectionItems1[GoalIndex]
		#print('The Goal is : %s'%Goal)
		exit()
		
	
	
	SelectionItems = []
	for i in range (len(Fitness)):
		if (Fitness[i] >= (KnapsackCap/2) ):
			SelectionItems.append(list(SelectionItems1[i]))
	SelectionItems1 = []
	counter+=1


