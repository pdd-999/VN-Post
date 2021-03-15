# Generated by Django 3.1.3 on 2021-03-15 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_deliverer',
            fields=[
                ('deliverer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('telephone', models.CharField(max_length=300)),
                ('cre_date', models.DateTimeField(auto_now=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Contract_Deliverer',
                'ordering': ['cre_date'],
            },
        ),
        migrations.CreateModel(
            name='Contract_desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=300)),
                ('client_name', models.CharField(max_length=300)),
                ('customer_id', models.CharField(blank=True, max_length=300)),
                ('plate_number', models.CharField(blank=True, max_length=300)),
                ('other_doc', models.CharField(blank=True, max_length=10)),
                ('mrc', models.BooleanField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'db_table': 'Contract_Description',
            },
        ),
        migrations.CreateModel(
            name='Motorbike_regis_cert',
            fields=[
                ('cert_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('province_public_security', models.CharField(max_length=300)),
                ('district_public_security', models.CharField(max_length=300)),
                ('number', models.CharField(max_length=8)),
                ('owner', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=300)),
                ('model_code', models.CharField(max_length=300)),
                ('engine', models.CharField(max_length=300)),
                ('chassis', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=20)),
                ('activation_scope', models.CharField(blank=True, max_length=300)),
                ('plate', models.CharField(max_length=50)),
                ('date_of_expiry', models.DateField()),
                ('cre_date', models.DateTimeField(auto_now=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Motorbike_Registration_Certificate',
                'ordering': ['cre_date'],
            },
        ),
        migrations.AddIndex(
            model_name='motorbike_regis_cert',
            index=models.Index(fields=['cert_id'], name='Motorbike_R_cert_id_a24763_idx'),
        ),
        migrations.AddIndex(
            model_name='motorbike_regis_cert',
            index=models.Index(fields=['owner'], name='Motorbike_R_owner_44a0f2_idx'),
        ),
        migrations.AddField(
            model_name='contract_desc',
            name='deliverer_id',
            field=models.ForeignKey(db_column='deliverer_id', on_delete=django.db.models.deletion.CASCADE, to='backend.contract_deliverer'),
        ),
        migrations.AddIndex(
            model_name='contract_deliverer',
            index=models.Index(fields=['deliverer_id'], name='Contract_De_deliver_d17c94_idx'),
        ),
        migrations.AddIndex(
            model_name='contract_deliverer',
            index=models.Index(fields=['full_name'], name='Contract_De_full_na_93cc3b_idx'),
        ),
    ]
