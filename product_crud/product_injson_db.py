import json 
from product_inmemory_db import ProductInMemoryDb
from product import StorageData

class ProductInJsonDb(StorageData):

    def __init__(self):
        self.file_name = './product_data.json'
        self.product_inmemory = ProductInMemoryDb()

    
    

    def read_from_json(self):
         with open(self.file_name,'r') as f:
            return json.load(f)

    def write_to_json(self):
            with open(self.file_name,'w') as f:
                json.dump(self.data,f)


    def insert(self,data:dict) -> None:
        self.product_inmemory.insert(data)
        self.data = self.product_inmemory.list()
        self.write_to_json()



    def update(self,id_item:int,data:dict) -> None:
        self.product_inmemory.update(id_item,data)
        self.data = self.product_inmemory.list()
        self.write_to_json()
    


    def delete(self,id:int) -> None:
        self.product_inmemory.delete(id)
        self.data = self.product_inmemory.list()
        self.write_to_json()

           
    def read(self,id:int) -> None:
        self.product_inmemory.read(id)
        self.data = self.product_inmemory.list()
        self.read_from_json()
 
    
    def findbyid(self,id:int) -> int:
        self.product_inmemory.findbyid(id)
        self.data = self.product_inmemory.list()
        self.read_from_json()
 
        
           
        

    def list(self) -> None:
        return self.product_inmemory.list()
