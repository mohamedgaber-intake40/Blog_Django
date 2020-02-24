<<<<<<< HEAD
# Generated by Django 3.0.3 on 2020-02-24 12:21
||||||| merged common ancestors
# Generated by Django 3.0.3 on 2020-02-22 21:51
=======
# Generated by Django 3.0.3 on 2020-02-24 06:40
>>>>>>> 3a21a0374be24cea13dee268d1d79be00e733dda

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Forbidden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(max_length=500, upload_to='Posts/')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='posts', to='Admin.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.IntegerField(choices=[(0, 'Super_Admin'), (1, 'Admin'), (2, 'User')], default=2)),
                ('image', models.ImageField(default=None, max_length=500, upload_to='Users/')),
||||||| merged common ancestors
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.IntegerField(choices=[(0, 'Super_Admin'), (1, 'Admin'), (2, 'User')], default=2)),
=======
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('role', models.IntegerField(choices=[(0, 'Super_Admin'), (1, 'Admin'), (2, 'User')], default=2, verbose_name='role')),
                ('is_active', models.BooleanField(default=True, verbose_name='active status')),
                ('avatar', models.ImageField(max_length=500, null=True, upload_to='Images/')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff status')),
>>>>>>> 3a21a0374be24cea13dee268d1d79be00e733dda
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User_Post',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('like', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts', to='Admin.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField(max_length=200)),
<<<<<<< HEAD
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Post')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Admin.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.User')),
||||||| merged common ancestors
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.User')),
=======
                ('post', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Admin.Post')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Admin.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
>>>>>>> 3a21a0374be24cea13dee268d1d79be00e733dda
            ],
        ),
    ]
