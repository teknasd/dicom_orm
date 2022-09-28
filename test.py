from orm import dcm_orm




path = "/mnt/c/Users/tekna/Downloads"
orm = dcm_orm(path)
result = orm.filter(endswith = "dcm")
print(result)



orm.filter(endswith = "dcm")

