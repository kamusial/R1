import os
import time
print('aktualna lokalizacja to:',os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop\\Kamil')
print('aktualna lokalizacja to:',os.getcwd())
os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', '2_new_folder')
time.sleep(2)
os.rmdir('2_new_folder')