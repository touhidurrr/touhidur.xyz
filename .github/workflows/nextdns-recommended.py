import json.load
from os import remove
from urllib.request import urlretrieve as download

# download the list
download('https://github.com/nextdns/metadata/raw/master/privacy/blocklists/nextdns-recommended.json', '.temp')

# open and parse list
Json = json.load(open('.temp', mode = 'r'))

exclu = Json['exclusions'] # excludesions from Json
List = [] # an empty list

# in Json.sources<list>
for source in Json['sources']:
  # in Json.sources<list entry>

  # download source url
  download(source['url'], '.temp')

  # open source url
  with open('.temp', mode = 'r') as f:
    # append lines in the list
    for host in f.readlines():
      # for each rule in exclusions

      # strip host
      host = host.strip()

      for ex in exclu:
        # check for wildcards
        if ex.startswith('*'):
          if host.endswith(ex[1:]): continue
        else:
          if host is ex: continue

        List.append(host)

List.sort()

# finally write list entries
with open('filterlists/nextdns-recommended.txt', mode = 'w', encoding = 'utf-8') as f:

  f.write('\n'.join(List))

# remove resulting temporary files
remove('.temp')
