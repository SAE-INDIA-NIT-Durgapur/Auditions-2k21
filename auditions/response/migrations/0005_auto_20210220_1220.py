# Generated by Django 3.1.6 on 2021-02-20 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('response', '0004_auto_20210219_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='response',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_round',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
