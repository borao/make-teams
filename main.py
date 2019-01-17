from student import *
from parse import *

stud = []
stud = sorted(stud, key=lambda x: x.__compare__())

for file in Parse.get_excel_files_in_current_dir():
    print(file)