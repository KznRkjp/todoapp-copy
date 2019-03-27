# Generated by Django 2.1.5 on 2019-03-27 20:28

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.RuTaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
