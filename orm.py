from glob import glob
import numpy as np

class dcm_orm():

    def __init__(self,path = None, ext = "", recursive = True) -> None:
        self.RECURSIVE = recursive
        self.PATH = path
        self.EXT = ext
        self.FILES = self._get_files()
        print(self.FILES)
        print("********")
        print("\n\n{count} files found".format(count = len(self.FILES)))
        self.result= np.array([1] * len(self.FILES))

    def _get_files(self):
        ''' 
        this function fetches the .EXT files from the path
        '''
        return list(glob(self.PATH + "/**/*" + self.EXT,recursive=self.RECURSIVE))


    def filter(self,**args):
        print(args)
        res = [0] * len(self.FILES)
        res = []
        for fil in self.FILES:
            for key,val in args.items(): 
                # print(arg)
                if key == "endswith":
                    res.append(self._filter_endswith(fil,key,val))


        res = np.array(res)
        print(type(self.result))
        print(type(res))
        print(self.result)
        print(res)
        self.result = (res & self.result)
        self.print_output()
        return self.result

    '''
    define custom filters here
    '''

    def _filter_endswith(self,obj,key,val):
        if obj.endswith(val):

            print(obj)
            return 1
        else:
            return 0


    def print_output(self):
        LEN = 50   
        for fil,res in zip(self.FILES,self.result):
            if len(fil)>LEN:
                print(f"{fil[:int(LEN/2)]}...{fil[-int(LEN/2):]} -> {res}")
            else:
                print(f"{fil} -> {res}")

                




