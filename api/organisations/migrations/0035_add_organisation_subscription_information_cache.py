# Generated by Django 3.2.16 on 2022-11-07 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0034_alter_subscription_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationSubscriptionInformationCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('api_calls_24h', models.IntegerField(default=0)),
                ('api_calls_7d', models.IntegerField(default=0)),
                ('api_calls_30d', models.IntegerField(default=0)),
                ('allowed_seats', models.IntegerField(default=1)),
                ('allowed_30d_api_calls', models.IntegerField(default=50000)),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_information_cache', to='organisations.organisation')),
            ],
        ),
    ]