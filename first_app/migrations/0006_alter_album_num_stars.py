# Generated by Django 4.2.1 on 2023-06-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_alter_album_num_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(3, 'Not Bad'), (4, 'Good'), (1, 'Worst'), (2, 'Bad'), (5, 'Excellent')]),
        ),
    ]
