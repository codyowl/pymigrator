import sys
import os

class Bootstrapmigrator:
    def project_path(self, path):
        self.path = path
        try:
            os.listdir(self.path)
            self.files_path = [os.path.join(path, names) for path, subdir, files in os.walk(self.path) for names in files]
            self.html_files = [files for files in self.files_path if files.endswith('.html')]
        except IOError as e:
           raise ValueError (e) 
    def to_version(self, version_number):
        self.version_number = version_number
    def migrate(self):
        print "your codings are migrating"
