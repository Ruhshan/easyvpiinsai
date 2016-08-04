import os
import time
import subprocess
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
		self.newconffilename=""
	
	def copyfiles(self):
		os.system("cp resources/receptor/" +self.receptor+" resources/experiment/")
		os.system("cp resources/ligands/"+self.ligand+ " resources/experiment/")

		newconf=""
		newconf+="receptor = "+self.receptor+"\n"
		newconf+="ligand = "+self.ligand+"\n"
		newconf+="log = "+self.ligand.replace(".pdbqt",".log")+"\n"
		newconf+=self.conf
		newconf+="out = "+self.receptor.replace(".pdbqt","_")+self.ligand.replace(".pdbqt","_complex.pdbqt")

		self.newconffilename=self.ligand.replace(".pdbqt",".conf")
		writer=open("resources/experiment/"+self.newconffilename,"w")
		writer.write(newconf)
		writer.close()

		return self.newconffilename+" created!"
	def dock(self):
		path=os.getcwd()
		os.chdir("resources/experiment/")
		#print os.getcwd()
		#os.system("./vina --config "+self.newconffilename)
		vina_execute=subprocess.Popen("./vina --config "+self.newconffilename,shell=True)
		#time.sleep(10)
		#vina_execute.kill()
		#os.killpg(os.getpgid(vina_execute.pid), signal.SIGTERM)
		#os.system("./vina --config "+self.newconffilename)
		vina_execute=subprocess.Popen("./vina --config "+self.newconffilename,shell=True)
		time.sleep(10)
		vina_execute.kill()
		os.chdir(path)




	
