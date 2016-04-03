import os
class Docker:
	def __init__(self, receptor, ligand, conf):
		##creates the folder experiment and copies vina binary
		folders=os.listdir("resources")
		if "experiment" not in folders:
			os.mkdir("resources/experiment")
			os.system("cp resources/vina/vina resources/experiment")
		self.receptor=receptor
		self.ligand=ligand
		self.conf=conf
	
	def copyfiles(self):
		os.system("cp resources/receptor/" +self.receptor+" resources/experiment/")
		os.system("cp resources/ligands/"+self.ligand+ " resources/experiment/")

		newconf=""
		newconf+="receptor = "+self.receptor+"\n"
		newconf+="ligand = "+self.ligand+"\n"
		newconf+="log = "+self.ligand.replace(".pdbqt",".log")+"\n"
		newconf+=self.conf
		newconf+="out = "+self.receptor.replace(".pdbqt","_")+self.ligand.replace(".pdbqt","_complex.pdbqt")

		newconffilename=self.ligand.replace(".pdbqt",".conf")
		writer=open("resources/experiment/"+newconffilename,"w")
		writer.write(newconf)
		writer.close()

		return newconffilename+" created!"



	
