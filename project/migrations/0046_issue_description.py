# Generated by Django 3.2.7 on 2021-10-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0045_project_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
