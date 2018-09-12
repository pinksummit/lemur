
# This is just Python which means you can inherit and tweak settings

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 8

# General

# These will need to be set to `True` if you are developing locally
CORS = False
debug = False

# this is the secret key used by flask session management
SECRET_KEY = 'xDdDRgrrf3WHqlmo0mA8/NUprJGO/vO2+KKDvCZKmYiiLwKqNXQr+g=='

# You should consider storing these separately from your config
LEMUR_TOKEN_SECRET = 'aFMSkF+2WE0FS2hwcFnd3TW8NLdkFOKrR20UPoNDsuP+CHdddaNaxg=='
LEMUR_ENCRYPTION_KEYS = 'rQrnNi1vcqEttL6JZeJ6Okhp7UfAU4O9AwCKPUPv7Es='

# List of domain regular expressions that non-admin users can issue
LEMUR_WHITELISTED_DOMAINS = []

# Mail Server

LEMUR_EMAIL = ''
LEMUR_SECURITY_TEAM_EMAIL = [ 'greg.hall@pinksummit.com' ]

CFSSL_URL ="http://127.0.0.1:8888"

CFSSL_ROOT = """-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIJANsLnsw5AZhOMA0GCSqGSIb3DQEBBQUAMGMxCzAJBgNV
BAYTAlVTMQswCQYDVQQIDAJWQTESMBAGA1UEBwwJQ2hhbnRpbGx5MQ0wCwYDVQQK
DARESTJFMREwDwYDVQQLDAhERVZDTE9VRDERMA8GA1UEAwwIZGV2Y2xvdWQwHhcN
MTgwOTEyMTM1MDA3WhcNMjgwOTA5MTM1MDA3WjBjMQswCQYDVQQGEwJVUzELMAkG
A1UECAwCVkExEjAQBgNVBAcMCUNoYW50aWxseTENMAsGA1UECgwEREkyRTERMA8G
A1UECwwIREVWQ0xPVUQxETAPBgNVBAMMCGRldmNsb3VkMIIBIjANBgkqhkiG9w0B
AQEFAAOCAQ8AMIIBCgKCAQEAqB5inHEddGrgIGvFhVMZvzbcGAMj/JTD4p6qegp+
oE1QL+i5kKt3QIyx3skJrGWEUXs+wFJ71f2WbaP/R4r0w3FzpIlP/4LQgYP5w6Ms
mWyXwNNkkrciIotTLopAiTPDBFz/TeZKAXyNCOF0bygDHA0cCcsQBdx72APEeqzU
J/SG4zV1DGhtbYko5oW0nK2Pf8LjY3SmGBEo0XZbqThdcXoKgGQAX9DNlCX7qwL5
Ej8W7cs34ddI9sJwzr4Clg7+FhRjouB8e7fPHPrWvHx78wUWhvTIly6jNVx3ALiZ
T9xGImYMw77d6/KaXKI7qyb8j5IYo6lheEoJX83xwT142wIDAQABo2YwZDAdBgNV
HQ4EFgQU7JLt2p7PNAe64evcJuMvLqZ2SSkwHwYDVR0jBBgwFoAU7JLt2p7PNAe6
4evcJuMvLqZ2SSkwDAYDVR0TBAUwAwEB/zAJBgNVHREEAjAAMAkGA1UdEgQCMAAw
DQYJKoZIhvcNAQEFBQADggEBAGzzSxvZIg6nDaDk+y3poCUtY5iDoTPfUI0QXVtT
j2JfAX9UkgScGzl89D1GvlJKwpMYF13xMR8ugmPpgWiDBKUp1JZLWw0ahp3hUp3V
mVfOEQAx+hnElpOeGdBOrluAeG6/dm5Dv/PFN22eBBI+YpVMmiT9ghBqa8KkMoqD
x5AiB5mWhMC17BCLneKic3sQVTaAZ0ENV6VDkfFCWZN0qEUOQHAjJyzEKYBpvNUC
4anxNjJH8aa+TkEvi2JvAI0W/PmshChIgpIFwb30VBKFMiWsZVhvjHsfon4+49Ks
uw9C93JQLUEyN/+k73FPLuDdGeHL9+KawlBZnvS9oz7+Tho=
-----END CERTIFICATE-----"""

