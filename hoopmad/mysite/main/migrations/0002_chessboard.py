# Generated by Django 4.1.7 on 2023-03-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChessBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('board_state', models.CharField(max_length=100)),
            ],
        ),
    ]