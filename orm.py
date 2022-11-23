from glob import glob
import numpy as np
from pprint import pprint
from pydicom import dcmread
from helper import show_time
import time
from logger import logging
# http://localhost:60848/?code=ad7310ee55d5afaca3b6&state=d4e466ff76d443159a51cafd6e5177d3
class dcm_orm():

    def __init__(self,path = None, ext = "", recursive = True) -> None:
        self.RECURSIVE = recursive
        self.PATH = path
        self.EXT = ext
        self.FILES = self._get_files()
        # pprint(self.FILES)
        # self.print_files()
        logging.info("********")
        logging.info(f"\n\n{len(self.FILES)} unique paths detected")
        self.result= np.array([1] * len(self.FILES))
        self.__times__ = []
        self.__cum_time__ = 0
        # self.map = self.FILES

    def __repr__(self):
        # print("\n\n{count} files found".format(count = len(self.FILES)))
        self.print_files()

    def __str__(self):
        return f"\n\n{len(self.FILES)} unique paths detected"
        # self.print_files()

    def _get_files(self):
        ''' 
        this function fetches the .EXT files from the path
        '''
        return list(glob(self.PATH + "/**/*" + self.EXT,recursive=self.RECURSIVE))


    def filter(self,**args):
        logging.info("\n\n--- start ---")
        # logging.info(f"alredy result \n{self.result}")
        logging.info(args)
        res = []
        '''
        Files -> N 
        Filters -> F
        complexity -> N*F 
        '''
        output = True

        # profile filter
        sttime = time.time()
        for fil in self.FILES:
            for key,val in args.items(): 
                # print(arg)
                output = True
                if key == "endswith":
                    output =  output & self._filter_endswith(fil,key,val)
                
                if key == "isfile":
                    output = output & self._filter_isfile(fil,key,val)
            res.append(output)
        entime = time.time()
        self.__times__.append(show_time(sttime,entime,args))
        # self.__cum_time__ = np.sum(self.__times__)
        

        res = np.array(res)
        # logging.info(res)
        self.result = (res & self.result)
        # self.logging.info_output()
        # logging.info(self.result)
        logging.info("\n\n--- end ---")
        return self

    '''
    define custom filters here
    '''

    def _filter_endswith(self,obj,key,val):
        if obj.endswith(val):
            # logging.info(obj)
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
                logging.info(f"{fil[:int(LEN/2)]}...{fil[-int(LEN/2):]} -> {res}")
            else:
                logging.info(f"{fil} -> {res}")

    def print_files(self):
        LEN = 100   
        for en,fil in enumerate(self.FILES):
            if len(fil)>LEN:
                logging.info(f"{en}->{fil[:int(LEN/2)]}...{fil[-int(LEN/2):]}")
            else:
                logging.info(f"{en}->{fil}")




                




