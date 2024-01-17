# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01a6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3")
        buf.write("\6\3\u0087\n\3\r\3\16\3\u0088\3\3\7\3\u008c\n\3\f\3\16")
        buf.write("\3\u008f\13\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u0097\n\6\3")
        buf.write("\7\3\7\7\7\u009b\n\7\f\7\16\7\u009e\13\7\3\b\3\b\5\b\u00a2")
        buf.write("\n\b\3\b\3\b\7\b\u00a6\n\b\f\b\16\b\u00a9\13\b\3\t\3\t")
        buf.write("\7\t\u00ad\n\t\f\t\16\t\u00b0\13\t\3\t\7\t\u00b3\n\t\f")
        buf.write("\t\16\t\u00b6\13\t\3\t\7\t\u00b9\n\t\f\t\16\t\u00bc\13")
        buf.write("\t\3\t\5\t\u00bf\n\t\3\n\3\n\5\n\u00c3\n\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\5\17\u00d4\n\17\3\20\3\20\7\20\u00d8\n\20\f\20\16")
        buf.write("\20\u00db\13\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\7;\u0186\n")
        buf.write(";\f;\16;\u0189\13;\3;\3;\3<\6<\u018e\n<\r<\16<\u018f\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\7@\u019d\n@\f@\16@\u01a0")
        buf.write("\13@\3@\3@\3@\3A\3A\2\2B\3\2\5\3\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\4\23\5\25\2\27\2\31\2\33\2\35\2\37\6!\7#\b%\t\'\n")
        buf.write(")\13+\f-\r/\16\61\17\63\20\65\21\67\229\23;\24=\25?\26")
        buf.write("A\27C\30E\31G\32I\33K\34M\35O\36Q\37S U!W\"Y#[$]%_&a\'")
        buf.write("c(e)g*i+k,m-o.q/s\2u\60w\61y\62{\2}\63\177\64\u0081\65")
        buf.write("\3\2\r\5\2C\\aac|\5\2\62;C\\c|\3\2\63;\4\2GGgg\4\2--/")
        buf.write("/\7\2\n\f\16\17$$))^^\3\2^^\3\2$$\3\2))\5\2\n\13\16\17")
        buf.write("\"\"\3\2\f\f\2\u01a9\2\5\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0086\3\2\2\2\7\u0090")
        buf.write("\3\2\2\2\t\u0092\3\2\2\2\13\u0096\3\2\2\2\r\u0098\3\2")
        buf.write("\2\2\17\u009f\3\2\2\2\21\u00be\3\2\2\2\23\u00c2\3\2\2")
        buf.write("\2\25\u00c4\3\2\2\2\27\u00c6\3\2\2\2\31\u00c9\3\2\2\2")
        buf.write("\33\u00cd\3\2\2\2\35\u00d3\3\2\2\2\37\u00d5\3\2\2\2!\u00df")
        buf.write("\3\2\2\2#\u00e4\3\2\2\2%\u00ea\3\2\2\2\'\u00f1\3\2\2\2")
        buf.write(")\u00f6\3\2\2\2+\u00fd\3\2\2\2-\u0104\3\2\2\2/\u0108\3")
        buf.write("\2\2\2\61\u0110\3\2\2\2\63\u0115\3\2\2\2\65\u0119\3\2")
        buf.write("\2\2\67\u011f\3\2\2\29\u0122\3\2\2\2;\u0128\3\2\2\2=\u0131")
        buf.write("\3\2\2\2?\u0134\3\2\2\2A\u0139\3\2\2\2C\u013e\3\2\2\2")
        buf.write("E\u0144\3\2\2\2G\u0148\3\2\2\2I\u014a\3\2\2\2K\u014c\3")
        buf.write("\2\2\2M\u014e\3\2\2\2O\u0150\3\2\2\2Q\u0152\3\2\2\2S\u0156")
        buf.write("\3\2\2\2U\u015a\3\2\2\2W\u015d\3\2\2\2Y\u015f\3\2\2\2")
        buf.write("[\u0162\3\2\2\2]\u0165\3\2\2\2_\u0167\3\2\2\2a\u0169\3")
        buf.write("\2\2\2c\u016c\3\2\2\2e\u016f\3\2\2\2g\u0172\3\2\2\2i\u0176")
        buf.write("\3\2\2\2k\u0178\3\2\2\2m\u017a\3\2\2\2o\u017c\3\2\2\2")
        buf.write("q\u017e\3\2\2\2s\u0180\3\2\2\2u\u0183\3\2\2\2w\u018d\3")
        buf.write("\2\2\2y\u0193\3\2\2\2{\u0195\3\2\2\2}\u0197\3\2\2\2\177")
        buf.write("\u019a\3\2\2\2\u0081\u01a4\3\2\2\2\u0083\u0084\t\2\2\2")
        buf.write("\u0084\4\3\2\2\2\u0085\u0087\5\3\2\2\u0086\u0085\3\2\2")
        buf.write("\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008d\3\2\2\2\u008a\u008c\t\3\2\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\6\3\2\2\2\u008f\u008d\3\2\2")
        buf.write("\2\u0090\u0091\7\62\2\2\u0091\b\3\2\2\2\u0092\u0093\t")
        buf.write("\4\2\2\u0093\n\3\2\2\2\u0094\u0097\5\7\4\2\u0095\u0097")
        buf.write("\5\t\5\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\f\3\2\2\2\u0098\u009c\7\60\2\2\u0099\u009b\5\13\6\2\u009a")
        buf.write("\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2")
        buf.write("\u009c\u009d\3\2\2\2\u009d\16\3\2\2\2\u009e\u009c\3\2")
        buf.write("\2\2\u009f\u00a1\t\5\2\2\u00a0\u00a2\t\6\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a7\5\t\5\2\u00a4\u00a6\5\13\6\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\20\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ae")
        buf.write("\5\t\5\2\u00ab\u00ad\5\13\6\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b4\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b3\5")
        buf.write("\r\7\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00ba\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00b9\5\17\b\2\u00b8\u00b7\3\2\2")
        buf.write("\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bf\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd")
        buf.write("\u00bf\5\7\4\2\u00be\u00aa\3\2\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00bf\22\3\2\2\2\u00c0\u00c3\5!\21\2\u00c1\u00c3\5#\22")
        buf.write("\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\24\3")
        buf.write("\2\2\2\u00c4\u00c5\n\7\2\2\u00c5\26\3\2\2\2\u00c6\u00c7")
        buf.write("\13\2\2\2\u00c7\u00c8\t\b\2\2\u00c8\30\3\2\2\2\u00c9\u00ca")
        buf.write("\13\2\2\2\u00ca\u00cb\5\27\f\2\u00cb\u00cc\n\t\2\2\u00cc")
        buf.write("\32\3\2\2\2\u00cd\u00ce\t\n\2\2\u00ce\u00cf\t\t\2\2\u00cf")
        buf.write("\34\3\2\2\2\u00d0\u00d4\5\31\r\2\u00d1\u00d4\5\33\16\2")
        buf.write("\u00d2\u00d4\5\25\13\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\36\3\2\2\2\u00d5\u00d9")
        buf.write("\t\t\2\2\u00d6\u00d8\5\35\17\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\t")
        buf.write("\t\2\2\u00dd\u00de\b\20\2\2\u00de \3\2\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\"\3\2\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9$\3\2\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7w\2\2\u00ec\u00ed\7o\2\2\u00ed\u00ee\7d\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7t\2\2\u00f0&\3\2\2\2\u00f1\u00f2")
        buf.write("\7d\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5(\3\2\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7p\2\2\u00fb\u00fc\7i\2\2\u00fc*\3\2\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7t\2\2\u0102\u0103\7p\2\2\u0103,\3")
        buf.write("\2\2\2\u0104\u0105\7x\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107.\3\2\2\2\u0108\u0109\7f\2\2\u0109\u010a")
        buf.write("\7{\2\2\u010a\u010b\7p\2\2\u010b\u010c\7c\2\2\u010c\u010d")
        buf.write("\7o\2\2\u010d\u010e\7k\2\2\u010e\u010f\7e\2\2\u010f\60")
        buf.write("\3\2\2\2\u0110\u0111\7h\2\2\u0111\u0112\7w\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113\u0114\7e\2\2\u0114\62\3\2\2\2\u0115\u0116")
        buf.write("\7h\2\2\u0116\u0117\7q\2\2\u0117\u0118\7t\2\2\u0118\64")
        buf.write("\3\2\2\2\u0119\u011a\7w\2\2\u011a\u011b\7p\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c\u011d\7k\2\2\u011d\u011e\7n\2\2\u011e\66")
        buf.write("\3\2\2\2\u011f\u0120\7d\2\2\u0120\u0121\7{\2\2\u01218")
        buf.write("\3\2\2\2\u0122\u0123\7d\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7g\2\2\u0125\u0126\7c\2\2\u0126\u0127\7m\2\2\u0127:\3")
        buf.write("\2\2\2\u0128\u0129\7e\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7v\2\2\u012c\u012d\7k\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\u012f\7w\2\2\u012f\u0130\7g\2\2\u0130<\3")
        buf.write("\2\2\2\u0131\u0132\7k\2\2\u0132\u0133\7h\2\2\u0133>\3")
        buf.write("\2\2\2\u0134\u0135\7g\2\2\u0135\u0136\7n\2\2\u0136\u0137")
        buf.write("\7u\2\2\u0137\u0138\7g\2\2\u0138@\3\2\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a\u013b\7n\2\2\u013b\u013c\7k\2\2\u013c\u013d")
        buf.write("\7h\2\2\u013dB\3\2\2\2\u013e\u013f\7d\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7i\2\2\u0141\u0142\7k\2\2\u0142\u0143")
        buf.write("\7p\2\2\u0143D\3\2\2\2\u0144\u0145\7g\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\u0147\7f\2\2\u0147F\3\2\2\2\u0148\u0149")
        buf.write("\7-\2\2\u0149H\3\2\2\2\u014a\u014b\7/\2\2\u014bJ\3\2\2")
        buf.write("\2\u014c\u014d\7,\2\2\u014dL\3\2\2\2\u014e\u014f\7\61")
        buf.write("\2\2\u014fN\3\2\2\2\u0150\u0151\7\'\2\2\u0151P\3\2\2\2")
        buf.write("\u0152\u0153\7p\2\2\u0153\u0154\7q\2\2\u0154\u0155\7v")
        buf.write("\2\2\u0155R\3\2\2\2\u0156\u0157\7c\2\2\u0157\u0158\7p")
        buf.write("\2\2\u0158\u0159\7f\2\2\u0159T\3\2\2\2\u015a\u015b\7q")
        buf.write("\2\2\u015b\u015c\7t\2\2\u015cV\3\2\2\2\u015d\u015e\7?")
        buf.write("\2\2\u015eX\3\2\2\2\u015f\u0160\7>\2\2\u0160\u0161\7/")
        buf.write("\2\2\u0161Z\3\2\2\2\u0162\u0163\7#\2\2\u0163\u0164\7?")
        buf.write("\2\2\u0164\\\3\2\2\2\u0165\u0166\7>\2\2\u0166^\3\2\2\2")
        buf.write("\u0167\u0168\7@\2\2\u0168`\3\2\2\2\u0169\u016a\7>\2\2")
        buf.write("\u016a\u016b\7?\2\2\u016bb\3\2\2\2\u016c\u016d\7@\2\2")
        buf.write("\u016d\u016e\7?\2\2\u016ed\3\2\2\2\u016f\u0170\7?\2\2")
        buf.write("\u0170\u0171\7?\2\2\u0171f\3\2\2\2\u0172\u0173\7\60\2")
        buf.write("\2\u0173\u0174\7\60\2\2\u0174\u0175\7\60\2\2\u0175h\3")
        buf.write("\2\2\2\u0176\u0177\7*\2\2\u0177j\3\2\2\2\u0178\u0179\7")
        buf.write("+\2\2\u0179l\3\2\2\2\u017a\u017b\7]\2\2\u017bn\3\2\2\2")
        buf.write("\u017c\u017d\7_\2\2\u017dp\3\2\2\2\u017e\u017f\7.\2\2")
        buf.write("\u017fr\3\2\2\2\u0180\u0181\7%\2\2\u0181\u0182\7%\2\2")
        buf.write("\u0182t\3\2\2\2\u0183\u0187\5s:\2\u0184\u0186\5{>\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u018a\u018b\b;\3\2\u018bv\3\2\2\2\u018c\u018e\t")
        buf.write("\13\2\2\u018d\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\b<\3\2\u0192x\3\2\2\2\u0193\u0194\7\f\2\2")
        buf.write("\u0194z\3\2\2\2\u0195\u0196\n\f\2\2\u0196|\3\2\2\2\u0197")
        buf.write("\u0198\13\2\2\2\u0198\u0199\b?\4\2\u0199~\3\2\2\2\u019a")
        buf.write("\u019e\t\t\2\2\u019b\u019d\5\35\17\2\u019c\u019b\3\2\2")
        buf.write("\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f")
        buf.write("\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1")
        buf.write("\u01a2\7\2\2\3\u01a2\u01a3\b@\5\2\u01a3\u0080\3\2\2\2")
        buf.write("\u01a4\u01a5\13\2\2\2\u01a5\u0082\3\2\2\2\23\2\u0088\u008d")
        buf.write("\u0096\u009c\u00a1\u00a7\u00ae\u00b4\u00ba\u00be\u00c2")
        buf.write("\u00d3\u00d9\u0187\u018f\u019e\6\3\20\2\b\2\2\3?\3\3@")
        buf.write("\4")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    NUMBER = 2
    BOOLEN = 3
    STRING = 4
    KW_TRUE = 5
    KW_FALSE = 6
    KW_NUMBER = 7
    KW_BOOL = 8
    KW_STRING = 9
    KW_RETURN = 10
    KW_VAR = 11
    KW_DYNAMIC = 12
    KW_FUNC = 13
    KW_FOR = 14
    KW_UNTIL = 15
    KW_BY = 16
    KW_BREAK = 17
    KW_CONTINUE = 18
    KW_IF = 19
    KW_ELSE = 20
    KW_ELIF = 21
    KW_BEGIN = 22
    KW_END = 23
    OP_ADD = 24
    OP_SUBTRACT = 25
    OP_MULTI = 26
    OP_DIVIDE = 27
    OP_REMAINDER = 28
    OP_NOT = 29
    OP_AND = 30
    OP_OR = 31
    OP_EQUAL = 32
    OP_LEFT_ARROW = 33
    OP_NOT_EQUAL = 34
    OP_SMALLER = 35
    OP_GREATER = 36
    OP_SMALLER_EQUAL = 37
    OP_GREATER_EQUAL = 38
    OP_EQUAL_COMPARE = 39
    OP_TRIPLE_DOT = 40
    SEP_OPEN_PAREN = 41
    SEP_CLOSE_PAREN = 42
    SEP_OPEN_BRACK = 43
    SEP_CLOSE_BRACK = 44
    SEP_COMA = 45
    COMMENT = 46
    WS = 47
    NEW_LINE = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
            "'or'", "'='", "'<-'", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=='", "'...'", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "BOOLEN", "STRING", "KW_TRUE", "KW_FALSE", 
            "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", 
            "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
            "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", 
            "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", 
            "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", "OP_NOT_EQUAL", 
            "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", 
            "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
            "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT", 
            "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER_HEAD", "IDENTIFIER", "ZERO", "NON_ZERO_DIGIT", 
                  "DIGIT", "FLOATING_POINT", "EXPONENTIAL", "NUMBER", "BOOLEN", 
                  "STRING_CHAR", "ESCAPE_SIGN", "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", 
                  "STRING_LITTERAL", "STRING", "KW_TRUE", "KW_FALSE", "KW_NUMBER", 
                  "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                  "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                  "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                  "KW_END", "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", 
                  "OP_REMAINDER", "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", 
                  "OP_LEFT_ARROW", "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", 
                  "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", "OP_EQUAL_COMPARE", 
                  "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
                  "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT_HEAD", 
                  "COMMENT", "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[14] = self.STRING_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.UNCLOSE_STRING_action 
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
            raise UncloseString(self.text)
     


