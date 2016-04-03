class ConfigManager:
	def __init__(self, coordinates, sizes):
		self.coordinates=coordinates
		self.sizes=sizes

	def checkcords(self):
		errorstrings=["Error in Center of X", "Error in Center of Y", "Error in Center of Z"]
		message=[]
		for i in range(len(self.coordinates)):
			try:
				float(self.coordinates[i])
			except:
				message.append(errorstrings[i])
		if len(message):
			return message
		else:
			return ["Co-ordinates are Okay!"]

	



