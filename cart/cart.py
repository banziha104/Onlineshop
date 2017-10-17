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
        products_ids= self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal[item['price']]
            item['total_price'] = item['price'] * item['quantity']
            yield item