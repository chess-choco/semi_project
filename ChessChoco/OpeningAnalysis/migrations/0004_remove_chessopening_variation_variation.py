# Generated by Django 4.1.7 on 2023-03-21 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OpeningAnalysis', '0003_chessopening_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chessopening',
            name='variation',
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('moves', models.TextField()),
                ('opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='OpeningAnalysis.chessopening')),
            ],
        ),
    ]
