# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-10 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_donationsmodalsettings_never_show_modal_to_uploaders'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationsEmailSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('never_send_email_to_uploaders', models.BooleanField(default=True)),
                ('days_after_donation', models.PositiveIntegerField(default=365, help_text="Send emails to user only if didn't made a donation in the last X days")),
                ('downloads_in_period', models.PositiveIntegerField(default=100, help_text='After user has download Z sounds...')),
            ],
        ),
    ]