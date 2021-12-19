# Generated by Django 3.2.5 on 2021-12-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Men', 'Man'), ('Women', 'Women')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'ExtraLarge'), ('XXL', 'XXtraLarge')], default='S', max_length=3)),
                ('orignal_price', models.PositiveSmallIntegerField()),
                ('current_price', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('sex', models.CharField(choices=[('Men', 'Man'), ('Women', 'Women')], max_length=5)),
                ('description', models.TextField()),
            ],
        ),
    ]
