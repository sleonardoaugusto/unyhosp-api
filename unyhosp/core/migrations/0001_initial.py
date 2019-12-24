# Generated by Django 3.0 on 2019-12-24 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document_id', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UTI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utis', to='core.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pacient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pacient')),
                ('uti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds', to='core.UTI')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_reason', models.TextField()),
                ('hma', models.TextField()),
                ('comorbidity', models.TextField()),
                ('atb', models.TextField()),
                ('hd', models.TextField()),
                ('medicines_in_use', models.TextField()),
                ('previous_pathologies', models.TextField()),
                ('allergies', models.TextField()),
                ('cultures', models.TextField()),
                ('vasoactive_drugs', models.TextField()),
                ('sedation', models.TextField()),
                ('venous_access', models.TextField()),
                ('diet', models.TextField()),
                ('probes_and_drains', models.TextField()),
                ('ventilation', models.TextField()),
                ('complications', models.TextField()),
                ('therapeutic_plan', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Hospital')),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pacient')),
            ],
        ),
    ]
