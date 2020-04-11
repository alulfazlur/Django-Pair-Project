# Generated by Django 3.0.5 on 2020-04-10 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 10, 10, 31, 26, 971231, tzinfo=utc))),
                ('Bio', models.TextField(blank=True, null=True)),
                ('avatar', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateField(blank=True, default=datetime.datetime(2020, 4, 10, 10, 31, 27, 2560, tzinfo=utc))),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='DesignLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=1)),
                ('username_comment', models.CharField(max_length=50)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.UserDesign')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='DesignComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('username_post', models.CharField(max_length=50)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.UserDesign')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=1)),
                ('username_like', models.CharField(max_length=50)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.DesignComment')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.UserDesign')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dribbble_app.User')),
            ],
        ),
    ]