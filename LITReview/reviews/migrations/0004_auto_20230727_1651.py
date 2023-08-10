# Generated by Django 3.2.9 on 2023-07-27 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0003_alter_review_options_alter_ticket_options_userfollow"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="is_closed",
        ),
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.TextField(
                blank=True, max_length=8192, verbose_name="Commentaire"
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="headline",
            field=models.CharField(max_length=128, verbose_name="Apréciation"),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="Note",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(
                blank=True, max_length=2048, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/reviews"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
    ]
