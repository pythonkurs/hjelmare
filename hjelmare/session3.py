import os

# Make a context manager which changes the current directory for the python script using it, and changes back to where you came from upon exit.

class ChangeDir(object):
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.old_dir = None

    def __enter__(self):
        self.old_dir = os.getcwd()
        os.chdir(self.new_dir)

    def __exit__(self, type, value, tb):
        os.chdir(self.old_dir)

class CourseRepo(object):

    def __init__(self, surname):
        self.surname = surname

    @property
    def surname(self):
        return self.name

    @surname.setter
    def surname(self, value):
        self.name = value
        self.required = [".git", "setup.py", "README.md", "scripts/getting_data.py", "scripts/check_repo.py", self.name+"/__init__.py", self.name+"/session3.py"]

    def check(self):

        # if all directories or files exist
        for req_path in self.required:
            if not os.path.exists(req_path):
                return False
        return True
