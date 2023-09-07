import os
  
  
# Ruta del archivo de origen.
source = 'main.txt'
  
# Ruta de archivo de destino
dest = 'newfile.txt'
  
  
# Ruta de destino
# Método os.rename() 
os.rename(source, dest)
print("La ruta de origen fue renombrada ruta de destino exitosamente.")
