# Generated by Django 3.2.4 on 2021-06-04 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Fornecedo',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='produtos',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.PositiveIntegerField()),
                ('ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.ordem')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordem_items', to='core.produtos')),
            ],
        ),
        migrations.AlterField(
            model_name='produtos',
            name='fornecedor',
            field=models.ForeignKey(max_length=225, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedores', to='core.fornecedor'),
        ),
    ]