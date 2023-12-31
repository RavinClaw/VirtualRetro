from .utils import ValidateFile, LoadFile
import os
import sys
from colorama import Fore as F



class Compiler:
    def __init__(self, filename: str):
        """
        Params:
         - filename: str (!NOTE! You don't have to include the path only the file, since all files are pulled from 'apps/')
        """
        if not ValidateFile(filename):
            print(F.RED + "[RetroCompiler] File Selected Could Not Be Validated Please Check To See If The File Exists & That It Has The Extension of (.rs)" + F.WHITE)
            sys.exit()
        
        self.contents = LoadFile(f"/apps/{filename}")
        self.variables = {}
        self.junk = {}
        self.episode = []
        self.delete = [] # Anything placed will be permantanly deleted
    
    
    def Compile(self):
        """ Runs the actual compiler program, fill be constantly improving and functions might change name in the future """
        pc = 0
        
        while (pc != -1):
            line = self.contents[pc]
            if line[0:2] == "//":
                pass
            elif line[0:3] == "var":
                opts = line[4:].split(" ")
            
            pc += 1