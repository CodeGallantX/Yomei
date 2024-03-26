# Generated by Django 5.0.3 on 2024-03-26 18:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfinityFinance', '0009_remove_bills_ecs_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('type', models.CharField(max_length=30)),
                ('trans_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal'), ('transfer', 'Transfer'), ('payment', 'Payment'), ('other', 'Other')], max_length=20)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InfinityFinance.account')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]
