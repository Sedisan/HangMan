def countChance(l):
	from math import ceil as ceiling
	return ceiling(len(l)/2)
class Check():
	def __init__(self,chance,chain):
		self.chance = chance
		self.guessed = 0
		self.lengthOfCh = self.retOfLengthChain(chain)
		self.chain =  list(chain[0])
		self.is_space = None
		self.howManySpace =0
		for i in range(1,len(chain)):
			if chain[i] !=' ':
				self.chain.append(' _ ')
			else:
				self.chain.append(' ')
				self.is_space = 1
				self.howManySpace+=1
		if self.is_space == 1:
			self.lengthOfCh = self.lengthOfCh-self.howManySpace
			
		self.fillAll(self.chain[0],chain)
	def checkLiteral(self,l,literal):
		pos = literal.find(l)
		if literal.find(l)!= -1:
			if str(self.chain).find(l)!=-1:
				print("Letter you inputed exist")
				return
			self.fillAll(l,chain)
			print("Liter Found")
			if self.lengthOfCh == self.guessed:
				print("Congratulation! You win the game. Program will exit")
				exit()
		else:
			self.chance = self.chance -1
			print("rest chance: "+str(self.chance))
			print("Not found")

	def fillAll(self,founded,main_chain):
		table = [i for i, value in enumerate(main_chain) if value == founded]

		for var in table:
			self.guessed+=1
			self.chain[var]=founded

	def retChance(self):
		return self.chance
	def showActualChain(self):
		for var in self.chain:
			print(var,end ='')
		print('\n')
	def retOfLengthChain(self,chain):
		return len(chain)
	def check_lose(self):
		if self.chance == 0:

		
			try:
				print("End game! Your chance ends. Try it again ? Enter 1 to accept")
				user = int(input())
				if user == 1:
					return True
				else:
					exit()
			except:
				exit()
		else:
			return False
	def countGuessed(self):
		pass
		
		
#class Count(Check):

#	def __init__(self,Check.retChance())
#		self.

while(True):
	print("Enter your chain to play. Max length is 10")
	chain = input()
	chain = chain.lower()
	
	assert (len(chain)>0)-(len(chain)>10),"Your length is too long or equal 0\n"
	print("Enter a short description of your chain")
	description = input();
	from sys import platform
	from os import system

	if platform.startswith('linux') or platform == "darwin":
		system('clear')
	else:
		system('cls')
	system = None
	platform =None
	del platform
	del system
	x = Check(countChance(chain),chain)
	while(x.retChance()>0):
		print("Description:",description)
		print("Enter a letter. Length of guessing word:"+str(len(chain)))
		x.showActualChain()
		player2=''
		while(len(player2)>2 or len(player2)<1):		
			player2 = input()
		x.checkLiteral(str(player2),chain)
		if x.check_lose():
			break;
		else:
			continue
	continue
