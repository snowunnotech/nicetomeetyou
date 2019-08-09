# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .utils import item_to_model, get_or_create, update_model

class NbatestPipeline(object):
    def process_item(self, item, spider):
        # item.save()
        try:
            item_model = item_to_model(item)
        except TypeError:
            return item

        model, created = get_or_create(item_model)

        update_model(model, item_model)


        return item