# Generated by Django 4.2.6 on 2023-10-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitatie', '0002_contactmessage_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('num_of_people', models.IntegerField()),
                ('additional_name', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
