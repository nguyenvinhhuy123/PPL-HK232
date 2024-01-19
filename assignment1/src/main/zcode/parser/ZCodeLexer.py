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
        buf.write("\u01b8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\6\4\u008c\n\4\r\4\16\4\u008d\3\4")
        buf.write("\7\4\u0091\n\4\f\4\16\4\u0094\13\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\5\7\u009c\n\7\3\b\3\b\7\b\u00a0\n\b\f\b\16\b\u00a3")
        buf.write("\13\b\3\t\3\t\5\t\u00a7\n\t\3\t\3\t\7\t\u00ab\n\t\f\t")
        buf.write("\16\t\u00ae\13\t\3\n\3\n\7\n\u00b2\n\n\f\n\16\n\u00b5")
        buf.write("\13\n\3\n\7\n\u00b8\n\n\f\n\16\n\u00bb\13\n\3\n\7\n\u00be")
        buf.write("\n\n\f\n\16\n\u00c1\13\n\3\n\5\n\u00c4\n\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\5\17\u00d5\n\17\3\20\3\20\7\20\u00d9\n\20\f\20\16")
        buf.write("\20\u00dc\13\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
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
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\7;\u0187\n")
        buf.write(";\f;\16;\u018a\13;\3;\3;\3<\6<\u018f\n<\r<\16<\u0190\3")
        buf.write("<\3<\3=\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\7@\u01a0\n@\f@\16")
        buf.write("@\u01a3\13@\3@\3@\3@\3A\3A\7A\u01aa\nA\fA\16A\u01ad\13")
        buf.write("A\3A\3A\7A\u01b1\nA\fA\16A\u01b4\13A\3A\3A\3A\2\2B\3\3")
        buf.write("\5\2\7\4\t\2\13\2\r\2\17\2\21\2\23\5\25\2\27\2\31\2\33")
        buf.write("\2\35\2\37\6!\7#\b%\t\'\n)\13+\f-\r/\16\61\17\63\20\65")
        buf.write("\21\67\229\23;\24=\25?\26A\27C\30E\31G\32I\33K\34M\35")
        buf.write("O\36Q\37S U!W\"Y#[$]%_&a\'c(e)g*i+k,m-o.q/s\2u\60w\61")
        buf.write("y\62{\2}\63\177\64\u0081\65\3\2\r\5\2C\\aac|\5\2\62;C")
        buf.write("\\c|\3\2\63;\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\3\2^")
        buf.write("^\3\2$$\3\2))\5\2\n\13\16\17\"\"\3\2\f\f\2\u01bc\2\3\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\23\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083")
        buf.write("\3\2\2\2\5\u0088\3\2\2\2\7\u008b\3\2\2\2\t\u0095\3\2\2")
        buf.write("\2\13\u0097\3\2\2\2\r\u009b\3\2\2\2\17\u009d\3\2\2\2\21")
        buf.write("\u00a4\3\2\2\2\23\u00c3\3\2\2\2\25\u00c5\3\2\2\2\27\u00c7")
        buf.write("\3\2\2\2\31\u00ca\3\2\2\2\33\u00ce\3\2\2\2\35\u00d4\3")
        buf.write("\2\2\2\37\u00d6\3\2\2\2!\u00e0\3\2\2\2#\u00e5\3\2\2\2")
        buf.write("%\u00eb\3\2\2\2\'\u00f2\3\2\2\2)\u00f7\3\2\2\2+\u00fe")
        buf.write("\3\2\2\2-\u0105\3\2\2\2/\u0109\3\2\2\2\61\u0111\3\2\2")
        buf.write("\2\63\u0116\3\2\2\2\65\u011a\3\2\2\2\67\u0120\3\2\2\2")
        buf.write("9\u0123\3\2\2\2;\u0129\3\2\2\2=\u0132\3\2\2\2?\u0135\3")
        buf.write("\2\2\2A\u013a\3\2\2\2C\u013f\3\2\2\2E\u0145\3\2\2\2G\u0149")
        buf.write("\3\2\2\2I\u014b\3\2\2\2K\u014d\3\2\2\2M\u014f\3\2\2\2")
        buf.write("O\u0151\3\2\2\2Q\u0153\3\2\2\2S\u0157\3\2\2\2U\u015b\3")
        buf.write("\2\2\2W\u015e\3\2\2\2Y\u0160\3\2\2\2[\u0163\3\2\2\2]\u0166")
        buf.write("\3\2\2\2_\u0168\3\2\2\2a\u016a\3\2\2\2c\u016d\3\2\2\2")
        buf.write("e\u0170\3\2\2\2g\u0173\3\2\2\2i\u0177\3\2\2\2k\u0179\3")
        buf.write("\2\2\2m\u017b\3\2\2\2o\u017d\3\2\2\2q\u017f\3\2\2\2s\u0181")
        buf.write("\3\2\2\2u\u0184\3\2\2\2w\u018e\3\2\2\2y\u0194\3\2\2\2")
        buf.write("{\u0198\3\2\2\2}\u019a\3\2\2\2\177\u019d\3\2\2\2\u0081")
        buf.write("\u01a7\3\2\2\2\u0083\u0084\7o\2\2\u0084\u0085\7c\2\2\u0085")
        buf.write("\u0086\7k\2\2\u0086\u0087\7p\2\2\u0087\4\3\2\2\2\u0088")
        buf.write("\u0089\t\2\2\2\u0089\6\3\2\2\2\u008a\u008c\5\5\3\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u0092\3\2\2\2\u008f\u0091\t")
        buf.write("\3\2\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\b\3\2\2\2\u0094\u0092")
        buf.write("\3\2\2\2\u0095\u0096\7\62\2\2\u0096\n\3\2\2\2\u0097\u0098")
        buf.write("\t\4\2\2\u0098\f\3\2\2\2\u0099\u009c\5\t\5\2\u009a\u009c")
        buf.write("\5\13\6\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\16\3\2\2\2\u009d\u00a1\7\60\2\2\u009e\u00a0\5\r\7\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a2\3\2\2\2\u00a2\20\3\2\2\2\u00a3\u00a1\3\2")
        buf.write("\2\2\u00a4\u00a6\t\5\2\2\u00a5\u00a7\t\6\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00ac\5\13\6\2\u00a9\u00ab\5\r\7\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\22\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b3")
        buf.write("\5\13\6\2\u00b0\u00b2\5\r\7\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b9\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b8\5")
        buf.write("\17\b\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bf\3\2\2\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bc\u00be\5\21\t\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c4\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c2\u00c4\5\t\5\2\u00c3\u00af\3\2\2\2\u00c3\u00c2\3")
        buf.write("\2\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\n\7\2\2\u00c6\26\3")
        buf.write("\2\2\2\u00c7\u00c8\13\2\2\2\u00c8\u00c9\t\b\2\2\u00c9")
        buf.write("\30\3\2\2\2\u00ca\u00cb\13\2\2\2\u00cb\u00cc\5\27\f\2")
        buf.write("\u00cc\u00cd\n\t\2\2\u00cd\32\3\2\2\2\u00ce\u00cf\t\n")
        buf.write("\2\2\u00cf\u00d0\t\t\2\2\u00d0\34\3\2\2\2\u00d1\u00d5")
        buf.write("\5\31\r\2\u00d2\u00d5\5\33\16\2\u00d3\u00d5\5\25\13\2")
        buf.write("\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3")
        buf.write("\2\2\2\u00d5\36\3\2\2\2\u00d6\u00da\t\t\2\2\u00d7\u00d9")
        buf.write("\5\35\17\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dd\u00de\t\t\2\2\u00de\u00df\b")
        buf.write("\20\2\2\u00df \3\2\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7g\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7n\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7g\2\2\u00ea$\3")
        buf.write("\2\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7o\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1&\3\2\2\2\u00f2\u00f3\7d\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7n\2\2\u00f6(\3")
        buf.write("\2\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7i\2\2\u00fd*\3\2\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\u0101\7v\2\2\u0101\u0102\7w\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7p\2\2\u0104,\3\2\2\2\u0105\u0106")
        buf.write("\7x\2\2\u0106\u0107\7c\2\2\u0107\u0108\7t\2\2\u0108.\3")
        buf.write("\2\2\2\u0109\u010a\7f\2\2\u010a\u010b\7{\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7c\2\2\u010d\u010e\7o\2\2\u010e\u010f")
        buf.write("\7k\2\2\u010f\u0110\7e\2\2\u0110\60\3\2\2\2\u0111\u0112")
        buf.write("\7h\2\2\u0112\u0113\7w\2\2\u0113\u0114\7p\2\2\u0114\u0115")
        buf.write("\7e\2\2\u0115\62\3\2\2\2\u0116\u0117\7h\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\u0119\7t\2\2\u0119\64\3\2\2\2\u011a\u011b")
        buf.write("\7w\2\2\u011b\u011c\7p\2\2\u011c\u011d\7v\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7n\2\2\u011f\66\3\2\2\2\u0120\u0121")
        buf.write("\7d\2\2\u0121\u0122\7{\2\2\u01228\3\2\2\2\u0123\u0124")
        buf.write("\7d\2\2\u0124\u0125\7t\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7m\2\2\u0128:\3\2\2\2\u0129\u012a")
        buf.write("\7e\2\2\u012a\u012b\7q\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d\u012e\7k\2\2\u012e\u012f\7p\2\2\u012f\u0130")
        buf.write("\7w\2\2\u0130\u0131\7g\2\2\u0131<\3\2\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7h\2\2\u0134>\3\2\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7n\2\2\u0137\u0138\7u\2\2\u0138\u0139")
        buf.write("\7g\2\2\u0139@\3\2\2\2\u013a\u013b\7g\2\2\u013b\u013c")
        buf.write("\7n\2\2\u013c\u013d\7k\2\2\u013d\u013e\7h\2\2\u013eB\3")
        buf.write("\2\2\2\u013f\u0140\7d\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7i\2\2\u0142\u0143\7k\2\2\u0143\u0144\7p\2\2\u0144D\3")
        buf.write("\2\2\2\u0145\u0146\7g\2\2\u0146\u0147\7p\2\2\u0147\u0148")
        buf.write("\7f\2\2\u0148F\3\2\2\2\u0149\u014a\7-\2\2\u014aH\3\2\2")
        buf.write("\2\u014b\u014c\7/\2\2\u014cJ\3\2\2\2\u014d\u014e\7,\2")
        buf.write("\2\u014eL\3\2\2\2\u014f\u0150\7\61\2\2\u0150N\3\2\2\2")
        buf.write("\u0151\u0152\7\'\2\2\u0152P\3\2\2\2\u0153\u0154\7p\2\2")
        buf.write("\u0154\u0155\7q\2\2\u0155\u0156\7v\2\2\u0156R\3\2\2\2")
        buf.write("\u0157\u0158\7c\2\2\u0158\u0159\7p\2\2\u0159\u015a\7f")
        buf.write("\2\2\u015aT\3\2\2\2\u015b\u015c\7q\2\2\u015c\u015d\7t")
        buf.write("\2\2\u015dV\3\2\2\2\u015e\u015f\7?\2\2\u015fX\3\2\2\2")
        buf.write("\u0160\u0161\7>\2\2\u0161\u0162\7/\2\2\u0162Z\3\2\2\2")
        buf.write("\u0163\u0164\7#\2\2\u0164\u0165\7?\2\2\u0165\\\3\2\2\2")
        buf.write("\u0166\u0167\7>\2\2\u0167^\3\2\2\2\u0168\u0169\7@\2\2")
        buf.write("\u0169`\3\2\2\2\u016a\u016b\7>\2\2\u016b\u016c\7?\2\2")
        buf.write("\u016cb\3\2\2\2\u016d\u016e\7@\2\2\u016e\u016f\7?\2\2")
        buf.write("\u016fd\3\2\2\2\u0170\u0171\7?\2\2\u0171\u0172\7?\2\2")
        buf.write("\u0172f\3\2\2\2\u0173\u0174\7\60\2\2\u0174\u0175\7\60")
        buf.write("\2\2\u0175\u0176\7\60\2\2\u0176h\3\2\2\2\u0177\u0178\7")
        buf.write("*\2\2\u0178j\3\2\2\2\u0179\u017a\7+\2\2\u017al\3\2\2\2")
        buf.write("\u017b\u017c\7]\2\2\u017cn\3\2\2\2\u017d\u017e\7_\2\2")
        buf.write("\u017ep\3\2\2\2\u017f\u0180\7.\2\2\u0180r\3\2\2\2\u0181")
        buf.write("\u0182\7%\2\2\u0182\u0183\7%\2\2\u0183t\3\2\2\2\u0184")
        buf.write("\u0188\5s:\2\u0185\u0187\5{>\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c\b")
        buf.write(";\3\2\u018cv\3\2\2\2\u018d\u018f\t\13\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\b<\3\2")
        buf.write("\u0193x\3\2\2\2\u0194\u0195\7\f\2\2\u0195\u0196\3\2\2")
        buf.write("\2\u0196\u0197\b=\4\2\u0197z\3\2\2\2\u0198\u0199\n\f\2")
        buf.write("\2\u0199|\3\2\2\2\u019a\u019b\13\2\2\2\u019b\u019c\b?")
        buf.write("\5\2\u019c~\3\2\2\2\u019d\u01a1\t\t\2\2\u019e\u01a0\5")
        buf.write("\35\17\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7\2\2\3\u01a5\u01a6\b")
        buf.write("@\6\2\u01a6\u0080\3\2\2\2\u01a7\u01ab\t\t\2\2\u01a8\u01aa")
        buf.write("\5\35\17\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01ab\3\2\2\2\u01ae\u01b2\5\27\f\2\u01af\u01b1")
        buf.write("\5\35\17\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2")
        buf.write("\u01b4\u01b2\3\2\2\2\u01b5\u01b6\t\t\2\2\u01b6\u01b7\b")
        buf.write("A\7\2\u01b7\u0082\3\2\2\2\24\2\u008d\u0092\u009b\u00a1")
        buf.write("\u00a6\u00ac\u00b3\u00b9\u00bf\u00c3\u00d4\u00da\u0188")
        buf.write("\u0190\u01a1\u01ab\u01b2\b\3\20\2\b\2\2\2\3\2\3?\3\3@")
        buf.write("\4\3A\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN_TOKEN = 1
    IDENTIFIER = 2
    NUMBER = 3
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
            "'main'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", 
            "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'...'", "'('", "')'", "'['", "']'", "','", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN_TOKEN", "IDENTIFIER", "NUMBER", "STRING", "KW_TRUE", "KW_FALSE", 
            "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", 
            "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
            "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", 
            "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", 
            "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", "OP_NOT_EQUAL", 
            "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", 
            "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
            "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT", 
            "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "MAIN_TOKEN", "IDENTIFIER_HEAD", "IDENTIFIER", "ZERO", 
                  "NON_ZERO_DIGIT", "DIGIT", "FLOATING_POINT", "EXPONENTIAL", 
                  "NUMBER", "STRING_CHAR", "ESCAPE_SIGN", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", "STRING", 
                  "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", "KW_STRING", 
                  "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", 
                  "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", 
                  "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", 
                  "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", 
                  "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", 
                  "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", 
                  "OP_GREATER_EQUAL", "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", 
                  "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", 
                  "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT_HEAD", "COMMENT", 
                  "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
     