CFSSL_INTERMEDIATE ="""-----BEGIN CERTIFICATE-----
MIIDyTCCArGgAwIBAgIJAOWHcACai9V4MA0GCSqGSIb3DQEBBQUAMHAxCzAJBgNV
BAYTAlVTMQswCQYDVQQIDAJWQTESMBAGA1UEBwwJQ2hhbnRpbGx5MQ0wCwYDVQQK
DARESTJFMREwDwYDVQQLDAhERVZDTE9VRDEeMBwGA1UEAwwVYXdzLWRldmNsb3Vk
LmRpMmUubmV0MB4XDTE4MDkxMjEzNTAwOFoXDTI4MDkwOTEzNTAwOFowcDELMAkG
A1UEBhMCVVMxCzAJBgNVBAgMAlZBMRIwEAYDVQQHDAlDaGFudGlsbHkxDTALBgNV
BAoMBERJMkUxETAPBgNVBAsMCERFVkNMT1VEMR4wHAYDVQQDDBVhd3MtZGV2Y2xv
dWQuZGkyZS5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDKorAi
AAsH6Np6H2SP+MROwNkUEHsM2rSkOBRmxja9gUk5b5RVrGRQ4cmFsFX1wKXaCol/
1RXyYuh7o14OOHgCtPX1gmCo/+APt4+ivl1XEa38gN19/fz+lmE2IzTD/IHnftyj
ERr90ykFJG+lB970YS+b0P15H5xDRvGat7opstFtzuGoItiuWIO2IGO1fSznU8f0
qQbUzwPCZev2lAb+DuxKs05I+2/lhjB1fWxoDauMEkW4QdgY09MwM0Gk1JXMcC85
pWZ6mVsNRTVUzgBaVqWIYy0V/l7BmOyQzhgT8hkU9pnigkNW0HjLFymglgyQHyiw
7virlFcwmrpC67ztAgMBAAGjZjBkMB0GA1UdDgQWBBQRhvT1THTwjhlq7JwnNd9Q
oTjGajAfBgNVHSMEGDAWgBQRhvT1THTwjhlq7JwnNd9QoTjGajAMBgNVHRMEBTAD
AQH/MAkGA1UdEQQCMAAwCQYDVR0SBAIwADANBgkqhkiG9w0BAQUFAAOCAQEACRC8
gTXQhJCXAlOrCzVNCT0z81FcXN4dLa6BQwjWNS+YC08PbvzqPSDvULOKJDSa4loB
dwNWihNotJtXuD1E3B6z39Ffly9T4xvaaLXBJ1mWcasIhzO3syMfjl0XLrx5Ccde
Z7g9Rq0vu8OquHg+Z8HcaEPcBHFpHgJXwIVx95AGQblsfCF9vliWaDHxWFHAgf7y
5JIrbp3eEuo73Ha22LME0ArDh34up1Nfp4GiiwSgQVtTOpTGr0S/yR61ydbunoFU
0pMd/KXEzrfDXUnzhPs8IV18WoOPn2pwbOI+/RPPKkRCzZ+kutmgUG8Jlm23zT81
x/fo/FPjq8W+2iPtqA==
-----END CERTIFICATE-----"""

# Certificate Defaults

LEMUR_DEFAULT_COUNTRY = 'US'
LEMUR_DEFAULT_STATE = 'CO'
LEMUR_DEFAULT_LOCATION = 'Chantilly'
LEMUR_DEFAULT_ORGANIZATION = 'DI2E'
LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = 'DEVCLOUD'
LEMUR_DEFAULT_ISSUER_PLUGIN = 'cfssl_issuer'

# Authentication Providers
ACTIVE_PROVIDERS = []

# Metrics Providers
METRIC_PROVIDERS = []

# Logging

LOG_LEVEL = "DEBUG"
LOG_FILE = "lemur.log"


# Database

# modify this if you are not using a local database
SQLALCHEMY_DATABASE_URI = 'postgresql://lemur:lemur@localhost:5432/lemur'

# AWS

#LEMUR_INSTANCE_PROFILE = 'Lemur'

# Issuers

# These will be dependent on which 3rd party that Lemur is
# configured to use.

# VERISIGN_URL = ''
# VERISIGN_PEM_PATH = ''
# VERISIGN_FIRST_NAME = ''
# VERISIGN_LAST_NAME = ''
# VERSIGN_EMAIL = ''