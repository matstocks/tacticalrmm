# Generated by Django 3.0.7 on 2020-07-02 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("agents", "0007_remove_agent_policies_pending"),
    ]

    operations = [
        migrations.RenameField(
            model_name="agent", old_name="is_updating", new_name="update_pending",
        ),
    ]
