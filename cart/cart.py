# cart.py

from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session                      #세션 요청
        cart = self.session.get(settings.CART_SESSION_ID)   #세팅에 카트를 가져옮
        if not cart:                                        #한번도 저장된 적이 없다면
            cart = self.session[settings.CART_SESSION_ID] = {}  # 초기화
        self.cart = cart                                    # 카트에 넣음

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    sum = 0

    # sum(item['quantity'] for item in self.cart.values()) sum = 0 과 같음
    # for item in self.cart.values():
    #     sum = sum + item['quantity']
    #     return sum

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal[item['price']]
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self,product,quantity=1,update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        if update_quantity:                                 # 장바구니에 없다면, 초기화 및 추가
            self.cart[product_id]['quantity'] = quantity
        else :                                              # 장바구니에 있다면, 기존에 추가
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart # 세션에 저장
        self.session.modified = True                       # 세션을 만들고나서

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}        #세션 초기하ㅗ
        self.session.modified = True