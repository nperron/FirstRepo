#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
usage: genCode.py <OutputFile> <NbCodeGen> <NbChar> [<Prefix>]

<OutputFile>
    Path of the output file. ex: "C:/codePromo.txt"

<NbCodeGen>
    Number of codes to generate.

<NbChar>
    Number of characters in the code generated, between 1 and 12.

[<Prefix>] Optionnal
    Prefix to use in each code generated.
"""

import sys #command line arguments
import os #system manipulation
import random

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    args = verifArg()
    gen = genCode(args[1], args[2], args[3])
    print "Results in: %s" % args[0]
    result = sorted(gen.main())
    result2 = sorted(list(set(result)))
    
    with open(args[0], 'w') as f:
        f.write("\n\t%d codes generated\n\n" % len(result2))
        for code in result2:
            f.write("%s\n" % code)
    

def usage():
    print __doc__

def verifArg():
    """
    Check if arguments are higher than 0
    """
    try:
        if len(sys.argv) in (4, 5):
            result = []
            fPath = os.path.abspath(sys.argv[1])
            #Create directory if it does not exist
            if not os.path.exists(os.path.dirname(fPath)):
                os.mkdir(os.path.dirname(fPath))
            result.append(fPath)
            for arg in sys.argv[2:4]:
                if int(arg) <= 0:
                    raise ValueError('must be higher than 0')
                result.append(int(arg))
            if len(sys.argv) == 5:
                result.append(sys.argv[4])
            else:
                result.append('')
            return result
    except Exception, err:
        print "Bad arguments\nError:", err
    usage()
    sys.exit(2)

class genCode(object):
    """
    Generate codes base 36
    """
    
    def __init__(self, nbCode, nbChar, prefix=''):
        """
        Initialize genCode
        
        @param nbCode: number of codes to generate
        @param nbChar: number of char in the code
        @param prefix: prefix to use in each code generated
        """
        self.nbCode = int(nbCode)
        self.nbChar = int(nbChar)
        self.prefix = prefix
    
    def main(self):
        """
        Main fonction which generate codes in base 36
        """
        result = []
        rawCodes = self.randomize()
        for code in rawCodes:
            code36 = self.base36_encode(code)
            #Be sure to have X characters in the code [ugly check]
            nbCharLeft = self.nbChar - len(code36)
            while nbCharLeft > 0:
                code36 = '0'+code36
                nbCharLeft = nbCharLeft - 1
            
            result.append(self.prefix+code36)
        print "Number of code to generate: %d" % self.nbCode
        print "Number of Character: %d" % self.nbChar
        if self.prefix != '':
            print "Prefix to use: %s" % self.prefix
        else:
            print "No prefix"
        
        return result
    
    def randomize(self):
        """
        Generate random numbers
        """
        try:
            return random.sample(xrange(36**self.nbChar), self.nbCode)
        except Exception, err:
                print ("Please use number of chars below 13\nReason: %s" % err)

    def base36_encode(self, num, alphabet=ALPHABET):
        """
        Encode a number in Base 36

        @param num: The number to encode
        @param alphabet: The alphabet to use for encoding
        """
        if (num <= 0):
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            rem = num % base
            num = num // base
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

        
################################################################################
if __name__ == "__main__":
    main()
