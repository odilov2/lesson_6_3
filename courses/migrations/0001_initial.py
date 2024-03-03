# Generated by Django 5.0.2 on 2024-03-03 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('speciality', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Techsub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.teacher')),
            ],
        ),
    ]
