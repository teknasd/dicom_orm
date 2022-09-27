from glob import glob

class dcm_orm():

    def __init__(self,path = None) -> None:
        self.files = list(glob(path + "/**/*",recursive=False))
        print(self.files)
        print("********")
        print("\n\n{count} files found".format(count = len(self.files)))
        self.result= [1] * len(self.files)


    def filter(self,**args):
        print(args)
        res = [0] * len(self.files)
        res = []
        for fil in self.files:
            for key,val in args.items():
                # print(arg)
                if key == "endswith":
                    if fil.endswith(val):

                        print(fil)
                        res.append(1)
                    else:
                        res.append(0)
        # print(res)
        return res and self.result





path = "/mnt/c/Users/tekna/Downloads"
orm = dcm_orm(path)
result = orm.filter(endswith = "dcm")
print(result)




