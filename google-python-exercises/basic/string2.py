#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  #print s, len(s)
  if len(s) >= 3:
    #print "length >= 3"
    #print s[-3:]
    if s[-3:] == 'ing':
      #print "ending in ing"
      s = s+"ly"
      #print s
      return s
    else:
      #print "not ending in ing"
      s = s+"ing"
      #print s
      return s
  else:
    return s
 
    # +++your code here+++
  return


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  #print s.find("not")
  #print s.find("bad")
  if s.find("not") < s.find("bad"):
    #print s[s.find("not"):s.find("bad")+3]
    return s.replace(s[s.find("not"):s.find("bad")+3],"good")
    #s.replace(s[s.find("not"):s.find("bad")+3],"good")
    #print s
  else:
    return s
  # +++your code here+++
  #return


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  print len(a), len(b)
  if len(a)%2 == 0 and len(b)%2 == 0:
    afhalf = a[:len(a)/2]
    bfhalf = b[:len(b)/2]
    ashalf = a[len(a)/2:]
    bshalf = b[len(b)/2:]
    s = afhalf+bfhalf+ashalf+bshalf
    print s
    return s
#    return s
  elif len(a)%2 <> 0 and len(b)%2 <> 0:
    afhalf = a[:(len(a)/2)+1]
    ashalf = a[(len(a)/2)+1:]
    bfhalf = b[:(len(b)/2)+1]
    bshalf = b[(len(b)/2)+1:]
    s = afhalf+bfhalf+ashalf+bshalf
    print s
    return s
  else: 
    if len(a)%2 <> 0:
      afhalf = a[:(len(a)/2)+1]
      ashalf = a[(len(a)/2)+1:]
      bfhalf = b[:len(b)/2]
      bshalf = b[len(b)/2:]
      s = afhalf+bfhalf+ashalf+bshalf
      print s
      return s
    elif len(b)%2 <> 0:
      bfhalf = b[:(len(b)/2)+1]
      bshalf = b[(len(b)/2)+1:]
      afhalf = a[:len(a)/2]
      ashalf = a[len(a)/2:]
      s = afhalf+bfhalf+ashalf+bshalf
      print s
      return s
#  s = afhalf+bfhalf+ashalf+bshalf
#  print s
#  return s       
    #print "failed"
  # +++your code here+++



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
