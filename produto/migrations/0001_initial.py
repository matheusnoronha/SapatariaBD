# Generated by Django 2.2.1 on 2019-06-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tamanho', models.IntegerField()),
                ('marca', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
