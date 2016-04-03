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

	def checksizes(self):
		errorstrings=["Error in Size of X", "Error in Size of Y", "Error in Size of Z"]
		message=[]
		for i in range(len(self.sizes)):
			try:
				float(self.sizes[i])
			except:
				message.append(errorstrings[i])
		if len(message):
			return message
		else:
			return ["Sizes are Okay!"]
	
	def writefile(self):
		outstring=""
		coordlabels=["center_x","center_y","center_z"]
		
		for c, vals in zip(coordlabels, self.coordinates):
			outstring+=c+" = "+vals+"\n"
		
		sizelabels=["size_x","size_y","size_z"]

		for s, vals in zip(sizelabels, self.sizes):
			outstring+=s+" = "+vals+"\n"

		writer=open("resources/baseconf","w")
		writer.write(outstring)
		writer.close()
		return "Created base Configuration"







