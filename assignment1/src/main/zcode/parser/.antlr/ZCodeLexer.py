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
        4,0,52,442,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,3,1,139,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,
        21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,
        26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,
        31,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,
        36,1,36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,
        41,1,41,1,42,1,42,1,43,1,43,1,44,4,44,305,8,44,11,44,12,44,306,1,
        44,5,44,310,8,44,10,44,12,44,313,9,44,1,45,1,45,1,46,1,46,1,47,1,
        47,3,47,321,8,47,1,48,1,48,5,48,325,8,48,10,48,12,48,328,9,48,1,
        49,1,49,3,49,332,8,49,1,49,1,49,5,49,336,8,49,10,49,12,49,339,9,
        49,1,50,1,50,5,50,343,8,50,10,50,12,50,346,9,50,1,50,5,50,349,8,
        50,10,50,12,50,352,9,50,1,50,5,50,355,8,50,10,50,12,50,358,9,50,
        1,50,3,50,361,8,50,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,1,53,
        1,54,1,54,1,54,1,55,1,55,1,55,3,55,378,8,55,1,56,1,56,5,56,382,8,
        56,10,56,12,56,385,9,56,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,
        5,58,395,8,58,10,58,12,58,398,9,58,1,58,1,58,1,59,4,59,403,8,59,
        11,59,12,59,404,1,59,1,59,1,60,1,60,1,61,1,61,1,62,1,62,1,62,1,63,
        1,63,5,63,418,8,63,10,63,12,63,421,9,63,1,63,1,63,1,63,1,64,1,64,
        5,64,428,8,64,10,64,12,64,431,9,64,1,64,1,64,5,64,435,8,64,10,64,
        12,64,438,9,64,1,64,1,64,1,64,0,0,65,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,0,89,44,91,0,93,0,95,0,97,0,99,0,101,45,103,
        0,105,0,107,0,109,0,111,0,113,46,115,0,117,47,119,48,121,49,123,
        0,125,50,127,51,129,52,1,0,11,3,0,65,90,95,95,97,122,3,0,48,57,65,
        90,97,122,1,0,49,57,2,0,69,69,101,101,2,0,43,43,45,45,5,0,8,10,12,
        13,34,34,39,39,92,92,1,0,92,92,1,0,34,34,1,0,39,39,3,0,8,9,12,13,
        32,32,1,0,10,10,447,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,
        0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,
        0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,
        0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,
        0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,
        0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,89,1,0,
        0,0,0,101,1,0,0,0,0,113,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,
        1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,1,131,1,0,0,0,
        3,138,1,0,0,0,5,140,1,0,0,0,7,145,1,0,0,0,9,151,1,0,0,0,11,158,1,
        0,0,0,13,163,1,0,0,0,15,170,1,0,0,0,17,177,1,0,0,0,19,181,1,0,0,
        0,21,189,1,0,0,0,23,194,1,0,0,0,25,198,1,0,0,0,27,204,1,0,0,0,29,
        207,1,0,0,0,31,213,1,0,0,0,33,222,1,0,0,0,35,225,1,0,0,0,37,230,
        1,0,0,0,39,235,1,0,0,0,41,241,1,0,0,0,43,245,1,0,0,0,45,247,1,0,
        0,0,47,249,1,0,0,0,49,251,1,0,0,0,51,253,1,0,0,0,53,255,1,0,0,0,
        55,259,1,0,0,0,57,263,1,0,0,0,59,266,1,0,0,0,61,268,1,0,0,0,63,271,
        1,0,0,0,65,274,1,0,0,0,67,276,1,0,0,0,69,278,1,0,0,0,71,281,1,0,
        0,0,73,284,1,0,0,0,75,287,1,0,0,0,77,291,1,0,0,0,79,293,1,0,0,0,
        81,295,1,0,0,0,83,297,1,0,0,0,85,299,1,0,0,0,87,301,1,0,0,0,89,304,
        1,0,0,0,91,314,1,0,0,0,93,316,1,0,0,0,95,320,1,0,0,0,97,322,1,0,
        0,0,99,329,1,0,0,0,101,360,1,0,0,0,103,362,1,0,0,0,105,364,1,0,0,
        0,107,367,1,0,0,0,109,371,1,0,0,0,111,377,1,0,0,0,113,379,1,0,0,
        0,115,389,1,0,0,0,117,392,1,0,0,0,119,402,1,0,0,0,121,408,1,0,0,
        0,123,410,1,0,0,0,125,412,1,0,0,0,127,415,1,0,0,0,129,425,1,0,0,
        0,131,132,5,109,0,0,132,133,5,97,0,0,133,134,5,105,0,0,134,135,5,
        110,0,0,135,2,1,0,0,0,136,139,3,5,2,0,137,139,3,7,3,0,138,136,1,
        0,0,0,138,137,1,0,0,0,139,4,1,0,0,0,140,141,5,116,0,0,141,142,5,
        114,0,0,142,143,5,117,0,0,143,144,5,101,0,0,144,6,1,0,0,0,145,146,
        5,102,0,0,146,147,5,97,0,0,147,148,5,108,0,0,148,149,5,115,0,0,149,
        150,5,101,0,0,150,8,1,0,0,0,151,152,5,110,0,0,152,153,5,117,0,0,
        153,154,5,109,0,0,154,155,5,98,0,0,155,156,5,101,0,0,156,157,5,114,
        0,0,157,10,1,0,0,0,158,159,5,98,0,0,159,160,5,111,0,0,160,161,5,
        111,0,0,161,162,5,108,0,0,162,12,1,0,0,0,163,164,5,115,0,0,164,165,
        5,116,0,0,165,166,5,114,0,0,166,167,5,105,0,0,167,168,5,110,0,0,
        168,169,5,103,0,0,169,14,1,0,0,0,170,171,5,114,0,0,171,172,5,101,
        0,0,172,173,5,116,0,0,173,174,5,117,0,0,174,175,5,114,0,0,175,176,
        5,110,0,0,176,16,1,0,0,0,177,178,5,118,0,0,178,179,5,97,0,0,179,
        180,5,114,0,0,180,18,1,0,0,0,181,182,5,100,0,0,182,183,5,121,0,0,
        183,184,5,110,0,0,184,185,5,97,0,0,185,186,5,109,0,0,186,187,5,105,
        0,0,187,188,5,99,0,0,188,20,1,0,0,0,189,190,5,102,0,0,190,191,5,
        117,0,0,191,192,5,110,0,0,192,193,5,99,0,0,193,22,1,0,0,0,194,195,
        5,102,0,0,195,196,5,111,0,0,196,197,5,114,0,0,197,24,1,0,0,0,198,
        199,5,117,0,0,199,200,5,110,0,0,200,201,5,116,0,0,201,202,5,105,
        0,0,202,203,5,108,0,0,203,26,1,0,0,0,204,205,5,98,0,0,205,206,5,
        121,0,0,206,28,1,0,0,0,207,208,5,98,0,0,208,209,5,114,0,0,209,210,
        5,101,0,0,210,211,5,97,0,0,211,212,5,107,0,0,212,30,1,0,0,0,213,
        214,5,99,0,0,214,215,5,111,0,0,215,216,5,110,0,0,216,217,5,116,0,
        0,217,218,5,105,0,0,218,219,5,110,0,0,219,220,5,117,0,0,220,221,
        5,101,0,0,221,32,1,0,0,0,222,223,5,105,0,0,223,224,5,102,0,0,224,
        34,1,0,0,0,225,226,5,101,0,0,226,227,5,108,0,0,227,228,5,115,0,0,
        228,229,5,101,0,0,229,36,1,0,0,0,230,231,5,101,0,0,231,232,5,108,
        0,0,232,233,5,105,0,0,233,234,5,102,0,0,234,38,1,0,0,0,235,236,5,
        98,0,0,236,237,5,101,0,0,237,238,5,103,0,0,238,239,5,105,0,0,239,
        240,5,110,0,0,240,40,1,0,0,0,241,242,5,101,0,0,242,243,5,110,0,0,
        243,244,5,100,0,0,244,42,1,0,0,0,245,246,5,43,0,0,246,44,1,0,0,0,
        247,248,5,45,0,0,248,46,1,0,0,0,249,250,5,42,0,0,250,48,1,0,0,0,
        251,252,5,47,0,0,252,50,1,0,0,0,253,254,5,37,0,0,254,52,1,0,0,0,
        255,256,5,110,0,0,256,257,5,111,0,0,257,258,5,116,0,0,258,54,1,0,
        0,0,259,260,5,97,0,0,260,261,5,110,0,0,261,262,5,100,0,0,262,56,
        1,0,0,0,263,264,5,111,0,0,264,265,5,114,0,0,265,58,1,0,0,0,266,267,
        5,61,0,0,267,60,1,0,0,0,268,269,5,60,0,0,269,270,5,45,0,0,270,62,
        1,0,0,0,271,272,5,33,0,0,272,273,5,61,0,0,273,64,1,0,0,0,274,275,
        5,60,0,0,275,66,1,0,0,0,276,277,5,62,0,0,277,68,1,0,0,0,278,279,
        5,60,0,0,279,280,5,61,0,0,280,70,1,0,0,0,281,282,5,62,0,0,282,283,
        5,61,0,0,283,72,1,0,0,0,284,285,5,61,0,0,285,286,5,61,0,0,286,74,
        1,0,0,0,287,288,5,46,0,0,288,289,5,46,0,0,289,290,5,46,0,0,290,76,
        1,0,0,0,291,292,5,40,0,0,292,78,1,0,0,0,293,294,5,41,0,0,294,80,
        1,0,0,0,295,296,5,91,0,0,296,82,1,0,0,0,297,298,5,93,0,0,298,84,
        1,0,0,0,299,300,5,44,0,0,300,86,1,0,0,0,301,302,7,0,0,0,302,88,1,
        0,0,0,303,305,3,87,43,0,304,303,1,0,0,0,305,306,1,0,0,0,306,304,
        1,0,0,0,306,307,1,0,0,0,307,311,1,0,0,0,308,310,7,1,0,0,309,308,
        1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,90,1,
        0,0,0,313,311,1,0,0,0,314,315,5,48,0,0,315,92,1,0,0,0,316,317,7,
        2,0,0,317,94,1,0,0,0,318,321,3,91,45,0,319,321,3,93,46,0,320,318,
        1,0,0,0,320,319,1,0,0,0,321,96,1,0,0,0,322,326,5,46,0,0,323,325,
        3,95,47,0,324,323,1,0,0,0,325,328,1,0,0,0,326,324,1,0,0,0,326,327,
        1,0,0,0,327,98,1,0,0,0,328,326,1,0,0,0,329,331,7,3,0,0,330,332,7,
        4,0,0,331,330,1,0,0,0,331,332,1,0,0,0,332,333,1,0,0,0,333,337,3,
        93,46,0,334,336,3,95,47,0,335,334,1,0,0,0,336,339,1,0,0,0,337,335,
        1,0,0,0,337,338,1,0,0,0,338,100,1,0,0,0,339,337,1,0,0,0,340,344,
        3,93,46,0,341,343,3,95,47,0,342,341,1,0,0,0,343,346,1,0,0,0,344,
        342,1,0,0,0,344,345,1,0,0,0,345,350,1,0,0,0,346,344,1,0,0,0,347,
        349,3,97,48,0,348,347,1,0,0,0,349,352,1,0,0,0,350,348,1,0,0,0,350,
        351,1,0,0,0,351,356,1,0,0,0,352,350,1,0,0,0,353,355,3,99,49,0,354,
        353,1,0,0,0,355,358,1,0,0,0,356,354,1,0,0,0,356,357,1,0,0,0,357,
        361,1,0,0,0,358,356,1,0,0,0,359,361,3,91,45,0,360,340,1,0,0,0,360,
        359,1,0,0,0,361,102,1,0,0,0,362,363,8,5,0,0,363,104,1,0,0,0,364,
        365,9,0,0,0,365,366,7,6,0,0,366,106,1,0,0,0,367,368,9,0,0,0,368,
        369,3,105,52,0,369,370,8,7,0,0,370,108,1,0,0,0,371,372,7,8,0,0,372,
        373,7,7,0,0,373,110,1,0,0,0,374,378,3,107,53,0,375,378,3,109,54,
        0,376,378,3,103,51,0,377,374,1,0,0,0,377,375,1,0,0,0,377,376,1,0,
        0,0,378,112,1,0,0,0,379,383,7,7,0,0,380,382,3,111,55,0,381,380,1,
        0,0,0,382,385,1,0,0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,386,1,
        0,0,0,385,383,1,0,0,0,386,387,7,7,0,0,387,388,6,56,0,0,388,114,1,
        0,0,0,389,390,5,35,0,0,390,391,5,35,0,0,391,116,1,0,0,0,392,396,
        3,115,57,0,393,395,3,123,61,0,394,393,1,0,0,0,395,398,1,0,0,0,396,
        394,1,0,0,0,396,397,1,0,0,0,397,399,1,0,0,0,398,396,1,0,0,0,399,
        400,6,58,1,0,400,118,1,0,0,0,401,403,7,9,0,0,402,401,1,0,0,0,403,
        404,1,0,0,0,404,402,1,0,0,0,404,405,1,0,0,0,405,406,1,0,0,0,406,
        407,6,59,1,0,407,120,1,0,0,0,408,409,5,10,0,0,409,122,1,0,0,0,410,
        411,8,10,0,0,411,124,1,0,0,0,412,413,9,0,0,0,413,414,6,62,2,0,414,
        126,1,0,0,0,415,419,7,7,0,0,416,418,3,111,55,0,417,416,1,0,0,0,418,
        421,1,0,0,0,419,417,1,0,0,0,419,420,1,0,0,0,420,422,1,0,0,0,421,
        419,1,0,0,0,422,423,5,0,0,1,423,424,6,63,3,0,424,128,1,0,0,0,425,
        429,7,7,0,0,426,428,3,111,55,0,427,426,1,0,0,0,428,431,1,0,0,0,429,
        427,1,0,0,0,429,430,1,0,0,0,430,432,1,0,0,0,431,429,1,0,0,0,432,
        436,3,105,52,0,433,435,3,111,55,0,434,433,1,0,0,0,435,438,1,0,0,
        0,436,434,1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,436,1,0,0,
        0,439,440,7,7,0,0,440,441,6,64,4,0,441,130,1,0,0,0,19,0,138,306,
        311,320,326,331,337,344,350,356,360,377,383,396,404,419,429,436,
        5,1,56,0,6,0,0,1,62,1,1,63,2,1,64,3
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN_TOKEN = 1
    BOOL = 2
    KW_TRUE = 3
    KW_FALSE = 4
    KW_NUMBER = 5
    KW_BOOL = 6
    KW_STRING = 7
    KW_RETURN = 8
    KW_VAR = 9
    KW_DYNAMIC = 10
    KW_FUNC = 11
    KW_FOR = 12
    KW_UNTIL = 13
    KW_BY = 14
    KW_BREAK = 15
    KW_CONTINUE = 16
    KW_IF = 17
    KW_ELSE = 18
    KW_ELIF = 19
    KW_BEGIN = 20
    KW_END = 21
    OP_ADD = 22
    OP_SUBTRACT = 23
    OP_MULTI = 24
    OP_DIVIDE = 25
    OP_REMAINDER = 26
    OP_NOT = 27
    OP_AND = 28
    OP_OR = 29
    OP_EQUAL = 30
    OP_LEFT_ARROW = 31
    OP_NOT_EQUAL = 32
    OP_SMALLER = 33
    OP_GREATER = 34
    OP_SMALLER_EQUAL = 35
    OP_GREATER_EQUAL = 36
    OP_EQUAL_COMPARE = 37
    OP_TRIPLE_DOT = 38
    SEP_OPEN_PAREN = 39
    SEP_CLOSE_PAREN = 40
    SEP_OPEN_BRACK = 41
    SEP_CLOSE_BRACK = 42
    SEP_COMA = 43
    IDENTIFIER = 44
    NUMBER = 45
    STRING = 46
    COMMENT = 47
    WS = 48
    NEW_LINE = 49
    ERROR_CHAR = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52

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
            "MAIN_TOKEN", "BOOL", "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", 
            "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", 
            "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", 
            "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", "OP_SUBTRACT", 
            "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", "OP_NOT", "OP_AND", 
            "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", "OP_NOT_EQUAL", "OP_SMALLER", 
            "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", "OP_EQUAL_COMPARE", 
            "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", 
            "SEP_CLOSE_BRACK", "SEP_COMA", "IDENTIFIER", "NUMBER", "STRING", 
            "COMMENT", "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "MAIN_TOKEN", "BOOL", "KW_TRUE", "KW_FALSE", "KW_NUMBER", 
                  "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                  "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                  "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                  "KW_END", "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", 
                  "OP_REMAINDER", "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", 
                  "OP_LEFT_ARROW", "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", 
                  "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", "OP_EQUAL_COMPARE", 
                  "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
                  "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "IDENTIFIER_HEAD", 
                  "IDENTIFIER", "ZERO", "NON_ZERO_DIGIT", "DIGIT", "FLOATING_POINT", 
                  "EXPONENTIAL", "NUMBER", "STRING_CHAR", "ESCAPE_SIGN", 
                  "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", 
                  "STRING", "COMMENT_HEAD", "COMMENT", "WS", "NEW_LINE", 
                  "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[56] = self.STRING_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
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
     


