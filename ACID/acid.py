import os
import sys
import json



class Acid:
    def __init__(self, size: int, name: str, pins: list):
        self.size = size
        self.name = name
        self.pins = pins
        self.contents = {}
        self.current_size = 0
    
    
    def Write(self, addr: int, value: int):
        if addr in self.contents:
            
    
    
    def Read(self, addr: int):
        return self.contents[addr]