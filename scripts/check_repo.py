from hjelmare.session3 import CourseRepo, ChangeDir
import os, sys
#This script should take an argument which is the absolute path to a repository.
if len(sys.argv) != 2:
    print("You should give one argument which should be the absolute path to the directory of interest.")
    sys.exit()
path = sys.argv[1]
if not os.path.exists(path):
    print(path+" is not a correct absolute path.")
    sys.exit()

path_final = os.path.basename(os.path.normpath(path))


#Make an instance of `CourseRepo` using the final part of the absolute path.
#Change directory to the absolute path using the context manager.
#Call the `check()` method. If `check()` returns `True` the script shall print "PASS", otherwise the script should print "FAIL".

repo = CourseRepo(path_final)

with ChangeDir(path):
    if repo.check():
        print("PASS")
    else:
        print("FAIL")
