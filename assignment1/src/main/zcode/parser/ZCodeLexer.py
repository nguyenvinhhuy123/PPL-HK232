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
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\7-\u0139\n")
        buf.write("-\f-\16-\u013c\13-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\5\61\u0147\n\61\3\62\6\62\u014a\n\62\r\62\16\62\u014b")
        buf.write("\3\63\3\63\7\63\u0150\n\63\f\63\16\63\u0153\13\63\3\63")
        buf.write("\5\63\u0156\n\63\3\64\3\64\3\64\5\64\u015b\n\64\3\64\6")
        buf.write("\64\u015e\n\64\r\64\16\64\u015f\3\64\5\64\u0163\n\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u016a\n\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\5=\u0181\n=\3>\3>\7>\u0185\n>\f>\16>\u0188\13>\3")
        buf.write(">\3>\3>\3?\3?\3?\3@\3@\7@\u0192\n@\f@\16@\u0195\13@\3")
        buf.write("@\3@\3A\6A\u019a\nA\rA\16A\u019b\3A\3A\3B\3B\3B\3B\5B")
        buf.write("\u01a4\nB\3C\3C\3C\3D\3D\3E\3E\3E\3F\3F\7F\u01b0\nF\f")
        buf.write("F\16F\u01b3\13F\3F\3F\3F\3G\3G\7G\u01ba\nG\fG\16G\u01bd")
        buf.write("\13G\3G\3G\3G\2\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y\2[-]\2_\2a\2c\2e\2g\2i")
        buf.write(".k\2m\2o\2q\2s\2u\2w\2y\2{/}\2\177\60\u0081\61\u0083\62")
        buf.write("\u0085\2\u0087\2\u0089\63\u008b\64\u008d\65\3\2\16\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2GGgg\4\2--//\3\2^^\t")
        buf.write("\2))^^ddhhppttvv\5\2\f\f$$^^\3\2))\3\2$$\5\2\n\13\16\17")
        buf.write("\"\"\4\2\f\f\17\17\2\u01bf\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2[\3\2\2\2\2i")
        buf.write("\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u008f\3\2\2\2\5\u0094\3\2\2\2\7\u0099\3\2\2\2\t\u009f")
        buf.write("\3\2\2\2\13\u00a6\3\2\2\2\r\u00ab\3\2\2\2\17\u00b2\3\2")
        buf.write("\2\2\21\u00b9\3\2\2\2\23\u00bd\3\2\2\2\25\u00c5\3\2\2")
        buf.write("\2\27\u00ca\3\2\2\2\31\u00ce\3\2\2\2\33\u00d4\3\2\2\2")
        buf.write("\35\u00d7\3\2\2\2\37\u00dd\3\2\2\2!\u00e6\3\2\2\2#\u00e9")
        buf.write("\3\2\2\2%\u00ee\3\2\2\2\'\u00f3\3\2\2\2)\u00f9\3\2\2\2")
        buf.write("+\u00fd\3\2\2\2-\u00ff\3\2\2\2/\u0101\3\2\2\2\61\u0103")
        buf.write("\3\2\2\2\63\u0105\3\2\2\2\65\u0107\3\2\2\2\67\u010b\3")
        buf.write("\2\2\29\u010f\3\2\2\2;\u0112\3\2\2\2=\u0114\3\2\2\2?\u0117")
        buf.write("\3\2\2\2A\u011a\3\2\2\2C\u011c\3\2\2\2E\u011e\3\2\2\2")
        buf.write("G\u0121\3\2\2\2I\u0124\3\2\2\2K\u0127\3\2\2\2M\u012b\3")
        buf.write("\2\2\2O\u012d\3\2\2\2Q\u012f\3\2\2\2S\u0131\3\2\2\2U\u0133")
        buf.write("\3\2\2\2W\u0135\3\2\2\2Y\u013a\3\2\2\2[\u013d\3\2\2\2")
        buf.write("]\u0140\3\2\2\2_\u0142\3\2\2\2a\u0146\3\2\2\2c\u0149\3")
        buf.write("\2\2\2e\u0155\3\2\2\2g\u0162\3\2\2\2i\u0169\3\2\2\2k\u016b")
        buf.write("\3\2\2\2m\u016d\3\2\2\2o\u0170\3\2\2\2q\u0172\3\2\2\2")
        buf.write("s\u0174\3\2\2\2u\u0177\3\2\2\2w\u0179\3\2\2\2y\u0180\3")
        buf.write("\2\2\2{\u0182\3\2\2\2}\u018c\3\2\2\2\177\u018f\3\2\2\2")
        buf.write("\u0081\u0199\3\2\2\2\u0083\u01a3\3\2\2\2\u0085\u01a5\3")
        buf.write("\2\2\2\u0087\u01a8\3\2\2\2\u0089\u01aa\3\2\2\2\u008b\u01ad")
        buf.write("\3\2\2\2\u008d\u01b7\3\2\2\2\u008f\u0090\7o\2\2\u0090")
        buf.write("\u0091\7c\2\2\u0091\u0092\7k\2\2\u0092\u0093\7p\2\2\u0093")
        buf.write("\4\3\2\2\2\u0094\u0095\7v\2\2\u0095\u0096\7t\2\2\u0096")
        buf.write("\u0097\7w\2\2\u0097\u0098\7g\2\2\u0098\6\3\2\2\2\u0099")
        buf.write("\u009a\7h\2\2\u009a\u009b\7c\2\2\u009b\u009c\7n\2\2\u009c")
        buf.write("\u009d\7u\2\2\u009d\u009e\7g\2\2\u009e\b\3\2\2\2\u009f")
        buf.write("\u00a0\7p\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7o\2\2\u00a2")
        buf.write("\u00a3\7d\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7t\2\2\u00a5")
        buf.write("\n\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8\7q\2\2\u00a8")
        buf.write("\u00a9\7q\2\2\u00a9\u00aa\7n\2\2\u00aa\f\3\2\2\2\u00ab")
        buf.write("\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7i\2\2\u00b1")
        buf.write("\16\3\2\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7g\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7t\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\20\3\2\2\2\u00b9\u00ba\7x\2\2\u00ba")
        buf.write("\u00bb\7c\2\2\u00bb\u00bc\7t\2\2\u00bc\22\3\2\2\2\u00bd")
        buf.write("\u00be\7f\2\2\u00be\u00bf\7{\2\2\u00bf\u00c0\7p\2\2\u00c0")
        buf.write("\u00c1\7c\2\2\u00c1\u00c2\7o\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write("\u00c4\7e\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\7h\2\2\u00c6")
        buf.write("\u00c7\7w\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7e\2\2\u00c9")
        buf.write("\26\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7q\2\2\u00cc")
        buf.write("\u00cd\7t\2\2\u00cd\30\3\2\2\2\u00ce\u00cf\7w\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\32\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5")
        buf.write("\u00d6\7{\2\2\u00d6\34\3\2\2\2\u00d7\u00d8\7d\2\2\u00d8")
        buf.write("\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7c\2\2\u00db")
        buf.write("\u00dc\7m\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7e\2\2\u00de")
        buf.write("\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7v\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7w\2\2\u00e4")
        buf.write("\u00e5\7g\2\2\u00e5 \3\2\2\2\u00e6\u00e7\7k\2\2\u00e7")
        buf.write("\u00e8\7h\2\2\u00e8\"\3\2\2\2\u00e9\u00ea\7g\2\2\u00ea")
        buf.write("\u00eb\7n\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed\7g\2\2\u00ed")
        buf.write("$\3\2\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7k\2\2\u00f1\u00f2\7h\2\2\u00f2&\3\2\2\2\u00f3")
        buf.write("\u00f4\7d\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7i\2\2\u00f6")
        buf.write("\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8(\3\2\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7f\2\2\u00fc")
        buf.write("*\3\2\2\2\u00fd\u00fe\7-\2\2\u00fe,\3\2\2\2\u00ff\u0100")
        buf.write("\7/\2\2\u0100.\3\2\2\2\u0101\u0102\7,\2\2\u0102\60\3\2")
        buf.write("\2\2\u0103\u0104\7\61\2\2\u0104\62\3\2\2\2\u0105\u0106")
        buf.write("\7\'\2\2\u0106\64\3\2\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7v\2\2\u010a\66\3\2\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7p\2\2\u010d\u010e\7f\2\2\u010e8\3")
        buf.write("\2\2\2\u010f\u0110\7q\2\2\u0110\u0111\7t\2\2\u0111:\3")
        buf.write("\2\2\2\u0112\u0113\7?\2\2\u0113<\3\2\2\2\u0114\u0115\7")
        buf.write(">\2\2\u0115\u0116\7/\2\2\u0116>\3\2\2\2\u0117\u0118\7")
        buf.write("#\2\2\u0118\u0119\7?\2\2\u0119@\3\2\2\2\u011a\u011b\7")
        buf.write(">\2\2\u011bB\3\2\2\2\u011c\u011d\7@\2\2\u011dD\3\2\2\2")
        buf.write("\u011e\u011f\7>\2\2\u011f\u0120\7?\2\2\u0120F\3\2\2\2")
        buf.write("\u0121\u0122\7@\2\2\u0122\u0123\7?\2\2\u0123H\3\2\2\2")
        buf.write("\u0124\u0125\7?\2\2\u0125\u0126\7?\2\2\u0126J\3\2\2\2")
        buf.write("\u0127\u0128\7\60\2\2\u0128\u0129\7\60\2\2\u0129\u012a")
        buf.write("\7\60\2\2\u012aL\3\2\2\2\u012b\u012c\7*\2\2\u012cN\3\2")
        buf.write("\2\2\u012d\u012e\7+\2\2\u012eP\3\2\2\2\u012f\u0130\7]")
        buf.write("\2\2\u0130R\3\2\2\2\u0131\u0132\7_\2\2\u0132T\3\2\2\2")
        buf.write("\u0133\u0134\7.\2\2\u0134V\3\2\2\2\u0135\u0136\t\2\2\2")
        buf.write("\u0136X\3\2\2\2\u0137\u0139\t\3\2\2\u0138\u0137\3\2\2")
        buf.write("\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013bZ\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e")
        buf.write("\5W,\2\u013e\u013f\5Y-\2\u013f\\\3\2\2\2\u0140\u0141\7")
        buf.write("\62\2\2\u0141^\3\2\2\2\u0142\u0143\t\4\2\2\u0143`\3\2")
        buf.write("\2\2\u0144\u0147\5]/\2\u0145\u0147\5_\60\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0145\3\2\2\2\u0147b\3\2\2\2\u0148\u014a")
        buf.write("\5a\61\2\u0149\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014cd\3\2\2\2\u014d")
        buf.write("\u0151\7\60\2\2\u014e\u0150\5a\61\2\u014f\u014e\3\2\2")
        buf.write("\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0156\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u0156\3\2\2\2\u0155\u014d\3\2\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0156f\3\2\2\2\u0157\u015a\t\5\2\2\u0158\u015b\t\6\2")
        buf.write("\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015e\5a\61\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u0163\3")
        buf.write("\2\2\2\u0162\u0157\3\2\2\2\u0162\u0161\3\2\2\2\u0163h")
        buf.write("\3\2\2\2\u0164\u0165\5c\62\2\u0165\u0166\5e\63\2\u0166")
        buf.write("\u0167\5g\64\2\u0167\u016a\3\2\2\2\u0168\u016a\5]/\2\u0169")
        buf.write("\u0164\3\2\2\2\u0169\u0168\3\2\2\2\u016aj\3\2\2\2\u016b")
        buf.write("\u016c\t\7\2\2\u016cl\3\2\2\2\u016d\u016e\5k\66\2\u016e")
        buf.write("\u016f\5o8\2\u016fn\3\2\2\2\u0170\u0171\t\b\2\2\u0171")
        buf.write("p\3\2\2\2\u0172\u0173\n\b\2\2\u0173r\3\2\2\2\u0174\u0175")
        buf.write("\5k\66\2\u0175\u0176\5q9\2\u0176t\3\2\2\2\u0177\u0178")
        buf.write("\n\t\2\2\u0178v\3\2\2\2\u0179\u017a\t\n\2\2\u017a\u017b")
        buf.write("\t\13\2\2\u017bx\3\2\2\2\u017c\u0181\5m\67\2\u017d\u0181")
        buf.write("\5w<\2\u017e\u0181\5u;\2\u017f\u0181\5\u0083B\2\u0180")
        buf.write("\u017c\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u017f\3\2\2\2\u0181z\3\2\2\2\u0182\u0186\t\13\2")
        buf.write("\2\u0183\u0185\5y=\2\u0184\u0183\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\t\13\2\2\u018a")
        buf.write("\u018b\b>\2\2\u018b|\3\2\2\2\u018c\u018d\7%\2\2\u018d")
        buf.write("\u018e\7%\2\2\u018e~\3\2\2\2\u018f\u0193\5}?\2\u0190\u0192")
        buf.write("\5\u0087D\2\u0191\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0196\u0197\b@\3\2\u0197\u0080\3")
        buf.write("\2\2\2\u0198\u019a\t\f\2\2\u0199\u0198\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019e\bA\3\2\u019e\u0082\3\2\2\2")
        buf.write("\u019f\u01a4\t\r\2\2\u01a0\u01a1\5\u0085C\2\u01a1\u01a2")
        buf.write("\bB\4\2\u01a2\u01a4\3\2\2\2\u01a3\u019f\3\2\2\2\u01a3")
        buf.write("\u01a0\3\2\2\2\u01a4\u0084\3\2\2\2\u01a5\u01a6\7\17\2")
        buf.write("\2\u01a6\u01a7\7\f\2\2\u01a7\u0086\3\2\2\2\u01a8\u01a9")
        buf.write("\n\r\2\2\u01a9\u0088\3\2\2\2\u01aa\u01ab\13\2\2\2\u01ab")
        buf.write("\u01ac\bE\5\2\u01ac\u008a\3\2\2\2\u01ad\u01b1\t\13\2\2")
        buf.write("\u01ae\u01b0\5y=\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2")
        buf.write("\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b4")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\7\2\2\3\u01b5")
        buf.write("\u01b6\bF\6\2\u01b6\u008c\3\2\2\2\u01b7\u01bb\t\13\2\2")
        buf.write("\u01b8\u01ba\5y=\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2")
        buf.write("\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\5s:\2\u01bf\u01c0")
        buf.write("\bG\7\2\u01c0\u008e\3\2\2\2\23\2\u013a\u0146\u014b\u0151")
        buf.write("\u0155\u015a\u015f\u0162\u0169\u0180\u0186\u0193\u019b")
        buf.write("\u01a3\u01b1\u01bb\b\3>\2\b\2\2\3B\3\3E\4\3F\5\3G\6")
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
                  "WINDOW_NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[60] = self.STRING_action 
            actions[64] = self.NEW_LINE_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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
     


