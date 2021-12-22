# Generated by Django 2.0 on 2019-03-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0007_auto_20190313_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='myuser',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='occupation',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='myuser',
            name='pick_your_course',
            field=models.CharField(choices=[('Pick a Course', 'Pick a Course'), ('MS Excel [Basic & Intermediate]', 'MS Excel [Basic & Intermediate]'), ('MS Excel [Advanced Masterclass]', 'MS Excel [Advanced Masterclass]'), ('MS PowerPoint [Advanced Masterclass]', 'MS PowerPoint [Advanced Masterclass]'), (' Essential MS Excel for HR Professionals ', ' Essential MS Excel for HR Professionals '), (' Excel Dashboard for Business Intelligence ', ' Excel Dashboard for Business Intelligence '), ('Financial Modelling', 'Financial Modelling'), ('Web Design for Beginners', 'Web Design for Beginners'), (' Programming(Python)', ' Programming(Python)'), ('Web Design for Advance Learners', 'Web Design for Advance Learners')], default='Pick a Course', max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='sex',
            field=models.CharField(default='', max_length=15),
        ),
    ]