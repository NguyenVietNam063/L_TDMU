# Generated by Django 2.2 on 2022-03-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libman', '0005_auto_20220126_1318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='books',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='books',
            name='book_detail',
        ),
        migrations.AlterField(
            model_name='books',
            name='department',
            field=models.CharField(choices=[('KT', 'Kinh tế'), ('CT', 'Chính trị'), ('CN', 'Công nghệ'), ('KH', 'Khoa học'), ('LS', 'Lịch sử')], max_length=3),
        ),
        migrations.AlterField(
            model_name='employer',
            name='timer',
            field=models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]