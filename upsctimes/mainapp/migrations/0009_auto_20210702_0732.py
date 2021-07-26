# Generated by Django 3.2.4 on 2021-07-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210520_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepost',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='a',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='ans',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='b',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='c',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='d',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='currentaffairs',
            name='qst',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='eml',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='a',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='ans',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='b',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='c',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='d',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='generalscience',
            name='qst',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='geography',
            name='a',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='geography',
            name='ans',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='geography',
            name='b',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='geography',
            name='c',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='geography',
            name='d',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='geography',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='geography',
            name='qst',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='history',
            name='a',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='history',
            name='ans',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='history',
            name='b',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='history',
            name='c',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='history',
            name='d',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='history',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='history',
            name='qst',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='homepost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='impupdates',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='polity',
            name='a',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='polity',
            name='ans',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='polity',
            name='b',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='polity',
            name='c',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='polity',
            name='d',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='polity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='polity',
            name='qst',
            field=models.TextField(max_length=600),
        ),
    ]