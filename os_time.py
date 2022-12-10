import os
import time

print(os.getcwd())
os.mkdir('new_folder')
time.sleep(5)
os.rename('new_folder', 'new_folder_2')
time.sleep(5)
os.rmdir('new_folder_2')

#os.system('cmd /c "cd C://Users//vdi-student//Desktop"')
