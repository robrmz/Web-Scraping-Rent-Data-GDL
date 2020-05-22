# Web-Scraping-Rent-Data-GDL
This program scrapes data out of "VivaAnuncios" to show rent prices in Guadalajara (Mexico) but it works for any other place within Viva Anuncio's site.

You can run the code in the cmd with (note you will need to install a few libraries to be able to execute it)
```scrapy crawl VivaAnuncios -o FileName.YourExtension(JSON,CSV,etc.)```

If you want to search for rentals in another place just go to the site and copy the address given for it and replace start_urls

Settings are not uploaded but the relevant options are shown next:

These are the middlewares used in this project, Splash is not needed for this specific project, it was used to load another spider with heavy **JavaScript**.
```
DOWNLOADER_MIDDLEWARES = {
    #'WebScrpy.middlewares.WebscrpyDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
}
```

This is the option so it can iterate over a list of proven proxies so you don't get banned. You need to pip install scrapy-proxy-pool and put the following settings:

```
PROXY_POOL_ENABLED = True
```

This is a standard User Agent for the site to recognize the bot as a regular person
```
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'
```

These are the rate limiting options built in within Scrapy's AutoThrottle extension. You can adjust as you please, specifically the DOWNLOAD_DELAY. For more info see documentation. https://docs.scrapy.org/en/latest/topics/autothrottle.html 
```
DOWNLOAD_DELAY = 1.5
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_TARGET_CONCURRENCY = 6
```
