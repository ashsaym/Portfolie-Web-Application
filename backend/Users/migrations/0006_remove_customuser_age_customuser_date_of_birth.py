# Generated by Django 5.1.4 on 2024-12-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_customuser_age_customuser_facebook_customuser_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
    ]
