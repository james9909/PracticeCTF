# -*- coding: utf-8 -*-
import optparse
import sys
import codecs
from threading import Thread

##
## Note that the way the key is generated doesn't ensure uniqueness
## resulting in many collisions, this script found 19 matches in a
## simple dictionary attack
##

def crack(password):
  result = decrypt(password)
  # It is assumed that the diary contains a flag_xxxxx value
  if ('flag_' in result):
    print('[+] Found password ' + password + '\n')
    print(result)

def xor(key):
  result = ""
  with codecs.open('encrypted', 'r', "utf-8") as in_file:
    input_data = in_file.read()
  for ch in input_data:
    result += chr(ord(ch) ^ key)
  return result


def decrypt(password):
  return xor(generateKey(password))

def generateKey(password):
  key = 0
  for ch in password:
    # Generate key by multiplying by prime
    key ^= ((2 * ord(ch)**2 + 3*ord(ch) + 7) & 0xff)
  return key


def main():
    parser = optparse.OptionParser("usage %prog "+\
      "-d <dictionary>")
    parser.add_option('-d', dest='dname', type='string',\
      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if(options.dname == None):
      print(parser.usage)
      exit(0)
    else:
      dname = options.dname

    passwordFile = open(dname)

    for line in passwordFile.readlines():
      password = line.strip('\n')
      t = Thread(target=crack, args=[password])
      t.start()


if __name__ == '__main__':
    main()

