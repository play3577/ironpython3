#####################################################################################
#
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
# This source code is subject to terms and conditions of the Apache License, Version 2.0. A
# copy of the license can be found in the License.html file at the root of this distribution. If
# you cannot locate the  Apache License, Version 2.0, please send an email to
# ironpy@microsoft.com. By using this source code in any fashion, you are agreeing to be bound
# by the terms of the Apache License, Version 2.0.
#
# You must not remove this notice, or any other, from this software.
#
#
#####################################################################################
'''
Tests the _bytesio standard module.
'''

import sys
import unittest

from _io import BytesIO

from iptest import run_test

def bytesio_helper():
    return (BytesIO(bytearray(b'')),
            BytesIO(bytearray(b'a')),
            BytesIO(bytearray(b'ab')),
            BytesIO(bytearray(b'abc')),
            BytesIO(bytearray(b'abcd')),
            BytesIO(bytearray(b'abcde')),
            BytesIO(bytearray(b'abcdef')),
            BytesIO(bytearray(b'abcdefg')),
            BytesIO(bytearray(b'abcdefgh')),
            BytesIO(bytearray(b'abcdefghi'))
            )

class BytesIOTest(unittest.TestCase):

    def test__BytesIO___class__(self):
        print("TODO")

    def test__BytesIO___delattr__(self):
        print("TODO")

    def test__BytesIO___doc__(self):
        print("TODO")

    def test__BytesIO___format__(self):
        print("TODO")

    def test__BytesIO___getattribute__(self):
        print("TODO")

    def test__BytesIO___hash__(self):
        print("TODO")

    def test__BytesIO___init__(self):
        print("TODO")

    def test__BytesIO___iter__(self):
        print("TODO")

    def test__BytesIO___new__(self):
        print("TODO")

    def test__BytesIO___reduce__(self):
        print("TODO")

    def test__BytesIO___reduce_ex__(self):
        print("TODO")

    def test__BytesIO___repr__(self):
        print("TODO")

    def test__BytesIO___setattr__(self):
        print("TODO")

    def test__BytesIO___sizeof__(self):
        print("TODO")

    def test__BytesIO___str__(self):
        print("TODO")

    def test__BytesIO___subclasshook__(self):
        print("TODO")

    def test__BytesIO_close(self):
        print("TODO")

    def test__BytesIO_closed(self):
        print("TODO")

    def test__BytesIO_flush(self):
        print("TODO")

    def test__BytesIO_getvalue(self):
        print("TODO")

    def test__BytesIO_isatty(self):
        print("TODO")

    def test__BytesIO_next(self):
        print("TODO")

    def test__BytesIO_read(self):
        print("TODO")

    def test__BytesIO_read1(self):
        print("TODO")

    def test__BytesIO_readable(self):
        print("TODO")

    def test__BytesIO_readinto(self):
        print("TODO")

    def test__BytesIO_readline(self):
        print("TODO")

    def test__BytesIO_readlines(self):
        print("TODO")

    def test__BytesIO_seek(self):
        print("TODO")

    def test__BytesIO_seekable(self):
        print("TODO")

    def test__BytesIO_tell(self):
        print("TODO")

    def test__BytesIO_truncate(self):
        print("TODO")

    def test__BytesIO_writable(self):
        print("TODO")

    def test__BytesIO_write(self):
        print("TODO")

    def test__BytesIO_writelines(self):
        print("TODO")


    def test_coverage(self):
        '''
        Test case holes discovered by code coverage runs. Test cases below need to
        be migrated elsewhere (TODO).
        '''
        #--BytesIO.readinto(array.array(...))
        import array
        
        readinto_cases = [
                            [('c',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('c',['z']),
                            [['z'],['a'],['a'],['a'],['a'],['a'],['a'],['a'],['a'],['a']],
                            [0,1,1,1,1,1,1,1,1,1]],
                            [('c',['a','z']),
                            [['a','z'],['a','z'],['a','b'],['a','b'],['a','b'],['a','b'],['a','b'],['a','b'],['a','b'],['a','b']],
                            [0,1,2,2,2,2,2,2,2,2]],
                            [('b',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('b',[0]),
                            [[0],[97],[97],[97],[97],[97],[97],[97],[97],[97]],
                            [0,1,1,1,1,1,1,1,1,1]],
                            [('b',[0,-1]),
                            [[0,-1],[97,-1],[97,98],[97,98],[97,98],[97,98],[97,98],[97,98],[97,98],[97,98]],
                            [0,1,2,2,2,2,2,2,2,2]],
                            [('b',[0,1,2]),
                            [[0,1,2],[97,1,2],[97,98,2],[97,98,99],[97,98,99],[97,98,99],[97,98,99],[97,98,99],[97,98,99],[97,98,99]],
                            [0,1,2,3,3,3,3,3,3,3]],
                            [('b',[0,1,2,3,4,5,6]),
                            [[0,1,2,3,4,5,6],[97,1,2,3,4,5,6],[97,98,2,3,4,5,6],[97,98,99,3,4,5,6],[97,98,99,100,4,5,6],[97,98,99,100,101,5,6],[97,98,99,100,101,102,6],[97,98,99,100,101,102,103],[97,98,99,100,101,102,103],[97,98,99,100,101,102,103]],
                            [0,1,2,3,4,5,6,7,7,7]],
                            [('b',[0,1,2,3,4,5,6,7]),
                            [[0,1,2,3,4,5,6,7],[97,1,2,3,4,5,6,7],[97,98,2,3,4,5,6,7],[97,98,99,3,4,5,6,7],[97,98,99,100,4,5,6,7],[97,98,99,100,101,5,6,7],[97,98,99,100,101,102,6,7],[97,98,99,100,101,102,103,7],[97,98,99,100,101,102,103,104],[97,98,99,100,101,102,103,104]],
                            [0,1,2,3,4,5,6,7,8,8]],
                            [('b',[0,1,2,3,4,5,6,7,8]),
                            [[0,1,2,3,4,5,6,7,8],[97,1,2,3,4,5,6,7,8],[97,98,2,3,4,5,6,7,8],[97,98,99,3,4,5,6,7,8],[97,98,99,100,4,5,6,7,8],[97,98,99,100,101,5,6,7,8],[97,98,99,100,101,102,6,7,8],[97,98,99,100,101,102,103,7,8],[97,98,99,100,101,102,103,104,8],[97,98,99,100,101,102,103,104,105]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('b',[0,1,2,3,4,5,6,7,8,9]),
                            [[0,1,2,3,4,5,6,7,8,9],[97,1,2,3,4,5,6,7,8,9],[97,98,2,3,4,5,6,7,8,9],[97,98,99,3,4,5,6,7,8,9],[97,98,99,100,4,5,6,7,8,9],[97,98,99,100,101,5,6,7,8,9],[97,98,99,100,101,102,6,7,8,9],[97,98,99,100,101,102,103,7,8,9],[97,98,99,100,101,102,103,104,8,9],[97,98,99,100,101,102,103,104,105,9]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('B',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('B',[0,1]),
                            [[0,1],[97,1],[97,98],[97,98],[97,98],[97,98],[97,98],[97,98],[97,98],[97,98]],
                            [0,1,2,2,2,2,2,2,2,2]],
                            [('u',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('u',''),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            #http://ironpython.codeplex.com/WorkItem/View.aspx?WorkItemId=24303
                            #[('u',u'z'),
                            # [[u'z'],[u'a'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261']],
                            # [0,1,2,2,2,2,2,2,2,2]],
                            #[('u',u'az'),
                            # [[u'a',u'z'],[u'a',u'z'],[u'\u6261',u'z'],[u'\u6261',u'c'],[u'\u6261',u'\u6463'],[u'\u6261',u'\u6463'],[u'\u6261',u'\u6463'],[u'\u6261',u'\u6463'],[u'\u6261',u'\u6463'],[u'\u6261',u'\u6463']],
                            # [0,1,2,3,4,4,4,4,4,4]],
                            #[('u',u'*'),
                            # [[u'*'],[u'a'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261'],[u'\u6261']],
                            # [0,1,2,2,2,2,2,2,2,2]],
                            [('h',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('h',[-1]),
                            [[-1],[-159],[25185],[25185],[25185],[25185],[25185],[25185],[25185],[25185]],
                            [0,1,2,2,2,2,2,2,2,2]],
                            [('h',[1,2]),
                            [[1,2],[97,2],[25185,2],[25185,99],[25185,25699],[25185,25699],[25185,25699],[25185,25699],[25185,25699],[25185,25699]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('h',[1,-99,47]),
                            [[1,-99,47],[97,-99,47],[25185,-99,47],[25185,-157,47],[25185,25699,47],[25185,25699,101],[25185,25699,26213],[25185,25699,26213],[25185,25699,26213],[25185,25699,26213]],
                            [0,1,2,3,4,5,6,6,6,6]],
                            [('H',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('H',[]),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('H',[49]),
                            [[49],[97],[25185],[25185],[25185],[25185],[25185],[25185],[25185],[25185]],
                            [0,1,2,2,2,2,2,2,2,2]],
                            [('H',[2,3]),
                            [[2,3],[97,3],[25185,3],[25185,99],[25185,25699],[25185,25699],[25185,25699],[25185,25699],[25185,25699],[25185,25699]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('i',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('i',[-1]),
                            [[-1],[-159],[-40351],[-10263967],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('i',[1,-99,47]),
                            [[1,-99,47],[97,-99,47],[25185,-99,47],[6513249,-99,47],[1684234849,-99,47],[1684234849,-155,47],[1684234849,-39323,47],[1684234849,-10000795,47],[1684234849,1751606885,47],[1684234849,1751606885,105]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('I',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('I',[1]),
                            [[1],[97],[25185],[6513249],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('I',[1,999,47]),
                            [[1,999,47],[97,999,47],[25185,999,47],[6513249,999,47],[1684234849,999,47],[1684234849,869,47],[1684234849,26213,47],[1684234849,6776421,47],[1684234849,1751606885,47],[1684234849,1751606885,105]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('l',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('l',[-1]),
                            [[-1],[-159],[-40351],[-10263967],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('l',[1,-99,47]),
                            [[1,-99,47],[97,-99,47],[25185,-99,47],[6513249,-99,47],[1684234849,-99,47],[1684234849,-155,47],[1684234849,-39323,47],[1684234849,-10000795,47],[1684234849,1751606885,47],[1684234849,1751606885,105]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('l',[1,-99,47,48]),
                            [[1,-99,47,48],[97,-99,47,48],[25185,-99,47,48],[6513249,-99,47,48],[1684234849,-99,47,48],[1684234849,-155,47,48],[1684234849,-39323,47,48],[1684234849,-10000795,47,48],[1684234849,1751606885,47,48],[1684234849,1751606885,105,48]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('l',[1,-99,47,48,49]),
                            [[1,-99,47,48,49],[97,-99,47,48,49],[25185,-99,47,48,49],[6513249,-99,47,48,49],[1684234849,-99,47,48,49],[1684234849,-155,47,48,49],[1684234849,-39323,47,48,49],[1684234849,-10000795,47,48,49],[1684234849,1751606885,47,48,49],[1684234849,1751606885,105,48,49]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('L',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('L',[100000000]),
                            [[100000000],[100000097],[99967585],[90399329],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849],[1684234849]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('L',[1,99,47]),
                            [[1,99,47],[97,99,47],[25185,99,47],[6513249,99,47],[1684234849,99,47],[1684234849,101,47],[1684234849,26213,47],[1684234849,6776421,47],[1684234849,1751606885,47],[1684234849,1751606885,105]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('f',[]),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('f',[3.1415926535897931]),
                            [[3.1415927410125732],[3.1415636539459229],[3.1466295719146729],[3.5528795719146729],[1.6777999408082104e+22],[1.6777999408082104e+22],[1.6777999408082104e+22],[1.6777999408082104e+22],[1.6777999408082104e+22],[1.6777999408082104e+22]],
                            [0,1,2,3,4,4,4,4,4,4]],
                            [('f',[1.0,3.1400000000000001,0.997]),
                            [[1.0,3.1400001049041748,0.99699997901916504],[1.0000115633010864,3.1400001049041748,0.99699997901916504],[1.0030022859573364,3.1400001049041748,0.99699997901916504],[0.88821989297866821,3.1400001049041748,0.99699997901916504],[1.6777999408082104e+22,3.1400001049041748,0.99699997901916504],[1.6777999408082104e+22,3.1399776935577393,0.99699997901916504],[1.6777999408082104e+22,3.1312496662139893,0.99699997901916504],[1.6777999408082104e+22,3.6156246662139893,0.99699997901916504],[1.6777999408082104e+22,4.371022013021617e+24,0.99699997901916504],[1.6777999408082104e+22,4.371022013021617e+24,0.99700027704238892]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('d',),
                            [[],[],[],[],[],[],[],[],[],[]],
                            [0,0,0,0,0,0,0,0,0,0]],
                            [('d',[3.1415926535897931]),
                            [[3.1415926535897931],[3.1415926535898255],[3.1415926535958509],[3.1415926544980697],[3.1415927737073592],[3.1413066714124374],[3.1749980776624374],[187.19987697039599],[8.5408832230361244e+194],[8.5408832230361244e+194]],
                            [0,1,2,3,4,5,6,7,8,8]],
                            [('d',[1.0,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004]),
                            [[1.0,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[1.0000000000000215,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[1.0000000000055922,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[1.0000000014462318,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[1.0000003739752616,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[1.0000966950812187,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[1.0249990388312187,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[0.002856443435217224,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[8.5408832230361244e+194,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004],[8.5408832230361244e+194,3.140000000000033,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('d',[1.0,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5]),
                            [[1.0,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[1.0000000000000215,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[1.0000000000055922,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[1.0000000014462318,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[1.0000003739752616,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[1.0000966950812187,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[1.0249990388312187,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[0.002856443435217224,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[8.5408832230361244e+194,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5],[8.5408832230361244e+194,3.140000000000033,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5]],
                            [0,1,2,3,4,5,6,7,8,9]],
                            [('d',[1.0,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996]),
                            [[1.0,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[1.0000000000000215,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[1.0000000000055922,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[1.0000000014462318,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[1.0000003739752616,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[1.0000966950812187,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[1.0249990388312187,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[0.002856443435217224,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[8.5408832230361244e+194,3.1400000000000001,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996],[8.5408832230361244e+194,3.140000000000033,0.99734343339999998,1.1000000000000001,2.2000000000000002,3.2999999999999998,4.4000000000000004,5.5,6.5999999999999996]],
                            [0,1,2,3,4,5,6,7,8,9]],    
                            ]

        for a_params, a_expected, b_expected in readinto_cases:
            b_list = bytesio_helper()
            
            for i in range(len(b_list)):
                a = array.array(*a_params)
                b = b_list[i]
                self.assertEqual(b.readinto(a),
                        b_expected[i])
                self.assertEqual(a.tolist(),
                        a_expected[i])

run_test(__name__)