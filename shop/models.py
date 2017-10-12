from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True) # URL 값이 영문이나 알파벳으로만 사용됨. 유효성이 있지는 않음

    class Meta:                         # 모델안에서 정보를 제공해주는 클래스
        ordering = ('name',)            # 이름으로 기본 정렬
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):                  # 어떤 값을 출력할지
        return self.name

    def get_absolute_url(self):         
        return reverse('shop:product_list_by_category',args=[self.slug])

class Product(models.Model):
    pass