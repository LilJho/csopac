# Generated by Django 3.2.15 on 2022-09-20 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=250)),
                ('firstname', models.CharField(max_length=250)),
                ('middlename', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='thesis',
            name='adviser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='thesis.adviser'),
        ),
    ]
