# Generated by Django 5.0.3 on 2024-03-27 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_chatmessage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chatmessage",
            old_name="receiver",
            new_name="reciever",
        ),
    ]
