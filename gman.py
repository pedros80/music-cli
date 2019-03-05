import fnmatch
import os
import shutil
import subprocess
import re

class GMan:

    def __init__(self, dir_name='out'):
        self.dir_name = dir_name
        self.command = "ffmpeg -i {} -r ntsc {} -loglevel error"
        if not os.path.exists(dir_name):
            print("Creating destination directory - {}".format(dir_name))
            os.mkdir(dir_name)
        else:
            print("Using destination directory - {}".format(dir_name))        

    def main(self):
        for root, dirnames, filenames in os.walk('.'):
            for filename in fnmatch.filter(filenames, '*.mp4'):
                src = os.path.join(root, filename)
                dst = self.get_destination_file(src)
                if not os.path.isfile(dst):
                    self.process_file(src, dst)

    def get_clean_file_name(self, filename):
        filename = filename.replace(' ', '_')
        regex = re.compile('\(.+?\)')
        filename = regex.sub('', filename)
        filename = filename.replace("'", "")
        filename = filename.replace("&", "")

        return filename

    def get_destination_file(self, src):
        dst = os.path.split(src)[-1]

        return os.path.join(self.dir_name, self.get_clean_file_name(dst))

    def process_file(self, src, dst):
        print("Processing file - {}".format(dst))
        shutil.copyfile(src, dst)
        mp3 = dst.replace('.mp4', '.mp3')
        subprocess.call(self.command.format(dst, mp3), shell=True)
        os.remove(dst)


if __name__ == '__main__':
    g = GMan()
    g.main()
