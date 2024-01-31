# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,583,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,1,0,1,0,5,0,167,8,0,10,0,12,0,170,
        9,0,1,0,5,0,173,8,0,10,0,12,0,176,9,0,1,0,1,0,5,0,180,8,0,10,0,12,
        0,183,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,
        3,1,3,3,3,200,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,208,8,4,1,5,1,5,5,
        5,212,8,5,10,5,12,5,215,9,5,1,6,1,6,1,6,3,6,220,8,6,1,7,1,7,3,7,
        224,8,7,1,7,1,7,1,8,1,8,3,8,230,8,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,247,8,11,1,12,1,12,
        1,13,1,13,1,14,1,14,3,14,255,8,14,1,15,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,3,17,265,8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,3,19,277,8,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,3,22,289,8,22,1,23,1,23,1,23,1,23,1,24,1,24,1,25,1,25,
        1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,3,28,310,
        8,28,1,29,1,29,3,29,314,8,29,1,30,1,30,1,30,1,31,1,31,1,31,3,31,
        322,8,31,1,32,1,32,3,32,326,8,32,1,33,1,33,1,33,1,33,1,34,1,34,1,
        34,1,35,1,35,1,35,1,35,1,35,3,35,340,8,35,1,36,1,36,1,36,1,36,1,
        36,3,36,347,8,36,1,37,1,37,3,37,351,8,37,1,38,1,38,1,38,1,38,1,39,
        1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,5,41,368,8,41,
        10,41,12,41,371,9,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,
        381,8,42,1,43,1,43,1,43,1,43,1,43,3,43,388,8,43,1,44,1,44,1,45,1,
        45,1,45,1,45,1,45,3,45,397,8,45,1,46,1,46,1,47,1,47,1,47,1,47,1,
        47,1,47,1,47,5,47,408,8,47,10,47,12,47,411,9,47,1,48,1,48,1,49,1,
        49,1,49,1,49,1,49,1,49,1,49,5,49,422,8,49,10,49,12,49,425,9,49,1,
        50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,5,51,436,8,51,10,51,12,
        51,439,9,51,1,52,1,52,1,53,1,53,1,53,1,53,3,53,447,8,53,1,54,1,54,
        1,55,1,55,1,55,3,55,454,8,55,1,56,1,56,1,56,1,56,3,56,460,8,56,1,
        57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,3,58,470,8,58,1,59,1,59,1,
        59,1,59,1,59,1,59,3,59,478,8,59,1,60,1,60,3,60,482,8,60,1,61,1,61,
        1,61,1,61,5,61,488,8,61,10,61,12,61,491,9,61,1,61,1,61,1,61,1,61,
        3,61,497,8,61,1,62,1,62,1,62,1,62,1,62,1,63,1,63,1,63,1,63,1,63,
        1,64,1,64,1,64,1,64,1,65,1,65,1,65,1,65,1,66,1,66,1,66,1,66,1,66,
        1,66,1,67,1,67,1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,71,
        1,71,1,72,1,72,1,72,3,72,539,8,72,1,73,1,73,1,73,1,73,1,74,1,74,
        1,74,1,74,3,74,549,8,74,1,75,1,75,1,75,1,75,1,75,3,75,556,8,75,1,
        76,1,76,1,76,1,77,1,77,1,77,1,77,1,77,1,77,1,78,1,78,1,78,3,78,570,
        8,78,1,79,1,79,1,80,1,80,3,80,576,8,80,1,81,4,81,579,8,81,11,81,
        12,81,580,1,81,0,3,94,98,102,82,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,
        110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,
        142,144,146,148,150,152,154,156,158,160,162,0,7,1,0,4,6,1,0,8,9,
        2,0,29,29,31,36,1,0,27,28,1,0,21,22,1,0,23,25,1,0,2,3,557,0,164,
        1,0,0,0,2,186,1,0,0,0,4,194,1,0,0,0,6,199,1,0,0,0,8,207,1,0,0,0,
        10,213,1,0,0,0,12,219,1,0,0,0,14,223,1,0,0,0,16,229,1,0,0,0,18,233,
        1,0,0,0,20,236,1,0,0,0,22,246,1,0,0,0,24,248,1,0,0,0,26,250,1,0,
        0,0,28,254,1,0,0,0,30,256,1,0,0,0,32,259,1,0,0,0,34,264,1,0,0,0,
        36,266,1,0,0,0,38,276,1,0,0,0,40,278,1,0,0,0,42,281,1,0,0,0,44,288,
        1,0,0,0,46,290,1,0,0,0,48,294,1,0,0,0,50,296,1,0,0,0,52,299,1,0,
        0,0,54,302,1,0,0,0,56,306,1,0,0,0,58,313,1,0,0,0,60,315,1,0,0,0,
        62,321,1,0,0,0,64,325,1,0,0,0,66,327,1,0,0,0,68,331,1,0,0,0,70,339,
        1,0,0,0,72,346,1,0,0,0,74,350,1,0,0,0,76,352,1,0,0,0,78,356,1,0,
        0,0,80,362,1,0,0,0,82,369,1,0,0,0,84,380,1,0,0,0,86,387,1,0,0,0,
        88,389,1,0,0,0,90,396,1,0,0,0,92,398,1,0,0,0,94,400,1,0,0,0,96,412,
        1,0,0,0,98,414,1,0,0,0,100,426,1,0,0,0,102,428,1,0,0,0,104,440,1,
        0,0,0,106,446,1,0,0,0,108,448,1,0,0,0,110,453,1,0,0,0,112,459,1,
        0,0,0,114,461,1,0,0,0,116,465,1,0,0,0,118,477,1,0,0,0,120,481,1,
        0,0,0,122,483,1,0,0,0,124,498,1,0,0,0,126,503,1,0,0,0,128,508,1,
        0,0,0,130,512,1,0,0,0,132,516,1,0,0,0,134,522,1,0,0,0,136,525,1,
        0,0,0,138,528,1,0,0,0,140,531,1,0,0,0,142,533,1,0,0,0,144,535,1,
        0,0,0,146,540,1,0,0,0,148,548,1,0,0,0,150,555,1,0,0,0,152,557,1,
        0,0,0,154,560,1,0,0,0,156,569,1,0,0,0,158,571,1,0,0,0,160,575,1,
        0,0,0,162,578,1,0,0,0,164,168,3,160,80,0,165,167,3,4,2,0,166,165,
        1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,174,
        1,0,0,0,170,168,1,0,0,0,171,173,3,6,3,0,172,171,1,0,0,0,173,176,
        1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,177,1,0,0,0,176,174,
        1,0,0,0,177,181,3,2,1,0,178,180,3,6,3,0,179,178,1,0,0,0,180,183,
        1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,181,
        1,0,0,0,184,185,5,0,0,1,185,1,1,0,0,0,186,187,5,10,0,0,187,188,5,
        1,0,0,188,189,5,38,0,0,189,190,5,39,0,0,190,191,3,160,80,0,191,192,
        3,154,77,0,192,193,3,160,80,0,193,3,1,0,0,0,194,195,3,80,40,0,195,
        196,3,162,81,0,196,5,1,0,0,0,197,200,3,78,39,0,198,200,3,14,7,0,
        199,197,1,0,0,0,199,198,1,0,0,0,200,7,1,0,0,0,201,202,3,154,77,0,
        202,203,3,162,81,0,203,208,1,0,0,0,204,205,3,144,72,0,205,206,3,
        162,81,0,206,208,1,0,0,0,207,201,1,0,0,0,207,204,1,0,0,0,208,9,1,
        0,0,0,209,212,3,12,6,0,210,212,3,20,10,0,211,209,1,0,0,0,211,210,
        1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,11,1,
        0,0,0,215,213,1,0,0,0,216,220,3,14,7,0,217,220,3,16,8,0,218,220,
        3,18,9,0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,13,
        1,0,0,0,221,224,3,28,14,0,222,224,3,48,24,0,223,221,1,0,0,0,223,
        222,1,0,0,0,224,225,1,0,0,0,225,226,3,162,81,0,226,15,1,0,0,0,227,
        230,3,40,20,0,228,230,3,68,34,0,229,227,1,0,0,0,229,228,1,0,0,0,
        230,231,1,0,0,0,231,232,3,162,81,0,232,17,1,0,0,0,233,234,3,84,42,
        0,234,235,3,162,81,0,235,19,1,0,0,0,236,237,3,22,11,0,237,238,3,
        162,81,0,238,21,1,0,0,0,239,247,3,122,61,0,240,247,3,132,66,0,241,
        247,3,140,70,0,242,247,3,142,71,0,243,247,3,144,72,0,244,247,3,154,
        77,0,245,247,3,152,76,0,246,239,1,0,0,0,246,240,1,0,0,0,246,241,
        1,0,0,0,246,242,1,0,0,0,246,243,1,0,0,0,246,244,1,0,0,0,246,245,
        1,0,0,0,247,23,1,0,0,0,248,249,7,0,0,0,249,25,1,0,0,0,250,251,7,
        1,0,0,251,27,1,0,0,0,252,255,3,36,18,0,253,255,3,38,19,0,254,252,
        1,0,0,0,254,253,1,0,0,0,255,29,1,0,0,0,256,257,3,24,12,0,257,258,
        5,43,0,0,258,31,1,0,0,0,259,260,5,30,0,0,260,261,3,84,42,0,261,33,
        1,0,0,0,262,265,3,32,16,0,263,265,1,0,0,0,264,262,1,0,0,0,264,263,
        1,0,0,0,265,35,1,0,0,0,266,267,3,24,12,0,267,268,5,43,0,0,268,269,
        3,34,17,0,269,37,1,0,0,0,270,271,5,8,0,0,271,272,5,43,0,0,272,277,
        3,32,16,0,273,274,5,9,0,0,274,275,5,43,0,0,275,277,3,34,17,0,276,
        270,1,0,0,0,276,273,1,0,0,0,277,39,1,0,0,0,278,279,5,43,0,0,279,
        280,3,32,16,0,280,41,1,0,0,0,281,282,5,44,0,0,282,283,3,44,22,0,
        283,43,1,0,0,0,284,285,5,42,0,0,285,286,5,44,0,0,286,289,3,44,22,
        0,287,289,1,0,0,0,288,284,1,0,0,0,288,287,1,0,0,0,289,45,1,0,0,0,
        290,291,5,40,0,0,291,292,3,42,21,0,292,293,5,41,0,0,293,47,1,0,0,
        0,294,295,3,54,27,0,295,49,1,0,0,0,296,297,3,24,12,0,297,298,3,52,
        26,0,298,51,1,0,0,0,299,300,5,43,0,0,300,301,3,46,23,0,301,53,1,
        0,0,0,302,303,3,24,12,0,303,304,3,52,26,0,304,305,3,58,29,0,305,
        55,1,0,0,0,306,309,5,30,0,0,307,310,5,43,0,0,308,310,3,66,33,0,309,
        307,1,0,0,0,309,308,1,0,0,0,310,57,1,0,0,0,311,314,3,56,28,0,312,
        314,1,0,0,0,313,311,1,0,0,0,313,312,1,0,0,0,314,59,1,0,0,0,315,316,
        3,64,32,0,316,317,3,62,31,0,317,61,1,0,0,0,318,319,5,42,0,0,319,
        322,3,60,30,0,320,322,1,0,0,0,321,318,1,0,0,0,321,320,1,0,0,0,322,
        63,1,0,0,0,323,326,3,66,33,0,324,326,3,84,42,0,325,323,1,0,0,0,325,
        324,1,0,0,0,326,65,1,0,0,0,327,328,5,40,0,0,328,329,3,60,30,0,329,
        330,5,41,0,0,330,67,1,0,0,0,331,332,5,43,0,0,332,333,3,56,28,0,333,
        69,1,0,0,0,334,335,3,74,37,0,335,336,3,160,80,0,336,337,3,72,36,
        0,337,340,1,0,0,0,338,340,1,0,0,0,339,334,1,0,0,0,339,338,1,0,0,
        0,340,71,1,0,0,0,341,342,5,42,0,0,342,343,3,74,37,0,343,344,3,72,
        36,0,344,347,1,0,0,0,345,347,1,0,0,0,346,341,1,0,0,0,346,345,1,0,
        0,0,347,73,1,0,0,0,348,351,3,50,25,0,349,351,3,30,15,0,350,348,1,
        0,0,0,350,349,1,0,0,0,351,75,1,0,0,0,352,353,5,38,0,0,353,354,3,
        70,35,0,354,355,5,39,0,0,355,77,1,0,0,0,356,357,5,10,0,0,357,358,
        5,43,0,0,358,359,3,76,38,0,359,360,3,160,80,0,360,361,3,8,4,0,361,
        79,1,0,0,0,362,363,5,10,0,0,363,364,5,43,0,0,364,365,3,76,38,0,365,
        81,1,0,0,0,366,368,3,84,42,0,367,366,1,0,0,0,368,371,1,0,0,0,369,
        367,1,0,0,0,369,370,1,0,0,0,370,83,1,0,0,0,371,369,1,0,0,0,372,381,
        3,86,43,0,373,381,3,90,45,0,374,381,3,94,47,0,375,381,3,98,49,0,
        376,381,3,102,51,0,377,381,3,106,53,0,378,381,3,118,59,0,379,381,
        3,112,56,0,380,372,1,0,0,0,380,373,1,0,0,0,380,374,1,0,0,0,380,375,
        1,0,0,0,380,376,1,0,0,0,380,377,1,0,0,0,380,378,1,0,0,0,380,379,
        1,0,0,0,381,85,1,0,0,0,382,383,3,90,45,0,383,384,3,88,44,0,384,385,
        3,90,45,0,385,388,1,0,0,0,386,388,3,90,45,0,387,382,1,0,0,0,387,
        386,1,0,0,0,388,87,1,0,0,0,389,390,5,37,0,0,390,89,1,0,0,0,391,392,
        3,94,47,0,392,393,3,92,46,0,393,394,3,94,47,0,394,397,1,0,0,0,395,
        397,3,94,47,0,396,391,1,0,0,0,396,395,1,0,0,0,397,91,1,0,0,0,398,
        399,7,2,0,0,399,93,1,0,0,0,400,401,6,47,-1,0,401,402,3,98,49,0,402,
        409,1,0,0,0,403,404,10,2,0,0,404,405,3,96,48,0,405,406,3,98,49,0,
        406,408,1,0,0,0,407,403,1,0,0,0,408,411,1,0,0,0,409,407,1,0,0,0,
        409,410,1,0,0,0,410,95,1,0,0,0,411,409,1,0,0,0,412,413,7,3,0,0,413,
        97,1,0,0,0,414,415,6,49,-1,0,415,416,3,102,51,0,416,423,1,0,0,0,
        417,418,10,2,0,0,418,419,3,100,50,0,419,420,3,102,51,0,420,422,1,
        0,0,0,421,417,1,0,0,0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,1,
        0,0,0,424,99,1,0,0,0,425,423,1,0,0,0,426,427,7,4,0,0,427,101,1,0,
        0,0,428,429,6,51,-1,0,429,430,3,106,53,0,430,437,1,0,0,0,431,432,
        10,2,0,0,432,433,3,104,52,0,433,434,3,106,53,0,434,436,1,0,0,0,435,
        431,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,
        103,1,0,0,0,439,437,1,0,0,0,440,441,7,5,0,0,441,105,1,0,0,0,442,
        443,3,108,54,0,443,444,3,106,53,0,444,447,1,0,0,0,445,447,3,110,
        55,0,446,442,1,0,0,0,446,445,1,0,0,0,447,107,1,0,0,0,448,449,5,26,
        0,0,449,109,1,0,0,0,450,451,5,22,0,0,451,454,3,110,55,0,452,454,
        3,112,56,0,453,450,1,0,0,0,453,452,1,0,0,0,454,111,1,0,0,0,455,456,
        3,120,60,0,456,457,3,114,57,0,457,460,1,0,0,0,458,460,3,118,59,0,
        459,455,1,0,0,0,459,458,1,0,0,0,460,113,1,0,0,0,461,462,5,40,0,0,
        462,463,3,116,58,0,463,464,5,41,0,0,464,115,1,0,0,0,465,469,3,84,
        42,0,466,467,5,42,0,0,467,470,3,116,58,0,468,470,1,0,0,0,469,466,
        1,0,0,0,469,468,1,0,0,0,470,117,1,0,0,0,471,472,5,38,0,0,472,473,
        3,84,42,0,473,474,5,39,0,0,474,478,1,0,0,0,475,478,3,156,78,0,476,
        478,3,120,60,0,477,471,1,0,0,0,477,475,1,0,0,0,477,476,1,0,0,0,478,
        119,1,0,0,0,479,482,5,43,0,0,480,482,3,152,76,0,481,479,1,0,0,0,
        481,480,1,0,0,0,482,121,1,0,0,0,483,489,3,124,62,0,484,485,3,162,
        81,0,485,486,3,126,63,0,486,488,1,0,0,0,487,484,1,0,0,0,488,491,
        1,0,0,0,489,487,1,0,0,0,489,490,1,0,0,0,490,496,1,0,0,0,491,489,
        1,0,0,0,492,493,3,162,81,0,493,494,3,128,64,0,494,497,1,0,0,0,495,
        497,1,0,0,0,496,492,1,0,0,0,496,495,1,0,0,0,497,123,1,0,0,0,498,
        499,5,16,0,0,499,500,3,130,65,0,500,501,3,160,80,0,501,502,3,22,
        11,0,502,125,1,0,0,0,503,504,5,18,0,0,504,505,3,130,65,0,505,506,
        3,160,80,0,506,507,3,22,11,0,507,127,1,0,0,0,508,509,5,17,0,0,509,
        510,3,160,80,0,510,511,3,22,11,0,511,129,1,0,0,0,512,513,5,38,0,
        0,513,514,3,84,42,0,514,515,5,39,0,0,515,131,1,0,0,0,516,517,3,134,
        67,0,517,518,3,136,68,0,518,519,3,138,69,0,519,520,3,160,80,0,520,
        521,3,22,11,0,521,133,1,0,0,0,522,523,5,11,0,0,523,524,5,43,0,0,
        524,135,1,0,0,0,525,526,5,12,0,0,526,527,3,84,42,0,527,137,1,0,0,
        0,528,529,5,13,0,0,529,530,3,84,42,0,530,139,1,0,0,0,531,532,5,14,
        0,0,532,141,1,0,0,0,533,534,5,15,0,0,534,143,1,0,0,0,535,538,5,7,
        0,0,536,539,3,84,42,0,537,539,1,0,0,0,538,536,1,0,0,0,538,537,1,
        0,0,0,539,145,1,0,0,0,540,541,5,38,0,0,541,542,3,148,74,0,542,543,
        5,39,0,0,543,147,1,0,0,0,544,545,3,84,42,0,545,546,3,150,75,0,546,
        549,1,0,0,0,547,549,1,0,0,0,548,544,1,0,0,0,548,547,1,0,0,0,549,
        149,1,0,0,0,550,551,5,42,0,0,551,552,3,84,42,0,552,553,3,150,75,
        0,553,556,1,0,0,0,554,556,1,0,0,0,555,550,1,0,0,0,555,554,1,0,0,
        0,556,151,1,0,0,0,557,558,5,43,0,0,558,559,3,146,73,0,559,153,1,
        0,0,0,560,561,5,19,0,0,561,562,3,160,80,0,562,563,3,10,5,0,563,564,
        3,160,80,0,564,565,5,20,0,0,565,155,1,0,0,0,566,570,5,44,0,0,567,
        570,5,45,0,0,568,570,3,158,79,0,569,566,1,0,0,0,569,567,1,0,0,0,
        569,568,1,0,0,0,570,157,1,0,0,0,571,572,7,6,0,0,572,159,1,0,0,0,
        573,576,3,162,81,0,574,576,1,0,0,0,575,573,1,0,0,0,575,574,1,0,0,
        0,576,161,1,0,0,0,577,579,5,48,0,0,578,577,1,0,0,0,579,580,1,0,0,
        0,580,578,1,0,0,0,580,581,1,0,0,0,581,163,1,0,0,0,43,168,174,181,
        199,207,211,213,219,223,229,246,254,264,276,288,309,313,321,325,
        339,346,350,369,380,387,396,409,423,437,446,453,459,469,477,481,
        489,496,538,548,555,569,575,580
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'...'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "MAIN_TOKEN", "KW_TRUE", "KW_FALSE", 
                      "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", 
                      "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", 
                      "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", "KW_ELSE", 
                      "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", "OP_SUBTRACT", 
                      "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", "OP_NOT", 
                      "OP_AND", "OP_OR", "OP_EQUAL", "OP_ASSIGN", "OP_NOT_EQUAL", 
                      "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", 
                      "OP_STRING_EQUAL", "OP_STRING_CONCAT", "SEP_OPEN_PAREN", 
                      "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", 
                      "SEP_COMA", "IDENTIFIER", "NUMBER", "STRING", "COMMENT", 
                      "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_main_def = 1
    RULE_forward_func = 2
    RULE_define = 3
    RULE_inner_scope = 4
    RULE_lines = 5
    RULE_line = 6
    RULE_def_line = 7
    RULE_assign_line = 8
    RULE_expr_line = 9
    RULE_statement_line = 10
    RULE_statement = 11
    RULE_type_def = 12
    RULE_implicit_type_def = 13
    RULE_var_def = 14
    RULE_var_def_for_param = 15
    RULE_value_init = 16
    RULE_optional_val_init = 17
    RULE_static_var_def = 18
    RULE_dynamic_var_def = 19
    RULE_var_assign = 20
    RULE_dim_list = 21
    RULE_dim_list_tail = 22
    RULE_array_dim = 23
    RULE_array_def = 24
    RULE_array_def_for_param = 25
    RULE_array_identifier = 26
    RULE_array_static_def = 27
    RULE_array_init = 28
    RULE_optional_array_init = 29
    RULE_array_value_init_list = 30
    RULE_array_value_init_tail = 31
    RULE_array_value = 32
    RULE_array_value_init = 33
    RULE_array_assign = 34
    RULE_param_def_list = 35
    RULE_param_def_list_tail = 36
    RULE_param = 37
    RULE_param_def = 38
    RULE_func_def = 39
    RULE_forward_func_def = 40
    RULE_expressions = 41
    RULE_expression = 42
    RULE_string_expr = 43
    RULE_string_op = 44
    RULE_relation_expr = 45
    RULE_relational_op = 46
    RULE_logic_expr = 47
    RULE_logic_op = 48
    RULE_add_expr = 49
    RULE_add_op = 50
    RULE_multi_expr = 51
    RULE_multi_op = 52
    RULE_negate_expr = 53
    RULE_negate_op = 54
    RULE_sign_expr = 55
    RULE_array_expr = 56
    RULE_indexer = 57
    RULE_index_op = 58
    RULE_primary_expression = 59
    RULE_term = 60
    RULE_if_statement = 61
    RULE_if_clause = 62
    RULE_elif_clause = 63
    RULE_else_clause = 64
    RULE_if_condition = 65
    RULE_for_statement = 66
    RULE_for_clause = 67
    RULE_condition_clause = 68
    RULE_update_clause = 69
    RULE_break_statement = 70
    RULE_continue_statement = 71
    RULE_return_statement = 72
    RULE_passing_arg = 73
    RULE_passing_list = 74
    RULE_passing_list_tail = 75
    RULE_func_call = 76
    RULE_block_statement = 77
    RULE_literal = 78
    RULE_boolean = 79
    RULE_optional_end_line = 80
    RULE_end_line = 81

    ruleNames =  [ "program", "main_def", "forward_func", "define", "inner_scope", 
                   "lines", "line", "def_line", "assign_line", "expr_line", 
                   "statement_line", "statement", "type_def", "implicit_type_def", 
                   "var_def", "var_def_for_param", "value_init", "optional_val_init", 
                   "static_var_def", "dynamic_var_def", "var_assign", "dim_list", 
                   "dim_list_tail", "array_dim", "array_def", "array_def_for_param", 
                   "array_identifier", "array_static_def", "array_init", 
                   "optional_array_init", "array_value_init_list", "array_value_init_tail", 
                   "array_value", "array_value_init", "array_assign", "param_def_list", 
                   "param_def_list_tail", "param", "param_def", "func_def", 
                   "forward_func_def", "expressions", "expression", "string_expr", 
                   "string_op", "relation_expr", "relational_op", "logic_expr", 
                   "logic_op", "add_expr", "add_op", "multi_expr", "multi_op", 
                   "negate_expr", "negate_op", "sign_expr", "array_expr", 
                   "indexer", "index_op", "primary_expression", "term", 
                   "if_statement", "if_clause", "elif_clause", "else_clause", 
                   "if_condition", "for_statement", "for_clause", "condition_clause", 
                   "update_clause", "break_statement", "continue_statement", 
                   "return_statement", "passing_arg", "passing_list", "passing_list_tail", 
                   "func_call", "block_statement", "literal", "boolean", 
                   "optional_end_line", "end_line" ]

    EOF = Token.EOF
    MAIN_TOKEN=1
    KW_TRUE=2
    KW_FALSE=3
    KW_NUMBER=4
    KW_BOOL=5
    KW_STRING=6
    KW_RETURN=7
    KW_VAR=8
    KW_DYNAMIC=9
    KW_FUNC=10
    KW_FOR=11
    KW_UNTIL=12
    KW_BY=13
    KW_BREAK=14
    KW_CONTINUE=15
    KW_IF=16
    KW_ELSE=17
    KW_ELIF=18
    KW_BEGIN=19
    KW_END=20
    OP_ADD=21
    OP_SUBTRACT=22
    OP_MULTI=23
    OP_DIVIDE=24
    OP_REMAINDER=25
    OP_NOT=26
    OP_AND=27
    OP_OR=28
    OP_EQUAL=29
    OP_ASSIGN=30
    OP_NOT_EQUAL=31
    OP_SMALLER=32
    OP_GREATER=33
    OP_SMALLER_EQUAL=34
    OP_GREATER_EQUAL=35
    OP_STRING_EQUAL=36
    OP_STRING_CONCAT=37
    SEP_OPEN_PAREN=38
    SEP_CLOSE_PAREN=39
    SEP_OPEN_BRACK=40
    SEP_CLOSE_BRACK=41
    SEP_COMA=42
    IDENTIFIER=43
    NUMBER=44
    STRING=45
    COMMENT=46
    WS=47
    NEW_LINE=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def main_def(self):
            return self.getTypedRuleContext(ZCodeParser.Main_defContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def forward_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Forward_funcContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Forward_funcContext,i)


        def define(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DefineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DefineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.optional_end_line()
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.forward_func() 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 171
                    self.define() 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 177
            self.main_def()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1904) != 0):
                self.state = 178
                self.define()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def MAIN_TOKEN(self):
            return self.getToken(ZCodeParser.MAIN_TOKEN, 0)

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def SEP_CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_PAREN, 0)

        def optional_end_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Optional_end_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,i)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_def




    def main_def(self):

        localctx = ZCodeParser.Main_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ZCodeParser.KW_FUNC)
            self.state = 187
            self.match(ZCodeParser.MAIN_TOKEN)
            self.state = 188
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 189
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
            self.state = 190
            self.optional_end_line()
            self.state = 191
            self.block_statement()
            self.state = 192
            self.optional_end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forward_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forward_func_def(self):
            return self.getTypedRuleContext(ZCodeParser.Forward_func_defContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forward_func




    def forward_func(self):

        localctx = ZCodeParser.Forward_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forward_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.forward_func_def()
            self.state = 195
            self.end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_def(self):
            return self.getTypedRuleContext(ZCodeParser.Func_defContext,0)


        def def_line(self):
            return self.getTypedRuleContext(ZCodeParser.Def_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_define




    def define(self):

        localctx = ZCodeParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_define)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.func_def()
                pass
            elif token in [4, 5, 6, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.def_line()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inner_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_inner_scope




    def inner_scope(self):

        localctx = ZCodeParser.Inner_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inner_scope)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.block_statement()
                self.state = 202
                self.end_line()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.return_statement()
                self.state = 205
                self.end_line()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LineContext,i)


        def statement_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Statement_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Statement_lineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lines




    def lines(self):

        localctx = ZCodeParser.LinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lines)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 61847601007612) != 0):
                self.state = 211
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 209
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 210
                    self.statement_line()
                    pass


                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def def_line(self):
            return self.getTypedRuleContext(ZCodeParser.Def_lineContext,0)


        def assign_line(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_lineContext,0)


        def expr_line(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_line




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_line)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.def_line()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.assign_line()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.expr_line()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Def_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def var_def(self):
            return self.getTypedRuleContext(ZCodeParser.Var_defContext,0)


        def array_def(self):
            return self.getTypedRuleContext(ZCodeParser.Array_defContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_def_line




    def def_line(self):

        localctx = ZCodeParser.Def_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_def_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 221
                self.var_def()
                pass

            elif la_ == 2:
                self.state = 222
                self.array_def()
                pass


            self.state = 225
            self.end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(ZCodeParser.Var_assignContext,0)


        def array_assign(self):
            return self.getTypedRuleContext(ZCodeParser.Array_assignContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_line




    def assign_line(self):

        localctx = ZCodeParser.Assign_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 227
                self.var_assign()
                pass

            elif la_ == 2:
                self.state = 228
                self.array_assign()
                pass


            self.state = 231
            self.end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_line




    def expr_line(self):

        localctx = ZCodeParser.Expr_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expression()
            self.state = 234
            self.end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_line




    def statement_line(self):

        localctx = ZCodeParser.Statement_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.statement()
            self.state = 237
            self.end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 239
                self.if_statement()
                pass
            elif token in [11]:
                self.state = 240
                self.for_statement()
                pass
            elif token in [14]:
                self.state = 241
                self.break_statement()
                pass
            elif token in [15]:
                self.state = 242
                self.continue_statement()
                pass
            elif token in [7]:
                self.state = 243
                self.return_statement()
                pass
            elif token in [19]:
                self.state = 244
                self.block_statement()
                pass
            elif token in [43]:
                self.state = 245
                self.func_call()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_def




    def type_def(self):

        localctx = ZCodeParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_type_def




    def implicit_type_def(self):

        localctx = ZCodeParser.Implicit_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_implicit_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_var_def(self):
            return self.getTypedRuleContext(ZCodeParser.Static_var_defContext,0)


        def dynamic_var_def(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_var_defContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_def




    def var_def(self):

        localctx = ZCodeParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_def)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.static_var_def()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.dynamic_var_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_def_for_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_def_for_param




    def var_def_for_param(self):

        localctx = ZCodeParser.Var_def_for_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_def_for_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.type_def()
            self.state = 257
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 260
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_val_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_val_init




    def optional_val_init(self):

        localctx = ZCodeParser.Optional_val_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_optional_val_init)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.value_init()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def optional_val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_static_var_def




    def static_var_def(self):

        localctx = ZCodeParser.Static_var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_static_var_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.type_def()
            self.state = 267
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 268
            self.optional_val_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def optional_val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_var_def




    def dynamic_var_def(self):

        localctx = ZCodeParser.Dynamic_var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dynamic_var_def)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(ZCodeParser.KW_VAR)
                self.state = 271
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 272
                self.value_init()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 274
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 275
                self.optional_val_init()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_assign




    def var_assign(self):

        localctx = ZCodeParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 279
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def dim_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dim_list




    def dim_list(self):

        localctx = ZCodeParser.Dim_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dim_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.NUMBER)
            self.state = 282
            self.dim_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def dim_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dim_list_tail




    def dim_list_tail(self):

        localctx = ZCodeParser.Dim_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_dim_list_tail)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(ZCodeParser.SEP_COMA)
                self.state = 285
                self.match(ZCodeParser.NUMBER)
                self.state = 286
                self.dim_list_tail()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_BRACK(self):
            return self.getToken(ZCodeParser.SEP_OPEN_BRACK, 0)

        def dim_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_listContext,0)


        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dim




    def array_dim(self):

        localctx = ZCodeParser.Array_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 291
            self.dim_list()
            self.state = 292
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_static_def(self):
            return self.getTypedRuleContext(ZCodeParser.Array_static_defContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_def




    def array_def(self):

        localctx = ZCodeParser.Array_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.array_static_def()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_def_for_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def array_identifier(self):
            return self.getTypedRuleContext(ZCodeParser.Array_identifierContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_def_for_param




    def array_def_for_param(self):

        localctx = ZCodeParser.Array_def_for_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_def_for_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.type_def()
            self.state = 297
            self.array_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dim(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_identifier




    def array_identifier(self):

        localctx = ZCodeParser.Array_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 300
            self.array_dim()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_static_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def array_identifier(self):
            return self.getTypedRuleContext(ZCodeParser.Array_identifierContext,0)


        def optional_array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_static_def




    def array_static_def(self):

        localctx = ZCodeParser.Array_static_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_static_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.type_def()
            self.state = 303
            self.array_identifier()
            self.state = 304
            self.optional_array_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.state = 307
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [40]:
                self.state = 308
                self.array_value_init()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_array_init




    def optional_array_init(self):

        localctx = ZCodeParser.Optional_array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_optional_array_init)
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.array_init()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_init_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def array_value_init_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_init_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init_list




    def array_value_init_list(self):

        localctx = ZCodeParser.Array_value_init_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_value_init_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.array_value()
            self.state = 316
            self.array_value_init_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_init_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def array_value_init_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_init_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init_tail




    def array_value_init_tail(self):

        localctx = ZCodeParser.Array_value_init_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_value_init_tail)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ZCodeParser.SEP_COMA)
                self.state = 319
                self.array_value_init_list()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_initContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 323
                self.array_value_init()
                pass
            elif token in [2, 3, 22, 26, 38, 43, 44, 45]:
                self.state = 324
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_BRACK(self):
            return self.getToken(ZCodeParser.SEP_OPEN_BRACK, 0)

        def array_value_init_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_init_listContext,0)


        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init




    def array_value_init(self):

        localctx = ZCodeParser.Array_value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_array_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 328
            self.array_value_init_list()
            self.state = 329
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_assign




    def array_assign(self):

        localctx = ZCodeParser.Array_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 332
            self.array_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_def_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def param_def_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list




    def param_def_list(self):

        localctx = ZCodeParser.Param_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_param_def_list)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.param()
                self.state = 335
                self.optional_end_line()
                self.state = 336
                self.param_def_list_tail()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_def_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def param_def_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list_tail




    def param_def_list_tail(self):

        localctx = ZCodeParser.Param_def_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_param_def_list_tail)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(ZCodeParser.SEP_COMA)
                self.state = 342
                self.param()
                self.state = 343
                self.param_def_list_tail()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_def_for_param(self):
            return self.getTypedRuleContext(ZCodeParser.Array_def_for_paramContext,0)


        def var_def_for_param(self):
            return self.getTypedRuleContext(ZCodeParser.Var_def_for_paramContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_param)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.array_def_for_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.var_def_for_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def param_def_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_listContext,0)


        def SEP_CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def




    def param_def(self):

        localctx = ZCodeParser.Param_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_param_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 353
            self.param_def_list()
            self.state = 354
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_def(self):
            return self.getTypedRuleContext(ZCodeParser.Param_defContext,0)


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def inner_scope(self):
            return self.getTypedRuleContext(ZCodeParser.Inner_scopeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_def




    def func_def(self):

        localctx = ZCodeParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ZCodeParser.KW_FUNC)
            self.state = 357
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 358
            self.param_def()
            self.state = 359
            self.optional_end_line()
            self.state = 360
            self.inner_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forward_func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_def(self):
            return self.getTypedRuleContext(ZCodeParser.Param_defContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forward_func_def




    def forward_func_def(self):

        localctx = ZCodeParser.Forward_func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forward_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.KW_FUNC)
            self.state = 363
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 364
            self.param_def()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expressions




    def expressions(self):

        localctx = ZCodeParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 61847600365580) != 0):
                self.state = 366
                self.expression()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self):
            return self.getTypedRuleContext(ZCodeParser.String_exprContext,0)


        def relation_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Relation_exprContext,0)


        def logic_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def multi_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_exprContext,0)


        def negate_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Negate_exprContext,0)


        def primary_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Primary_expressionContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expression)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.string_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.relation_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.logic_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.add_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
                self.multi_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 377
                self.negate_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 378
                self.primary_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 379
                self.array_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relation_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relation_exprContext,i)


        def string_op(self):
            return self.getTypedRuleContext(ZCodeParser.String_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_string_expr




    def string_expr(self):

        localctx = ZCodeParser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_string_expr)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.relation_expr()
                self.state = 383
                self.string_op()
                self.state = 384
                self.relation_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.relation_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_STRING_CONCAT(self):
            return self.getToken(ZCodeParser.OP_STRING_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_op




    def string_op(self):

        localctx = ZCodeParser.String_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_string_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ZCodeParser.OP_STRING_CONCAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logic_exprContext,i)


        def relational_op(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relation_expr




    def relation_expr(self):

        localctx = ZCodeParser.Relation_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_relation_expr)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.logic_expr(0)
                self.state = 392
                self.relational_op()
                self.state = 393
                self.logic_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.logic_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_GREATER(self):
            return self.getToken(ZCodeParser.OP_GREATER, 0)

        def OP_GREATER_EQUAL(self):
            return self.getToken(ZCodeParser.OP_GREATER_EQUAL, 0)

        def OP_EQUAL(self):
            return self.getToken(ZCodeParser.OP_EQUAL, 0)

        def OP_NOT_EQUAL(self):
            return self.getToken(ZCodeParser.OP_NOT_EQUAL, 0)

        def OP_SMALLER(self):
            return self.getToken(ZCodeParser.OP_SMALLER, 0)

        def OP_SMALLER_EQUAL(self):
            return self.getToken(ZCodeParser.OP_SMALLER_EQUAL, 0)

        def OP_STRING_EQUAL(self):
            return self.getToken(ZCodeParser.OP_STRING_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_op




    def relational_op(self):

        localctx = ZCodeParser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135828340736) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def logic_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_exprContext,0)


        def logic_op(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logic_expr



    def logic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    self.logic_op()
                    self.state = 405
                    self.add_expr(0) 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_AND(self):
            return self.getToken(ZCodeParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(ZCodeParser.OP_OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logic_op




    def logic_op(self):

        localctx = ZCodeParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multi_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def add_op(self):
            return self.getTypedRuleContext(ZCodeParser.Add_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_add_expr



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_add_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.multi_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 417
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 418
                    self.add_op()
                    self.state = 419
                    self.multi_expr(0) 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADD(self):
            return self.getToken(ZCodeParser.OP_ADD, 0)

        def OP_SUBTRACT(self):
            return self.getToken(ZCodeParser.OP_SUBTRACT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_op




    def add_op(self):

        localctx = ZCodeParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Negate_exprContext,0)


        def multi_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_exprContext,0)


        def multi_op(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_multi_expr



    def multi_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multi_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_multi_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.negate_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multi_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multi_expr)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 432
                    self.multi_op()
                    self.state = 433
                    self.negate_expr() 
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multi_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULTI(self):
            return self.getToken(ZCodeParser.OP_MULTI, 0)

        def OP_DIVIDE(self):
            return self.getToken(ZCodeParser.OP_DIVIDE, 0)

        def OP_REMAINDER(self):
            return self.getToken(ZCodeParser.OP_REMAINDER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multi_op




    def multi_op(self):

        localctx = ZCodeParser.Multi_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_multi_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Negate_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_op(self):
            return self.getTypedRuleContext(ZCodeParser.Negate_opContext,0)


        def negate_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Negate_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_negate_expr




    def negate_expr(self):

        localctx = ZCodeParser.Negate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_negate_expr)
        try:
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.negate_op()
                self.state = 443
                self.negate_expr()
                pass
            elif token in [2, 3, 22, 38, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Negate_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(ZCodeParser.OP_NOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_negate_op




    def negate_op(self):

        localctx = ZCodeParser.Negate_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_negate_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(ZCodeParser.OP_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def OP_SUBTRACT(self):
            return self.getToken(ZCodeParser.OP_SUBTRACT, 0)

        def array_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_sign_expr)
        try:
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(ZCodeParser.OP_SUBTRACT)
                self.state = 451
                self.sign_expr()
                pass
            elif token in [2, 3, 38, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.array_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def indexer(self):
            return self.getTypedRuleContext(ZCodeParser.IndexerContext,0)


        def primary_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Primary_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expr




    def array_expr(self):

        localctx = ZCodeParser.Array_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array_expr)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.term()
                self.state = 456
                self.indexer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.primary_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_BRACK(self):
            return self.getToken(ZCodeParser.SEP_OPEN_BRACK, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indexer




    def indexer(self):

        localctx = ZCodeParser.IndexerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_indexer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 462
            self.index_op()
            self.state = 463
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.expression()
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 466
                self.match(ZCodeParser.SEP_COMA)
                self.state = 467
                self.index_op()
                pass
            elif token in [41]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def SEP_CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_PAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_primary_expression




    def primary_expression(self):

        localctx = ZCodeParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_primary_expression)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(ZCodeParser.SEP_OPEN_PAREN)
                self.state = 472
                self.expression()
                self.state = 473
                self.match(ZCodeParser.SEP_CLOSE_PAREN)
                pass
            elif token in [2, 3, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.literal()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.term()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_term




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_term)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_clause(self):
            return self.getTypedRuleContext(ZCodeParser.If_clauseContext,0)


        def end_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.End_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.End_lineContext,i)


        def else_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Else_clauseContext,0)


        def elif_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_clauseContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_clauseContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.if_clause()
            self.state = 489
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 484
                    self.end_line()
                    self.state = 485
                    self.elif_clause() 
                self.state = 491
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 492
                self.end_line()
                self.state = 493
                self.else_clause()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(ZCodeParser.KW_IF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(ZCodeParser.If_conditionContext,0)


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_clause




    def if_clause(self):

        localctx = ZCodeParser.If_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_if_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(ZCodeParser.KW_IF)
            self.state = 499
            self.if_condition()
            self.state = 500
            self.optional_end_line()
            self.state = 501
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELIF(self):
            return self.getToken(ZCodeParser.KW_ELIF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(ZCodeParser.If_conditionContext,0)


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clause




    def elif_clause(self):

        localctx = ZCodeParser.Elif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_elif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(ZCodeParser.KW_ELIF)
            self.state = 504
            self.if_condition()
            self.state = 505
            self.optional_end_line()
            self.state = 506
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(ZCodeParser.KW_ELSE, 0)

        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_clause




    def else_clause(self):

        localctx = ZCodeParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(ZCodeParser.KW_ELSE)
            self.state = 509
            self.optional_end_line()
            self.state = 510
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def SEP_CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_condition




    def if_condition(self):

        localctx = ZCodeParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 513
            self.expression()
            self.state = 514
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_clause(self):
            return self.getTypedRuleContext(ZCodeParser.For_clauseContext,0)


        def condition_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_clauseContext,0)


        def update_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Update_clauseContext,0)


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.for_clause()
            self.state = 517
            self.condition_clause()
            self.state = 518
            self.update_clause()
            self.state = 519
            self.optional_end_line()
            self.state = 520
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(ZCodeParser.KW_FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_clause




    def for_clause(self):

        localctx = ZCodeParser.For_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_for_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(ZCodeParser.KW_FOR)
            self.state = 523
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_UNTIL(self):
            return self.getToken(ZCodeParser.KW_UNTIL, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_condition_clause




    def condition_clause(self):

        localctx = ZCodeParser.Condition_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_condition_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 526
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BY(self):
            return self.getToken(ZCodeParser.KW_BY, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_update_clause




    def update_clause(self):

        localctx = ZCodeParser.Update_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_update_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(ZCodeParser.KW_BY)
            self.state = 529
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(ZCodeParser.KW_BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(ZCodeParser.KW_BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONTINUE(self):
            return self.getToken(ZCodeParser.KW_CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(ZCodeParser.KW_CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(ZCodeParser.KW_RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(ZCodeParser.KW_RETURN)
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 22, 26, 38, 43, 44, 45]:
                self.state = 536
                self.expression()
                pass
            elif token in [48]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Passing_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def passing_list(self):
            return self.getTypedRuleContext(ZCodeParser.Passing_listContext,0)


        def SEP_CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_passing_arg




    def passing_arg(self):

        localctx = ZCodeParser.Passing_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_passing_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 541
            self.passing_list()
            self.state = 542
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Passing_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def passing_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Passing_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_passing_list




    def passing_list(self):

        localctx = ZCodeParser.Passing_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_passing_list)
        try:
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 22, 26, 38, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.expression()
                self.state = 545
                self.passing_list_tail()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Passing_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def passing_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Passing_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_passing_list_tail




    def passing_list_tail(self):

        localctx = ZCodeParser.Passing_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_passing_list_tail)
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.match(ZCodeParser.SEP_COMA)
                self.state = 551
                self.expression()
                self.state = 552
                self.passing_list_tail()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def passing_arg(self):
            return self.getTypedRuleContext(ZCodeParser.Passing_argContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 558
            self.passing_arg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BEGIN(self):
            return self.getToken(ZCodeParser.KW_BEGIN, 0)

        def optional_end_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Optional_end_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,i)


        def lines(self):
            return self.getTypedRuleContext(ZCodeParser.LinesContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 561
            self.optional_end_line()
            self.state = 562
            self.lines()
            self.state = 563
            self.optional_end_line()
            self.state = 564
            self.match(ZCodeParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def boolean(self):
            return self.getTypedRuleContext(ZCodeParser.BooleanContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_literal)
        try:
            self.state = 569
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.match(ZCodeParser.STRING)
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 568
                self.boolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TRUE(self):
            return self.getToken(ZCodeParser.KW_TRUE, 0)

        def KW_FALSE(self):
            return self.getToken(ZCodeParser.KW_FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean




    def boolean(self):

        localctx = ZCodeParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_end_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_end_line




    def optional_end_line(self):

        localctx = ZCodeParser.Optional_end_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_optional_end_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 573
                self.end_line()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_end_line




    def end_line(self):

        localctx = ZCodeParser.End_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_end_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 577
                    self.match(ZCodeParser.NEW_LINE)

                else:
                    raise NoViableAltException(self)
                self.state = 580 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[47] = self.logic_expr_sempred
        self._predicates[49] = self.add_expr_sempred
        self._predicates[51] = self.multi_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multi_expr_sempred(self, localctx:Multi_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




