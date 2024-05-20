from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=80, verbose_name='عنوان')
    slug = models.SlugField(max_length=80, unique=True, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    def __str__(self) -> str:
        return self.title


class LabelModel(models.Model):
    title = models.CharField(max_length=80, verbose_name='عنوان')
    slug = models.SlugField(max_length=80, unique=True, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'
    
    def __str__(self) -> str:
        return self.title


class BagManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class BagModel(models.Model):
    STATUS_CHOICES = (
        ('p', 'انتشار'),
        ('d', 'پیش نویس'),
    )
    title = models.CharField(max_length=80, verbose_name='عنوان')
    slug = models.SlugField(max_length=80, db_index=True, unique=True, verbose_name='عنوان در url')
    text = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    category = models.ManyToManyField(CategoryModel, related_name='bags', verbose_name='دسته بندی')
    label = models.ManyToManyField(LabelModel, related_name='bags', verbose_name='برچسب')
    status = models.CharField(
        max_length=1, 
        choices=STATUS_CHOICES, 
        default='d',
        verbose_name='وضعیت'
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'کیف'
        verbose_name_plural = 'کیف ها'
    
    def __str__(self) -> str:
        return self.title
    
    objects = BagManager()


class ImageOfBagModel(models.Model):
    bag = models.ForeignKey(
        BagModel, 
        related_name='images', 
        on_delete=models.CASCADE,
        verbose_name='کیف',
    )
    image = models.ImageField(upload_to='images/bag', verbose_name='عکس')

    class Meta:
        verbose_name = 'عکس محصول'
        verbose_name_plural = 'عکس های محصول'
    
    def __str__(self) -> str:
        return self.bag.title
