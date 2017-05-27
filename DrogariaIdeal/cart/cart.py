from products.models import Product

class Cart():

    _productIds = []

    def getProductAtIndex(self, index):

        product = None
        if index < _productIds.count:
            id = self._productIds[index]
            product = Product.objects.get(id = id)

        return product

    def getAllProducts(self):
        products = []
        for id in self._productIds:
            products.append(Product.objects.get(id = id))

        return products

    def addProduct(self, id):
        if id not in self._productIds:
            self._productIds.append(id)

    def removeProduct(self, id):
        if id in self._productIds:
            index = self._productIds.index(id)
            self._productIds.pop(index)

    def clear(self):
        self._productIds.clear()
