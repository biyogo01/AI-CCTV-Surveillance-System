# Generated by Django 4.2 on 2025-02-06 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('ip_address', models.GenericIPAddressField()),
                ('port', models.IntegerField(default=8080)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('last_accessed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threat_type', models.CharField(choices=[('intrusion', 'Intrusion'), ('violence', 'Violence'), ('theft', 'Theft'), ('suspicious', 'Suspicious Activity')], max_length=50)),
                ('confidence', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='alerts/images/')),
                ('video_clip', models.FileField(upload_to='alerts/videos/')),
                ('is_reviewed', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveillance.camera')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
