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
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\7-\u013b")
        buf.write("\n-\f-\16-\u013e\13-\3-\3-\3.\6.\u0143\n.\r.\16.\u0144")
        buf.write("\3.\3.\3/\3/\3/\5/\u014c\n/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\7\63\u0158\n\63\f\63\16\63\u015b")
        buf.write("\13\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\5")
        buf.write("\67\u0166\n\67\38\68\u0169\n8\r8\168\u016a\39\39\79\u016f")
        buf.write("\n9\f9\169\u0172\139\39\59\u0175\n9\3:\3:\3:\5:\u017a")
        buf.write("\n:\3:\6:\u017d\n:\r:\16:\u017e\3:\5:\u0182\n:\3;\3;\3")
        buf.write(";\3;\3;\5;\u0189\n;\3<\3<\3=\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("@\3A\3A\3B\3B\3B\3C\3C\3C\5C\u019f\nC\3D\3D\3D\7D\u01a4")
        buf.write("\nD\fD\16D\u01a7\13D\3D\3D\3D\3E\3E\3E\3F\3F\3F\7F\u01b2")
        buf.write("\nF\fF\16F\u01b5\13F\3F\3F\3F\3G\3G\3G\7G\u01bd\nG\fG")
        buf.write("\16G\u01c0\13G\3G\3G\3G\2\2H\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y-[.]/_\2a\2c\2")
        buf.write("e\2g\60i\2k\2m\2o\2q\2s\2u\61w\2y\2{\2}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\62\u0089\63\u008b\64\u008d\65")
        buf.write("\3\2\16\5\2\n\13\16\16\"\"\4\2\f\f\17\17\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\63;\4\2GGgg\4\2--//\3\2^^\t\2))^^dd")
        buf.write("hhppttvv\6\2\f\f\17\17$$^^\3\2))\3\2$$\2\u01c5\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2g\3\2\2\2\2u")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0094\3\2\2\2\7\u0099")
        buf.write("\3\2\2\2\t\u009f\3\2\2\2\13\u00a6\3\2\2\2\r\u00ab\3\2")
        buf.write("\2\2\17\u00b2\3\2\2\2\21\u00b9\3\2\2\2\23\u00bd\3\2\2")
        buf.write("\2\25\u00c5\3\2\2\2\27\u00ca\3\2\2\2\31\u00ce\3\2\2\2")
        buf.write("\33\u00d4\3\2\2\2\35\u00d7\3\2\2\2\37\u00dd\3\2\2\2!\u00e6")
        buf.write("\3\2\2\2#\u00e9\3\2\2\2%\u00ee\3\2\2\2\'\u00f3\3\2\2\2")
        buf.write(")\u00f9\3\2\2\2+\u00fd\3\2\2\2-\u00ff\3\2\2\2/\u0101\3")
        buf.write("\2\2\2\61\u0103\3\2\2\2\63\u0105\3\2\2\2\65\u0107\3\2")
        buf.write("\2\2\67\u010b\3\2\2\29\u010f\3\2\2\2;\u0112\3\2\2\2=\u0114")
        buf.write("\3\2\2\2?\u0117\3\2\2\2A\u011a\3\2\2\2C\u011c\3\2\2\2")
        buf.write("E\u011e\3\2\2\2G\u0121\3\2\2\2I\u0124\3\2\2\2K\u0127\3")
        buf.write("\2\2\2M\u012b\3\2\2\2O\u012d\3\2\2\2Q\u012f\3\2\2\2S\u0131")
        buf.write("\3\2\2\2U\u0133\3\2\2\2W\u0135\3\2\2\2Y\u0138\3\2\2\2")
        buf.write("[\u0142\3\2\2\2]\u014b\3\2\2\2_\u014f\3\2\2\2a\u0152\3")
        buf.write("\2\2\2c\u0154\3\2\2\2e\u0159\3\2\2\2g\u015c\3\2\2\2i\u015f")
        buf.write("\3\2\2\2k\u0161\3\2\2\2m\u0165\3\2\2\2o\u0168\3\2\2\2")
        buf.write("q\u0174\3\2\2\2s\u0181\3\2\2\2u\u0188\3\2\2\2w\u018a\3")
        buf.write("\2\2\2y\u018c\3\2\2\2{\u018f\3\2\2\2}\u0191\3\2\2\2\177")
        buf.write("\u0193\3\2\2\2\u0081\u0196\3\2\2\2\u0083\u0198\3\2\2\2")
        buf.write("\u0085\u019e\3\2\2\2\u0087\u01a0\3\2\2\2\u0089\u01ab\3")
        buf.write("\2\2\2\u008b\u01ae\3\2\2\2\u008d\u01b9\3\2\2\2\u008f\u0090")
        buf.write("\7o\2\2\u0090\u0091\7c\2\2\u0091\u0092\7k\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\4\3\2\2\2\u0094\u0095\7v\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7w\2\2\u0097\u0098\7g\2\2\u0098\6")
        buf.write("\3\2\2\2\u0099\u009a\7h\2\2\u009a\u009b\7c\2\2\u009b\u009c")
        buf.write("\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e\7g\2\2\u009e\b")
        buf.write("\3\2\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2")
        buf.write("\7o\2\2\u00a2\u00a3\7d\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\n\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7n\2\2\u00aa\f")
        buf.write("\3\2\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7i\2\2\u00b1\16\3\2\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7p\2\2\u00b8\20\3\2\2\2\u00b9\u00ba")
        buf.write("\7x\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7t\2\2\u00bc\22")
        buf.write("\3\2\2\2\u00bd\u00be\7f\2\2\u00be\u00bf\7{\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7o\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7e\2\2\u00c4\24\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7t\2\2\u00cd\30\3\2\2\2\u00ce\u00cf")
        buf.write("\7w\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7n\2\2\u00d3\32\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7{\2\2\u00d6\34\3\2\2\2\u00d7\u00d8")
        buf.write("\7d\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7m\2\2\u00dc\36\3\2\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7w\2\2\u00e4\u00e5\7g\2\2\u00e5 \3\2\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7h\2\2\u00e8\"\3\2\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed$\3\2\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7h\2\2\u00f2&\3")
        buf.write("\2\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7i\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8(\3")
        buf.write("\2\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7f\2\2\u00fc*\3\2\2\2\u00fd\u00fe\7-\2\2\u00fe,\3\2\2")
        buf.write("\2\u00ff\u0100\7/\2\2\u0100.\3\2\2\2\u0101\u0102\7,\2")
        buf.write("\2\u0102\60\3\2\2\2\u0103\u0104\7\61\2\2\u0104\62\3\2")
        buf.write("\2\2\u0105\u0106\7\'\2\2\u0106\64\3\2\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7q\2\2\u0109\u010a\7v\2\2\u010a\66")
        buf.write("\3\2\2\2\u010b\u010c\7c\2\2\u010c\u010d\7p\2\2\u010d\u010e")
        buf.write("\7f\2\2\u010e8\3\2\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111:\3\2\2\2\u0112\u0113\7?\2\2\u0113<\3\2\2")
        buf.write("\2\u0114\u0115\7>\2\2\u0115\u0116\7/\2\2\u0116>\3\2\2")
        buf.write("\2\u0117\u0118\7#\2\2\u0118\u0119\7?\2\2\u0119@\3\2\2")
        buf.write("\2\u011a\u011b\7>\2\2\u011bB\3\2\2\2\u011c\u011d\7@\2")
        buf.write("\2\u011dD\3\2\2\2\u011e\u011f\7>\2\2\u011f\u0120\7?\2")
        buf.write("\2\u0120F\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123\7?\2")
        buf.write("\2\u0123H\3\2\2\2\u0124\u0125\7?\2\2\u0125\u0126\7?\2")
        buf.write("\2\u0126J\3\2\2\2\u0127\u0128\7\60\2\2\u0128\u0129\7\60")
        buf.write("\2\2\u0129\u012a\7\60\2\2\u012aL\3\2\2\2\u012b\u012c\7")
        buf.write("*\2\2\u012cN\3\2\2\2\u012d\u012e\7+\2\2\u012eP\3\2\2\2")
        buf.write("\u012f\u0130\7]\2\2\u0130R\3\2\2\2\u0131\u0132\7_\2\2")
        buf.write("\u0132T\3\2\2\2\u0133\u0134\7.\2\2\u0134V\3\2\2\2\u0135")
        buf.write("\u0136\7%\2\2\u0136\u0137\7%\2\2\u0137X\3\2\2\2\u0138")
        buf.write("\u013c\5W,\2\u0139\u013b\5a\61\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0140\b")
        buf.write("-\2\2\u0140Z\3\2\2\2\u0141\u0143\t\2\2\2\u0142\u0141\3")
        buf.write("\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\b.\2\2\u0147")
        buf.write("\\\3\2\2\2\u0148\u014c\7\f\2\2\u0149\u014c\5_\60\2\u014a")
        buf.write("\u014c\7\17\2\2\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2")
        buf.write("\2\u014b\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e")
        buf.write("\b/\3\2\u014e^\3\2\2\2\u014f\u0150\7\17\2\2\u0150\u0151")
        buf.write("\7\f\2\2\u0151`\3\2\2\2\u0152\u0153\n\3\2\2\u0153b\3\2")
        buf.write("\2\2\u0154\u0155\t\4\2\2\u0155d\3\2\2\2\u0156\u0158\t")
        buf.write("\5\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u015a\3\2\2\2\u015af\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015c\u015d\5c\62\2\u015d\u015e\5e\63\2\u015e")
        buf.write("h\3\2\2\2\u015f\u0160\7\62\2\2\u0160j\3\2\2\2\u0161\u0162")
        buf.write("\t\6\2\2\u0162l\3\2\2\2\u0163\u0166\5i\65\2\u0164\u0166")
        buf.write("\5k\66\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("n\3\2\2\2\u0167\u0169\5m\67\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016bp\3\2\2\2\u016c\u0170\7\60\2\2\u016d\u016f\5m\67")
        buf.write("\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0175\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u016c\3\2\2\2")
        buf.write("\u0174\u0173\3\2\2\2\u0175r\3\2\2\2\u0176\u0179\t\7\2")
        buf.write("\2\u0177\u017a\t\b\2\2\u0178\u017a\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017c\3\2\2\2\u017b")
        buf.write("\u017d\5m\67\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0182\3")
        buf.write("\2\2\2\u0180\u0182\3\2\2\2\u0181\u0176\3\2\2\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182t\3\2\2\2\u0183\u0184\5o8\2\u0184\u0185")
        buf.write("\5q9\2\u0185\u0186\5s:\2\u0186\u0189\3\2\2\2\u0187\u0189")
        buf.write("\5i\65\2\u0188\u0183\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("v\3\2\2\2\u018a\u018b\t\t\2\2\u018bx\3\2\2\2\u018c\u018d")
        buf.write("\5w<\2\u018d\u018e\5{>\2\u018ez\3\2\2\2\u018f\u0190\t")
        buf.write("\n\2\2\u0190|\3\2\2\2\u0191\u0192\n\n\2\2\u0192~\3\2\2")
        buf.write("\2\u0193\u0194\5w<\2\u0194\u0195\5}?\2\u0195\u0080\3\2")
        buf.write("\2\2\u0196\u0197\n\13\2\2\u0197\u0082\3\2\2\2\u0198\u0199")
        buf.write("\t\f\2\2\u0199\u019a\t\r\2\2\u019a\u0084\3\2\2\2\u019b")
        buf.write("\u019f\5y=\2\u019c\u019f\5\u0083B\2\u019d\u019f\5\u0081")
        buf.write("A\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019f\u0086\3\2\2\2\u01a0\u01a5\t\r\2\2\u01a1")
        buf.write("\u01a4\5]/\2\u01a2\u01a4\5\u0085C\2\u01a3\u01a1\3\2\2")
        buf.write("\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a8\u01a9\t\r\2\2\u01a9\u01aa\bD\4\2")
        buf.write("\u01aa\u0088\3\2\2\2\u01ab\u01ac\13\2\2\2\u01ac\u01ad")
        buf.write("\bE\5\2\u01ad\u008a\3\2\2\2\u01ae\u01b3\t\r\2\2\u01af")
        buf.write("\u01b2\5\u0085C\2\u01b0\u01b2\5]/\2\u01b1\u01af\3\2\2")
        buf.write("\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b7\7\2\2\3\u01b7\u01b8\bF\6\2")
        buf.write("\u01b8\u008c\3\2\2\2\u01b9\u01be\t\r\2\2\u01ba\u01bd\5")
        buf.write("\u0085C\2\u01bb\u01bd\5]/\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c1\u01c2\5\177@\2\u01c2\u01c3\bG\7\2\u01c3\u008e")
        buf.write("\3\2\2\2\26\2\u013c\u0144\u014b\u0159\u0165\u016a\u0170")
        buf.write("\u0174\u0179\u017e\u0181\u0188\u019e\u01a3\u01a5\u01b1")
        buf.write("\u01b3\u01bc\u01be\b\b\2\2\3/\2\3D\3\3E\4\3F\5\3G\6")
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
    COMMENT = 43
    WS = 44
    NEW_LINE = 45
    IDENTIFIER = 46
    NUMBER = 47
    STRING = 48
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
            "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT", "WS", "NEW_LINE", 
            "IDENTIFIER", "NUMBER", "STRING", "ERROR_CHAR", "UNCLOSE_STRING", 
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
                  "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT_HEAD", "COMMENT", 
                  "WS", "NEW_LINE", "WINDOW_NEW_LINE", "NOT_NEW_LINE", "IDENTIFIER_HEAD", 
                  "IDENTIFIER_TAIL", "IDENTIFIER", "ZERO", "NON_ZERO_DIGIT", 
                  "DIGIT", "DECIMAL", "FLOATING_POINT", "EXPONENTIAL", "NUMBER", 
                  "ESCAPE_SIGN", "ESCAPE_SEQUENCE", "ESCAPE_REP", "NOT_ESCAPE_REP", 
                  "ILLEGAL_ESCAPE_SEQ", "STRING_CHAR", "DOUBLE_QUOTE_IN_STRING", 
                  "STRING_LITTERAL", "STRING", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[45] = self.NEW_LINE_action 
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
            self.text = '\n'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     


