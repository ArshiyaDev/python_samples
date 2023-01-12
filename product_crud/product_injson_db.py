import json 

class ProductInJsonDb:
    
    def __init__(self,file_json:str):
        self.file_json = file_json

    

    def to_list(self,data:dict) -> list:
        product_list = []
        product_list.append(data)
        return product_list

        
    def insert(self,data:dict) -> None:
        _product_listdb_json = self.to_list(data)
        with open(self.file_json,'w') as json_file:
            json.dump(_product_listdb_json,json_file)


    def update(self,id_item:int,_data:dict) -> None:
        with open(self.file_json,'r') as json_file:
            data = json.load(json_file)
            for item in data:
                if item['id'] == id_item:
                    item.update(_data)
        with open(self.file_json, "w") as json_file:
            json.dump(data, json_file)
        json_file.close()
        
    


    def delete(self,id:int) -> None:
       with open(self.file_json, 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                    if item["id"] == id:
                        data.remove(item)
       with open(self.file_json, 'r') as json_file:
            json.dump(data,json_file)

    def read(self,id:int) -> None:
        with open(self.file_json, 'r') as json_file:
            data = json.load(json_file)
            for i in data:
                if i['id'] == id:
                    return i
                    
                
    
    def findbyid(self,id:int) -> None:
        with open(self.file_json, 'r') as json_file:
            data = json.load(json_file)
            for i in data:
                    if i['id'] == id:
                      return 0
        

    def list(self) -> None:
         with open(self.file_json, 'r') as json_file:
            data = json.load(json_file)
            return data
