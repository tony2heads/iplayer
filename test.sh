#!/bin/bash
#
/usr/bin/get-iplayer --type radio --listformat='<name> <episode> <channel>\\<desc>| <pid>' ".*" > /tmp/tst2
