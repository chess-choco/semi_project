# Generated by Django 4.1.6 on 2023-03-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpeningAnalysis', '0013_moveanalysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='moveanalysis',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
