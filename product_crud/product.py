from datetime import datetime
from product_inmemory_db import ProductInMemoryDb



class Product(): #inherits from dict or make it dataclass 



    def __init__(self ,title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        self.id = None
        self.category_id = category_id
        self.title = title
        self.short_description =  short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt
        self.db = ProductInMemoryDb()
        


    def create(self,id:int):
        self.id = id
        self.db.insert(self.to_dict())


        # _productdb.insert(dict({'id':self.id,'category_id':self.category_id,'tittle':self.title,'short_description':self.short_description,
        # 'description':self.description,'slug':self.slug,'permalink':self.permalink,'is_available':self.is_available,'sku':self.sku,
        # 'price':self.price,'regular_price':self.regular_price,'sale_price':self.sale_price,'manage_stock':self.manage_stock,'stock_quantity':self.stock_quantity,
        # 'is_visible':self.is_visible,'data_cretaed_modified':self.date_created_gmt,'data_modified_gmt':self.date_created_gmt}))
        
    def to_dict(self) -> dict:
        dict = {'id':self.id,'category_id':self.category_id,'tittle':self.title,'short_description':self.short_description,
        'description':self.description,'slug':self.slug,'permalink':self.permalink,'is_available':self.is_available,'sku':self.sku,
        'price':self.price,'regular_price':self.regular_price,'sale_price':self.sale_price,'manage_stock':self.manage_stock,'stock_quantity':self.stock_quantity,
        'is_visible':self.is_visible,'data_cretaed_modified':self.date_created_gmt,'data_modified_gmt':self.date_created_gmt}        
        return dict
    
    
    
    #this method shall be able read a product via id/uuid or ... from the the product datastructure (dictionary,list or maybe database)
    @classmethod
    def read(cls,id:int):
        for i in cls._product_list:
            if i['id'] == id:
                return i
                
        return "we can't find that item"
        
    
    #this method shall be able to update product and amend the data structure for related product
    def update(self):
        for key,value in self._product_list.items():
            if key in self.__dict__:
                setattr(self,key,value)


                
    #this method shall be able to remove the product
    @staticmethod    
    def delete(id:int):
        for i in Product._product_list:
            if i['id'] == id:
                return Product._product_list.remove(i)
                
        return 'id is wrong'
       

    #shall I get all products with staticmethod ? any better solution ? what about a class method ?
    # what is the diffrence ?
    # shall I seprate the datastructe from the class ? why? who? any better solution?
        
    def list_all(self):
        #return Product._product_list
        return self.db

    def __del__(self):
        pass

    

    # def __repr__(self) -> dict:
    #     self.__setitem__('id', self.id)
    #     self.__setitem__('category_id', self.category_id)
    #     self.__setitem__('title', self.title)
    #     self.__setitem__('short_description', self.short_description)
    #     self.__setitem__('description', self.description)
    #     self.__setitem__('slug', self.slug)
    #     self.__setitem__('permalink', self.permalink)
    #     self.__setitem__('is_available', self.is_available)
    #     self.__setitem__('sku', self.sku)
    #     self.__setitem__('price', self.price)
    #     self.__setitem__('regular_price', self.regular_price)
    #     self.__setitem__('sale_price', self.sale_price)
    #     self.__setitem__('manage_stock', self.manage_stock)
    #     self.__setitem__('stock_quantity', self.stock_quantity)
    #     self.__setitem__('is_visible', self.is_visible)
    #     self.__setitem__('date_created_gmt', self.date_created_gmt)
    #     self.__setitem__('date_modified_gmt', self.date_modified_gmt)
    #     return super().__repr__()


    

 
    # def __str__(self) -> str:
    #     return json.dumps({
    #     "id": self.id, 
    #     "title": self.title,
    #     "short_description": self.short_description,
    #     "description": self.description,
    #     "slug": self.slug,
    #     "permalink": self.permalink, 
    #     "is_available": self.is_available,
    #     "sku": self.sku,
    #     "Price": self.price,
    #     "regular_price": self.regular_price, 
    #     "sale_price": self.sale_price, 
    #     "manage_stock": self.manage_stock, 
    #     "stock_quantity": self.stock_quantity, 
    #     "is_visible": self.is_visible, 
    #     "date_created_gmt": self.date_created_gmt, 
    #     "date_modified_gmt": self.date_modified_gmt 
    #     },indent=4)

        
    # def __str__(self) -> str:
    #     return f'{{\
    #     "id": "{self.id}",\n\
    #     "title": "{self.title}",\n\
    #     "short_description": "{self.short_description}",\n\
    #     "description": "{self.description}",\n\
    #     "slug": "{self.slug}",\n\
    #     "permalink": "{self.permalink}", \n\
    #     "is_available": "{self.is_available}",\n\
    #     "sku": "{self.sku}",\n\
    #     "Price": "{self.price}",\n\
    #     "regular_price": "{self.regular_price}", \n\
    #     "sale_price": "{self.sale_price}", \n\
    #     "manage_stock" "{self.manage_stock}", \n\
    #     "stock_quantity": "{self.stock_quantity}", \n\
    #     "is_visible": "{self.is_visible}", \n\
    #     "date_created_gmt": "{self.date_created_gmt}", \n\
    #     "date_modified_gmt": "{self.date_modified_gmt}", \n\
    #     }}'



    # def __str__(self) -> str:
    #     return f"\n\
    #     Id: {self.id} \n\
    #     Title: {self.title} \n\
    #     Short description: {self.short_description} \n\
    #     Description: {self.description} \n\
    #     Slug: {self.slug} \n\
    #     Permanent link: {self.permalink} \n\
    #     availablity: {self.is_available} \n\
    #     Stock keeping Unit: {self.sku} \n\
    #     Price: {self.price} \n\
    #     Reqular Price: ${self.regular_price} \n\
    #     Sale Price: ${self.sale_price} \n\
    #     Manage Stock {self.manage_stock} \n\
    #     Stock Quantity: {self.stock_quantity} \n\
    #     Visible: {self.is_visible} \n\
    #     Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
    #     Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
    #     "