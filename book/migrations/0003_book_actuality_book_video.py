# Generated by Django 4.2.6 on 2023-10-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0002_alter_book_cost_alter_book_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="actuality",
            field=models.CharField(
                choices=[
                    ("Actual", "Actual"),
                    ("50 on 50", "50 on 50"),
                    ("0 on 0", "0 on 0"),
                ],
                default=("Actual", "Actual"),
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="video",
            field=models.URLField(null=True),
        ),
    ]
