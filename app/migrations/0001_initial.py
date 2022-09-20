# Generated by Django 4.1.1 on 2022-09-16 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('empresa_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('rol_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuario_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rol')),
            ],
        ),
        migrations.CreateModel(
            name='registro_contable',
            fields=[
                ('contabilidad_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('empleado_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
                ('registro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.registro_contable')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]
