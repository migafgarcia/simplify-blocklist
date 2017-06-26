# Simplify Blocklist

A script to parse blocklists that removes duplicates and sub-domains.
May be useful for host blocking software, to simplify/compress blocklists from various sources.

## Implementation

This was implemented using a tree, as follows:

.

├─ com

│  ├─ ads

│  └─ malware

├─ net

│  ├─ a8

│  └─ a2dfp

└─ xyz

   └─ fwdbreuse
