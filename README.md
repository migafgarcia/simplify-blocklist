# Simplify Blocklist

A script to parse blocklists that removes duplicates and sub-domains.
May be useful for host blocking software, to simplify/compress blocklists from various sources.

## Implementation

This was implemented using a tree, as follows:

.<br>
├─ com<br>
│  ├─ ads<br>
│  └─ malware<br>
├─ net<br>
│  ├─ a8<br>
│  └─ a2dfp<br>
└─ xyz<br>
   └─ fwdbreuse<br>
