import zipfile
import os
import tarfile


path = r'C:\Users\Chris Green\Documents\job10-8-19'

files_extracted = r'C:\Users\Chris Green\Documents\job10-8-19\data'
#create directory
try:
	os.mkdir(files_extracted)
except:
	print("directory already excitst")

with zipfile.ZipFile(path + "\sample_data.zip", 'r') as zip_ref:
    zip_ref.extractall(files_extracted)

list = os.listdir(files_extracted) # dir is your directory path
number_files = len(list)
print(number_files)

#try:
for dirpath, dir, files in os.walk(top=files_extracted):
	for file in files:
		print(files)
		tar = tarfile.open(os.path.join(dirpath, file))
		#print(tar)
		tar.extractall()
		tar.close()
#except tarfile.ReadError:
#	print("No files to untar, moving on.")

