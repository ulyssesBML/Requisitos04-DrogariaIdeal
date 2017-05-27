from products.models import Product

__productIds = []

def getProductAtIndex(self, index):

    product = None
    if index < __productIds.count:
        id = __productIds[index]
        product = Product.objects.get(id = id)

    return product

def getAllProducts(self):
    products = []
    for id in __productIds:
        products.append(Product.objects.get(id = id))

    return products

def addProduct(self, id):
    if id not in __productIds:
        __productIds.append(id)

def removeProduct(self, id):
    if id in __productIds:
        index = __productIds.index(id)
        self.__productIds.pop(index)

def clear(self):
    __productIds.clear()
