#!/bin/bash

START='{"files":['
END='"https://touhidur.xyz/robots.txt"]}'
URLS=''

for i in $(git diff --name-only HEAD~1)
do
  URLS+="\"https://touhidur.xyz/$i\","
done

curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
  -H "Authorization: Bearer $CF_TOKEN" \
  -H "Content-Type: application/json" \
  --data "$START$URLS$END"
