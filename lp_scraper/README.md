# Scrapers

>Here lies the dark apparatus for seeking forbidden knowledge from the depths of internet.  
>Use with caution.

# How to run

1) Install scrapy and its dependencies: `pip install scrapy image`
2) Inside this folder enter: `scrapy crawl lp_spider`

# How to deploy the dataset to S3

You need to have aws-cli and Imagemagick installed.

After scraping the images you want to first resize them. I am using default 256x256 size.

So simply just run: `./resize.sh output tmp` to resize all images inside `output`-folder to new folder `tmp`.

Then to send that folder as zip-file to S3 use: `./deploy.sh tmp luontoportti_2017_10_30 deepshroom` to zip the folder into a file `luontoportti_2017_10_30.zip` which is then sent to s3 `deep-shrooms`-bucket using AWS-profile `deepshroom` (you have to configure it to `~/.aws/credentials`).