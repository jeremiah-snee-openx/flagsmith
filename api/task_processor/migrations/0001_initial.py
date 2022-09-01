# Generated by Django 3.2.14 on 2022-08-02 11:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_for', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('task_identifier', models.CharField(max_length=200)),
                ('serialized_args', models.TextField(blank=True, null=True)),
                ('serialized_kwargs', models.TextField(blank=True, null=True)),
                ('num_failures', models.IntegerField(default=0)),
            ],
            options={
                'index_together': {('scheduled_for', 'num_failures')},
            },
        ),
        migrations.CreateModel(
            name='TaskRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('result', models.CharField(blank=True, choices=[('SUCCESS', 'Success'), ('FAILURE', 'Failure')], db_index=True, max_length=50, null=True)),
                ('error_details', models.TextField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_runs', to='task_processor.task')),
            ],
        ),
    ]