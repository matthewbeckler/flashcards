# Generated by Django 2.0.5 on 2018-05-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidea', models.CharField(max_length=200)),
                ('sideb', models.CharField(max_length=200)),
                ('update_date', models.DateTimeField()),
                ('reversable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='decks',
            field=models.ManyToManyField(to='flashcardsapp.Deck'),
        ),
    ]
