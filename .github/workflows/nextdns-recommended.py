from os import remove
from datetime import datetime
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
  with open('.temp', mode = 'r', encoding = 'utf-8') as f:
    # append lines in the list
    for host in f.readlines():

      # strip host
      host = host.strip()

      # skip comments or empty lines
      if ('#' in host) or (host is '') or ('(' in host): continue

      # for each rule in exclusions
      for ex in exclu:

        host = host.split()[-1]

        # check for wildcards
        if ex.startswith('*'):
          if host.endswith(ex[2:]): continue
        else:
          if host is ex: continue

        List.append(host)

# remove duplicates
List = list(set(List))
# sort lists
List.sort()

# remove 0.0.0.0 if it is there
try:
  List.remove('0.0.0.0')
except ValueError:
  pass

# Starting lines to specify various information about Blocklist
now = datetime.utcnow()
info =
'''# Title: NextDNS Ads & Trackers Blocklist Mirror by touhidurrr
# Description: Mirror for https://github.com/nextdns/metadata/blob/master/privacy/blocklists/nextdns-recommended.json
# Version: %s
# Entries: %i
# Updated: %s
''' % ( now.strftime('%Y%m%d'), len(List), now.strftime('%a, %d %b %y %H:%M:%S') )

# finally write list entries
with open('filterlists/nextdns-recommended.txt', mode = 'w', encoding = 'utf-8') as f:

  f.write(info)
  f.write('\n'.join(List))

# remove resulting temporary files
remove('.temp')
