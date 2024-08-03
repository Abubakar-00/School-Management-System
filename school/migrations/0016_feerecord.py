# Generated by Django 3.0.5 on 2023-06-11 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20230610_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=9)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=7)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.StudentExtra')),
            ],
        ),
    ]