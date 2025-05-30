# Generated by Django 4.2 on 2023-06-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PERSON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField()),
                ('reserved_user_id', models.IntegerField(null=True)),
                ('pronoun_id', models.IntegerField(null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
                ('nationality', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('passport_num_hash', models.TextField(max_length=4000)),
                ('passport_num_salt', models.TextField(max_length=4000)),
                ('passport_photo_ref', models.CharField(max_length=255)),
                ('bio', models.TextField(max_length=2000, null=True)),
                ('avatar_ref', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
