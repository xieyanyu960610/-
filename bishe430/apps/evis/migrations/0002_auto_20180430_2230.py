# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devcompevi',
            name='picUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devCompEvi/', verbose_name='装置物证外观图片路径'),
        ),
        migrations.AlterField(
            model_name='devcompevifile',
            name='docUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/devCompEviFile/', verbose_name='录入文档路径'),
        ),
        migrations.AlterField(
            model_name='devshapeevi',
            name='nomUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeEviNom/', verbose_name='归一化图像文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapeevi',
            name='originalUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeEviOriginal/', verbose_name='原始图像文件路径'),
        ),
        migrations.AlterField(
            model_name='exploevi',
            name='picUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/exploEvi/', verbose_name='炸药物证外观图片路径'),
        ),
        migrations.AlterField(
            model_name='exploevifile',
            name='docUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/exploEviFile/', verbose_name='录入文档路径'),
        ),
    ]
