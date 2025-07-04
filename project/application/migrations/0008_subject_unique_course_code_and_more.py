# Generated by Django 5.1.6 on 2025-05-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_subject_course_type'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subject',
            constraint=models.UniqueConstraint(fields=('course_code',), name='unique_course_code'),
        ),
        migrations.AddConstraint(
            model_name='subject',
            constraint=models.UniqueConstraint(fields=('course_name',), name='unique_course_name'),
        ),
    ]
