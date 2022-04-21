# Generated by Django 4.0.2 on 2022-02-23 21:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rules', models.TextField()),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('stages', models.IntegerField()),
                ('event_start_time', models.TimeField()),
                ('event_end_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='event/speakers_images')),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StudentCouncilMembers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('P', 'President'), ('R', 'Vice President'), ('S', 'Secretary'), ('T', 'Treasurer'), ('JS', 'Joint Secretary'), ('JT', 'Joint Treasurer')], max_length=50)),
            ],
            options={
                'verbose_name': 'Student Council',
                'verbose_name_plural': 'Student Council Members',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TechFest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tech Fest',
                'verbose_name_plural': 'Tech Fest',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('video', models.ImageField(null=True, upload_to='event/videos')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_videos', to='myapp.events')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='TeacherCoordinators',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='event/teacher_coordinator_images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_teacher_coordinators', to='myapp.events')),
            ],
            options={
                'verbose_name': 'Teacher Coordinator',
                'verbose_name_plural': 'Teacher Coordinators',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StudentCoordinators',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='event/student_coordinators_images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_student_coordinators', to='myapp.events')),
            ],
            options={
                'verbose_name': 'Student Coordinator',
                'verbose_name_plural': 'Student Coordinators',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='event/images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_images', to='myapp.events')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
