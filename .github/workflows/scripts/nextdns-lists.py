from os import remove
from datetime import datetime
from json import load as parse
from urllib.request import urlretrieve as download

# download the list
download('https://raw.githubusercontent.com/nextdns/blocklists/refs/heads/main/blocklists/nextdns-recommended.json', '.temp')

# open and parse list
json = parse(open('.temp', mode = 'r'))

exclu = json['exclusions'] # excludesions from json
hostsList = [] # an empty hosts list
domainsList = [] # an empty domains list

localhosts = [
  '0.0.0.0', '127.0.0.1', '255.255.255.255',
  '::1', 'broadcasthost', 'fe80::1%lo0',
  'ff00::0', 'ff02::1', 'ff02::2', 'ff02::3',
  'ip6-allhosts', 'ip6-allnodes', 'ip6-allrouters',
  'ip6-localhost', 'ip6-localnet', 'ip6-loopback', 'ip6-mcastprefix',
  'local', 'localhost', 'localhost.localdomain'
]

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
      if ('#' in host) or (host == '') or ('(' in host): continue

      domain = host.split()[-1]
      if domain in localhosts: continue

      # for each rule in exclusions
      for ex in exclu:

        # check for wildcards
        if ex.startswith('*'):
          if domain.endswith(ex[2:]): continue
        elif domain is ex: continue

        hostsList.append(host)
        domainsList.append(domain)

# remove duplicates
hostsList = list(set(hostsList))
domainsList = list(set(domainsList))
# sort lists
hostsList.sort()
domainsList.sort()

# Starting lines to specify various information about Blocklist
now = datetime.now(datetime.UTC)
info = '''\
# --------------------------------------------------------------------------------------------------------
# Title: NextDNS Ads & Trackers Blocklist Mirror by touhidurrr
# Description: Parsed Mirror for
#              https://github.com/nextdns/metadata/blob/master/privacy/blocklists/nextdns-recommended.json
# Format: {}
# Version: %s
# Entries: {:,}
# Updated: %s
# RAW: https://touhidur.xyz/filterlists/nextdns-{}.txt
# --------------------------------------------------------------------------------------------------------
''' % ( now.strftime('%Y%m%d'), now.strftime('%a, %d %b %y %H:%M:%S') )

localhostSkips = '''
# ------ skip localhosts ------
127.0.0.1 localhost
127.0.0.1 localhost.localdomain
127.0.0.1 local
255.255.255.255 broadcasthost
::1 localhost
::1 ip6-localhost
::1 ip6-loopback
fe80::1%lo0 localhost
ff00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
0.0.0.0 0.0.0.0
# ------ localhosts end -------

'''

# finally write list entries
with open('filterlists/nextdns-hosts.txt', mode = 'w', encoding = 'utf-8') as f:

  f.write(info.format('hosts', len(domainsList), 'hosts'))
  f.write(localhostSkips)
  f.write('\n'.join(hostsList))
  f.write('\n')

with open('filterlists/nextdns-domains.txt', mode = 'w', encoding = 'utf-8') as f:

  f.write(info.format('domain list', len(domainsList), 'domains'))
  f.write('\n'.join(domainsList))
  f.write('\n')

# remove resulting temporary files
remove('.temp')
