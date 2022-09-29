from reprlib import recursive_repr
from orm import dcm_orm




path = "/mnt/c/Users/tekna/Downloads"
orm = dcm_orm(path,recursive = False)
result = orm.filter(endswith = "dcm")
print(result)

