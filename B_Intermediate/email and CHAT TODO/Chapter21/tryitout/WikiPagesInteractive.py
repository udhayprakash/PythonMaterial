from BittyWiki import Wiki
wiki = Wiki("localwiki")
homePage = wiki.getPage()
homePage.text = "Here's the home page.\n\nIt links to PageTwo and PageThree."
homePage.save()
#The "localwiki" directory now contains your wiki's files.
import os
open(os.path.join("localwiki","HomePage")).read()
page2 = wiki.getPage("PageTwo")
page2.exists()
page2.text = "Here's page 2.\n\nIt links back to HomePage."
page2.save()
page2.exists()
wiki.getPage("Wiki")
