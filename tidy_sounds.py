import os
import sys

class TidySounds:

	def __init__(self):
		self.files = {'urls': [], 'fxps': [], 'empty_dirs': []}

	def parse_files(self, root):
		for subdir, dirs, files in os.walk(root):
			for file in files:
				filepath = os.path.join(subdir, file)
				if file.endswith('.url'):
					self.files['urls'].append(filepath)
				elif file.endswith('.fxp'):
					self.files['fxps'].append(filepath)
				elif os.path.isdir(filepath) and not os.listdir(filepath):
					self.files['empty_dir'].append(filepath)

	def process_files(self):
		for tidy_type in self.files:
			if len(self.files[tidy_type]):
				print ('Found {} {}'.format(len(self.files[tidy_type]), tidy_type))
				if self.confirm_delete(tidy_type):
					self.delete_type(tidy_type)

	def confirm_delete(self, tidy_type):
		return input('Really delete {} {}?'.format(len(self.files[tidy_type]), tidy_type)).lower().startswith('y')

	def delete_type(self, tidy_type):
		for filepath in self.files[tidy_type]:
			print('Deleting {}'.format(filepath))
			os.remove(filepath)

	def main(self, root='.'):

		self.parse_files(root)
		self.process_files()


if __name__ == '__main__':
	
	if len(sys.argv) > 1:
		root = sys.argv[1]
	else:
		root = '.'

	ts = TidySounds()
	ts.main(root)