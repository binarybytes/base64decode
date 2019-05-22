#!/usr/bin/python
import base64
import zlib
import sys
 
encoded = sys.argv[1]
 
#encoded = "RVDbagIxEP2VfQhEsZv0oVAwLAi1F6QthUXE0pdJdupGs0nMjm5F/"
decoded = base64.b64decode(encoded)
 
decompressed = zlib.decompress(decoded, -15)
print decompressed
