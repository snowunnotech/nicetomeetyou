# -*- coding: utf-8 -*-
# Don't forget to add your pipeline to the ITEM_PIPELINES setting


class NbaNewsPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
