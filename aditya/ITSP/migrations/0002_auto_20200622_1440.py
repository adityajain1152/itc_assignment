# Generated by Django 3.0.5 on 2020-06-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_id', models.CharField(max_length=30)),
                ('team_mem1', models.CharField(max_length=100)),
                ('team_mem2', models.CharField(max_length=100)),
                ('team_mem3', models.CharField(max_length=100)),
                ('team_mem4', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]