# Generated by Django 2.2.17 on 2021-04-27 20:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('duration', models.SmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
