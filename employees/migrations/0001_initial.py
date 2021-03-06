# Generated by Django 2.2.14 on 2020-11-19 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('id_card', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.Area')),
                ('managers', models.ManyToManyField(related_name='employees', to='managers.Manager')),
            ],
        ),
    ]
