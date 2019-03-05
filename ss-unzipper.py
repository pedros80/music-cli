import zipfile
import os
import fnmatch
import time

class SampleSwapUnzipper:

	def __init__(self, user='pedros', dest='Sounds', file_prefix='pedrodelsol'):
		self.home        = '/home/{}/'.format(user)
		self.source_dir  = self.home + 'Downloads'
		self.destination = self.home + dest
		self.zip_count   = 0
		self.files_count = 0
		self.start_time  = time.time()
		self.file_prefix = file_prefix

	def main(self):
		for root, dirnames, filenames in os.walk(self.source_dir):
			for filename in fnmatch.filter(filenames, '*.zip'):
				if filename.startswith(self.file_prefix):
					self.zip_count += 1
					print('Processing File - {}'.format(filename))
					print('-' * len('processing {}'.format(filename)))
					src = os.path.join(root, filename)
					print('Unzipping - ' + src)
					with zipfile.ZipFile(src, 'r') as zip_ref:
						zip_ref.extractall(self.destination)
						self.files_count += len(zip_ref.infolist())
						zip_ref.printdir()
					print('Removing - ' + src + "\n")
					os.remove(src)

		elapsed_time = time.time() - self.start_time

		print('Processed {} zip files, adding {} samples in {} seconds'.format(self.zip_count, self.files_count, elapsed_time))


if __name__ == '__main__':
	ssu = SampleSwapUnzipper()
	ssu.main()