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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01a7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7\3\7\7\7\u009b\n\7\f\7\16\7\u009e\13\7\3\b\3\b\7\b\u00a2")
        buf.write("\n\b\f\b\16\b\u00a5\13\b\3\b\3\b\7\b\u00a9\n\b\f\b\16")
        buf.write("\b\u00ac\13\b\3\t\3\t\7\t\u00b0\n\t\f\t\16\t\u00b3\13")
        buf.write("\t\3\t\7\t\u00b6\n\t\f\t\16\t\u00b9\13\t\3\t\7\t\u00bc")
        buf.write("\n\t\f\t\16\t\u00bf\13\t\3\t\5\t\u00c2\n\t\3\n\3\n\5\n")
        buf.write("\u00c6\n\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00d4\n\r\3\16\3\16\3\16\3\17\3\17\3\17\5\17")
        buf.write("\u00dc\n\17\3\20\3\20\7\20\u00e0\n\20\f\20\16\20\u00e3")
        buf.write("\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3:\3;\3;\7;\u018d\n;\f;\16;\u0190")
        buf.write("\13;\3;\3;\5;\u0194\n;\3<\6<\u0197\n<\r<\16<\u0198\3<")
        buf.write("\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\2\2B\3\2\5\3\7\2")
        buf.write("\t\2\13\2\r\2\17\2\21\4\23\5\25\2\27\2\31\2\33\2\35\2")
        buf.write("\37\6!\7#\b%\t\'\n)\13+\f-\r/\16\61\17\63\20\65\21\67")
        buf.write("\229\23;\24=\25?\26A\27C\30E\31G\32I\33K\34M\35O\36Q\37")
        buf.write("S U!W\"Y#[$]%_&a\'c(e)g*i+k,m-o.q/s\2u\60w\61y\62{\63")
        buf.write("}\64\177\65\u0081\66\3\2\13\5\2C\\aac|\5\2\62;C\\c|\3")
        buf.write("\2\63;\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\3\2$$\5\2\n")
        buf.write("\13\16\17\"\"\3\2\f\f\2\u01ac\2\5\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2")
        buf.write("\2\5\u0086\3\2\2\2\7\u0090\3\2\2\2\t\u0092\3\2\2\2\13")
        buf.write("\u0096\3\2\2\2\r\u0098\3\2\2\2\17\u009f\3\2\2\2\21\u00c1")
        buf.write("\3\2\2\2\23\u00c5\3\2\2\2\25\u00c7\3\2\2\2\27\u00c9\3")
        buf.write("\2\2\2\31\u00d3\3\2\2\2\33\u00d5\3\2\2\2\35\u00db\3\2")
        buf.write("\2\2\37\u00dd\3\2\2\2!\u00e6\3\2\2\2#\u00eb\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f8\3\2\2\2)\u00fd\3\2\2\2+\u0104\3\2\2\2")
        buf.write("-\u010b\3\2\2\2/\u010f\3\2\2\2\61\u0117\3\2\2\2\63\u011c")
        buf.write("\3\2\2\2\65\u0120\3\2\2\2\67\u0126\3\2\2\29\u0129\3\2")
        buf.write("\2\2;\u012f\3\2\2\2=\u0138\3\2\2\2?\u013b\3\2\2\2A\u0140")
        buf.write("\3\2\2\2C\u0145\3\2\2\2E\u014b\3\2\2\2G\u014f\3\2\2\2")
        buf.write("I\u0151\3\2\2\2K\u0153\3\2\2\2M\u0155\3\2\2\2O\u0157\3")
        buf.write("\2\2\2Q\u0159\3\2\2\2S\u015d\3\2\2\2U\u0161\3\2\2\2W\u0164")
        buf.write("\3\2\2\2Y\u0166\3\2\2\2[\u0169\3\2\2\2]\u016c\3\2\2\2")
        buf.write("_\u016e\3\2\2\2a\u0170\3\2\2\2c\u0173\3\2\2\2e\u0176\3")
        buf.write("\2\2\2g\u0179\3\2\2\2i\u017d\3\2\2\2k\u017f\3\2\2\2m\u0181")
        buf.write("\3\2\2\2o\u0183\3\2\2\2q\u0185\3\2\2\2s\u0187\3\2\2\2")
        buf.write("u\u018a\3\2\2\2w\u0196\3\2\2\2y\u019c\3\2\2\2{\u019e\3")
        buf.write("\2\2\2}\u01a0\3\2\2\2\177\u01a3\3\2\2\2\u0081\u01a5\3")
        buf.write("\2\2\2\u0083\u0084\t\2\2\2\u0084\4\3\2\2\2\u0085\u0087")
        buf.write("\5\3\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008d\3\2\2\2")
        buf.write("\u008a\u008c\t\3\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3")
        buf.write("\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\6")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7\62\2\2\u0091")
        buf.write("\b\3\2\2\2\u0092\u0093\t\4\2\2\u0093\n\3\2\2\2\u0094\u0097")
        buf.write("\5\7\4\2\u0095\u0097\5\t\5\2\u0096\u0094\3\2\2\2\u0096")
        buf.write("\u0095\3\2\2\2\u0097\f\3\2\2\2\u0098\u009c\7\60\2\2\u0099")
        buf.write("\u009b\5\13\6\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2")
        buf.write("\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\16\3")
        buf.write("\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a3\t\5\2\2\u00a0\u00a2")
        buf.write("\t\6\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2")
        buf.write("\u00a5\u00a3\3\2\2\2\u00a6\u00aa\5\t\5\2\u00a7\u00a9\5")
        buf.write("\13\6\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\20\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ad\u00b1\5\t\5\2\u00ae\u00b0\5\13\6")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b7\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b6\5\r\7\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00bd\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bc")
        buf.write("\5\17\b\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c2\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00c0\u00c2\5\7\4\2\u00c1\u00ad\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\22\3\2\2\2\u00c3\u00c6")
        buf.write("\5!\21\2\u00c4\u00c6\5#\22\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\24\3\2\2\2\u00c7\u00c8\n\7\2\2\u00c8")
        buf.write("\26\3\2\2\2\u00c9\u00ca\13\2\2\2\u00ca\u00cb\7^\2\2\u00cb")
        buf.write("\30\3\2\2\2\u00cc\u00cd\13\2\2\2\u00cd\u00ce\5\27\f\2")
        buf.write("\u00ce\u00cf\n\b\2\2\u00cf\u00d4\3\2\2\2\u00d0\u00d1\5")
        buf.write("\27\f\2\u00d1\u00d2\5y=\2\u00d2\u00d4\3\2\2\2\u00d3\u00cc")
        buf.write("\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d4\32\3\2\2\2\u00d5\u00d6")
        buf.write("\7)\2\2\u00d6\u00d7\7$\2\2\u00d7\34\3\2\2\2\u00d8\u00dc")
        buf.write("\5\31\r\2\u00d9\u00dc\5\33\16\2\u00da\u00dc\5\25\13\2")
        buf.write("\u00db\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3")
        buf.write("\2\2\2\u00dc\36\3\2\2\2\u00dd\u00e1\7$\2\2\u00de\u00e0")
        buf.write("\5\35\17\2\u00df\u00de\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e4\u00e5\7$\2\2\u00e5 \3\2\2\2")
        buf.write("\u00e6\u00e7\7v\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7w")
        buf.write("\2\2\u00e9\u00ea\7g\2\2\u00ea\"\3\2\2\2\u00eb\u00ec\7")
        buf.write("h\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef")
        buf.write("\7u\2\2\u00ef\u00f0\7g\2\2\u00f0$\3\2\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4\7o\2\2\u00f4\u00f5")
        buf.write("\7d\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7t\2\2\u00f7&\3")
        buf.write("\2\2\2\u00f8\u00f9\7d\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7n\2\2\u00fc(\3\2\2\2\u00fd\u00fe")
        buf.write("\7u\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103\7i\2\2\u0103*\3")
        buf.write("\2\2\2\u0104\u0105\7t\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7w\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a,\3\2\2\2\u010b\u010c\7x\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7t\2\2\u010e.\3\2\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110\u0111\7{\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7o\2\2\u0114\u0115\7k\2\2\u0115\u0116")
        buf.write("\7e\2\2\u0116\60\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119")
        buf.write("\7w\2\2\u0119\u011a\7p\2\2\u011a\u011b\7e\2\2\u011b\62")
        buf.write("\3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7t\2\2\u011f\64\3\2\2\2\u0120\u0121\7w\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7v\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7n\2\2\u0125\66\3\2\2\2\u0126\u0127\7d\2\2\u0127\u0128")
        buf.write("\7{\2\2\u01288\3\2\2\2\u0129\u012a\7d\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\u012c\7g\2\2\u012c\u012d\7c\2\2\u012d\u012e")
        buf.write("\7m\2\2\u012e:\3\2\2\2\u012f\u0130\7e\2\2\u0130\u0131")
        buf.write("\7q\2\2\u0131\u0132\7p\2\2\u0132\u0133\7v\2\2\u0133\u0134")
        buf.write("\7k\2\2\u0134\u0135\7p\2\2\u0135\u0136\7w\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137<\3\2\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7h\2\2\u013a>\3\2\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7n\2\2\u013d\u013e\7u\2\2\u013e\u013f\7g\2\2\u013f@\3")
        buf.write("\2\2\2\u0140\u0141\7g\2\2\u0141\u0142\7n\2\2\u0142\u0143")
        buf.write("\7k\2\2\u0143\u0144\7h\2\2\u0144B\3\2\2\2\u0145\u0146")
        buf.write("\7d\2\2\u0146\u0147\7g\2\2\u0147\u0148\7i\2\2\u0148\u0149")
        buf.write("\7k\2\2\u0149\u014a\7p\2\2\u014aD\3\2\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7p\2\2\u014d\u014e\7f\2\2\u014eF\3")
        buf.write("\2\2\2\u014f\u0150\7-\2\2\u0150H\3\2\2\2\u0151\u0152\7")
        buf.write("/\2\2\u0152J\3\2\2\2\u0153\u0154\7,\2\2\u0154L\3\2\2\2")
        buf.write("\u0155\u0156\7\61\2\2\u0156N\3\2\2\2\u0157\u0158\7\'\2")
        buf.write("\2\u0158P\3\2\2\2\u0159\u015a\7p\2\2\u015a\u015b\7q\2")
        buf.write("\2\u015b\u015c\7v\2\2\u015cR\3\2\2\2\u015d\u015e\7c\2")
        buf.write("\2\u015e\u015f\7p\2\2\u015f\u0160\7f\2\2\u0160T\3\2\2")
        buf.write("\2\u0161\u0162\7q\2\2\u0162\u0163\7t\2\2\u0163V\3\2\2")
        buf.write("\2\u0164\u0165\7?\2\2\u0165X\3\2\2\2\u0166\u0167\7>\2")
        buf.write("\2\u0167\u0168\7/\2\2\u0168Z\3\2\2\2\u0169\u016a\7#\2")
        buf.write("\2\u016a\u016b\7?\2\2\u016b\\\3\2\2\2\u016c\u016d\7>\2")
        buf.write("\2\u016d^\3\2\2\2\u016e\u016f\7@\2\2\u016f`\3\2\2\2\u0170")
        buf.write("\u0171\7>\2\2\u0171\u0172\7?\2\2\u0172b\3\2\2\2\u0173")
        buf.write("\u0174\7@\2\2\u0174\u0175\7?\2\2\u0175d\3\2\2\2\u0176")
        buf.write("\u0177\7?\2\2\u0177\u0178\7?\2\2\u0178f\3\2\2\2\u0179")
        buf.write("\u017a\7\60\2\2\u017a\u017b\7\60\2\2\u017b\u017c\7\60")
        buf.write("\2\2\u017ch\3\2\2\2\u017d\u017e\7*\2\2\u017ej\3\2\2\2")
        buf.write("\u017f\u0180\7+\2\2\u0180l\3\2\2\2\u0181\u0182\7]\2\2")
        buf.write("\u0182n\3\2\2\2\u0183\u0184\7_\2\2\u0184p\3\2\2\2\u0185")
        buf.write("\u0186\7.\2\2\u0186r\3\2\2\2\u0187\u0188\7%\2\2\u0188")
        buf.write("\u0189\7%\2\2\u0189t\3\2\2\2\u018a\u018e\5s:\2\u018b\u018d")
        buf.write("\5{>\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0193\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0191\u0194\5y=\2\u0192\u0194\7\2\2\3\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194v\3\2\2\2\u0195")
        buf.write("\u0197\t\t\2\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019a\u019b\b<\2\2\u019bx\3\2\2\2\u019c\u019d\7")
        buf.write("\f\2\2\u019dz\3\2\2\2\u019e\u019f\n\n\2\2\u019f|\3\2\2")
        buf.write("\2\u01a0\u01a1\13\2\2\2\u01a1\u01a2\b?\3\2\u01a2~\3\2")
        buf.write("\2\2\u01a3\u01a4\13\2\2\2\u01a4\u0080\3\2\2\2\u01a5\u01a6")
        buf.write("\13\2\2\2\u01a6\u0082\3\2\2\2\24\2\u0088\u008d\u0096\u009c")
        buf.write("\u00a3\u00aa\u00b1\u00b7\u00bd\u00c1\u00c5\u00d3\u00db")
        buf.write("\u00e1\u018e\u0193\u0198\4\b\2\2\3?\2")
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
    NOT_NEW_LINE = 49
    ERROR_CHAR = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52

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
            "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

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
            actions[61] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


