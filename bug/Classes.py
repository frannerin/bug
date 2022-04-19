import sys, os, io, re, time

from multiprocess import Pool

from . import utils
from . import Pkgs



class State:    
    def __init__(self, pdb='', trajs:list=[], GPCR=False):
        self.GPCR = GPCR
        
        if not isinstance(self.GPCR, bool) and isinstance(self.GPCR, int):
            self._gpcrmdid = self.GPCR
            self._pdbf = f"{self.GPCR}.pdb"
            self._trajs = (f"{self.GPCR}_1.xtc", f"{self.GPCR}_2.xtc", f"{self.GPCR}_3.xtc")
        
        else:
            self._pdbf = pdb
            self._trajs = tuple(trajs)
    
    
    
    def calculate(self, pkgs=["Protpkg"], cores=2, **kwargs):
        mypool = Pool(cores)
        utils.pool = mypool
        print(utils.pool)
        
        for pkg in pkgs:
            pkgclass = eval(f"Pkgs.{pkg}")
            setattr(self, pkg, pkgclass(self, **kwargs))
        
        mypool.close()
        mypool.join()
            
    
    


