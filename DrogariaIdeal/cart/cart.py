from products.models import Product

__productIds = []

def get_product_at_index(self, index):

    product = None
    if index < __productIds.count:
        id = __productIds[index]
        product = Product.objects.get(id = id)

    return product

def get_all_products(self):
    products = []
    for id in __productIds:
        products.append(Product.objects.get(id = id))

    return products

def add_product(self, id):
    if id not in __productIds:
        __productIds.append(id)

def remove_product(self, id):
    if id in __productIds:
        index = __productIds.index(id)
        self.__productIds.pop(index)

def clear(self):
    __productIds.clear()
