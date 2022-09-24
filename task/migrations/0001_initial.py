# Generated by Django 4.1.1 on 2022-09-24 13:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('task_created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]