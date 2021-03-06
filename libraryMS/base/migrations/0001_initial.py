# Generated by Django 3.2.9 on 2021-11-20 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('author_name', models.CharField(blank=True, max_length=45)),
                ('author_surname', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDetails',
            fields=[
                ('category_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='BookDeatils',
            fields=[
                ('book_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('ISBN', models.CharField(blank=True, max_length=45, null=True)),
                ('book_title', models.CharField(blank=True, max_length=100, null=True)),
                ('publication_year', models.IntegerField(default=0)),
                ('language', models.CharField(blank=True, max_length=45, null=True)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity_for_sale', models.IntegerField(default=0)),
                ('autor_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='base.author')),
                ('category_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='base.categorydetails')),
            ],
        ),
    ]
