<<<<<<< HEAD
# Generated by Django 4.0.5 on 2022-07-06 09:23
=======
<<<<<<< HEAD
# Generated by Django 4.0.5 on 2022-07-06 09:31
>>>>>>> f76e76fc72e13e20a4000b7c60e2c1274a93ea12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=100)),
            ],
        ),
    ]
=======
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('publish_date', models.CharField(max_length=100)),
                ('book_id', models.CharField(max_length=100)),
                ('book_image', models.CharField(max_length=1000)),
                ('book_collection', models.CharField(max_length=300)),
            ],
        ),
    ]
=======
# Generated by Django 4.0.6 on 2022-07-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
    ]
>>>>>>> 2a00dea7b0e8548078cdb4b7a69e5a3d96b9e4b0
>>>>>>> f76e76fc72e13e20a4000b7c60e2c1274a93ea12
