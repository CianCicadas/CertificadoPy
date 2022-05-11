import nacl
from nacl import utils
def prng(s):
    prnum = nacl.utils.random(size = s)
    return prnum

prng(128)
