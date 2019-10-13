import os
import hashlib
import sys

class FindDupes:

	def __init__(self, root):
		self.dupes = {}
		self.root = root

	def parse_files(self):
		for subdir, dirs, files in os.walk(self.root):
			for file in files:
				filepath = os.path.join(subdir, file)
				file_hash = hashfile(filepath)
				if file_hash in self.dupes:
					self.dupes[file_hash].append(filepath)
				else:
					self.dupes[file_hash] = [filepath]	

	def hashfile(self, path, blocksize = 65536):
		afile = open(path, 'rb')
		hasher = hashlib.md5()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()


	def main(self):
		self.parse_files()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		root = sys.argv[1]
	else:
		root = '.'

	fd = FindDupes(root)
	fd.main()