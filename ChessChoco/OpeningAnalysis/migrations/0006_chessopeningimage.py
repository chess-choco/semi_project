# Generated by Django 4.1.6 on 2023-03-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpeningAnalysis', '0005_chessvariation_delete_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChessOpeningImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='_media/image')),
            ],
        ),
    ]
