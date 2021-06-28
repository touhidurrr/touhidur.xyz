from os import remove
from json import load as parse
from urllib.request import urlretrieve as download

# download the list
download('https://github.com/nextdns/metadata/raw/master/privacy/blocklists/nextdns-recommended.json', '.temp')

# open and parse list
json = parse(open('.temp', mode = 'r'))

exclu = json['exclusions'] # excludesions from json
List = [] # an empty list

# in json.sources<list>
for source in json['sources']:
  # in json.sources<list entry>

  # download source url
  download(source['url'], '.temp')

  # open source url
  with open('.temp', mode = 'r') as f:
    # append lines in the list
    for host in f.readlines():

      # strip host
      host = host.strip()

      # skip comments or empty lines
      if host.startswith('#') or (host is '') or host.startswith('('): continue

      # for each rule in exclusions
      for ex in exclu:
        # check for wildcards
        if ex.startswith('*'):
          if host.endswith(ex[1:]): continue
        else:
          if host is ex: continue

        host = host.split()[-1]
        List.append(host)

# remove duplicates
List = list(set(List))
# sort lists
List.sort()

# finally write list entries
with open('filterlists/nextdns-recommended.txt', mode = 'w', encoding = 'utf-8') as f:

  f.write('\n'.join(List))

# remove resulting temporary files
remove('.temp')
