# Generated by Django 4.2.5 on 2023-10-02 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trufa', '0008_delete_categoria_delete_categoriaserializer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trufa',
            name='ao_leite',
        ),
    ]
