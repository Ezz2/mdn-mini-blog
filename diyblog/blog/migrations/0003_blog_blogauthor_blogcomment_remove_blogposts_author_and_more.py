# Generated by Django 4.2.5 on 2023-09-06 16:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_comments_blog_post_comments_comment_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter your blog text here.', max_length=150)),
                ('post_date', models.DateField(default=datetime.date(2023, 9, 6))),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='Enter your bio details here.', max_length=400)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Enter comment about blog here', max_length=100, verbose_name='Comment')),
                ('post_date', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
        migrations.RemoveField(
            model_name='blogposts',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='blog_post',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comment_by',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='BlogPosts',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogauthor'),
        ),
    ]
