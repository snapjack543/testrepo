# Generated by Django 2.0.2 on 2018-02-24 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingAuditTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='status time')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_people', models.IntegerField(verbose_name='Number of people for booking')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='booking request time')),
            ],
        ),
        migrations.CreateModel(
            name='BookingStatuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='booking status', max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Resource',
            new_name='Resources',
        ),
        migrations.AddField(
            model_name='bookings',
            name='room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Resources'),
        ),
        migrations.AddField(
            model_name='bookingaudittrail',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Bookings'),
        ),
        migrations.AddField(
            model_name='bookingaudittrail',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.BookingStatuses'),
        ),
    ]
