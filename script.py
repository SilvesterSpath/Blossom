# -*- coding utf: 8 -*-

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
    
  def hash(self, key):
    key_code = key.encode()
    hash_code = sum(key_code)
    return hash_code
  
  def compressor(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[index]
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
        return
    list_at_array.insert(payload)        
  
  def retrieve(self, key):
    index = self.compressor(self.hash(key))
    list_at_index = self.array[index]
    for i in list_at_index:
      if key == i[0]:
        return i[1]
    return None
      
    #if payload == None or payload[0] != key:
     # return None
    #if payload[0] == key:
     # return payload[1]
      
blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
  blossom.assign(i[0], i[1])
  
print(blossom.retrieve("daisy"))  
    
   


raw_input("> ")

	