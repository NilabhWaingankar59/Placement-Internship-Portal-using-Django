# Generated by Django 3.1.7 on 2021-07-19 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_companyuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='placementInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(default='', max_length=255)),
                ('domain', models.CharField(default='', max_length=255)),
                ('cgpa_req', models.FloatField(default=0)),
                ('backlog', models.IntegerField(default=0)),
                ('comimg', models.ImageField(upload_to='Images/')),
                ('company_email', models.EmailField(max_length=254)),
                ('company_phone', models.CharField(max_length=13)),
                ('company_website', models.URLField(default='')),
                ('regform_link', models.URLField(default='')),
                ('status', models.BooleanField(default=False)),
                ('company_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.companyuser')),
            ],
        ),
    ]
