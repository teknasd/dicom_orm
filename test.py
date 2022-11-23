from reprlib import recursive_repr
from orm import dcm_orm
import time
from helper import show_time
import numpy as np


# path = "/mnt/c/Users/Sanket.deshpande/Documents/dicom_orm"
path = "/mnt/c/Users/Sanket.deshpande/Documents"
# path = "/mnt/c/Users/Sanket.deshpande/Downloads/Hip Fracture, Reader Says No Fracture_3366_3462"
orm = dcm_orm(path, recursive = True)
st1time = time.time()

# result = orm.filter(endswith = ".dcm", isfile = True)
# result = orm.filter(endswith = ".dcm").filter(isfile = True)

# PATH IS FILE AND DCM FORMAT
result = orm.filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True).filter(isfile = True)
result.print_output()
# PATH IS FILE AND DEFAULT DCM FORMAT
# result = orm.filter(isfile = True)

# PATH IS FILE AND DEFAULT DCM FORMAT
# result = orm.filter()
en1time = time.time()
print(result)
print(f"TAT: {np.sum(result.__times__)} secs")

show_time(st1time,en1time,"all")



