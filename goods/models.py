from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, unique=True)
    category = models.ForeignKey(to=Categories, verbose_name='Категория', on_delete=models.CASCADE) # Связь с моделью Categories
    # models.CASCADE - удаляет все связанные продукты, если категория удалена
    # models.SET_NULL - устанавливает значение NULL для связанных продуктов, если категория удалена
    # models.SET_DEFAULT - устанавливает значение по умолчанию для связанных продуктов, если категория удалена
    # models.RESTRICT - запрещает удаление категории, если есть связанные с ней продукты
    # models.DO_NOTHING - ничего не делает, если категория удалена
    # models.SET - устанавливает значение, которое вы укажете, если категория удалена
    # models.PROTECT - запрещает удаление категории, если есть связанные с ней продукты
    
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Скидка')
    
    image = models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение')

    class Meta:
        db_table = 'procucts'
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'
    def __str__(self):
        return self.name