# Generated by Django 4.2.5 on 2023-09-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trufa', '0005_categoria_categoriaserializer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaViewSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
