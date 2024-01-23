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
        buf.write("\u01bc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\5\3\u008d\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\6.\u0133\n.\r.\16")
        buf.write(".\u0134\3.\7.\u0138\n.\f.\16.\u013b\13.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\5\61\u0143\n\61\3\62\3\62\7\62\u0147\n\62\f")
        buf.write("\62\16\62\u014a\13\62\3\63\3\63\5\63\u014e\n\63\3\63\3")
        buf.write("\63\7\63\u0152\n\63\f\63\16\63\u0155\13\63\3\64\3\64\7")
        buf.write("\64\u0159\n\64\f\64\16\64\u015c\13\64\3\64\7\64\u015f")
        buf.write("\n\64\f\64\16\64\u0162\13\64\3\64\7\64\u0165\n\64\f\64")
        buf.write("\16\64\u0168\13\64\3\64\5\64\u016b\n\64\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\39\39\39\59\u017c")
        buf.write("\n9\3:\3:\7:\u0180\n:\f:\16:\u0183\13:\3:\3:\3:\3;\3;")
        buf.write("\3;\3<\3<\7<\u018d\n<\f<\16<\u0190\13<\3<\3<\3=\6=\u0195")
        buf.write("\n=\r=\16=\u0196\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\7A\u01a4")
        buf.write("\nA\fA\16A\u01a7\13A\3A\3A\3A\3B\3B\7B\u01ae\nB\fB\16")
        buf.write("B\u01b1\13B\3B\3B\7B\u01b5\nB\fB\16B\u01b8\13B\3B\3B\3")
        buf.write("B\2\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y\2[.]\2_\2a\2c\2e\2g/i\2k\2m\2o\2q\2s\60")
        buf.write("u\2w\61y\62{\63}\2\177\64\u0081\65\u0083\66\3\2\r\5\2")
        buf.write("C\\aac|\5\2\62;C\\c|\3\2\63;\4\2GGgg\4\2--//\7\2\n\f\16")
        buf.write("\17$$))^^\3\2^^\3\2$$\3\2))\5\2\n\13\16\17\"\"\3\2\f\f")
        buf.write("\2\u01c1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2[\3\2\2\2\2g\3\2")
        buf.write("\2\2\2s\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2")
        buf.write("\2\5\u008c\3\2\2\2\7\u008e\3\2\2\2\t\u0093\3\2\2\2\13")
        buf.write("\u0099\3\2\2\2\r\u00a0\3\2\2\2\17\u00a5\3\2\2\2\21\u00ac")
        buf.write("\3\2\2\2\23\u00b3\3\2\2\2\25\u00b7\3\2\2\2\27\u00bf\3")
        buf.write("\2\2\2\31\u00c4\3\2\2\2\33\u00c8\3\2\2\2\35\u00ce\3\2")
        buf.write("\2\2\37\u00d1\3\2\2\2!\u00d7\3\2\2\2#\u00e0\3\2\2\2%\u00e3")
        buf.write("\3\2\2\2\'\u00e8\3\2\2\2)\u00ed\3\2\2\2+\u00f3\3\2\2\2")
        buf.write("-\u00f7\3\2\2\2/\u00f9\3\2\2\2\61\u00fb\3\2\2\2\63\u00fd")
        buf.write("\3\2\2\2\65\u00ff\3\2\2\2\67\u0101\3\2\2\29\u0105\3\2")
        buf.write("\2\2;\u0109\3\2\2\2=\u010c\3\2\2\2?\u010e\3\2\2\2A\u0111")
        buf.write("\3\2\2\2C\u0114\3\2\2\2E\u0116\3\2\2\2G\u0118\3\2\2\2")
        buf.write("I\u011b\3\2\2\2K\u011e\3\2\2\2M\u0121\3\2\2\2O\u0125\3")
        buf.write("\2\2\2Q\u0127\3\2\2\2S\u0129\3\2\2\2U\u012b\3\2\2\2W\u012d")
        buf.write("\3\2\2\2Y\u012f\3\2\2\2[\u0132\3\2\2\2]\u013c\3\2\2\2")
        buf.write("_\u013e\3\2\2\2a\u0142\3\2\2\2c\u0144\3\2\2\2e\u014b\3")
        buf.write("\2\2\2g\u016a\3\2\2\2i\u016c\3\2\2\2k\u016e\3\2\2\2m\u0171")
        buf.write("\3\2\2\2o\u0175\3\2\2\2q\u017b\3\2\2\2s\u017d\3\2\2\2")
        buf.write("u\u0187\3\2\2\2w\u018a\3\2\2\2y\u0194\3\2\2\2{\u019a\3")
        buf.write("\2\2\2}\u019c\3\2\2\2\177\u019e\3\2\2\2\u0081\u01a1\3")
        buf.write("\2\2\2\u0083\u01ab\3\2\2\2\u0085\u0086\7o\2\2\u0086\u0087")
        buf.write("\7c\2\2\u0087\u0088\7k\2\2\u0088\u0089\7p\2\2\u0089\4")
        buf.write("\3\2\2\2\u008a\u008d\5\7\4\2\u008b\u008d\5\t\5\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\6\3\2\2\2\u008e")
        buf.write("\u008f\7v\2\2\u008f\u0090\7t\2\2\u0090\u0091\7w\2\2\u0091")
        buf.write("\u0092\7g\2\2\u0092\b\3\2\2\2\u0093\u0094\7h\2\2\u0094")
        buf.write("\u0095\7c\2\2\u0095\u0096\7n\2\2\u0096\u0097\7u\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\n\3\2\2\2\u0099\u009a\7p\2\2\u009a")
        buf.write("\u009b\7w\2\2\u009b\u009c\7o\2\2\u009c\u009d\7d\2\2\u009d")
        buf.write("\u009e\7g\2\2\u009e\u009f\7t\2\2\u009f\f\3\2\2\2\u00a0")
        buf.write("\u00a1\7d\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7q\2\2\u00a3")
        buf.write("\u00a4\7n\2\2\u00a4\16\3\2\2\2\u00a5\u00a6\7u\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9")
        buf.write("\u00aa\7p\2\2\u00aa\u00ab\7i\2\2\u00ab\20\3\2\2\2\u00ac")
        buf.write("\u00ad\7t\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7v\2\2\u00af")
        buf.write("\u00b0\7w\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7p\2\2\u00b2")
        buf.write("\22\3\2\2\2\u00b3\u00b4\7x\2\2\u00b4\u00b5\7c\2\2\u00b5")
        buf.write("\u00b6\7t\2\2\u00b6\24\3\2\2\2\u00b7\u00b8\7f\2\2\u00b8")
        buf.write("\u00b9\7{\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7c\2\2\u00bb")
        buf.write("\u00bc\7o\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7e\2\2\u00be")
        buf.write("\26\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1\7w\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\u00c3\7e\2\2\u00c3\30\3\2\2\2\u00c4")
        buf.write("\u00c5\7h\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7t\2\2\u00c7")
        buf.write("\32\3\2\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7n\2\2\u00cd")
        buf.write("\34\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0\7{\2\2\u00d0")
        buf.write("\36\3\2\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3\7t\2\2\u00d3")
        buf.write("\u00d4\7g\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7m\2\2\u00d6")
        buf.write(" \3\2\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u00da\7p\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7k\2\2\u00dc")
        buf.write("\u00dd\7p\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7g\2\2\u00df")
        buf.write("\"\3\2\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7h\2\2\u00e2")
        buf.write("$\3\2\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7n\2\2\u00e5")
        buf.write("\u00e6\7u\2\2\u00e6\u00e7\7g\2\2\u00e7&\3\2\2\2\u00e8")
        buf.write("\u00e9\7g\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7k\2\2\u00eb")
        buf.write("\u00ec\7h\2\2\u00ec(\3\2\2\2\u00ed\u00ee\7d\2\2\u00ee")
        buf.write("\u00ef\7g\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1\7k\2\2\u00f1")
        buf.write("\u00f2\7p\2\2\u00f2*\3\2\2\2\u00f3\u00f4\7g\2\2\u00f4")
        buf.write("\u00f5\7p\2\2\u00f5\u00f6\7f\2\2\u00f6,\3\2\2\2\u00f7")
        buf.write("\u00f8\7-\2\2\u00f8.\3\2\2\2\u00f9\u00fa\7/\2\2\u00fa")
        buf.write("\60\3\2\2\2\u00fb\u00fc\7,\2\2\u00fc\62\3\2\2\2\u00fd")
        buf.write("\u00fe\7\61\2\2\u00fe\64\3\2\2\2\u00ff\u0100\7\'\2\2\u0100")
        buf.write("\66\3\2\2\2\u0101\u0102\7p\2\2\u0102\u0103\7q\2\2\u0103")
        buf.write("\u0104\7v\2\2\u01048\3\2\2\2\u0105\u0106\7c\2\2\u0106")
        buf.write("\u0107\7p\2\2\u0107\u0108\7f\2\2\u0108:\3\2\2\2\u0109")
        buf.write("\u010a\7q\2\2\u010a\u010b\7t\2\2\u010b<\3\2\2\2\u010c")
        buf.write("\u010d\7?\2\2\u010d>\3\2\2\2\u010e\u010f\7>\2\2\u010f")
        buf.write("\u0110\7/\2\2\u0110@\3\2\2\2\u0111\u0112\7#\2\2\u0112")
        buf.write("\u0113\7?\2\2\u0113B\3\2\2\2\u0114\u0115\7>\2\2\u0115")
        buf.write("D\3\2\2\2\u0116\u0117\7@\2\2\u0117F\3\2\2\2\u0118\u0119")
        buf.write("\7>\2\2\u0119\u011a\7?\2\2\u011aH\3\2\2\2\u011b\u011c")
        buf.write("\7@\2\2\u011c\u011d\7?\2\2\u011dJ\3\2\2\2\u011e\u011f")
        buf.write("\7?\2\2\u011f\u0120\7?\2\2\u0120L\3\2\2\2\u0121\u0122")
        buf.write("\7\60\2\2\u0122\u0123\7\60\2\2\u0123\u0124\7\60\2\2\u0124")
        buf.write("N\3\2\2\2\u0125\u0126\7*\2\2\u0126P\3\2\2\2\u0127\u0128")
        buf.write("\7+\2\2\u0128R\3\2\2\2\u0129\u012a\7]\2\2\u012aT\3\2\2")
        buf.write("\2\u012b\u012c\7_\2\2\u012cV\3\2\2\2\u012d\u012e\7.\2")
        buf.write("\2\u012eX\3\2\2\2\u012f\u0130\t\2\2\2\u0130Z\3\2\2\2\u0131")
        buf.write("\u0133\5Y-\2\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0139\3\2\2\2")
        buf.write("\u0136\u0138\t\3\2\2\u0137\u0136\3\2\2\2\u0138\u013b\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\\")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\7\62\2\2\u013d")
        buf.write("^\3\2\2\2\u013e\u013f\t\4\2\2\u013f`\3\2\2\2\u0140\u0143")
        buf.write("\5]/\2\u0141\u0143\5_\60\2\u0142\u0140\3\2\2\2\u0142\u0141")
        buf.write("\3\2\2\2\u0143b\3\2\2\2\u0144\u0148\7\60\2\2\u0145\u0147")
        buf.write("\5a\61\2\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149d\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014b\u014d\t\5\2\2\u014c\u014e\t\6\2\2")
        buf.write("\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3")
        buf.write("\2\2\2\u014f\u0153\5_\60\2\u0150\u0152\5a\61\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154f\3\2\2\2\u0155\u0153\3\2\2\2\u0156")
        buf.write("\u015a\5_\60\2\u0157\u0159\5a\61\2\u0158\u0157\3\2\2\2")
        buf.write("\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3")
        buf.write("\2\2\2\u015b\u0160\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015f")
        buf.write("\5c\62\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0166\3\2\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0163\u0165\5e\63\2\u0164\u0163\3")
        buf.write("\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u016b\3\2\2\2\u0168\u0166\3\2\2\2\u0169")
        buf.write("\u016b\5]/\2\u016a\u0156\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("h\3\2\2\2\u016c\u016d\n\7\2\2\u016dj\3\2\2\2\u016e\u016f")
        buf.write("\13\2\2\2\u016f\u0170\t\b\2\2\u0170l\3\2\2\2\u0171\u0172")
        buf.write("\13\2\2\2\u0172\u0173\5k\66\2\u0173\u0174\n\t\2\2\u0174")
        buf.write("n\3\2\2\2\u0175\u0176\t\n\2\2\u0176\u0177\t\t\2\2\u0177")
        buf.write("p\3\2\2\2\u0178\u017c\5m\67\2\u0179\u017c\5o8\2\u017a")
        buf.write("\u017c\5i\65\2\u017b\u0178\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017a\3\2\2\2\u017cr\3\2\2\2\u017d\u0181\t\t\2")
        buf.write("\2\u017e\u0180\5q9\2\u017f\u017e\3\2\2\2\u0180\u0183\3")
        buf.write("\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\t\t\2\2\u0185")
        buf.write("\u0186\b:\2\2\u0186t\3\2\2\2\u0187\u0188\7%\2\2\u0188")
        buf.write("\u0189\7%\2\2\u0189v\3\2\2\2\u018a\u018e\5u;\2\u018b\u018d")
        buf.write("\5}?\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0191\u0192\b<\3\2\u0192x\3\2\2\2\u0193")
        buf.write("\u0195\t\13\2\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2")
        buf.write("\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u0199\b=\3\2\u0199z\3\2\2\2\u019a\u019b")
        buf.write("\7\f\2\2\u019b|\3\2\2\2\u019c\u019d\n\f\2\2\u019d~\3\2")
        buf.write("\2\2\u019e\u019f\13\2\2\2\u019f\u01a0\b@\4\2\u01a0\u0080")
        buf.write("\3\2\2\2\u01a1\u01a5\t\t\2\2\u01a2\u01a4\5q9\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a8\u01a9\7\2\2\3\u01a9\u01aa\bA\5\2\u01aa\u0082\3")
        buf.write("\2\2\2\u01ab\u01af\t\t\2\2\u01ac\u01ae\5q9\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b2\u01b6\5k\66\2\u01b3\u01b5\5q9\2\u01b4\u01b3\3\2")
        buf.write("\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9")
        buf.write("\u01ba\t\t\2\2\u01ba\u01bb\bB\6\2\u01bb\u0084\3\2\2\2")
        buf.write("\25\2\u008c\u0134\u0139\u0142\u0148\u014d\u0153\u015a")
        buf.write("\u0160\u0166\u016a\u017b\u0181\u018e\u0196\u01a5\u01af")
        buf.write("\u01b6\7\3:\2\b\2\2\3@\3\3A\4\3B\5")
        return buf.getvalue()


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
    OP_ASSIGN = 31
    OP_NOT_EQUAL = 32
    OP_SMALLER = 33
    OP_GREATER = 34
    OP_SMALLER_EQUAL = 35
    OP_GREATER_EQUAL = 36
    OP_STRING_EQUAL = 37
    OP_STRING_CONCAT = 38
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
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN_TOKEN", "BOOL", "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", 
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

    ruleNames = [ "MAIN_TOKEN", "BOOL", "KW_TRUE", "KW_FALSE", "KW_NUMBER", 
                  "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                  "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                  "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                  "KW_END", "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", 
                  "OP_REMAINDER", "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", 
                  "OP_ASSIGN", "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", 
                  "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", "OP_STRING_EQUAL", 
                  "OP_STRING_CONCAT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
                  "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "IDENTIFIER_HEAD", 
                  "IDENTIFIER", "ZERO", "NON_ZERO_DIGIT", "DIGIT", "FLOATING_POINT", 
                  "EXPONENTIAL", "NUMBER", "STRING_CHAR", "ESCAPE_SIGN", 
                  "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", "STRING_LITTERAL", 
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
     


