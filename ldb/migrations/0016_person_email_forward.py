# Generated by Django 2.2.12 on 2020-05-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ldb", "0015_auto_20200514_2343"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="email_forward",
            field=models.BooleanField(
                default=False, verbose_name="forward CH e-mail to Dienst2 e-mail"
            ),
        ),
    ]
