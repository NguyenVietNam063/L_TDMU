# Generated by Django 2.2 on 2022-04-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libman', '0006_auto_20220304_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='department',
            field=models.CharField(choices=[('Kinh tế', 'Kinh tế'), ('Chính trị', 'Chính trị'), ('Công nghệ', 'Công nghệ'), ('Khoa học', 'Khoa học'), ('Lịch sử', 'Lịch sử'), ('Văn học', 'Văn học'), ('Toán học', 'Toán học'), ('Y khoa', 'Y khoa'), ('Giáo dục', 'Giáo dục'), ('Xây dựng', 'Xây dựng'), ('Nghệ thuật', 'Nghệ thuật'), ('Địa lý', 'Địa lý'), ('Vật lý', 'Vật lý')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employer',
            name='timer',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=20),
        ),
    ]
