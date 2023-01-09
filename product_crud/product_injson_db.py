import json 

class ProductInJsonDb:
    

    _product_listdb_json = []

    

    def insert(self,data:dict) -> None:
        self._product_listdb_json.append(data)
        with open('product_data.json','w') as json_file:
            json.dump(self._product_listdb_json,json_file)


    def update(self,id_item:int,_data:dict) -> None:
        with open('product_data.json','r') as json_file:
            data = json.load(json_file)
            for item in data:
                if item['id'] == id_item:
                    item.update(_data)
        with open("data_file.json", "w") as json_file:
            json.dump(data, json_file)
        json_file.close()
        
    

    def delete(self,id:int) -> None:
       with open('product_data.json', 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                    if item["id"] == id:
                        self._product_listdb.remove(item)
                        return self._product_listdb


    def read(self,id:int) -> None:
        with open('product_data.json', 'r') as json_file:
            data = json.load(json_file)
            for i in data:
                if i['id'] == id:
                    return i
                    
            return "we can't find that item"
                
    


    def findbyid(self,id:int) -> None:
        with open('product_data.json', 'r') as json_file:
            data = json.load(json_file)
            for i in data:
                    if i['id'] == id:
                        return f"this {id} is available"
                    else:
                        return "this id doesn't exist"

        

    def list(self) -> None:
         with open('product_data.json', 'r') as json_file:
            data = json.load(json_file)
            return data
