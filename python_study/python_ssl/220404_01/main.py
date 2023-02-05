# Study this documentation:
# https://www.pyopenssl.org/en/stable/api/ssl.html#OpenSSL.SSL.Context

from OpenSSL import SSL

# Context
# Connection

SSL

# those are constants
SSL.TLS_METHOD # 7
SSL.TLS_SERVER_METHOD # 8
SSL.TLS_CLIENT_METHOD # 9



context = SSL.Context(SSL.TLS_METHOD)

type(context)

context

























