from glob import glob
import numpy as np
from pprint import pprint
# http://localhost:60848/?code=ad7310ee55d5afaca3b6&state=d4e466ff76d443159a51cafd6e5177d3
class dcm_orm():

    def __init__(self,path = None, ext = "", recursive = True) -> None:
        self.RECURSIVE = recursive
        self.PATH = path
        self.EXT = ext
        self.FILES = self._get_files()
        # pprint(self.FILES)
        self.print_files()
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
                output = True
                if key == "endswith":
                    output =  output & self._filter_endswith(fil,key,val)
                
                if key == "isfile":
                    output = output & self._filter_isfile(fil,key,val)



            res.append(output)



        res = np.array(res)
        print(type(self.result))
        print(type(res))
        print(self.result)
        print(res)
        self.result = (res & self.result)
        self.print_output()
        return self

    '''
    define custom filters here
    '''

    def _filter_endswith(self,obj,key,val):
        if obj.endswith(val):
            # print(obj)
            return 1
        else:
            return 0

    def _filter_isfile(self,obj,key,val):
        from pathlib import Path
        path = Path(obj)
        return path.is_file()


    def print_output(self):
        LEN = 100   
        for fil,res in zip(self.FILES,self.result):
            if len(fil)>LEN:
                print(f"{fil[:int(LEN/2)]}...{fil[-int(LEN/2):]} -> {res}")
            else:
                print(f"{fil} -> {res}")

    def print_files(self):
        LEN = 100   
        for en,fil in enumerate(self.FILES):
            if len(fil)>LEN:
                print(f"{en}->{fil[:int(LEN/2)]}...{fil[-int(LEN/2):]}")
            else:
                print(f"{en}->{fil}")


                




