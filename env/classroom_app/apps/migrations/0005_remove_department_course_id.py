# Generated by Django 5.0.1 on 2024-02-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_department_course_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='course_id',
        ),
    ]