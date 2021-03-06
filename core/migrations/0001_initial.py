# Generated by Django 3.0.1 on 2020-03-04 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('imagem', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('imagem', models.CharField(blank=True, max_length=256, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Nacional', 'Nacional'), ('Internacional', 'Internacional')], max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Linha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('imagem', models.CharField(blank=True, max_length=256, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('imagem', models.CharField(blank=True, max_length=256, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1024, null=True)),
                ('lattes', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Premiacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('ano', models.CharField(blank=True, max_length=256, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('ano', models.CharField(blank=True, max_length=256, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1024, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Livro', 'Livro'), ('Journal Papers', 'Journal Papers'), ('Conference Papers', 'Conference Papers'), ('Keynote Speaches', 'Keynote Speaches'), ('Outro', 'Outro')], max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=256, null=True)),
                ('imagem', models.CharField(blank=True, max_length=256, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1024, null=True)),
                ('telefone', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('endereco', models.CharField(blank=True, max_length=256, null=True)),
                ('facebook', models.CharField(blank=True, max_length=256, null=True)),
                ('twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('instagram', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor_destaque', models.CharField(blank=True, max_length=256, null=True)),
                ('cor_um', models.CharField(blank=True, max_length=256, null=True)),
                ('cor_dois', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Idioma')),
                ('instituicao', models.ManyToManyField(to='core.Instituicao')),
                ('linhas', models.ManyToManyField(to='core.Linha')),
                ('pesquisadores', models.ManyToManyField(to='core.Pesquisador')),
                ('premiacoes', models.ManyToManyField(to='core.Premiacao')),
                ('projetos', models.ManyToManyField(to='core.Projeto')),
                ('publicacoes', models.ManyToManyField(to='core.Publicacao')),
                ('sobre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sobre')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tema')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('informacoes', models.ManyToManyField(to='core.Informacao')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
