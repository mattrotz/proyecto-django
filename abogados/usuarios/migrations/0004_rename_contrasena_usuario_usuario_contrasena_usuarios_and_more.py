# Generated by Django 5.1.3 on 2024-11-15 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_rename_contrasena_abogado_contrasena_abogado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasena_usuario',
            new_name='contrasena_usuarios',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='correo_usuario',
            new_name='correo_usuarios',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='direccion_usuario',
            new_name='direccion_usuarios',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fecha_registro_usuario',
            new_name='fecha_registro_usuarios',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre_usuario',
            new_name='nombre_usuarios',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='telefono_usuario',
            new_name='telefono_usuarios',
        ),
    ]