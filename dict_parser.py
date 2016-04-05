import os,json
files=os.listdir("/home/anmol/Desktop/NLP lab/eng-hindi-dict-utf8")
print files
os.chdir("/home/anmol/Desktop/NLP lab/eng-hindi-dict-utf8/")
for file in files:
	print file
	fil=open(file,"r").read().split("\n<br>")
	for elems in fil:
		try:
			lines=elems.split("<br>")
			print lines[0]
			op=open("output","a")
			op.write(str(lines[0]))
		except Exception as e:
			print e;