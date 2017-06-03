from products.models import Product

__carts = {}

PRODUCT_ID_KEY = 'product_id'
PRODUCT_COUNT_KEY = 'product_count'

# key: user_id
## value: [{product_id, product_count}]

def get_cart_for_user_id(id):

    if __carts.get(id) == None:

        __carts[id] = []

    return __carts[id]


def get_product_at_index(user_id, index):
    cart = get_cart_for_user_id(user_id)

    product = None
    if index < cart.count:
        cart_item = cart[index]
        id = cart_item[PRODUCT_ID_KEY]
        product = Product.objects.get(id = id)

    return product


def get_all_products(user_id):
    cart = get_cart_for_user_id(user_id)

    products = []
    for cart_item in cart:
        products.append(Product.objects.get(id = cart_item[PRODUCT_ID_KEY]))

    return products


def add_product(user_id, id, amount):
    cart = get_cart_for_user_id(user_id)

    contains = False
    for cart_item in cart:
        if cart_item[PRODUCT_ID_KEY] == id:
            contains = True
            break

    if not contains:
        cart.append({PRODUCT_ID_KEY: id, PRODUCT_COUNT_KEY: amount})


def remove_product(user_id, id):
    cart = get_cart_for_user_id(user_id)

    for i, cart_item in enumerate(cart):
        if cart_item[PRODUCT_ID_KEY] == id:
            cart.pop(i)
            break

def get_amount(user_id, product_id):
    cart = get_cart_for_user_id(user_id)

    for i, cart_item in enumerate(cart):
        if cart_item[PRODUCT_ID_KEY] == product_id:
            amount = cart_item[PRODUCT_COUNT_KEY]

    return amount


def clear(user_id):
    __carts[user_id] = []
