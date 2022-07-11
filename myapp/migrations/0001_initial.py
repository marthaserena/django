# Generated by Django 4.0.5 on 2022-07-08 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=200)),
                ('publish_date', models.DateField()),
                ('book_id', models.CharField(max_length=100)),
                ('book_image', models.CharField(max_length=1000)),
                ('book_collection', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('FirstName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=100)),
                ('PAYMENT_REQUIRED', models.CharField(max_length=100)),
                ('DatePaid', models.DateTimeField(auto_now_add=True)),
                ('Date_Bookreturned', models.DateTimeField(auto_now_add=True)),
                ('fine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Return_date', models.DateTimeField(auto_now_add=True)),
                ('Date_taken', models.DateTimeField(auto_now_add=True)),
                ('BorrowerId', models.CharField(max_length=100)),
                ('borrowedBook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='PostBook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.librarian'),
        ),
    ]
