# Generated by Django 3.2.16 on 2023-02-03 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(default='zero', max_length=40),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
            options={
                'verbose_name_plural': 'replies',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('replies', models.ManyToManyField(blank=True, to='main.Reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='main.Comment'),
        ),
    ]
