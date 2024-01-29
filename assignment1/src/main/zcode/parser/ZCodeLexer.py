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
        buf.write("\u01be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\7-\u0137\n-\f-\16")
        buf.write("-\u013a\13-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\5\61\u0145")
        buf.write("\n\61\3\62\6\62\u0148\n\62\r\62\16\62\u0149\3\63\3\63")
        buf.write("\7\63\u014e\n\63\f\63\16\63\u0151\13\63\3\63\5\63\u0154")
        buf.write("\n\63\3\64\3\64\3\64\5\64\u0159\n\64\3\64\6\64\u015c\n")
        buf.write("\64\r\64\16\64\u015d\3\64\5\64\u0161\n\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u0168\n\65\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3=\5=\u017f")
        buf.write("\n=\3>\3>\7>\u0183\n>\f>\16>\u0186\13>\3>\3>\3>\3?\3?")
        buf.write("\3?\3@\3@\7@\u0190\n@\f@\16@\u0193\13@\3@\3@\3A\6A\u0198")
        buf.write("\nA\rA\16A\u0199\3A\3A\3B\3B\5B\u01a0\nB\3B\3B\5B\u01a4")
        buf.write("\nB\3C\3C\3D\3D\3D\3E\3E\7E\u01ad\nE\fE\16E\u01b0\13E")
        buf.write("\3E\3E\3E\3F\3F\7F\u01b7\nF\fF\16F\u01ba\13F\3F\3F\3F")
        buf.write("\2\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W\2Y\2[-]\2_\2a\2c\2e\2g\2i.k\2m\2o\2q\2s\2")
        buf.write("u\2w\2y\2{/}\2\177\60\u0081\61\u0083\62\u0085\2\u0087")
        buf.write("\63\u0089\64\u008b\65\3\2\16\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\63;\4\2GGgg\4\2--//\3\2^^\t\2))^^ddhhppttvv\5\2")
        buf.write("\f\f$$^^\3\2))\3\2$$\5\2\n\13\16\16\"\"\4\2\f\f\17\17")
        buf.write("\2\u01be\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2[\3\2\2\2\2i\3\2\2\2\2{\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2")
        buf.write("\2\5\u0092\3\2\2\2\7\u0097\3\2\2\2\t\u009d\3\2\2\2\13")
        buf.write("\u00a4\3\2\2\2\r\u00a9\3\2\2\2\17\u00b0\3\2\2\2\21\u00b7")
        buf.write("\3\2\2\2\23\u00bb\3\2\2\2\25\u00c3\3\2\2\2\27\u00c8\3")
        buf.write("\2\2\2\31\u00cc\3\2\2\2\33\u00d2\3\2\2\2\35\u00d5\3\2")
        buf.write("\2\2\37\u00db\3\2\2\2!\u00e4\3\2\2\2#\u00e7\3\2\2\2%\u00ec")
        buf.write("\3\2\2\2\'\u00f1\3\2\2\2)\u00f7\3\2\2\2+\u00fb\3\2\2\2")
        buf.write("-\u00fd\3\2\2\2/\u00ff\3\2\2\2\61\u0101\3\2\2\2\63\u0103")
        buf.write("\3\2\2\2\65\u0105\3\2\2\2\67\u0109\3\2\2\29\u010d\3\2")
        buf.write("\2\2;\u0110\3\2\2\2=\u0112\3\2\2\2?\u0115\3\2\2\2A\u0118")
        buf.write("\3\2\2\2C\u011a\3\2\2\2E\u011c\3\2\2\2G\u011f\3\2\2\2")
        buf.write("I\u0122\3\2\2\2K\u0125\3\2\2\2M\u0129\3\2\2\2O\u012b\3")
        buf.write("\2\2\2Q\u012d\3\2\2\2S\u012f\3\2\2\2U\u0131\3\2\2\2W\u0133")
        buf.write("\3\2\2\2Y\u0138\3\2\2\2[\u013b\3\2\2\2]\u013e\3\2\2\2")
        buf.write("_\u0140\3\2\2\2a\u0144\3\2\2\2c\u0147\3\2\2\2e\u0153\3")
        buf.write("\2\2\2g\u0160\3\2\2\2i\u0167\3\2\2\2k\u0169\3\2\2\2m\u016b")
        buf.write("\3\2\2\2o\u016e\3\2\2\2q\u0170\3\2\2\2s\u0172\3\2\2\2")
        buf.write("u\u0175\3\2\2\2w\u0177\3\2\2\2y\u017e\3\2\2\2{\u0180\3")
        buf.write("\2\2\2}\u018a\3\2\2\2\177\u018d\3\2\2\2\u0081\u0197\3")
        buf.write("\2\2\2\u0083\u01a3\3\2\2\2\u0085\u01a5\3\2\2\2\u0087\u01a7")
        buf.write("\3\2\2\2\u0089\u01aa\3\2\2\2\u008b\u01b4\3\2\2\2\u008d")
        buf.write("\u008e\7o\2\2\u008e\u008f\7c\2\2\u008f\u0090\7k\2\2\u0090")
        buf.write("\u0091\7p\2\2\u0091\4\3\2\2\2\u0092\u0093\7v\2\2\u0093")
        buf.write("\u0094\7t\2\2\u0094\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\6\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099\7c\2\2\u0099")
        buf.write("\u009a\7n\2\2\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c")
        buf.write("\b\3\2\2\2\u009d\u009e\7p\2\2\u009e\u009f\7w\2\2\u009f")
        buf.write("\u00a0\7o\2\2\u00a0\u00a1\7d\2\2\u00a1\u00a2\7g\2\2\u00a2")
        buf.write("\u00a3\7t\2\2\u00a3\n\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5")
        buf.write("\u00a6\7q\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7n\2\2\u00a8")
        buf.write("\f\3\2\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7v\2\2\u00ab")
        buf.write("\u00ac\7t\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae")
        buf.write("\u00af\7i\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1")
        buf.write("\u00b2\7g\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7w\2\2\u00b4")
        buf.write("\u00b5\7t\2\2\u00b5\u00b6\7p\2\2\u00b6\20\3\2\2\2\u00b7")
        buf.write("\u00b8\7x\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\22\3\2\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7{\2\2\u00bd")
        buf.write("\u00be\7p\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7o\2\2\u00c0")
        buf.write("\u00c1\7k\2\2\u00c1\u00c2\7e\2\2\u00c2\24\3\2\2\2\u00c3")
        buf.write("\u00c4\7h\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\u00c7\7e\2\2\u00c7\26\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9")
        buf.write("\u00ca\7q\2\2\u00ca\u00cb\7t\2\2\u00cb\30\3\2\2\2\u00cc")
        buf.write("\u00cd\7w\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf")
        buf.write("\u00d0\7k\2\2\u00d0\u00d1\7n\2\2\u00d1\32\3\2\2\2\u00d2")
        buf.write("\u00d3\7d\2\2\u00d3\u00d4\7{\2\2\u00d4\34\3\2\2\2\u00d5")
        buf.write("\u00d6\7d\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7m\2\2\u00da\36\3\2\2\2\u00db")
        buf.write("\u00dc\7e\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1")
        buf.write("\u00e2\7w\2\2\u00e2\u00e3\7g\2\2\u00e3 \3\2\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7h\2\2\u00e6\"\3\2\2\2\u00e7")
        buf.write("\u00e8\7g\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7u\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb$\3\2\2\2\u00ec\u00ed\7g\2\2\u00ed")
        buf.write("\u00ee\7n\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7h\2\2\u00f0")
        buf.write("&\3\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\u00f4\7i\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write("(\3\2\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\u00fa\7f\2\2\u00fa*\3\2\2\2\u00fb\u00fc\7-\2\2\u00fc")
        buf.write(",\3\2\2\2\u00fd\u00fe\7/\2\2\u00fe.\3\2\2\2\u00ff\u0100")
        buf.write("\7,\2\2\u0100\60\3\2\2\2\u0101\u0102\7\61\2\2\u0102\62")
        buf.write("\3\2\2\2\u0103\u0104\7\'\2\2\u0104\64\3\2\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7q\2\2\u0107\u0108\7v\2\2\u0108\66")
        buf.write("\3\2\2\2\u0109\u010a\7c\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7f\2\2\u010c8\3\2\2\2\u010d\u010e\7q\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f:\3\2\2\2\u0110\u0111\7?\2\2\u0111<\3\2\2")
        buf.write("\2\u0112\u0113\7>\2\2\u0113\u0114\7/\2\2\u0114>\3\2\2")
        buf.write("\2\u0115\u0116\7#\2\2\u0116\u0117\7?\2\2\u0117@\3\2\2")
        buf.write("\2\u0118\u0119\7>\2\2\u0119B\3\2\2\2\u011a\u011b\7@\2")
        buf.write("\2\u011bD\3\2\2\2\u011c\u011d\7>\2\2\u011d\u011e\7?\2")
        buf.write("\2\u011eF\3\2\2\2\u011f\u0120\7@\2\2\u0120\u0121\7?\2")
        buf.write("\2\u0121H\3\2\2\2\u0122\u0123\7?\2\2\u0123\u0124\7?\2")
        buf.write("\2\u0124J\3\2\2\2\u0125\u0126\7\60\2\2\u0126\u0127\7\60")
        buf.write("\2\2\u0127\u0128\7\60\2\2\u0128L\3\2\2\2\u0129\u012a\7")
        buf.write("*\2\2\u012aN\3\2\2\2\u012b\u012c\7+\2\2\u012cP\3\2\2\2")
        buf.write("\u012d\u012e\7]\2\2\u012eR\3\2\2\2\u012f\u0130\7_\2\2")
        buf.write("\u0130T\3\2\2\2\u0131\u0132\7.\2\2\u0132V\3\2\2\2\u0133")
        buf.write("\u0134\t\2\2\2\u0134X\3\2\2\2\u0135\u0137\t\3\2\2\u0136")
        buf.write("\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139Z\3\2\2\2\u013a\u0138\3\2\2")
        buf.write("\2\u013b\u013c\5W,\2\u013c\u013d\5Y-\2\u013d\\\3\2\2\2")
        buf.write("\u013e\u013f\7\62\2\2\u013f^\3\2\2\2\u0140\u0141\t\4\2")
        buf.write("\2\u0141`\3\2\2\2\u0142\u0145\5]/\2\u0143\u0145\5_\60")
        buf.write("\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145b\3\2")
        buf.write("\2\2\u0146\u0148\5a\61\2\u0147\u0146\3\2\2\2\u0148\u0149")
        buf.write("\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("d\3\2\2\2\u014b\u014f\7\60\2\2\u014c\u014e\5a\61\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0154\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0152\u0154\3\2\2\2\u0153\u014b\3\2\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154f\3\2\2\2\u0155\u0158\t\5\2\2\u0156\u0159")
        buf.write("\t\6\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u015c\5a\61\2")
        buf.write("\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015d\u015e\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u0161")
        buf.write("\3\2\2\2\u0160\u0155\3\2\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write("h\3\2\2\2\u0162\u0163\5c\62\2\u0163\u0164\5e\63\2\u0164")
        buf.write("\u0165\5g\64\2\u0165\u0168\3\2\2\2\u0166\u0168\5]/\2\u0167")
        buf.write("\u0162\3\2\2\2\u0167\u0166\3\2\2\2\u0168j\3\2\2\2\u0169")
        buf.write("\u016a\t\7\2\2\u016al\3\2\2\2\u016b\u016c\5k\66\2\u016c")
        buf.write("\u016d\5o8\2\u016dn\3\2\2\2\u016e\u016f\t\b\2\2\u016f")
        buf.write("p\3\2\2\2\u0170\u0171\n\b\2\2\u0171r\3\2\2\2\u0172\u0173")
        buf.write("\5k\66\2\u0173\u0174\5q9\2\u0174t\3\2\2\2\u0175\u0176")
        buf.write("\n\t\2\2\u0176v\3\2\2\2\u0177\u0178\t\n\2\2\u0178\u0179")
        buf.write("\t\13\2\2\u0179x\3\2\2\2\u017a\u017f\5m\67\2\u017b\u017f")
        buf.write("\5w<\2\u017c\u017f\5u;\2\u017d\u017f\5\u0083B\2\u017e")
        buf.write("\u017a\3\2\2\2\u017e\u017b\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017d\3\2\2\2\u017fz\3\2\2\2\u0180\u0184\t\13\2")
        buf.write("\2\u0181\u0183\5y=\2\u0182\u0181\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\t\13\2\2\u0188")
        buf.write("\u0189\b>\2\2\u0189|\3\2\2\2\u018a\u018b\7%\2\2\u018b")
        buf.write("\u018c\7%\2\2\u018c~\3\2\2\2\u018d\u0191\5}?\2\u018e\u0190")
        buf.write("\5\u0085C\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0194\u0195\b@\3\2\u0195\u0080\3")
        buf.write("\2\2\2\u0196\u0198\t\f\2\2\u0197\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019c\bA\3\2\u019c\u0082\3\2\2\2")
        buf.write("\u019d\u01a4\7\17\2\2\u019e\u01a0\7\17\2\2\u019f\u019e")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a2\7\f\2\2\u01a2\u01a4\bB\4\2\u01a3\u019d\3\2\2\2")
        buf.write("\u01a3\u019f\3\2\2\2\u01a4\u0084\3\2\2\2\u01a5\u01a6\n")
        buf.write("\r\2\2\u01a6\u0086\3\2\2\2\u01a7\u01a8\13\2\2\2\u01a8")
        buf.write("\u01a9\bD\5\2\u01a9\u0088\3\2\2\2\u01aa\u01ae\t\13\2\2")
        buf.write("\u01ab\u01ad\5y=\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0\3\2")
        buf.write("\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\7\2\2\3\u01b2")
        buf.write("\u01b3\bE\6\2\u01b3\u008a\3\2\2\2\u01b4\u01b8\t\13\2\2")
        buf.write("\u01b5\u01b7\5y=\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2")
        buf.write("\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\5s:\2\u01bc\u01bd")
        buf.write("\bF\7\2\u01bd\u008c\3\2\2\2\24\2\u0138\u0144\u0149\u014f")
        buf.write("\u0153\u0158\u015d\u0160\u0167\u017e\u0184\u0191\u0199")
        buf.write("\u019f\u01a3\u01ae\u01b8\b\3>\2\b\2\2\3B\3\3D\4\3E\5\3")
        buf.write("F\6")
        return buf.getvalue()


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
            "'>='", "'=='", "'...'", "'('", "')'", "'['", "']'", "','" ]

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
                  "SEP_CLOSE_BRACK", "SEP_COMA", "IDENTIFIER_HEAD", "IDENTIFIER_TAIL", 
                  "IDENTIFIER", "ZERO", "NON_ZERO_DIGIT", "DIGIT", "DECIMAL", 
                  "FLOATING_POINT", "EXPONENTIAL", "NUMBER", "ESCAPE_SIGN", 
                  "ESCAPE_SEQUENCE", "ESCAPE_REP", "NOT_ESCAPE_REP", "ILLEGAL_ESCAPE_SEQ", 
                  "STRING_CHAR", "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", 
                  "STRING", "COMMENT_HEAD", "COMMENT", "WS", "NEW_LINE", 
                  "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[60] = self.STRING_action 
            actions[64] = self.NEW_LINE_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEW_LINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = '\n'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     


