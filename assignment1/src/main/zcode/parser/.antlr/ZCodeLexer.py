# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
#MSSV: 2152597


def serializedATN():
    return [
        4,0,51,436,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,1,0,1,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,
        23,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,
        27,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,32,1,32,1,
        33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,
        37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,4,
        43,299,8,43,11,43,12,43,300,1,43,5,43,304,8,43,10,43,12,43,307,9,
        43,1,44,1,44,1,45,1,45,1,46,1,46,3,46,315,8,46,1,47,1,47,5,47,319,
        8,47,10,47,12,47,322,9,47,1,48,1,48,3,48,326,8,48,1,48,1,48,5,48,
        330,8,48,10,48,12,48,333,9,48,1,49,1,49,5,49,337,8,49,10,49,12,49,
        340,9,49,1,49,5,49,343,8,49,10,49,12,49,346,9,49,1,49,5,49,349,8,
        49,10,49,12,49,352,9,49,1,49,3,49,355,8,49,1,50,1,50,1,51,1,51,1,
        51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,54,3,54,372,8,
        54,1,55,1,55,5,55,376,8,55,10,55,12,55,379,9,55,1,55,1,55,1,55,1,
        56,1,56,1,56,1,57,1,57,5,57,389,8,57,10,57,12,57,392,9,57,1,57,1,
        57,1,58,4,58,397,8,58,11,58,12,58,398,1,58,1,58,1,59,1,59,1,60,1,
        60,1,61,1,61,1,61,1,62,1,62,5,62,412,8,62,10,62,12,62,415,9,62,1,
        62,1,62,1,62,1,63,1,63,5,63,422,8,63,10,63,12,63,425,9,63,1,63,1,
        63,5,63,429,8,63,10,63,12,63,432,9,63,1,63,1,63,1,63,0,0,64,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,
        73,37,75,38,77,39,79,40,81,41,83,42,85,0,87,43,89,0,91,0,93,0,95,
        0,97,0,99,44,101,0,103,0,105,0,107,0,109,0,111,45,113,0,115,46,117,
        47,119,48,121,0,123,49,125,50,127,51,1,0,11,3,0,65,90,95,95,97,122,
        3,0,48,57,65,90,97,122,1,0,49,57,2,0,69,69,101,101,2,0,43,43,45,
        45,5,0,8,10,12,13,34,34,39,39,92,92,1,0,92,92,1,0,34,34,1,0,39,39,
        3,0,8,9,12,13,32,32,1,0,10,10,440,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,
        0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,
        0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,87,1,0,
        0,0,0,99,1,0,0,0,0,111,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,
        1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,1,129,1,0,0,0,
        3,134,1,0,0,0,5,139,1,0,0,0,7,145,1,0,0,0,9,152,1,0,0,0,11,157,1,
        0,0,0,13,164,1,0,0,0,15,171,1,0,0,0,17,175,1,0,0,0,19,183,1,0,0,
        0,21,188,1,0,0,0,23,192,1,0,0,0,25,198,1,0,0,0,27,201,1,0,0,0,29,
        207,1,0,0,0,31,216,1,0,0,0,33,219,1,0,0,0,35,224,1,0,0,0,37,229,
        1,0,0,0,39,235,1,0,0,0,41,239,1,0,0,0,43,241,1,0,0,0,45,243,1,0,
        0,0,47,245,1,0,0,0,49,247,1,0,0,0,51,249,1,0,0,0,53,253,1,0,0,0,
        55,257,1,0,0,0,57,260,1,0,0,0,59,262,1,0,0,0,61,265,1,0,0,0,63,268,
        1,0,0,0,65,270,1,0,0,0,67,272,1,0,0,0,69,275,1,0,0,0,71,278,1,0,
        0,0,73,281,1,0,0,0,75,285,1,0,0,0,77,287,1,0,0,0,79,289,1,0,0,0,
        81,291,1,0,0,0,83,293,1,0,0,0,85,295,1,0,0,0,87,298,1,0,0,0,89,308,
        1,0,0,0,91,310,1,0,0,0,93,314,1,0,0,0,95,316,1,0,0,0,97,323,1,0,
        0,0,99,354,1,0,0,0,101,356,1,0,0,0,103,358,1,0,0,0,105,361,1,0,0,
        0,107,365,1,0,0,0,109,371,1,0,0,0,111,373,1,0,0,0,113,383,1,0,0,
        0,115,386,1,0,0,0,117,396,1,0,0,0,119,402,1,0,0,0,121,404,1,0,0,
        0,123,406,1,0,0,0,125,409,1,0,0,0,127,419,1,0,0,0,129,130,5,109,
        0,0,130,131,5,97,0,0,131,132,5,105,0,0,132,133,5,110,0,0,133,2,1,
        0,0,0,134,135,5,116,0,0,135,136,5,114,0,0,136,137,5,117,0,0,137,
        138,5,101,0,0,138,4,1,0,0,0,139,140,5,102,0,0,140,141,5,97,0,0,141,
        142,5,108,0,0,142,143,5,115,0,0,143,144,5,101,0,0,144,6,1,0,0,0,
        145,146,5,110,0,0,146,147,5,117,0,0,147,148,5,109,0,0,148,149,5,
        98,0,0,149,150,5,101,0,0,150,151,5,114,0,0,151,8,1,0,0,0,152,153,
        5,98,0,0,153,154,5,111,0,0,154,155,5,111,0,0,155,156,5,108,0,0,156,
        10,1,0,0,0,157,158,5,115,0,0,158,159,5,116,0,0,159,160,5,114,0,0,
        160,161,5,105,0,0,161,162,5,110,0,0,162,163,5,103,0,0,163,12,1,0,
        0,0,164,165,5,114,0,0,165,166,5,101,0,0,166,167,5,116,0,0,167,168,
        5,117,0,0,168,169,5,114,0,0,169,170,5,110,0,0,170,14,1,0,0,0,171,
        172,5,118,0,0,172,173,5,97,0,0,173,174,5,114,0,0,174,16,1,0,0,0,
        175,176,5,100,0,0,176,177,5,121,0,0,177,178,5,110,0,0,178,179,5,
        97,0,0,179,180,5,109,0,0,180,181,5,105,0,0,181,182,5,99,0,0,182,
        18,1,0,0,0,183,184,5,102,0,0,184,185,5,117,0,0,185,186,5,110,0,0,
        186,187,5,99,0,0,187,20,1,0,0,0,188,189,5,102,0,0,189,190,5,111,
        0,0,190,191,5,114,0,0,191,22,1,0,0,0,192,193,5,117,0,0,193,194,5,
        110,0,0,194,195,5,116,0,0,195,196,5,105,0,0,196,197,5,108,0,0,197,
        24,1,0,0,0,198,199,5,98,0,0,199,200,5,121,0,0,200,26,1,0,0,0,201,
        202,5,98,0,0,202,203,5,114,0,0,203,204,5,101,0,0,204,205,5,97,0,
        0,205,206,5,107,0,0,206,28,1,0,0,0,207,208,5,99,0,0,208,209,5,111,
        0,0,209,210,5,110,0,0,210,211,5,116,0,0,211,212,5,105,0,0,212,213,
        5,110,0,0,213,214,5,117,0,0,214,215,5,101,0,0,215,30,1,0,0,0,216,
        217,5,105,0,0,217,218,5,102,0,0,218,32,1,0,0,0,219,220,5,101,0,0,
        220,221,5,108,0,0,221,222,5,115,0,0,222,223,5,101,0,0,223,34,1,0,
        0,0,224,225,5,101,0,0,225,226,5,108,0,0,226,227,5,105,0,0,227,228,
        5,102,0,0,228,36,1,0,0,0,229,230,5,98,0,0,230,231,5,101,0,0,231,
        232,5,103,0,0,232,233,5,105,0,0,233,234,5,110,0,0,234,38,1,0,0,0,
        235,236,5,101,0,0,236,237,5,110,0,0,237,238,5,100,0,0,238,40,1,0,
        0,0,239,240,5,43,0,0,240,42,1,0,0,0,241,242,5,45,0,0,242,44,1,0,
        0,0,243,244,5,42,0,0,244,46,1,0,0,0,245,246,5,47,0,0,246,48,1,0,
        0,0,247,248,5,37,0,0,248,50,1,0,0,0,249,250,5,110,0,0,250,251,5,
        111,0,0,251,252,5,116,0,0,252,52,1,0,0,0,253,254,5,97,0,0,254,255,
        5,110,0,0,255,256,5,100,0,0,256,54,1,0,0,0,257,258,5,111,0,0,258,
        259,5,114,0,0,259,56,1,0,0,0,260,261,5,61,0,0,261,58,1,0,0,0,262,
        263,5,60,0,0,263,264,5,45,0,0,264,60,1,0,0,0,265,266,5,33,0,0,266,
        267,5,61,0,0,267,62,1,0,0,0,268,269,5,60,0,0,269,64,1,0,0,0,270,
        271,5,62,0,0,271,66,1,0,0,0,272,273,5,60,0,0,273,274,5,61,0,0,274,
        68,1,0,0,0,275,276,5,62,0,0,276,277,5,61,0,0,277,70,1,0,0,0,278,
        279,5,61,0,0,279,280,5,61,0,0,280,72,1,0,0,0,281,282,5,46,0,0,282,
        283,5,46,0,0,283,284,5,46,0,0,284,74,1,0,0,0,285,286,5,40,0,0,286,
        76,1,0,0,0,287,288,5,41,0,0,288,78,1,0,0,0,289,290,5,91,0,0,290,
        80,1,0,0,0,291,292,5,93,0,0,292,82,1,0,0,0,293,294,5,44,0,0,294,
        84,1,0,0,0,295,296,7,0,0,0,296,86,1,0,0,0,297,299,3,85,42,0,298,
        297,1,0,0,0,299,300,1,0,0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,
        305,1,0,0,0,302,304,7,1,0,0,303,302,1,0,0,0,304,307,1,0,0,0,305,
        303,1,0,0,0,305,306,1,0,0,0,306,88,1,0,0,0,307,305,1,0,0,0,308,309,
        5,48,0,0,309,90,1,0,0,0,310,311,7,2,0,0,311,92,1,0,0,0,312,315,3,
        89,44,0,313,315,3,91,45,0,314,312,1,0,0,0,314,313,1,0,0,0,315,94,
        1,0,0,0,316,320,5,46,0,0,317,319,3,93,46,0,318,317,1,0,0,0,319,322,
        1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,96,1,0,0,0,322,320,1,
        0,0,0,323,325,7,3,0,0,324,326,7,4,0,0,325,324,1,0,0,0,325,326,1,
        0,0,0,326,327,1,0,0,0,327,331,3,91,45,0,328,330,3,93,46,0,329,328,
        1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,98,1,
        0,0,0,333,331,1,0,0,0,334,338,3,91,45,0,335,337,3,93,46,0,336,335,
        1,0,0,0,337,340,1,0,0,0,338,336,1,0,0,0,338,339,1,0,0,0,339,344,
        1,0,0,0,340,338,1,0,0,0,341,343,3,95,47,0,342,341,1,0,0,0,343,346,
        1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,350,1,0,0,0,346,344,
        1,0,0,0,347,349,3,97,48,0,348,347,1,0,0,0,349,352,1,0,0,0,350,348,
        1,0,0,0,350,351,1,0,0,0,351,355,1,0,0,0,352,350,1,0,0,0,353,355,
        3,89,44,0,354,334,1,0,0,0,354,353,1,0,0,0,355,100,1,0,0,0,356,357,
        8,5,0,0,357,102,1,0,0,0,358,359,9,0,0,0,359,360,7,6,0,0,360,104,
        1,0,0,0,361,362,9,0,0,0,362,363,3,103,51,0,363,364,8,7,0,0,364,106,
        1,0,0,0,365,366,7,8,0,0,366,367,7,7,0,0,367,108,1,0,0,0,368,372,
        3,105,52,0,369,372,3,107,53,0,370,372,3,101,50,0,371,368,1,0,0,0,
        371,369,1,0,0,0,371,370,1,0,0,0,372,110,1,0,0,0,373,377,7,7,0,0,
        374,376,3,109,54,0,375,374,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,
        0,377,378,1,0,0,0,378,380,1,0,0,0,379,377,1,0,0,0,380,381,7,7,0,
        0,381,382,6,55,0,0,382,112,1,0,0,0,383,384,5,35,0,0,384,385,5,35,
        0,0,385,114,1,0,0,0,386,390,3,113,56,0,387,389,3,121,60,0,388,387,
        1,0,0,0,389,392,1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,393,
        1,0,0,0,392,390,1,0,0,0,393,394,6,57,1,0,394,116,1,0,0,0,395,397,
        7,9,0,0,396,395,1,0,0,0,397,398,1,0,0,0,398,396,1,0,0,0,398,399,
        1,0,0,0,399,400,1,0,0,0,400,401,6,58,1,0,401,118,1,0,0,0,402,403,
        5,10,0,0,403,120,1,0,0,0,404,405,8,10,0,0,405,122,1,0,0,0,406,407,
        9,0,0,0,407,408,6,61,2,0,408,124,1,0,0,0,409,413,7,7,0,0,410,412,
        3,109,54,0,411,410,1,0,0,0,412,415,1,0,0,0,413,411,1,0,0,0,413,414,
        1,0,0,0,414,416,1,0,0,0,415,413,1,0,0,0,416,417,5,0,0,1,417,418,
        6,62,3,0,418,126,1,0,0,0,419,423,7,7,0,0,420,422,3,109,54,0,421,
        420,1,0,0,0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,
        426,1,0,0,0,425,423,1,0,0,0,426,430,3,103,51,0,427,429,3,109,54,
        0,428,427,1,0,0,0,429,432,1,0,0,0,430,428,1,0,0,0,430,431,1,0,0,
        0,431,433,1,0,0,0,432,430,1,0,0,0,433,434,7,7,0,0,434,435,6,63,4,
        0,435,128,1,0,0,0,18,0,300,305,314,320,325,331,338,344,350,354,371,
        377,390,398,413,423,430,5,1,55,0,6,0,0,1,61,1,1,62,2,1,63,3
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN_TOKEN = 1
    KW_TRUE = 2
    KW_FALSE = 3
    KW_NUMBER = 4
    KW_BOOL = 5
    KW_STRING = 6
    KW_RETURN = 7
    KW_VAR = 8
    KW_DYNAMIC = 9
    KW_FUNC = 10
    KW_FOR = 11
    KW_UNTIL = 12
    KW_BY = 13
    KW_BREAK = 14
    KW_CONTINUE = 15
    KW_IF = 16
    KW_ELSE = 17
    KW_ELIF = 18
    KW_BEGIN = 19
    KW_END = 20
    OP_ADD = 21
    OP_SUBTRACT = 22
    OP_MULTI = 23
    OP_DIVIDE = 24
    OP_REMAINDER = 25
    OP_NOT = 26
    OP_AND = 27
    OP_OR = 28
    OP_EQUAL = 29
    OP_ASSIGN = 30
    OP_NOT_EQUAL = 31
    OP_SMALLER = 32
    OP_GREATER = 33
    OP_SMALLER_EQUAL = 34
    OP_GREATER_EQUAL = 35
    OP_STRING_EQUAL = 36
    OP_STRING_CONCAT = 37
    SEP_OPEN_PAREN = 38
    SEP_CLOSE_PAREN = 39
    SEP_OPEN_BRACK = 40
    SEP_CLOSE_BRACK = 41
    SEP_COMA = 42
    IDENTIFIER = 43
    NUMBER = 44
    STRING = 45
    COMMENT = 46
    WS = 47
    NEW_LINE = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", 
            "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'...'", "'('", "')'", "'['", "']'", "','", 
            "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN_TOKEN", "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", 
            "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", 
            "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", 
            "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", "OP_SUBTRACT", 
            "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", "OP_NOT", "OP_AND", 
            "OP_OR", "OP_EQUAL", "OP_ASSIGN", "OP_NOT_EQUAL", "OP_SMALLER", 
            "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", "OP_STRING_EQUAL", 
            "OP_STRING_CONCAT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", 
            "SEP_CLOSE_BRACK", "SEP_COMA", "IDENTIFIER", "NUMBER", "STRING", 
            "COMMENT", "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "MAIN_TOKEN", "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", 
                  "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", 
                  "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", 
                  "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", 
                  "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", 
                  "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_ASSIGN", 
                  "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", 
                  "OP_GREATER_EQUAL", "OP_STRING_EQUAL", "OP_STRING_CONCAT", 
                  "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", 
                  "SEP_CLOSE_BRACK", "SEP_COMA", "IDENTIFIER_HEAD", "IDENTIFIER", 
                  "ZERO", "NON_ZERO_DIGIT", "DIGIT", "FLOATING_POINT", "EXPONENTIAL", 
                  "NUMBER", "STRING_CHAR", "ESCAPE_SIGN", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", "STRING", 
                  "COMMENT_HEAD", "COMMENT", "WS", "NEW_LINE", "NOT_NEW_LINE", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.STRING_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:-1])
     


