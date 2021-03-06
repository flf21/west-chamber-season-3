#!/usr/bin/env python
# -*- coding: utf-8 -*-

gConfig = {
    "VERSION" : "20120424",
    "PROXY_PASSWD" : "",
    #proxy without any content rewrite, to fetch IP blocked sites
    "GOAGENT_FETCHHOST": "goagent-hrd.appspot.com",
    "GOAGENT_PASSWORD": "",
    "BLOCKED_DOMAINS_URI" : "https://raw.github.com/liruqi/west-chamber-season-3/master/west-chamber-proxy/status/timedout.txt",
    "REMOTE_DNS" : "168.95.1.1",
    "SKIP_LOCAL_RESOLV" : False,
    "REDIRECT_DOMAINS": {
        "plus.url.google.com":"url",
        "plus.url.google.com.hk":"q|url"
    },
    "LOCAL_PORT" : 1998,
    "HSTS_DOMAINS" : {
        "developers.facebook.com": 1,
        "groups.google.com": 1,
        "www.paypal.com" : 1,
        "www.elanex.biz" : 1,
        "jottit.com" : 1,
        "sunshinepress.org" : 1,
        "www.noisebridge.net" : 1,
        "neg9.org" : 1,
        "riseup.net" : 1,
        "factor.cc" : 1,
        "splendidbacon.com" : 1,
        "aladdinschools.appspot.com" : 1,
        "ottospora.nl" : 1,
        "www.paycheckrecords.com" : 1,
        "market.android.com" : 1,
        "lastpass.com" : 1,
        "www.lastpass.com" : 1,
        "keyerror.com" : 1,
        "entropia.de" : 1,
        "romab.com" : 1,
        "logentries.com" : 1,
        "stripe.com" : 1,
        "facebook.com": 1,
        "www.facebook.com": 1,
    },
    #collect domains that support HTTPS, to reduce usage of web proxy
    "HSTS_ON_EXCEPTION_DOMAINS" : {
        "s.ytimg.com": 1,
        "i1.ytimg.com": 1,
        "i2.ytimg.com": 1,
        "i3.ytimg.com": 1,
        "i4.ytimg.com": 1,
        "i1.tdimg.com": 1,
        "i2.tdimg.com": 1,
        "i3.tdimg.com": 1,
        "i4.tdimg.com": 1,
        "bits.wikimedia.org": 1,
        "www.wikipedia.org": 1,
        "www.google-analytics.com": 1,
        "apps.facebook.com": 1,
        "graph.facebook.com": 1,
        "www.youtube.com": 1,
        "m.facebook.com": 1,
    },
    "BLOCKED_DOMAINS": {
        "baidu.jp" : True,
        "search.twitter.com" : True,
        "www.baidu.jp" : True,
        "www.nicovideo.jp": True,
        "ext.nicovideo.jp": True,
        "blog.roodo.com": True,
        "www.dwnews.com": True,
        "china.dwnews.com": True,
        "www.mediafire.com": True,
        "thepiratebay.org": True,
        "thepiratebay.se": True,
        "www.bbc.co.uk": True,
        "chinadigitaltimes.net": True,
        "www.wenxuecity.com": True,
        "bbs.wenxuecity.com": True,
        "www.blogger.com": True,
        "blogger.com": True,
    },
    "BLOCKED_IPS": {
        "23.21.220.40":1, "23.21.242.194":1, #dropbox
        "50.16.240.166":1, #dropbox
        "70.86.20.29" : 1, #www.bullogger.com
        "69.93.206.250": 1, #www.xys.org,
        "174.121.98.156": 1,
        "50.22.53.157": 1,
        "50.22.53.155": 1,
        "72.32.231.8": 1,
        "72.233.2.58": 1,
        "74.125.39.102": 1,
        "174.121.66.230": 1,
        "107.20.170.126": 1,
        "204.236.224.226": 1,
        "69.163.223.11": 1, #letscorp.net
        "199.59.148.12": 1, "199.59.149.210": 1, #t.co
    },
    "CHINA_IP_LIST_FILE":"exclude-ip.json",
    "PAGE_RELOAD_HTML": """<html>
    <head>
        <script type="text/javascript" charset="utf-8">
            window.location.reload();
        </script>
    </head>
    <body>
    </body></html>""",
}

