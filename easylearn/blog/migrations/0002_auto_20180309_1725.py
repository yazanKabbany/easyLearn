# Generated by Django 2.0.3 on 2018-03-09 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'ordering': ['-create_date'],
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-create_date'], 'verbose_name': 'Blog post', 'verbose_name_plural': 'Blog posts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(max_length=4000),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
