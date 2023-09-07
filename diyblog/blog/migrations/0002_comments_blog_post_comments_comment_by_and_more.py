# Generated by Django 4.2.5 on 2023-09-05 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='blog_post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='blog.blogposts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='blog.author'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_date_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogposts',
            name='post_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]