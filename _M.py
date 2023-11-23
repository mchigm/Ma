import imodule


#Input with ":"
while True:
	receives = input(":")
get = []
for i in range(len(receives)):
	receive = receives[i]
	if receive == " ":
		get = []
	elif receive == "\":
		get = []
		level.update(1)
	elif receive == "'":
		get = []
		rec = ""
		while rec != "'":
			get.append(rec)
			i +=1
			rec = receives[i]
			try: i > range(len(receives.split())):
			except: m_error.syntax("0", "", "", i)
				break
	else:
			get.append(receive)
			

#############
# Token
#############
class Tokens:
	def __init__ (self):
		pass
	def ver(command, self):
		pass
	def tokens(self):
		pass