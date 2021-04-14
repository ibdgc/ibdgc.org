from pyzotero import zotero

zot = zotero.Zotero(2358267, 'group', 'QUDnhvIt7ax1hKJ7cXD85dC1')
zot.add_parameters(format="bibtex")
items = zot.top(limit=5)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:
    print('Item Type: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
