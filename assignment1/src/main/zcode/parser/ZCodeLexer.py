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
        buf.write("\u01bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\61\3\62\3\62\7\62\u0149\n\62\f\62\16\62\u014c\13\62")
        buf.write("\3\63\3\63\7\63\u0150\n\63\f\63\16\63\u0153\13\63\3\63")
        buf.write("\5\63\u0156\n\63\3\64\3\64\5\64\u015a\n\64\3\64\3\64\7")
        buf.write("\64\u015e\n\64\f\64\16\64\u0161\13\64\3\64\5\64\u0164")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u016b\n\65\3\66\3")
        buf.write("\66\3\67\3\67\3\67\38\38\38\38\39\39\3:\3:\3;\3;\3;\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\5=\u0184\n=\3>\3>\7>\u0188\n>\f>\16")
        buf.write(">\u018b\13>\3>\3>\3>\3?\3?\3?\3@\3@\7@\u0195\n@\f@\16")
        buf.write("@\u0198\13@\3@\3@\3A\6A\u019d\nA\rA\16A\u019e\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3D\3E\3E\7E\u01ac\nE\fE\16E\u01af\13")
        buf.write("E\3E\3E\3E\3F\3F\7F\u01b6\nF\fF\16F\u01b9\13F\3F\3F\3")
        buf.write("F\2\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W\2Y\2[-]\2_\2a\2c\2e\2g\2i.k\2m\2o\2q\2s\2")
        buf.write("u\2w\2y\2{/}\2\177\60\u0081\61\u0083\62\u0085\2\u0087")
        buf.write("\63\u0089\64\u008b\65\3\2\16\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\63;\4\2GGgg\4\2--//\5\2\f\f$$^^\3\2^^\n\2$$))^^")
        buf.write("ddhhppttvv\3\2))\3\2$$\5\2\n\13\16\17\"\"\3\2\f\f\2\u01bb")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2[\3\2\2\2\2i\3\2\2\2\2{\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0092")
        buf.write("\3\2\2\2\7\u0097\3\2\2\2\t\u009d\3\2\2\2\13\u00a4\3\2")
        buf.write("\2\2\r\u00a9\3\2\2\2\17\u00b0\3\2\2\2\21\u00b7\3\2\2\2")
        buf.write("\23\u00bb\3\2\2\2\25\u00c3\3\2\2\2\27\u00c8\3\2\2\2\31")
        buf.write("\u00cc\3\2\2\2\33\u00d2\3\2\2\2\35\u00d5\3\2\2\2\37\u00db")
        buf.write("\3\2\2\2!\u00e4\3\2\2\2#\u00e7\3\2\2\2%\u00ec\3\2\2\2")
        buf.write("\'\u00f1\3\2\2\2)\u00f7\3\2\2\2+\u00fb\3\2\2\2-\u00fd")
        buf.write("\3\2\2\2/\u00ff\3\2\2\2\61\u0101\3\2\2\2\63\u0103\3\2")
        buf.write("\2\2\65\u0105\3\2\2\2\67\u0109\3\2\2\29\u010d\3\2\2\2")
        buf.write(";\u0110\3\2\2\2=\u0112\3\2\2\2?\u0115\3\2\2\2A\u0118\3")
        buf.write("\2\2\2C\u011a\3\2\2\2E\u011c\3\2\2\2G\u011f\3\2\2\2I\u0122")
        buf.write("\3\2\2\2K\u0125\3\2\2\2M\u0129\3\2\2\2O\u012b\3\2\2\2")
        buf.write("Q\u012d\3\2\2\2S\u012f\3\2\2\2U\u0131\3\2\2\2W\u0133\3")
        buf.write("\2\2\2Y\u0138\3\2\2\2[\u013b\3\2\2\2]\u013e\3\2\2\2_\u0140")
        buf.write("\3\2\2\2a\u0144\3\2\2\2c\u0146\3\2\2\2e\u0155\3\2\2\2")
        buf.write("g\u0163\3\2\2\2i\u016a\3\2\2\2k\u016c\3\2\2\2m\u016e\3")
        buf.write("\2\2\2o\u0171\3\2\2\2q\u0175\3\2\2\2s\u0177\3\2\2\2u\u0179")
        buf.write("\3\2\2\2w\u017c\3\2\2\2y\u0183\3\2\2\2{\u0185\3\2\2\2")
        buf.write("}\u018f\3\2\2\2\177\u0192\3\2\2\2\u0081\u019c\3\2\2\2")
        buf.write("\u0083\u01a2\3\2\2\2\u0085\u01a4\3\2\2\2\u0087\u01a6\3")
        buf.write("\2\2\2\u0089\u01a9\3\2\2\2\u008b\u01b3\3\2\2\2\u008d\u008e")
        buf.write("\7o\2\2\u008e\u008f\7c\2\2\u008f\u0090\7k\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\4\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096\6")
        buf.write("\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099\7c\2\2\u0099\u009a")
        buf.write("\7n\2\2\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c\b")
        buf.write("\3\2\2\2\u009d\u009e\7p\2\2\u009e\u009f\7w\2\2\u009f\u00a0")
        buf.write("\7o\2\2\u00a0\u00a1\7d\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\n\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7n\2\2\u00a8\f")
        buf.write("\3\2\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7i\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7p\2\2\u00b6\20\3\2\2\2\u00b7\u00b8")
        buf.write("\7x\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7t\2\2\u00ba\22")
        buf.write("\3\2\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7{\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7o\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7e\2\2\u00c2\24\3\2\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7e\2\2\u00c7\26\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca")
        buf.write("\7q\2\2\u00ca\u00cb\7t\2\2\u00cb\30\3\2\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7n\2\2\u00d1\32\3\2\2\2\u00d2\u00d3")
        buf.write("\7d\2\2\u00d3\u00d4\7{\2\2\u00d4\34\3\2\2\2\u00d5\u00d6")
        buf.write("\7d\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7c\2\2\u00d9\u00da\7m\2\2\u00da\36\3\2\2\2\u00db\u00dc")
        buf.write("\7e\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7w\2\2\u00e2\u00e3\7g\2\2\u00e3 \3\2\2\2\u00e4\u00e5")
        buf.write("\7k\2\2\u00e5\u00e6\7h\2\2\u00e6\"\3\2\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb$\3\2\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7h\2\2\u00f0&\3")
        buf.write("\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4")
        buf.write("\7i\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6(\3")
        buf.write("\2\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7f\2\2\u00fa*\3\2\2\2\u00fb\u00fc\7-\2\2\u00fc,\3\2\2")
        buf.write("\2\u00fd\u00fe\7/\2\2\u00fe.\3\2\2\2\u00ff\u0100\7,\2")
        buf.write("\2\u0100\60\3\2\2\2\u0101\u0102\7\61\2\2\u0102\62\3\2")
        buf.write("\2\2\u0103\u0104\7\'\2\2\u0104\64\3\2\2\2\u0105\u0106")
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
        buf.write("\2\2\u0146\u014a\5_\60\2\u0147\u0149\5a\61\2\u0148\u0147")
        buf.write("\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014bd\3\2\2\2\u014c\u014a\3\2\2\2\u014d")
        buf.write("\u0151\7\60\2\2\u014e\u0150\5a\61\2\u014f\u014e\3\2\2")
        buf.write("\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0156\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u0156\3\2\2\2\u0155\u014d\3\2\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0156f\3\2\2\2\u0157\u0159\t\5\2\2\u0158\u015a\t\6\2")
        buf.write("\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015f\5_\60\2\u015c\u015e\5a\61\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\u0164\3\2\2\2\u0161\u015f\3")
        buf.write("\2\2\2\u0162\u0164\3\2\2\2\u0163\u0157\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164h\3\2\2\2\u0165\u0166\5c\62\2\u0166\u0167")
        buf.write("\5e\63\2\u0167\u0168\5g\64\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u016b\5]/\2\u016a\u0165\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("j\3\2\2\2\u016c\u016d\n\7\2\2\u016dl\3\2\2\2\u016e\u016f")
        buf.write("\13\2\2\2\u016f\u0170\t\b\2\2\u0170n\3\2\2\2\u0171\u0172")
        buf.write("\13\2\2\2\u0172\u0173\5m\67\2\u0173\u0174\5q9\2\u0174")
        buf.write("p\3\2\2\2\u0175\u0176\t\t\2\2\u0176r\3\2\2\2\u0177\u0178")
        buf.write("\n\t\2\2\u0178t\3\2\2\2\u0179\u017a\5m\67\2\u017a\u017b")
        buf.write("\5s:\2\u017bv\3\2\2\2\u017c\u017d\t\n\2\2\u017d\u017e")
        buf.write("\t\13\2\2\u017ex\3\2\2\2\u017f\u0184\5k\66\2\u0180\u0184")
        buf.write("\5o8\2\u0181\u0184\5w<\2\u0182\u0184\5\u0083B\2\u0183")
        buf.write("\u017f\3\2\2\2\u0183\u0180\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184z\3\2\2\2\u0185\u0189\t\13\2")
        buf.write("\2\u0186\u0188\5y=\2\u0187\u0186\3\2\2\2\u0188\u018b\3")
        buf.write("\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\t\13\2\2\u018d")
        buf.write("\u018e\b>\2\2\u018e|\3\2\2\2\u018f\u0190\7%\2\2\u0190")
        buf.write("\u0191\7%\2\2\u0191~\3\2\2\2\u0192\u0196\5}?\2\u0193\u0195")
        buf.write("\5\u0085C\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0199\u019a\b@\3\2\u019a\u0080\3")
        buf.write("\2\2\2\u019b\u019d\t\f\2\2\u019c\u019b\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\bA\3\2\u01a1\u0082\3\2\2\2")
        buf.write("\u01a2\u01a3\t\r\2\2\u01a3\u0084\3\2\2\2\u01a4\u01a5\n")
        buf.write("\r\2\2\u01a5\u0086\3\2\2\2\u01a6\u01a7\13\2\2\2\u01a7")
        buf.write("\u01a8\bD\4\2\u01a8\u0088\3\2\2\2\u01a9\u01ad\t\13\2\2")
        buf.write("\u01aa\u01ac\5y=\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2")
        buf.write("\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\7\2\2\3\u01b1")
        buf.write("\u01b2\bE\5\2\u01b2\u008a\3\2\2\2\u01b3\u01b7\t\13\2\2")
        buf.write("\u01b4\u01b6\5y=\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3\2")
        buf.write("\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bb\5u;\2\u01bb\u01bc")
        buf.write("\bF\6\2\u01bc\u008c\3\2\2\2\22\2\u0138\u0144\u014a\u0151")
        buf.write("\u0155\u0159\u015f\u0163\u016a\u0183\u0189\u0196\u019e")
        buf.write("\u01ad\u01b7\7\3>\2\b\2\2\3D\3\3E\4\3F\5")
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
                  "FLOATING_POINT", "EXPONENTIAL", "NUMBER", "STRING_CHAR", 
                  "ESCAPE_SIGN", "ESCAPE_SEQUENCE", "ESCAPE_REP", "NOT_ESCAPE_REP", 
                  "ILLEGAL_ESCAPE_SEQ", "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", 
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
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


