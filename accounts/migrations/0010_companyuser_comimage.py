# Generated by Django 3.2.5 on 2021-08-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_studentuser_stuimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuser',
            name='comImage',
            field=models.ImageField(default='INTERNSHIP-PLACEMENT/static/images/user_profile1.png', null=True, upload_to='Images/'),
        ),
    ]
