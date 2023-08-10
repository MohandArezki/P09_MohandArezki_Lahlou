# Generated by Django 4.2.3 on 2023-07-19 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="is_closed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="review",
            name="ticket",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="reviews.ticket"
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img"),
        ),
    ]
