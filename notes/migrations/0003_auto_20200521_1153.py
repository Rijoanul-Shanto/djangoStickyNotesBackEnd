# Generated by Django 3.0.5 on 2020-05-21 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200521_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='notes.Topic'),
        ),
    ]
