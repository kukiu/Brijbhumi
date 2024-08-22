# Generated by Django 4.2 on 2024-05-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brajbhumi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('choice', models.CharField(choices=[('vrindavan', 'Vrindavan'), ('gokul', 'Gokul'), ('barsana', 'Barsana')], max_length=10)),
                ('textfield', models.TextField()),
            ],
        ),
    ]