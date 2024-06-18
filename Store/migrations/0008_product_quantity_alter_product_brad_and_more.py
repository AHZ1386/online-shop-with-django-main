# Generated by Django 4.2.6 on 2024-06-13 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_order_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(help_text='تعداد در انبار', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Brad',
            field=models.ForeignKey(help_text='برند', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='Store.brad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(help_text='دسته بندی', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='Store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='توضیحات', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(help_text='تصویر 1', null=True, upload_to='Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(help_text='تصویر 2', null=True, upload_to='Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(help_text='تصویر 3', null=True, upload_to='Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(help_text='قیمت', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='اسلاگ', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(help_text='نام', max_length=100, null=True),
        ),
    ]