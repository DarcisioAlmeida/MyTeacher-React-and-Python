# Generated by Django 4.1.2 on 2022-10-13 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descricao', models.TextField()),
                ('foto', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='teacher.professor')),
            ],
        ),
    ]
