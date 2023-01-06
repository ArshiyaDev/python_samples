
class ProductInMemoryDb():
    
    _product_listdb = []


    def __init__(self):
        pass
    


    def insert(self,data:dict) -> dict:
        self._product_listdb.append(data)


    def update(self,data:dict):
        pass
        
    

    def delete(self,id:int):
        for i in self._product_listdb:
            if i['id'] == id:
                return self._product_listdb.clear()
                
        return "id couldn't find'"
    
    def findbyid(self,id:int):
        self.id = id 
        if id in self._product_listdb:
            return f"this {id} is available"
        else:
            return "we don't have it"
        


        
    def list(self):
        return self._product_listdb
