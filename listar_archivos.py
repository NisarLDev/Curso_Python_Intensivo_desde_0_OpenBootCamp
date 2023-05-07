import os
import math

start_path = "Descargas"

for (path,dirs,files) in os.walk(start_path):
    
    for file in files:
        fstat = os.stat(os.path.join(path,file))

        # Convert file size to MB, KB or Bytes
        if (fstat.st_size > 1024 * 1024):
            fsize = math.ceil(fstat.st_size / (1024 * 1024))
            unit = "MB"
        elif (fstat.st_size > 1024):
            fsize = math.ceil(fstat.st_size / 1024)
            unit = "KB"
        else:
            fsize = fstat.st_size
            unit = "B"

        print('\t{:15.15s}{:8d} {:18s}'.format(file,fsize,unit))

start_path = "Carpeta_personal"

for (path,dirs,files) in os.walk(start_path):
    
    for file in files:
        fstat = os.stat(os.path.join(path,file))

        # Convert file size to MB, KB or Bytes
        if (fstat.st_size > 1024 * 1024):
            fsize = math.ceil(fstat.st_size / (1024 * 1024))
            unit = "MB"
        elif (fstat.st_size > 1024):
            fsize = math.ceil(fstat.st_size / 1024)
            unit = "KB"
        else:
            fsize = fstat.st_size
            unit = "B"

        print('\t{:15.15s}{:8d} {:18s}'.format(file,fsize,unit))

