# Generated by Django 4.1.1 on 2022-10-24 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_bugatti_desc_bugatti_img_bugatti_img1_bugatti_img2_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="bugatti", name="img5",),
        migrations.RemoveField(model_name="bugatti", name="img6",),
    ]
