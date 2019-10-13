import os
import hashlib
import sys

class FindDupes:

	def __init__(self, root):
		self.dupes = {}
		self.root = root
		self.num_deleted = 0
		self.BLOCKSIZE = 65536

	def parse_files(self):
		for subdir, dirs, files in os.walk(self.root):
			for file in files:
				filepath = os.path.join(subdir, file)
				file_hash = self.hashfile(filepath)
				if file_hash in self.dupes:
					self.dupes[file_hash].append(filepath)
				else:
					self.dupes[file_hash] = [filepath]	

	def parse_dupes(self):
		for h in self.dupes:
			if len(self.dupes[h]) > 1:
				for filepath in self.dupes[h][1:]:
					self.num_deleted += 1
					os.remove(filepath)
				print('Keeping {}'.format(self.dupes[h][0]))	

	def hashfile(self, path):
		hasher = hashlib.md5()
		with open(path, 'rb') as the_file:
			buf = the_file.read(self.BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = the_file.read(self.BLOCKSIZE)
		return hasher.hexdigest()

	def main(self):
		print('Parsing Files...')
		self.parse_files()
		print('Parsing Dupes...')
		self.parse_dupes()
		print('Deleted {} duplicates'.format(self.num_deleted))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		root = sys.argv[1]
	else:
		root = '.'

	fd = FindDupes(root)
	fd.main()
	