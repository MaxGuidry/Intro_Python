import math



class Vector3:
	x=0
	y=0
	z=0
	
	def __init__(self,ex,why,zee):
		self.x=ex
		self.y=why
		self.z=zee
	
	def Magnitude(self):
		return math.sqrt(self.x**2+self.y**2+self.z**2)
		
	def Normalized(self):
		return Vector3(self.x/self.Magnitude(),self.y/self.Magnitude(),self.z/self.Magnitude())
		
	def Print(self):
		print self.x
		print self.y
		print self.z