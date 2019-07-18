# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NbaNewsScrapyPipeline(object):
    #def open_spider(self, spider):
    #    self.conn = sqlite3.connect("NBAnews.sqlite")
    #    self.cur = self.conn.cursor()
    #    self.cur.execute("CREATE TABLE IF NOT EXISTS NBAnews(title varchar(100), content text, image varchar(100), time varchar(50));")
    
    #def close_spider(self, spider):
    #    self.conn.commit()
    #    self.conn.close()
    
    #def process_item(self, item, spider):
    #    col = ",".join(item.keys())
    #    print(col)
    #    placeholders = ",".join(len(item) * "?")
    #    print(placeholders)
    #    sql = "INSERT INTO NBAnews({}) VALUES({})"
    #    self.cur.execute(sql.format(col, placeholders), tuple(item.values()))
    #    return item
    def process_item(self, item, spider):
        item.save()
        return item
