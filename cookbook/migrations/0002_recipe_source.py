# Generated by Django 2.2.7 on 2019-12-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='source',
            field=models.CharField(default='https://www.homemadeinterest.com/portuguese-rice-pudding-arroz-doce/', max_length=200),
            preserve_default=False,
        ),
    ]