import scrapy

from lp_scraper.items import ImageItem, MushroomItem

class LPSpider(scrapy.Spider):
  name = 'lp_spider'
  start_urls = ['http://www.luontoportti.com/suomi/fi/sienet/akansieni']

  def parse(self, response):
    name_fin = response.css('div#teksti h3 ::text').extract_first()
    name_latin = response.css('div#teksti h4 ::text').extract_first()
    # Used for naming the pictures eg. "Chlorophyllum rhacodes" -> "chlorophyllum_rhacodes"
    latin_formatted = name_latin.lower().replace(' ', '_')

    for i, li_item in enumerate(response.css('div#teksti ul li')):
      if i == 2:
        # Third item is edibility eg. 'Syötävyys: O** – keittämisen jälkeen hyvä ruokasieni'
        edibility = li_item.css('::text').extract_first().lower().strip()
    
    for i, img_link in enumerate(response.css('div#kuvat a')):
      link_url = response.urljoin(img_link.css('::attr(href)').extract_first().strip())
      # Picks last 4 characters from the link -> 1.jpg / .jpeg / 1.png
      # And then splits them by "." and takes the last item from the list
      img_ext = link_url[-4:].split('.')[-1].lower()
      name_img = "{}{}.{}".format(latin_formatted, i, img_ext)
      img_dict = {
        'name_latin': name_latin,
        'name_fin': name_fin,
        'edibility': edibility,
        'name_img': name_img,
        'img_url': link_url,
      }
      yield ImageItem(img_dict)

    # List of links, only 1 in the first and the last page (of all mushrooms), otherwise 2
    nav_links = response.css('div.float_l a[rel=prev]')
    next_url = nav_links[len(nav_links) - 1].css('::attr(href)').extract_first()
    shroom_dict = {
      'name_latin': name_latin,
      'name_fin': name_fin,
      'edibility': edibility,
      'url_lp': response.url
    }
    yield MushroomItem(shroom_dict)
    yield response.follow(next_url)
