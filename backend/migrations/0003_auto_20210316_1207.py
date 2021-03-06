# Generated by Django 3.1.3 on 2021-03-16 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210316_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractdesc',
            options={'ordering': ['cre_date']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['cre_date']},
        ),
        migrations.RemoveIndex(
            model_name='contractdeliverer',
            name='ContractDel_id_38ebde_idx',
        ),
        migrations.RemoveIndex(
            model_name='contractdeliverer',
            name='ContractDel_full_na_ff3495_idx',
        ),
        migrations.RemoveIndex(
            model_name='motorbikeregiscert',
            name='Motorbike_R_id_8c137e_idx',
        ),
        migrations.RemoveIndex(
            model_name='motorbikeregiscert',
            name='Motorbike_R_owner_44a0f2_idx',
        ),
        migrations.AddField(
            model_name='customer',
            name='cre_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='upd_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='contractdeliverer',
            table=None,
        ),
        migrations.AlterModelTable(
            name='contractdesc',
            table=None,
        ),
        migrations.AlterModelTable(
            name='motorbikeregiscert',
            table=None,
        ),
    ]
