from glob import glob
import numpy as np

class dcm_orm():

    def __init__(self,path = None, ext = "", recursive = True) -> None:
        self.recursive = recursive
        self.path = path
        self.ext = ext
        self.files = self._get_dicom_files()
        print(self.files)
        print("********")
        print("\n\n{count} files found".format(count = len(self.files)))
        self.result= np.array([1] * len(self.files))

    def _get_dicom_files(self):
        ''' 
        this function fetches the dicom files from the path assuming file format is .dcm
        '''
        return list(glob(self.path + "/**/*" + self.ext,recursive=self.recursive))


    def filter(self,**args):
        print(args)
        res = [0] * len(self.files)
        res = []
        for fil in self.files:
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
        return np.array(res) &  np.array(self.result)





    '''
    define custom filters here
    '''

    def _filter_endswith(self,obj,key,val):
        if obj.endswith(val):

            print(obj)
            return 1
        else:
            return 0




