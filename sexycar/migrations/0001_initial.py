# Generated by Django 3.2.7 on 2023-04-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('max_gb', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(max_length=127)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('date_issue', models.DateField()),
            ],
        ),
    ]
