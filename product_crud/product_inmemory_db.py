from product import StorageData

class ProductInMemoryDb(StorageData):
    
    _product_listdb = []


    def __init__(self):
        pass


    @staticmethod
    def loaddata(data:list):
        ProductInMemoryDb._product_listdb.extend(data)

    

    def insert(self,data:dict):
        self._product_listdb.append(data)


    def update(self,id_item:int,data:dict) -> dict:
        for item in self._product_listdb:
            if item['id'] == id_item:
                item.update(data)
                break
        
    

    def delete(self,id:int) -> dict:
       for item in self._product_listdb:
            if item["id"] == id:
                self._product_listdb.remove(item)
                return self._product_listdb


    def read(self,id:int) -> dict:
        for i in self._product_listdb:
            if i['id'] == id:
                return i
                
                
    


    def findbyid(self,id:int) -> int:
          for i in self._product_listdb:
                if i['id'] == id:
                  return 0

        

    def list(self) -> list:
        return self._product_listdb
