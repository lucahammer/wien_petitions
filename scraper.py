# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

active = ["PetitionDetail.aspx?PetID=7c041e560c8d4288b317dee97f68d564", "PetitionDetail.aspx?PetID=78eb8b1122dd4a1ba527a4c50f9aeb20", "PetitionDetail.aspx?PetID=63341764f47e484b982ad4b37e5b9358", "PetitionDetail.aspx?PetID=24edfbbf941147f983d84c27df368710", "PetitionDetail.aspx?PetID=cd471b56f1914751a47aeb6ad065b47b", "PetitionDetail.aspx?PetID=e25615557ebd4542a9bbaa8777ce2788", "PetitionDetail.aspx?PetID=551f48235e574fc19a8de15b03c68ed0", "PetitionDetail.aspx?PetID=086a30184d094f978aee9e22c73626dd", "PetitionDetail.aspx?PetID=84bcf12b9bb643408ff766389abce1f9", "PetitionDetail.aspx?PetID=0125ecc7baae425483568819aecc912c", "PetitionDetail.aspx?PetID=8955a1e3f6984a1ca1bec9d20524f5a5", "PetitionDetail.aspx?PetID=8e4818cf8def4b3193b567d2e55082a5", "PetitionDetail.aspx?PetID=6aa229f5838e46878fcac0f1a9a25fc1", "PetitionDetail.aspx?PetID=a382a5e00bc9402fa52eb1518d855e24", "PetitionDetail.aspx?PetID=5158e659bf954f0080dd09c635307f4a", "PetitionDetail.aspx?PetID=b2a3cd9e647b41cb95c49b5897fe467e", "PetitionDetail.aspx?PetID=434625b98580493aac1ebbb46061619a", "PetitionDetail.aspx?PetID=769ee23b2de24bc888dfd405cf0cb950", "PetitionDetail.aspx?PetID=1585a60982ae4050b29770a86ac4d8ec", "PetitionDetail.aspx?PetID=d8c0bd07f452450d8913ae93377aac8e", "PetitionDetail.aspx?PetID=a7c68eb20baa4d49a02424417d0bfd43"]
ended = ["PetitionDetail.aspx?PetID=76a0d66d841c468d9a0ca01961f5498b", "PetitionDetail.aspx?PetID=590e6028e9e74281bd1e300a3342a4e2", "PetitionDetail.aspx?PetID=8e776de0574c4f5fbb790b5002f82e7c", "PetitionDetail.aspx?PetID=bc52302d0d3e4bd4898b2a562f6c0e17", "PetitionDetail.aspx?PetID=bdc7f129d39f4bd5b5f084d5fd9c8d71", "PetitionDetail.aspx?PetID=24358bd3b7024f55b1db46a987edea00", "PetitionDetail.aspx?PetID=1909129d6bbc426d969eb38b53618660", "PetitionDetail.aspx?PetID=323f0f0d3f424eafb87d234dab1451fb", "PetitionDetail.aspx?PetID=d36460e29508409f893074708395cbfc", "PetitionDetail.aspx?PetID=63efce3a32854941be6cfc47ab115e92", "PetitionDetail.aspx?PetID=8516ce2b7a7f4964bdbf7d0296ae38f9", "PetitionDetail.aspx?PetID=fbe7142c46c64036a1514ba9fc647eac", "PetitionDetail.aspx?PetID=6e789389951e41eea7f760f87ade7e7a", "PetitionDetail.aspx?PetID=363e4820bc3540c3b9b225ed108b38f6", "PetitionDetail.aspx?PetID=c835d69a64a34f51b5af1f8a2c02b561", "PetitionDetail.aspx?PetID=d4e6bcfae35042f79ed99641087c79da", "PetitionDetail.aspx?PetID=d5b3accd98834ec38f54d7b7b91ba89a", "PetitionDetail.aspx?PetID=74ebd610eaac44308c708131efbed1f2", "PetitionDetail.aspx?PetID=a9f80c562b354b17b16f42327a16b29f", "PetitionDetail.aspx?PetID=3a24431c7fef4f46b7d40e88b509606b", "PetitionDetail.aspx?PetID=013175f150db486abcfc5db9f5d3b999", "PetitionDetail.aspx?PetID=12328ec0a3594f38817e32400752ea10", "PetitionDetail.aspx?PetID=28939999edba4612a51510e092cf32c6", "PetitionDetail.aspx?PetID=90421b3aa3cf47d394be852e288814f7", "PetitionDetail.aspx?PetID=061c51935b18417eb57d6be5343b8ec9", "PetitionDetail.aspx?PetID=e6d702e9b9c940b09af5afca99a0c3f7", "PetitionDetail.aspx?PetID=23b73205719c4e99a05e59c0096ae4cc", "PetitionDetail.aspx?PetID=6765bbb5437d411498b3543f2efbc6ff", "PetitionDetail.aspx?PetID=f4084921ee4c40eeb283cf14b3124151", "PetitionDetail.aspx?PetID=a91680882c0e4b41a8dfed2d953e3ea1", "PetitionDetail.aspx?PetID=41e66732b95c42d998c7b990f57f1277", "PetitionDetail.aspx?PetID=9e3982da90d54af2aa773ff12981839d", "PetitionDetail.aspx?PetID=67492beee6a64c1586f12e816c20a36d", "PetitionDetail.aspx?PetID=82e1a5d9a0a44ab6ae10d8c8cfb92563", "PetitionDetail.aspx?PetID=eb1342610e2b4a4f80217219275f3818", "PetitionDetail.aspx?PetID=2253eddd9bf64536b27e268145481da9", "PetitionDetail.aspx?PetID=b9e7cf56089e49a0bd7e1a0d321727b1", "PetitionDetail.aspx?PetID=31b6652687744322801239394cc14b96", "PetitionDetail.aspx?PetID=f1b5108f219e4488be39b1891120ed4c", "PetitionDetail.aspx?PetID=602e4068f410429db6ebc655ba39b552", "PetitionDetail.aspx?PetID=4607ee31be4b448d80ef445a574500c5", "PetitionDetail.aspx?PetID=acb1d7aea9df46e89ddc12e5287b8480", "PetitionDetail.aspx?PetID=ade4f7013fef49a0aef22c527a7e831e", "PetitionDetail.aspx?PetID=952055c6af574389bbdf2d21dfdc5423", "PetitionDetail.aspx?PetID=f6ed4c2c49034fe98ab74edf82e4b5e5", "PetitionDetail.aspx?PetID=111eb64ab6a74c7481c78d9f9f81f3c1", "PetitionDetail.aspx?PetID=37d2bf3886154155b2ea8a419d7652f2", "PetitionDetail.aspx?PetID=5615a33162054fa6a499be1e900edf2b", "PetitionDetail.aspx?PetID=2c6f8ca76ac4446781f130ba4fc12a9f", "PetitionDetail.aspx?PetID=334189de5f6542b38796f2c4af061bcf", "PetitionDetail.aspx?PetID=a89b7dd29981456e894f01d8e552fe8e", "PetitionDetail.aspx?PetID=f0b5fcc9c5084952bcb6d434ffbeb1ca", "PetitionDetail.aspx?PetID=0d2282cccfec4219a4b9e12e1d077826", "PetitionDetail.aspx?PetID=e30c1d7693064cb7a7910cacdebf817d", "PetitionDetail.aspx?PetID=d23065792e9c455f890cee40db2b5088", "PetitionDetail.aspx?PetID=54903ede7cdd48d6a0b87f1add3a8aac", "PetitionDetail.aspx?PetID=74a161645f6141a49360f7342e3e8fff", "PetitionDetail.aspx?PetID=8d46cfca38f94de0b14bdba540d37bd8", "PetitionDetail.aspx?PetID=c19ad40d01f444c28c48f456bafe9fe9", "PetitionDetail.aspx?PetID=a3e7b88ebd2145bc9f03d395ac7e0020", "PetitionDetail.aspx?PetID=c197aff6d3a0449e972d532da26779d5", "PetitionDetail.aspx?PetID=f3f78034ba6a43bcbae5f27761bbf513", "PetitionDetail.aspx?PetID=ae5843d7899c4f40b1ddd9521bdaabb7", "PetitionDetail.aspx?PetID=70437c187b8142b5b4473985e2914839", "PetitionDetail.aspx?PetID=a4956d106ce14a6dbde06f1d40ce0245", "PetitionDetail.aspx?PetID=416c276f490b4d1fb9072ae452d98757", "PetitionDetail.aspx?PetID=5825027f7d1e40738322f309b515d459", "PetitionDetail.aspx?PetID=10d96d67dbdb497380cc73df5d1df928", "PetitionDetail.aspx?PetID=d21ec2817e184c05b86de5425354e8a8", "PetitionDetail.aspx?PetID=2fc60fbbb0fc495e95396029152cc914", "PetitionDetail.aspx?PetID=9f20bee63c7143b2bade10d613fc69bb", "PetitionDetail.aspx?PetID=2148a774f48645febbde07d7227d8de0", "PetitionDetail.aspx?PetID=6fb528e43c23420b8f9fc45f06591e47", "PetitionDetail.aspx?PetID=492a9af72f8d462d8fa8ed45f15b0b05", "PetitionDetail.aspx?PetID=f3a327cd24e64fcea4e718d5ce61da7f", "PetitionDetail.aspx?PetID=07f79f87aaf743da92e45c704c389d59", "PetitionDetail.aspx?PetID=f8e15ed3e64c4a5a8fef4525bca4b728", "PetitionDetail.aspx?PetID=8a3d9ffade9e435da00d41f64389d006", "PetitionDetail.aspx?PetID=64e3a167d738405ea08fae7c2a886947", "PetitionDetail.aspx?PetID=5d6719ed41c6419ba25829df41367ff9", "PetitionDetail.aspx?PetID=be1449adfa094910892134cbaacc679d", "PetitionDetail.aspx?PetID=e2a59f0f83d049fe9f0fe947176519ee", "PetitionDetail.aspx?PetID=d353521014ce494288b730c8ec6acb8e", "PetitionDetail.aspx?PetID=5006de45e5844c3d8c594bb3e72f3252", "PetitionDetail.aspx?PetID=8d524a2ca3e74ddd881bc9c675793c6b", "PetitionDetail.aspx?PetID=062dae55e1904d239ee312e6645ba67c", "PetitionDetail.aspx?PetID=79da7d5dec8845548e1546c39ee89804", "PetitionDetail.aspx?PetID=fa313f852ae14ded84a126f2a89c4fc0", "PetitionDetail.aspx?PetID=41f21b0f03854b49b7c074b0e1ef987a", "PetitionDetail.aspx?PetID=ed5e5f54828241d09b5e42edb5bc3a6d", "PetitionDetail.aspx?PetID=9c5a8349ded64db98015905c3eea6bea", "PetitionDetail.aspx?PetID=d1b819f27ce3458ebefcbf0df3fe528a", "PetitionDetail.aspx?PetID=3887f3876e754271a20492c937a58f9d", "PetitionDetail.aspx?PetID=42a6f545685f4589922ce2f0819e28a9", "PetitionDetail.aspx?PetID=73ac7a339ce046ee9d138757d0dc4d9c", "PetitionDetail.aspx?PetID=da59fc1601ec45f283131f4150f268a8", "PetitionDetail.aspx?PetID=83fa68244adf44fdb7ffb892ffb5428c", "PetitionDetail.aspx?PetID=6e7d9a1f86274cc4af79ce733a675a65", "PetitionDetail.aspx?PetID=467e9b6297b5417eb1026015997db7b1", "PetitionDetail.aspx?PetID=1a711537099e45388555f6d926164c1b", "PetitionDetail.aspx?PetID=446def6e128c4f199ddfdce70c599775", "PetitionDetail.aspx?PetID=d4efda7020a14f919f122c2fa73da1cd", "PetitionDetail.aspx?PetID=64946ba22b614613ae0b1cff54b49a29"]
testing = ["PetitionDetail.aspx?PetID=7c041e560c8d4288b317dee97f68d564", "PetitionDetail.aspx?PetID=78eb8b1122dd4a1ba527a4c50f9aeb20"]

import scraperwiki
import lxml.html

# # Read in a page
for page in testing:
  html = scraperwiki.scrape("https://www.wien.gv.at/petition/online/"+page)

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
results = root.cssselect("td[width='70%']")
#test = root.xpath('//tr/td[last()-1]')
for item in results:
  prntabl = item.text.encode('ascii', 'ignore')
  print (prntabl)
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
