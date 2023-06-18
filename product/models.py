from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    STATUS = (
        ('true', 'evet'),
        ('false', 'hayır',),
    )
    title = models.CharField(max_length=140)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/', default='images/resimyok.jpeg')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = AutoSlugField(populate_from='title')
    parent = TreeForeignKey('self', blank=True,  null=True,
                            related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        # level_attr = 'mptt_level's
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1

        while Category.objects.filter(slug=unique).exists():
            unique = {}-{}.format(slug, number)
            number += 1
        return unique

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Product(models.Model):
    STATUS = (
        ('true', 'evet'),
        ('false', 'hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,
                              upload_to='images/', default='images/resimyok.jpeg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    slug = AutoSlugField(populate_from='title')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1

        while Product.objects.filter(slug=unique).exists():
            unique = {}-{}.format(slug, number)
            number += 1
        return unique

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=130, blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/resimyok.jpeg')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Comment(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    comment = models.TextField(max_length=200)
    rate = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-create_at']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
