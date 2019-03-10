from webscraping import download
 
D = download.Download()
 
emails = D.get_emails("http://buklijas.info/", max_depth=2, max_urls=None, max_emails=None)
 
print emails