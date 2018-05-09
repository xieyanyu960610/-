# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_auto_20180430_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devcompchsample',
            options={'verbose_name': '爆炸装置常见样本成分子元素表', 'verbose_name_plural': '爆炸装置常见样本成分子元素表'},
        ),
        migrations.AlterModelOptions(
            name='devcompsample',
            options={'verbose_name': '爆炸装置常见样本成分表', 'verbose_name_plural': '爆炸装置常见样本成分表'},
        ),
        migrations.AlterModelOptions(
            name='devcompsamplefile',
            options={'verbose_name': '爆炸装置常见样本成分文件存储表', 'verbose_name_plural': '爆炸装置常见样本成分文件存储表'},
        ),
        migrations.AlterModelOptions(
            name='devcompsamplepeak',
            options={'verbose_name': '爆炸装置常见样本成分峰值表', 'verbose_name_plural': '爆炸装置常见样本成分峰值表'},
        ),
        migrations.AlterModelOptions(
            name='devshapesample',
            options={'verbose_name': '爆炸装置常见样本形态表', 'verbose_name_plural': '爆炸装置常见样本形态表'},
        ),
        migrations.AlterModelOptions(
            name='explochsample',
            options={'verbose_name': '炸药及原材料常见样本子元素表', 'verbose_name_plural': '炸药及原材料常见样本子元素表'},
        ),
        migrations.AlterModelOptions(
            name='explosample',
            options={'verbose_name': '炸药及原材料常见样本表', 'verbose_name_plural': '炸药及原材料常见样本表'},
        ),
        migrations.AlterModelOptions(
            name='explosamplefile',
            options={'verbose_name': '炸药及原材料常见样本文件存储表', 'verbose_name_plural': '炸药及原材料常见样本文件存储表'},
        ),
        migrations.AlterModelOptions(
            name='explosamplepeak',
            options={'verbose_name': '炸药及原材料常见样本峰值表', 'verbose_name_plural': '炸药及原材料常见样本峰值表'},
        ),
        migrations.AlterField(
            model_name='devcompsample',
            name='picUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devCompSample/', verbose_name='爆炸装置样本外观图片路径'),
        ),
        migrations.AlterField(
            model_name='devcompsamplefile',
            name='docUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/devCompSampleFile/', verbose_name='录入文档路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='nomUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSampleNom/', verbose_name='归一化图像文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='originalUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSampleOriginal/', verbose_name='原始图像文件路径'),
        ),
        migrations.AlterField(
            model_name='explosample',
            name='picUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/exploSample/', verbose_name='炸药外观图片路径'),
        ),
        migrations.AlterField(
            model_name='explosamplefile',
            name='docUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/exploSampleFile/', verbose_name='录入文档路径'),
        ),
    ]
