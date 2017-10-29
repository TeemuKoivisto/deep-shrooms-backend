# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from lp_scraper.items import ImageItem, MushroomItem
  
class LPImagePipeline(ImagesPipeline):
  def get_media_requests(self, item, info):
    if isinstance(item, ImageItem):
      yield scrapy.Request(item['img_url'], meta={'image_name': item['name_img']})
    else:
      return item

  def file_path(self, request, response=None, info=None):
    return request.meta['image_name']

  def item_completed(self, results, item, info):
    if isinstance(item, ImageItem):
      image_paths = [x['path'] for ok, x in results if ok]
      if not image_paths:
        raise DropItem("Item contains no images")
      # Only a single downloaded item in the image_paths -list
      item['file_path'] = "{}{}".format('output/lp_mushroom_img/', image_paths[0])
      return item
    else:
      return item

class JsonWriterPipeline(object):
  def open_spider(self, spider):
    self.file_classes = open('output/lp_mushroom_classes.csv', 'w')
    self.file_imgs = open('output/lp_mushroom_imgs.csv', 'w')
    self.writer_classes = csv.DictWriter(self.file_classes, delimiter='\t', fieldnames=[
      'name_latin', 'name_fin', 'url_lp', 'edibility'])
    self.writer_imgs = csv.DictWriter(self.file_imgs, delimiter='\t', fieldnames=[
      'name_latin', 'name_fin', 'name_img', 'edibility', 'img_url', 'file_path'])
    self.writer_classes.writeheader()
    self.writer_imgs.writeheader()

  def close_spider(self, spider):
    self.file_classes.close()
    self.file_imgs.close()

  def process_item(self, item, spider):
    if isinstance(item, MushroomItem):
      print(dict(item))
      self.writer_classes.writerow(dict(item))
      return item
    if isinstance(item, ImageItem):
      print(dict(item))
      self.writer_imgs.writerow(dict(item))
      return item