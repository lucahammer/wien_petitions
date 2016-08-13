# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

pages = ["PetitionDetail.aspx?PetID=7c041e560c8d4288b317dee97f68d564", "PetitionDetail.aspx?PetID=78eb8b1122dd4a1ba527a4c50f9aeb20", "PetitionDetail.aspx?PetID=63341764f47e484b982ad4b37e5b9358", "PetitionDetail.aspx?PetID=24edfbbf941147f983d84c27df368710", "PetitionDetail.aspx?PetID=cd471b56f1914751a47aeb6ad065b47b", "PetitionDetail.aspx?PetID=e25615557ebd4542a9bbaa8777ce2788", "PetitionDetail.aspx?PetID=551f48235e574fc19a8de15b03c68ed0", "PetitionDetail.aspx?PetID=086a30184d094f978aee9e22c73626dd", "PetitionDetail.aspx?PetID=84bcf12b9bb643408ff766389abce1f9", "PetitionDetail.aspx?PetID=0125ecc7baae425483568819aecc912c", "PetitionDetail.aspx?PetID=8955a1e3f6984a1ca1bec9d20524f5a5", "PetitionDetail.aspx?PetID=8e4818cf8def4b3193b567d2e55082a5", "PetitionDetail.aspx?PetID=6aa229f5838e46878fcac0f1a9a25fc1", "PetitionDetail.aspx?PetID=a382a5e00bc9402fa52eb1518d855e24", "PetitionDetail.aspx?PetID=5158e659bf954f0080dd09c635307f4a", "PetitionDetail.aspx?PetID=b2a3cd9e647b41cb95c49b5897fe467e", "PetitionDetail.aspx?PetID=434625b98580493aac1ebbb46061619a", "PetitionDetail.aspx?PetID=769ee23b2de24bc888dfd405cf0cb950", "PetitionDetail.aspx?PetID=1585a60982ae4050b29770a86ac4d8ec", "PetitionDetail.aspx?PetID=d8c0bd07f452450d8913ae93377aac8e", "PetitionDetail.aspx?PetID=a7c68eb20baa4d49a02424417d0bfd43"]
testing = ["PetitionDetail.aspx?PetID=7c041e560c8d4288b317dee97f68d564", "PetitionDetail.aspx?PetID=78eb8b1122dd4a1ba527a4c50f9aeb20"]
import scraperwiki
import lxml.html

# # Read in a page
for page in testing:
  html = scraperwiki.scrape("https://www.wien.gv.at/petition/online/"+page)

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
#root.cssselect("div[align='left']")
test = root.xpath('//tr/td[last()-1]')
print (test)
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
