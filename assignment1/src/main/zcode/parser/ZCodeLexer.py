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
        buf.write("\u01c6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3\'\3\'\3(")
        buf.write("\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\7,\u0136\n,\f,\16,\u0139")
        buf.write("\13,\3,\3,\3-\6-\u013e\n-\r-\16-\u013f\3-\3-\3.\3.\5.")
        buf.write("\u0146\n.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\7\62")
        buf.write("\u0152\n\62\f\62\16\62\u0155\13\62\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u015b\n\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3")
        buf.write("\66\3\66\3\67\3\67\5\67\u0168\n\67\38\68\u016b\n8\r8\16")
        buf.write("8\u016c\39\39\79\u0171\n9\f9\169\u0174\139\39\59\u0177")
        buf.write("\n9\3:\3:\3:\5:\u017c\n:\3:\6:\u017f\n:\r:\16:\u0180\3")
        buf.write(":\5:\u0184\n:\3;\3;\3;\3;\3;\5;\u018b\n;\3<\3<\3=\3=\3")
        buf.write("=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3B\3C\3C\3C\5C\u01a1")
        buf.write("\nC\3D\3D\3D\7D\u01a6\nD\fD\16D\u01a9\13D\3D\3D\3D\3E")
        buf.write("\3E\3E\3F\3F\3F\7F\u01b4\nF\fF\16F\u01b7\13F\3F\3F\3F")
        buf.write("\3G\3G\3G\7G\u01bf\nG\fG\16G\u01c2\13G\3G\3G\3G\2\2H\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U\2W,Y-[.]\2_\2a\2c\2e/g\60i\2k\2m\2o\2q\2s\2u\61w\2")
        buf.write("y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\62\u0089")
        buf.write("\63\u008b\64\u008d\65\3\2\16\5\2\n\13\16\16\"\"\4\2\f")
        buf.write("\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2GGgg\4\2")
        buf.write("--//\3\2^^\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\3\2))\3")
        buf.write("\2$$\2\u01c7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2u\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3")
        buf.write("\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2")
        buf.write("\5\u0094\3\2\2\2\7\u009a\3\2\2\2\t\u00a1\3\2\2\2\13\u00a6")
        buf.write("\3\2\2\2\r\u00ad\3\2\2\2\17\u00b4\3\2\2\2\21\u00b8\3\2")
        buf.write("\2\2\23\u00c0\3\2\2\2\25\u00c5\3\2\2\2\27\u00c9\3\2\2")
        buf.write("\2\31\u00cf\3\2\2\2\33\u00d2\3\2\2\2\35\u00d8\3\2\2\2")
        buf.write("\37\u00e1\3\2\2\2!\u00e4\3\2\2\2#\u00e9\3\2\2\2%\u00ee")
        buf.write("\3\2\2\2\'\u00f4\3\2\2\2)\u00f8\3\2\2\2+\u00fa\3\2\2\2")
        buf.write("-\u00fc\3\2\2\2/\u00fe\3\2\2\2\61\u0100\3\2\2\2\63\u0102")
        buf.write("\3\2\2\2\65\u0106\3\2\2\2\67\u010a\3\2\2\29\u010d\3\2")
        buf.write("\2\2;\u010f\3\2\2\2=\u0112\3\2\2\2?\u0115\3\2\2\2A\u0117")
        buf.write("\3\2\2\2C\u0119\3\2\2\2E\u011c\3\2\2\2G\u011f\3\2\2\2")
        buf.write("I\u0122\3\2\2\2K\u0126\3\2\2\2M\u0128\3\2\2\2O\u012a\3")
        buf.write("\2\2\2Q\u012c\3\2\2\2S\u012e\3\2\2\2U\u0130\3\2\2\2W\u0133")
        buf.write("\3\2\2\2Y\u013d\3\2\2\2[\u0145\3\2\2\2]\u0149\3\2\2\2")
        buf.write("_\u014c\3\2\2\2a\u014e\3\2\2\2c\u0153\3\2\2\2e\u015a\3")
        buf.write("\2\2\2g\u015c\3\2\2\2i\u0161\3\2\2\2k\u0163\3\2\2\2m\u0167")
        buf.write("\3\2\2\2o\u016a\3\2\2\2q\u0176\3\2\2\2s\u0183\3\2\2\2")
        buf.write("u\u018a\3\2\2\2w\u018c\3\2\2\2y\u018e\3\2\2\2{\u0191\3")
        buf.write("\2\2\2}\u0193\3\2\2\2\177\u0195\3\2\2\2\u0081\u0198\3")
        buf.write("\2\2\2\u0083\u019a\3\2\2\2\u0085\u01a0\3\2\2\2\u0087\u01a2")
        buf.write("\3\2\2\2\u0089\u01ad\3\2\2\2\u008b\u01b0\3\2\2\2\u008d")
        buf.write("\u01bb\3\2\2\2\u008f\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091")
        buf.write("\u0092\7w\2\2\u0092\u0093\7g\2\2\u0093\4\3\2\2\2\u0094")
        buf.write("\u0095\7h\2\2\u0095\u0096\7c\2\2\u0096\u0097\7n\2\2\u0097")
        buf.write("\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099\6\3\2\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7w\2\2\u009c\u009d\7o\2\2\u009d")
        buf.write("\u009e\7d\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\b\3\2\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3\7q\2\2\u00a3")
        buf.write("\u00a4\7q\2\2\u00a4\u00a5\7n\2\2\u00a5\n\3\2\2\2\u00a6")
        buf.write("\u00a7\7u\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7t\2\2\u00a9")
        buf.write("\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7i\2\2\u00ac")
        buf.write("\f\3\2\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af")
        buf.write("\u00b0\7v\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2\7t\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\16\3\2\2\2\u00b4\u00b5\7x\2\2\u00b5")
        buf.write("\u00b6\7c\2\2\u00b6\u00b7\7t\2\2\u00b7\20\3\2\2\2\u00b8")
        buf.write("\u00b9\7f\2\2\u00b9\u00ba\7{\2\2\u00ba\u00bb\7p\2\2\u00bb")
        buf.write("\u00bc\7c\2\2\u00bc\u00bd\7o\2\2\u00bd\u00be\7k\2\2\u00be")
        buf.write("\u00bf\7e\2\2\u00bf\22\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1")
        buf.write("\u00c2\7w\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7e\2\2\u00c4")
        buf.write("\24\3\2\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7t\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\7w\2\2\u00ca")
        buf.write("\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7n\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7d\2\2\u00d0")
        buf.write("\u00d1\7{\2\2\u00d1\32\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3")
        buf.write("\u00d4\7t\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7c\2\2\u00d6")
        buf.write("\u00d7\7m\2\2\u00d7\34\3\2\2\2\u00d8\u00d9\7e\2\2\u00d9")
        buf.write("\u00da\7q\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc")
        buf.write("\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7w\2\2\u00df")
        buf.write("\u00e0\7g\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7h\2\2\u00e3 \3\2\2\2\u00e4\u00e5\7g\2\2\u00e5")
        buf.write("\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\"\3\2\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7n\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7h\2\2\u00ed$\3\2\2\2\u00ee")
        buf.write("\u00ef\7d\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7i\2\2\u00f1")
        buf.write("\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3&\3\2\2\2\u00f4")
        buf.write("\u00f5\7g\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7f\2\2\u00f7")
        buf.write("(\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9*\3\2\2\2\u00fa\u00fb")
        buf.write("\7/\2\2\u00fb,\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd.\3\2\2")
        buf.write("\2\u00fe\u00ff\7\61\2\2\u00ff\60\3\2\2\2\u0100\u0101\7")
        buf.write("\'\2\2\u0101\62\3\2\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104\u0105\7v\2\2\u0105\64\3\2\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7p\2\2\u0108\u0109\7f\2\2\u0109\66")
        buf.write("\3\2\2\2\u010a\u010b\7q\2\2\u010b\u010c\7t\2\2\u010c8")
        buf.write("\3\2\2\2\u010d\u010e\7?\2\2\u010e:\3\2\2\2\u010f\u0110")
        buf.write("\7>\2\2\u0110\u0111\7/\2\2\u0111<\3\2\2\2\u0112\u0113")
        buf.write("\7#\2\2\u0113\u0114\7?\2\2\u0114>\3\2\2\2\u0115\u0116")
        buf.write("\7>\2\2\u0116@\3\2\2\2\u0117\u0118\7@\2\2\u0118B\3\2\2")
        buf.write("\2\u0119\u011a\7>\2\2\u011a\u011b\7?\2\2\u011bD\3\2\2")
        buf.write("\2\u011c\u011d\7@\2\2\u011d\u011e\7?\2\2\u011eF\3\2\2")
        buf.write("\2\u011f\u0120\7?\2\2\u0120\u0121\7?\2\2\u0121H\3\2\2")
        buf.write("\2\u0122\u0123\7\60\2\2\u0123\u0124\7\60\2\2\u0124\u0125")
        buf.write("\7\60\2\2\u0125J\3\2\2\2\u0126\u0127\7*\2\2\u0127L\3\2")
        buf.write("\2\2\u0128\u0129\7+\2\2\u0129N\3\2\2\2\u012a\u012b\7]")
        buf.write("\2\2\u012bP\3\2\2\2\u012c\u012d\7_\2\2\u012dR\3\2\2\2")
        buf.write("\u012e\u012f\7.\2\2\u012fT\3\2\2\2\u0130\u0131\7%\2\2")
        buf.write("\u0131\u0132\7%\2\2\u0132V\3\2\2\2\u0133\u0137\5U+\2\u0134")
        buf.write("\u0136\5_\60\2\u0135\u0134\3\2\2\2\u0136\u0139\3\2\2\2")
        buf.write("\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b\b,\2\2\u013bX\3")
        buf.write("\2\2\2\u013c\u013e\t\2\2\2\u013d\u013c\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141\u0142\b-\2\2\u0142Z\3\2\2\2\u0143")
        buf.write("\u0146\5]/\2\u0144\u0146\t\3\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\b.\3\2")
        buf.write("\u0148\\\3\2\2\2\u0149\u014a\7\17\2\2\u014a\u014b\7\f")
        buf.write("\2\2\u014b^\3\2\2\2\u014c\u014d\n\3\2\2\u014d`\3\2\2\2")
        buf.write("\u014e\u014f\t\4\2\2\u014fb\3\2\2\2\u0150\u0152\t\5\2")
        buf.write("\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154d\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0156\u0157\5a\61\2\u0157\u0158\5c\62\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u015b\5g\64\2\u015a\u0156\3\2\2\2")
        buf.write("\u015a\u0159\3\2\2\2\u015bf\3\2\2\2\u015c\u015d\7o\2\2")
        buf.write("\u015d\u015e\7c\2\2\u015e\u015f\7k\2\2\u015f\u0160\7p")
        buf.write("\2\2\u0160h\3\2\2\2\u0161\u0162\7\62\2\2\u0162j\3\2\2")
        buf.write("\2\u0163\u0164\t\6\2\2\u0164l\3\2\2\2\u0165\u0168\5i\65")
        buf.write("\2\u0166\u0168\5k\66\2\u0167\u0165\3\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168n\3\2\2\2\u0169\u016b\5m\67\2\u016a\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016dp\3\2\2\2\u016e\u0172\7\60\2\2\u016f")
        buf.write("\u0171\5m\67\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0177\3")
        buf.write("\2\2\2\u0174\u0172\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u016e")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177r\3\2\2\2\u0178\u017b")
        buf.write("\t\7\2\2\u0179\u017c\t\b\2\2\u017a\u017c\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c\u017e\3\2\2\2")
        buf.write("\u017d\u017f\5m\67\2\u017e\u017d\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0184")
        buf.write("\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0178\3\2\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184t\3\2\2\2\u0185\u0186\5o8\2\u0186")
        buf.write("\u0187\5q9\2\u0187\u0188\5s:\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u018b\5i\65\2\u018a\u0185\3\2\2\2\u018a\u0189\3\2\2\2")
        buf.write("\u018bv\3\2\2\2\u018c\u018d\t\t\2\2\u018dx\3\2\2\2\u018e")
        buf.write("\u018f\5w<\2\u018f\u0190\5{>\2\u0190z\3\2\2\2\u0191\u0192")
        buf.write("\t\n\2\2\u0192|\3\2\2\2\u0193\u0194\n\n\2\2\u0194~\3\2")
        buf.write("\2\2\u0195\u0196\5w<\2\u0196\u0197\5}?\2\u0197\u0080\3")
        buf.write("\2\2\2\u0198\u0199\n\13\2\2\u0199\u0082\3\2\2\2\u019a")
        buf.write("\u019b\t\f\2\2\u019b\u019c\t\r\2\2\u019c\u0084\3\2\2\2")
        buf.write("\u019d\u01a1\5y=\2\u019e\u01a1\5\u0083B\2\u019f\u01a1")
        buf.write("\5\u0081A\2\u01a0\u019d\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u0086\3\2\2\2\u01a2\u01a7\t\r\2\2")
        buf.write("\u01a3\u01a6\5[.\2\u01a4\u01a6\5\u0085C\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01aa\u01ab\t\r\2\2\u01ab\u01ac\b")
        buf.write("D\4\2\u01ac\u0088\3\2\2\2\u01ad\u01ae\13\2\2\2\u01ae\u01af")
        buf.write("\bE\5\2\u01af\u008a\3\2\2\2\u01b0\u01b5\t\r\2\2\u01b1")
        buf.write("\u01b4\5\u0085C\2\u01b2\u01b4\5[.\2\u01b3\u01b1\3\2\2")
        buf.write("\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b8\u01b9\7\2\2\3\u01b9\u01ba\bF\6\2")
        buf.write("\u01ba\u008c\3\2\2\2\u01bb\u01c0\t\r\2\2\u01bc\u01bf\5")
        buf.write("\u0085C\2\u01bd\u01bf\5[.\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01c0\3")
        buf.write("\2\2\2\u01c3\u01c4\5\177@\2\u01c4\u01c5\bG\7\2\u01c5\u008e")
        buf.write("\3\2\2\2\27\2\u0137\u013f\u0145\u0153\u015a\u0167\u016c")
        buf.write("\u0172\u0176\u017b\u0180\u0183\u018a\u01a0\u01a5\u01a7")
        buf.write("\u01b3\u01b5\u01be\u01c0\b\b\2\2\3.\2\3D\3\3E\4\3F\5\3")
        buf.write("G\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    KW_TRUE = 1
    KW_FALSE = 2
    KW_NUMBER = 3
    KW_BOOL = 4
    KW_STRING = 5
    KW_RETURN = 6
    KW_VAR = 7
    KW_DYNAMIC = 8
    KW_FUNC = 9
    KW_FOR = 10
    KW_UNTIL = 11
    KW_BY = 12
    KW_BREAK = 13
    KW_CONTINUE = 14
    KW_IF = 15
    KW_ELSE = 16
    KW_ELIF = 17
    KW_BEGIN = 18
    KW_END = 19
    OP_ADD = 20
    OP_SUBTRACT = 21
    OP_MULTI = 22
    OP_DIVIDE = 23
    OP_REMAINDER = 24
    OP_NOT = 25
    OP_AND = 26
    OP_OR = 27
    OP_EQUAL = 28
    OP_ASSIGN = 29
    OP_NOT_EQUAL = 30
    OP_SMALLER = 31
    OP_GREATER = 32
    OP_SMALLER_EQUAL = 33
    OP_GREATER_EQUAL = 34
    OP_STRING_EQUAL = 35
    OP_STRING_CONCAT = 36
    SEP_OPEN_PAREN = 37
    SEP_CLOSE_PAREN = 38
    SEP_OPEN_BRACK = 39
    SEP_CLOSE_BRACK = 40
    SEP_COMA = 41
    COMMENT = 42
    WS = 43
    NEW_LINE = 44
    IDENTIFIER = 45
    MAIN_TOKEN = 46
    NUMBER = 47
    STRING = 48
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
            "'=='", "'...'", "'('", "')'", "'['", "']'", "','", "'main'" ]

    symbolicNames = [ "<INVALID>",
            "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", "KW_STRING", 
            "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", 
            "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", 
            "KW_BEGIN", "KW_END", "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", 
            "OP_REMAINDER", "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_ASSIGN", 
            "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", 
            "OP_GREATER_EQUAL", "OP_STRING_EQUAL", "OP_STRING_CONCAT", "SEP_OPEN_PAREN", 
            "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", 
            "COMMENT", "WS", "NEW_LINE", "IDENTIFIER", "MAIN_TOKEN", "NUMBER", 
            "STRING", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", "KW_STRING", 
                  "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", 
                  "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", 
                  "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", 
                  "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", 
                  "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_ASSIGN", 
                  "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", 
                  "OP_GREATER_EQUAL", "OP_STRING_EQUAL", "OP_STRING_CONCAT", 
                  "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", 
                  "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT_HEAD", "COMMENT", 
                  "WS", "NEW_LINE", "WINDOW_NEW_LINE", "NOT_NEW_LINE", "IDENTIFIER_HEAD", 
                  "IDENTIFIER_TAIL", "IDENTIFIER", "MAIN_TOKEN", "ZERO", 
                  "NON_ZERO_DIGIT", "DIGIT", "DECIMAL", "FLOATING_POINT", 
                  "EXPONENTIAL", "NUMBER", "ESCAPE_SIGN", "ESCAPE_SEQUENCE", 
                  "ESCAPE_REP", "NOT_ESCAPE_REP", "ILLEGAL_ESCAPE_SEQ", 
                  "STRING_CHAR", "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", 
                  "STRING", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[44] = self.NEW_LINE_action 
            actions[66] = self.STRING_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEW_LINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
            raise IllegalEscape(self.text[1:])
     


