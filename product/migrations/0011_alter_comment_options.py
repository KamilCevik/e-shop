# Generated by Django 4.2.1 on 2023-06-05 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_alter_comment_comment_alter_comment_rate_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-create_at"]},
        ),
    ]