# 74.125.71.0/24
blockedIpString = """74.125.71.88
74.125.71.89
74.125.71.99
74.125.71.100
74.125.71.101
74.125.71.106
74.125.71.113
74.125.71.116
74.125.71.121
74.125.71.128
74.125.71.138
74.125.71.139
74.125.71.150
74.125.71.160
74.125.71.161
74.125.71.162
74.125.71.163
74.125.71.188
74.125.71.192"""

# 199.59.150.0/24
blockedIpString += """
199.59.150.7
199.59.150.8
199.59.150.9
199.59.150.10
199.59.150.11
199.59.150.12
199.59.150.39
199.59.150.40
199.59.150.41
199.59.150.42
199.59.150.43
199.59.150.44"""

# 199.59.149.0/24
blockedIpString += """
199.59.149.65
199.59.149.66
199.59.149.67
199.59.149.68
199.59.149.70
199.59.149.76
199.59.149.77
199.59.149.81
199.59.149.82
199.59.149.83
199.59.149.84
199.59.149.86
199.59.149.87
199.59.149.88
199.59.149.89
199.59.149.90
199.59.149.91
199.59.149.92
199.59.149.93
199.59.149.94
199.59.149.97
199.59.149.98
199.59.149.99
199.59.149.100
199.59.149.101
199.59.149.105
199.59.149.106
199.59.149.107
199.59.149.108
199.59.149.109
199.59.149.110
199.59.149.111
199.59.149.112
199.59.149.113
199.59.149.114
199.59.149.115
199.59.149.116
199.59.149.117
199.59.149.118
199.59.149.119
199.59.149.120
199.59.149.121
199.59.149.122
199.59.149.123
199.59.149.124
199.59.149.125
199.59.149.129
199.59.149.130
199.59.149.131
199.59.149.132
199.59.149.133
199.59.149.134
199.59.149.135
199.59.149.136
199.59.149.138
199.59.149.139
199.59.149.161
199.59.149.162
199.59.149.163
199.59.149.164
199.59.149.165
199.59.149.166
199.59.149.193
199.59.149.194
199.59.149.195
199.59.149.225
199.59.149.226
199.59.149.227
199.59.149.228
199.59.149.229
199.59.149.230
199.59.149.231
199.59.149.232
199.59.149.233
199.59.149.234
199.59.149.235
199.59.149.240
199.59.149.243
199.59.149.245
199.59.149.246"""

# 199.59.148.0/24
blockedIpString += """
199.59.148.6
199.59.148.7
199.59.148.8
199.59.148.9
199.59.148.10
199.59.148.11
199.59.148.12
199.59.148.15
199.59.148.20
199.59.148.21
199.59.148.22
199.59.148.23
199.59.148.60
199.59.148.69
199.59.148.82
199.59.148.84
199.59.148.85
199.59.148.87
199.59.148.88
199.59.148.89
199.59.148.92
199.59.148.96
199.59.148.97
199.59.148.102
199.59.148.104
199.59.148.105
199.59.148.106
199.59.148.124
199.59.148.125
199.59.148.126
199.59.148.129
199.59.148.130
199.59.148.131
199.59.148.132
199.59.148.133
199.59.148.135
199.59.148.139
199.59.148.140
199.59.148.181
199.59.148.193
199.59.148.194
199.59.148.195
199.59.148.201
199.59.148.204
199.59.148.206
199.59.148.207
199.59.148.208
199.59.148.209
199.59.148.213
199.59.148.215
199.59.148.216
199.59.148.217
199.59.148.218
199.59.148.219
199.59.148.222
199.59.148.224
199.59.148.226
199.59.148.230
199.59.148.231
199.59.148.232
199.59.148.233
199.59.148.234
199.59.148.235
199.59.148.236
199.59.148.237
199.59.148.238
199.59.148.239
199.59.148.240
199.59.148.241"""


for ip in blockedIpString.split("\n"):
    if len(ip) > 0:
        gConfig["BLOCKED_IPS"][ip] = 1


