from reprlib import recursive_repr
from orm import dcm_orm




path = "/mnt/c/Users/Sanket.deshpande/Documents/dicom_orm"
orm = dcm_orm(path, recursive = True)
result = orm.filter(endswith = ".py")
print(result)

