# Generated by Django 4.1.3 on 2022-12-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_nombre', models.CharField(max_length=40)),
                ('cat_id', models.IntegerField()),
                ('cat_descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usu_nom', models.CharField(max_length=40)),
                ('usu_ape', models.CharField(max_length=40)),
                ('usu_mail', models.CharField(max_length=50)),
            ],
        ),
    ]
