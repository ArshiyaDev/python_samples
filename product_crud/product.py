# arshiya
from datetime import datetime

class Product():

    _product_list = {}

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
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
       

    def create(self):
        self._product_list[self] = self.id
        return self.__repr__()

    #this method shall be able read a product via id/uuid or ... from the the product datastructure (dictionary,list or maybe database)
    def read(self):
        for i in self._product_list:
            print(i)

    #this method shall be able to update product and amend the data structure for related product
    def update(self):

        new_item = f"category_id:{self._product_list['category-id']}\n\
            tittle:{self._product_list['title']}\n\
            short_description:{self._product_list['short_description']}\n\
            description:{self._product_list['description']}\n\
            slug:{self._product_list['slug']}\n\
            permalink:{self._product_list['permalink']}\n\
            is_available:{self._product_list['is_available']}\n\
            sku:{self._product_list['sku']}\n\
            price:{self._product_list['price']}\n\
            regular_price:{self._product_list['regular_price']}\n\
            sale_price:{self._product_list['sale_price']}\n\
            manage_stock:{self._product_list['manage_stock']}\n\
            stock_quantity:{self._product_list['stock_quantity']}\n\
            is_visible:{self._product_list['is_visible']}\n\
            date_created_gmt:{self._product_list['date_created_gmt']}\n\
            date_modified_gmt:{self._product_list['date_modified_gmt']}"
        
        return self._product_list.update(new_item)
                

    #this method shall be able to remove the product
    def delete(self):
        return Product._product_list.clear()
        
       

    #shall I get all products with staticmethod ? any better solution ? what about a class method ?
    # what is the diffrence ?
    # shall I seprate the datastructe from the class ? why? who? any better solution?
    @staticmethod
    def list_all():
        return tuple(Product._product_list.keys())


    def __repr__(self) -> str:
        return f"the product with \n\
        Product Id: N/A \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availablity: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Reqular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "
       
