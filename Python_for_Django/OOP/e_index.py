#importing d_code_storage.py file and use their functionality
#If we want to import all the elements of the d_code_storage.py than using this command.
import d_code_storage

#but if we want to import individual elements of the d_code_storage than use this command.
from d_code_storage import add
#if we want to import folder's folcer than use this command
#From main_folder.file_name import function_name,class_name,variable_name,etc
#From main_folder.first_sub_folder.file_name import function_name,class_name,variable_name,etc


#obj = d_code_storage.Name()
print(d_code_storage.add(1000,232)) #import d_code_storage.py use this.
print(dir(d_code_storage))