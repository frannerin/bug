import sys, os, time

from .utils import *

    
    
class Pkg:
    def __new__(cls, state, **kwargs):
        print("new", os.getpid(), state, dir(state), dir())
        new = super().__new__(cls)
        new._name = new.__class__.__name__
        
        new.state = state
        new._pdb = new.state._pdbf
        new._trajectories = new.state._trajs
        
        return new
    
    
    def __getnewargs__(self):
        return self.state,
        
        
    def __init__(self, *args, **kwargs):
        for xtc in self._trajectories:
            self._calculate(xtc)
            # time.sleep(0.25)
        
        
    
    def _calculate(self, xtc):
        get_pool().apply_async(self._computation,
                               args=(xtc,))
        
    # def _computation
    
    

class Protpkg(Pkg):
    def __new__(cls, state, **kwargs):
        new = super().__new__(cls, state, **kwargs)
        new._selection = "protein"
        return new
    
    
    def _computation(self, xtc):
        print("computing", self._selection, xtc)