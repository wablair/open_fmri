# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0024_dataset_curated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationpubmedlink',
            name='dataset',
            field=models.ForeignKey(related_name='pubmed_link', to='dataset.Dataset'),
        ),
    ]
