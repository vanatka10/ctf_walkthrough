import httpx, ssl

ssl_ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)  # prefer TLS 1.2
ssl_ctx.set_alpn_protocols(["h2", "http/1.1"])
# see "openssl ciphers" command for cipher names
CIPHERS = "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-ECDSA-AES256-GCM-SHA384"
ssl_ctx.set_ciphers(CIPHERS)

default = httpx.get("https://tools.scrapfly.io/api/fp/ja3?extended=1").json()
fixed = httpx.get("https://tools.scrapfly.io/api/fp/ja3?extended=1", verify=ssl_ctx).json()
print('Default:')
print(default['tls']['ciphers'])
print(default['ja3'])
print('Patched:')
print(fixed['tls']['ciphers'])
print(fixed['ja3'])