# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u023f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2\7\2\u0098")
        buf.write("\n\2\f\2\16\2\u009b\13\2\3\2\7\2\u009e\n\2\f\2\16\2\u00a1")
        buf.write("\13\2\3\2\3\2\7\2\u00a5\n\2\f\2\16\2\u00a8\13\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\5\5\u00b9\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00c2\n")
        buf.write("\6\3\7\3\7\7\7\u00c6\n\7\f\7\16\7\u00c9\13\7\3\b\3\b\3")
        buf.write("\b\5\b\u00ce\n\b\3\t\3\t\5\t\u00d2\n\t\3\t\3\t\3\n\3\n")
        buf.write("\5\n\u00d8\n\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00e5\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u00ef\n\17\3\20\3\20\3\20\3\21\3\21\3\21\5")
        buf.write("\21\u00f7\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ff")
        buf.write("\n\22\5\22\u0101\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u010a\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0111")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\27\3\27\5\27\u0119\n\27\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\5\31\u0121\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\5\33\u012a\n\33\3\34\3\34\6")
        buf.write("\34\u012e\n\34\r\34\16\34\u012f\3\34\5\34\u0133\n\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\36\3\36\5\36\u013c\n\36\3\36")
        buf.write("\3\36\3\36\5\36\u0141\n\36\3\36\5\36\u0144\n\36\3\37\3")
        buf.write("\37\3\37\5\37\u0149\n\37\3\37\3\37\3\37\5\37\u014e\n\37")
        buf.write("\3 \3 \5 \u0152\n \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3#\3$\7$\u0162\n$\f$\16$\u0165\13$\3%\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\5%\u016f\n%\3&\3&\3&\3&\3&\5&\u0176\n&\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\5(\u017f\n(\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\7*\u018a\n*\f*\16*\u018d\13*\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\7,\u0198\n,\f,\16,\u019b\13,\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\7.\u01a6\n.\f.\16.\u01a9\13.\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u01b1\n\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u01bb\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\7\63\u01c2\n\63\f\63\16\63\u01c5\13\63\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\7\65\u01ce\n\65\f\65\16\65\u01d1")
        buf.write("\13\65\3\66\3\66\5\66\u01d5\n\66\3\67\3\67\7\67\u01d9")
        buf.write("\n\67\f\67\16\67\u01dc\13\67\3\67\5\67\u01df\n\67\38\3")
        buf.write("8\38\58\u01e4\n8\38\38\39\39\39\59\u01eb\n9\39\39\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3<\3<\3<\3<\5<\u01fa\n<\3<\3<\3=\3=\3")
        buf.write("=\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\5B\u020d\nB\3C\3")
        buf.write("C\3C\3C\3D\3D\3D\3D\5D\u0217\nD\3E\3E\3E\3E\3E\5E\u021e")
        buf.write("\nE\3F\3F\3F\3G\3G\5G\u0225\nG\3G\3G\5G\u0229\nG\3G\3")
        buf.write("G\3H\3H\5H\u022f\nH\3H\3H\3I\3I\3I\5I\u0236\nI\3J\3J\3")
        buf.write("K\6K\u023b\nK\rK\16K\u023c\3K\2\6RVZdL\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\2\t\3\2\6\b")
        buf.write("\3\2\n\13\4\2\37\37!&\3\2\35\36\3\2\27\30\3\2\31\33\3")
        buf.write("\2\4\5\2\u0238\2\u0099\3\2\2\2\4\u00ac\3\2\2\2\6\u00b2")
        buf.write("\3\2\2\2\b\u00b8\3\2\2\2\n\u00c1\3\2\2\2\f\u00c7\3\2\2")
        buf.write("\2\16\u00cd\3\2\2\2\20\u00d1\3\2\2\2\22\u00d7\3\2\2\2")
        buf.write("\24\u00db\3\2\2\2\26\u00e4\3\2\2\2\30\u00e8\3\2\2\2\32")
        buf.write("\u00ea\3\2\2\2\34\u00ee\3\2\2\2\36\u00f0\3\2\2\2 \u00f3")
        buf.write("\3\2\2\2\"\u0100\3\2\2\2$\u0102\3\2\2\2&\u0109\3\2\2\2")
        buf.write("(\u0110\3\2\2\2*\u0112\3\2\2\2,\u0118\3\2\2\2.\u011a\3")
        buf.write("\2\2\2\60\u011d\3\2\2\2\62\u0122\3\2\2\2\64\u0126\3\2")
        buf.write("\2\2\66\u012b\3\2\2\28\u0136\3\2\2\2:\u0143\3\2\2\2<\u014d")
        buf.write("\3\2\2\2>\u0151\3\2\2\2@\u0153\3\2\2\2B\u0157\3\2\2\2")
        buf.write("D\u015c\3\2\2\2F\u0163\3\2\2\2H\u016e\3\2\2\2J\u0175\3")
        buf.write("\2\2\2L\u0177\3\2\2\2N\u017e\3\2\2\2P\u0180\3\2\2\2R\u0182")
        buf.write("\3\2\2\2T\u018e\3\2\2\2V\u0190\3\2\2\2X\u019c\3\2\2\2")
        buf.write("Z\u019e\3\2\2\2\\\u01aa\3\2\2\2^\u01b0\3\2\2\2`\u01b2")
        buf.write("\3\2\2\2b\u01ba\3\2\2\2d\u01bc\3\2\2\2f\u01c6\3\2\2\2")
        buf.write("h\u01ca\3\2\2\2j\u01d4\3\2\2\2l\u01d6\3\2\2\2n\u01e0\3")
        buf.write("\2\2\2p\u01e7\3\2\2\2r\u01ee\3\2\2\2t\u01f1\3\2\2\2v\u01f5")
        buf.write("\3\2\2\2x\u01fd\3\2\2\2z\u0200\3\2\2\2|\u0203\3\2\2\2")
        buf.write("~\u0206\3\2\2\2\u0080\u0208\3\2\2\2\u0082\u020a\3\2\2")
        buf.write("\2\u0084\u020e\3\2\2\2\u0086\u0216\3\2\2\2\u0088\u021d")
        buf.write("\3\2\2\2\u008a\u021f\3\2\2\2\u008c\u0222\3\2\2\2\u008e")
        buf.write("\u022e\3\2\2\2\u0090\u0235\3\2\2\2\u0092\u0237\3\2\2\2")
        buf.write("\u0094\u023a\3\2\2\2\u0096\u0098\5D#\2\u0097\u0096\3\2")
        buf.write("\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u009f\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009e\5\b\5\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3")
        buf.write("\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a6\5\4\3\2\u00a3\u00a5")
        buf.write("\5\b\5\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a9\u00aa\7\2\2\3\u00aa\u00ab\7")
        buf.write("\2\2\3\u00ab\3\3\2\2\2\u00ac\u00ad\7\f\2\2\u00ad\u00ae")
        buf.write("\7\3\2\2\u00ae\u00af\7(\2\2\u00af\u00b0\7)\2\2\u00b0\u00b1")
        buf.write("\5\n\6\2\u00b1\5\3\2\2\2\u00b2\u00b3\5D#\2\u00b3\u00b4")
        buf.write("\5\u0094K\2\u00b4\7\3\2\2\2\u00b5\u00b9\5B\"\2\u00b6\u00b9")
        buf.write("\5\6\4\2\u00b7\u00b9\5\20\t\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\t\3\2\2\2\u00ba")
        buf.write("\u00bb\5\u008cG\2\u00bb\u00bc\5\u0094K\2\u00bc\u00c2\3")
        buf.write("\2\2\2\u00bd\u00be\5\f\7\2\u00be\u00bf\5\u0082B\2\u00bf")
        buf.write("\u00c0\5\u0094K\2\u00c0\u00c2\3\2\2\2\u00c1\u00ba\3\2")
        buf.write("\2\2\u00c1\u00bd\3\2\2\2\u00c2\13\3\2\2\2\u00c3\u00c6")
        buf.write("\5\16\b\2\u00c4\u00c6\5\26\f\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\r\3\2\2\2\u00c9\u00c7\3\2\2")
        buf.write("\2\u00ca\u00ce\5\20\t\2\u00cb\u00ce\5\22\n\2\u00cc\u00ce")
        buf.write("\5\24\13\2\u00cd\u00ca\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\17\3\2\2\2\u00cf\u00d2\5\34\17\2")
        buf.write("\u00d0\u00d2\5,\27\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\5\u0094K\2\u00d4")
        buf.write("\21\3\2\2\2\u00d5\u00d8\5$\23\2\u00d6\u00d8\58\35\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00da\5\u0094K\2\u00da\23\3\2\2\2\u00db\u00dc\5")
        buf.write("H%\2\u00dc\u00dd\5\u0094K\2\u00dd\25\3\2\2\2\u00de\u00e5")
        buf.write("\5l\67\2\u00df\u00e5\5v<\2\u00e0\u00e5\5~@\2\u00e1\u00e5")
        buf.write("\5\u0080A\2\u00e2\u00e5\5\u0082B\2\u00e3\u00e5\5\u008c")
        buf.write("G\2\u00e4\u00de\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4\u00e0")
        buf.write("\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\5\u0094")
        buf.write("K\2\u00e7\27\3\2\2\2\u00e8\u00e9\t\2\2\2\u00e9\31\3\2")
        buf.write("\2\2\u00ea\u00eb\t\3\2\2\u00eb\33\3\2\2\2\u00ec\u00ef")
        buf.write("\5 \21\2\u00ed\u00ef\5\"\22\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef\35\3\2\2\2\u00f0\u00f1\7 \2\2\u00f1")
        buf.write("\u00f2\5H%\2\u00f2\37\3\2\2\2\u00f3\u00f4\5\30\r\2\u00f4")
        buf.write("\u00f6\7-\2\2\u00f5\u00f7\5\36\20\2\u00f6\u00f5\3\2\2")
        buf.write("\2\u00f6\u00f7\3\2\2\2\u00f7!\3\2\2\2\u00f8\u00f9\7\n")
        buf.write("\2\2\u00f9\u00fa\7-\2\2\u00fa\u0101\5\36\20\2\u00fb\u00fc")
        buf.write("\7\13\2\2\u00fc\u00fe\7-\2\2\u00fd\u00ff\5\36\20\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2")
        buf.write("\u0100\u00f8\3\2\2\2\u0100\u00fb\3\2\2\2\u0101#\3\2\2")
        buf.write("\2\u0102\u0103\7-\2\2\u0103\u0104\5\36\20\2\u0104%\3\2")
        buf.write("\2\2\u0105\u0106\5H%\2\u0106\u0107\5(\25\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0105\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\'\3\2\2\2\u010b\u010c\7,\2\2\u010c")
        buf.write("\u010d\5H%\2\u010d\u010e\5(\25\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u010b\3\2\2\2\u0110\u010f\3\2\2\2")
        buf.write("\u0111)\3\2\2\2\u0112\u0113\7*\2\2\u0113\u0114\5&\24\2")
        buf.write("\u0114\u0115\7+\2\2\u0115+\3\2\2\2\u0116\u0119\5\60\31")
        buf.write("\2\u0117\u0119\5\62\32\2\u0118\u0116\3\2\2\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119-\3\2\2\2\u011a\u011b\7-\2\2\u011b\u011c")
        buf.write("\5*\26\2\u011c/\3\2\2\2\u011d\u011e\5\30\r\2\u011e\u0120")
        buf.write("\5.\30\2\u011f\u0121\5\64\33\2\u0120\u011f\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\61\3\2\2\2\u0122\u0123\7\n\2\2\u0123")
        buf.write("\u0124\5.\30\2\u0124\u0125\5\64\33\2\u0125\63\3\2\2\2")
        buf.write("\u0126\u0129\7 \2\2\u0127\u012a\7-\2\2\u0128\u012a\5\66")
        buf.write("\34\2\u0129\u0127\3\2\2\2\u0129\u0128\3\2\2\2\u012a\65")
        buf.write("\3\2\2\2\u012b\u0132\7*\2\2\u012c\u012e\5\66\34\2\u012d")
        buf.write("\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2")
        buf.write("\u012f\u0130\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u0133\5")
        buf.write("H%\2\u0132\u012d\3\2\2\2\u0132\u0131\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134\u0135\7+\2\2\u0135\67\3\2\2\2\u0136\u0137")
        buf.write("\7-\2\2\u0137\u0138\5\64\33\2\u01389\3\2\2\2\u0139\u013b")
        buf.write("\5> \2\u013a\u013c\5\u0094K\2\u013b\u013a\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\5<\37\2")
        buf.write("\u013e\u0144\3\2\2\2\u013f\u0141\5\u0094K\2\u0140\u013f")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0144\3\2\2\2\u0142")
        buf.write("\u0144\3\2\2\2\u0143\u0139\3\2\2\2\u0143\u0140\3\2\2\2")
        buf.write("\u0143\u0142\3\2\2\2\u0144;\3\2\2\2\u0145\u0146\7,\2\2")
        buf.write("\u0146\u0148\5> \2\u0147\u0149\5\u0094K\2\u0148\u0147")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\5<\37\2\u014b\u014e\3\2\2\2\u014c\u014e\3\2\2\2")
        buf.write("\u014d\u0145\3\2\2\2\u014d\u014c\3\2\2\2\u014e=\3\2\2")
        buf.write("\2\u014f\u0152\5,\27\2\u0150\u0152\5\34\17\2\u0151\u014f")
        buf.write("\3\2\2\2\u0151\u0150\3\2\2\2\u0152?\3\2\2\2\u0153\u0154")
        buf.write("\7(\2\2\u0154\u0155\5:\36\2\u0155\u0156\7)\2\2\u0156A")
        buf.write("\3\2\2\2\u0157\u0158\7\f\2\2\u0158\u0159\7-\2\2\u0159")
        buf.write("\u015a\5@!\2\u015a\u015b\5\n\6\2\u015bC\3\2\2\2\u015c")
        buf.write("\u015d\7\f\2\2\u015d\u015e\7-\2\2\u015e\u015f\5@!\2\u015f")
        buf.write("E\3\2\2\2\u0160\u0162\5H%\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164G\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u016f\5J&\2")
        buf.write("\u0167\u016f\5N(\2\u0168\u016f\5R*\2\u0169\u016f\5V,\2")
        buf.write("\u016a\u016f\5Z.\2\u016b\u016f\5^\60\2\u016c\u016f\5b")
        buf.write("\62\2\u016d\u016f\5d\63\2\u016e\u0166\3\2\2\2\u016e\u0167")
        buf.write("\3\2\2\2\u016e\u0168\3\2\2\2\u016e\u0169\3\2\2\2\u016e")
        buf.write("\u016a\3\2\2\2\u016e\u016b\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016e\u016d\3\2\2\2\u016fI\3\2\2\2\u0170\u0171\5N(\2")
        buf.write("\u0171\u0172\5L\'\2\u0172\u0173\5N(\2\u0173\u0176\3\2")
        buf.write("\2\2\u0174\u0176\5N(\2\u0175\u0170\3\2\2\2\u0175\u0174")
        buf.write("\3\2\2\2\u0176K\3\2\2\2\u0177\u0178\7\'\2\2\u0178M\3\2")
        buf.write("\2\2\u0179\u017a\5R*\2\u017a\u017b\5P)\2\u017b\u017c\5")
        buf.write("R*\2\u017c\u017f\3\2\2\2\u017d\u017f\5R*\2\u017e\u0179")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017fO\3\2\2\2\u0180\u0181")
        buf.write("\t\4\2\2\u0181Q\3\2\2\2\u0182\u0183\b*\1\2\u0183\u0184")
        buf.write("\5V,\2\u0184\u018b\3\2\2\2\u0185\u0186\f\4\2\2\u0186\u0187")
        buf.write("\5T+\2\u0187\u0188\5V,\2\u0188\u018a\3\2\2\2\u0189\u0185")
        buf.write("\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018cS\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write("\u018f\t\5\2\2\u018fU\3\2\2\2\u0190\u0191\b,\1\2\u0191")
        buf.write("\u0192\5Z.\2\u0192\u0199\3\2\2\2\u0193\u0194\f\4\2\2\u0194")
        buf.write("\u0195\5X-\2\u0195\u0196\5Z.\2\u0196\u0198\3\2\2\2\u0197")
        buf.write("\u0193\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019aW\3\2\2\2\u019b\u0199\3\2\2")
        buf.write("\2\u019c\u019d\t\6\2\2\u019dY\3\2\2\2\u019e\u019f\b.\1")
        buf.write("\2\u019f\u01a0\5^\60\2\u01a0\u01a7\3\2\2\2\u01a1\u01a2")
        buf.write("\f\4\2\2\u01a2\u01a3\5\\/\2\u01a3\u01a4\5^\60\2\u01a4")
        buf.write("\u01a6\3\2\2\2\u01a5\u01a1\3\2\2\2\u01a6\u01a9\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8[\3\2\2")
        buf.write("\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\t\7\2\2\u01ab]\3\2")
        buf.write("\2\2\u01ac\u01ad\5`\61\2\u01ad\u01ae\5^\60\2\u01ae\u01b1")
        buf.write("\3\2\2\2\u01af\u01b1\5b\62\2\u01b0\u01ac\3\2\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1_\3\2\2\2\u01b2\u01b3\7\34\2\2\u01b3")
        buf.write("a\3\2\2\2\u01b4\u01b5\7(\2\2\u01b5\u01b6\5H%\2\u01b6\u01b7")
        buf.write("\7)\2\2\u01b7\u01bb\3\2\2\2\u01b8\u01bb\5\u0090I\2\u01b9")
        buf.write("\u01bb\5d\63\2\u01ba\u01b4\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01ba\u01b9\3\2\2\2\u01bbc\3\2\2\2\u01bc\u01bd\b\63\1")
        buf.write("\2\u01bd\u01be\5j\66\2\u01be\u01c3\3\2\2\2\u01bf\u01c0")
        buf.write("\f\4\2\2\u01c0\u01c2\5f\64\2\u01c1\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4e\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7*\2\2")
        buf.write("\u01c7\u01c8\5h\65\2\u01c8\u01c9\7+\2\2\u01c9g\3\2\2\2")
        buf.write("\u01ca\u01cf\5H%\2\u01cb\u01cc\7,\2\2\u01cc\u01ce\5h\65")
        buf.write("\2\u01cd\u01cb\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0i\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d2\u01d5\7-\2\2\u01d3\u01d5\5\u008aF\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5k\3\2\2\2\u01d6")
        buf.write("\u01da\5n8\2\u01d7\u01d9\5p9\2\u01d8\u01d7\3\2\2\2\u01d9")
        buf.write("\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01df\5")
        buf.write("r:\2\u01de\u01dd\3\2\2\2\u01de\u01df\3\2\2\2\u01dfm\3")
        buf.write("\2\2\2\u01e0\u01e1\7\22\2\2\u01e1\u01e3\5t;\2\u01e2\u01e4")
        buf.write("\5\u0094K\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u01e6\5\26\f\2\u01e6o\3\2\2\2\u01e7")
        buf.write("\u01e8\7\24\2\2\u01e8\u01ea\5t;\2\u01e9\u01eb\5\u0094")
        buf.write("K\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec")
        buf.write("\3\2\2\2\u01ec\u01ed\5\26\f\2\u01edq\3\2\2\2\u01ee\u01ef")
        buf.write("\7\23\2\2\u01ef\u01f0\5\26\f\2\u01f0s\3\2\2\2\u01f1\u01f2")
        buf.write("\7(\2\2\u01f2\u01f3\5H%\2\u01f3\u01f4\7)\2\2\u01f4u\3")
        buf.write("\2\2\2\u01f5\u01f6\5x=\2\u01f6\u01f7\5z>\2\u01f7\u01f9")
        buf.write("\5|?\2\u01f8\u01fa\5\u0094K\2\u01f9\u01f8\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\5\26\f")
        buf.write("\2\u01fcw\3\2\2\2\u01fd\u01fe\7\r\2\2\u01fe\u01ff\7-\2")
        buf.write("\2\u01ffy\3\2\2\2\u0200\u0201\7\16\2\2\u0201\u0202\5H")
        buf.write("%\2\u0202{\3\2\2\2\u0203\u0204\7\17\2\2\u0204\u0205\5")
        buf.write("H%\2\u0205}\3\2\2\2\u0206\u0207\7\20\2\2\u0207\177\3\2")
        buf.write("\2\2\u0208\u0209\7\21\2\2\u0209\u0081\3\2\2\2\u020a\u020c")
        buf.write("\7\t\2\2\u020b\u020d\5H%\2\u020c\u020b\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u0083\3\2\2\2\u020e\u020f\7(\2\2\u020f")
        buf.write("\u0210\5\u0086D\2\u0210\u0211\7+\2\2\u0211\u0085\3\2\2")
        buf.write("\2\u0212\u0213\5H%\2\u0213\u0214\5\u0088E\2\u0214\u0217")
        buf.write("\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u0212\3\2\2\2\u0216")
        buf.write("\u0215\3\2\2\2\u0217\u0087\3\2\2\2\u0218\u0219\7,\2\2")
        buf.write("\u0219\u021a\5H%\2\u021a\u021b\5\u0088E\2\u021b\u021e")
        buf.write("\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u0218\3\2\2\2\u021d")
        buf.write("\u021c\3\2\2\2\u021e\u0089\3\2\2\2\u021f\u0220\7-\2\2")
        buf.write("\u0220\u0221\5\u0084C\2\u0221\u008b\3\2\2\2\u0222\u0224")
        buf.write("\7\25\2\2\u0223\u0225\5\u0094K\2\u0224\u0223\3\2\2\2\u0224")
        buf.write("\u0225\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228\5\f\7\2")
        buf.write("\u0227\u0229\5\u0094K\2\u0228\u0227\3\2\2\2\u0228\u0229")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\7\26\2\2\u022b")
        buf.write("\u008d\3\2\2\2\u022c\u022f\7\30\2\2\u022d\u022f\3\2\2")
        buf.write("\2\u022e\u022c\3\2\2\2\u022e\u022d\3\2\2\2\u022f\u0230")
        buf.write("\3\2\2\2\u0230\u0231\7.\2\2\u0231\u008f\3\2\2\2\u0232")
        buf.write("\u0236\5\u008eH\2\u0233\u0236\7/\2\2\u0234\u0236\5\u0092")
        buf.write("J\2\u0235\u0232\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0234")
        buf.write("\3\2\2\2\u0236\u0091\3\2\2\2\u0237\u0238\t\b\2\2\u0238")
        buf.write("\u0093\3\2\2\2\u0239\u023b\7\62\2\2\u023a\u0239\3\2\2")
        buf.write("\2\u023b\u023c\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d")
        buf.write("\3\2\2\2\u023d\u0095\3\2\2\2\67\u0099\u009f\u00a6\u00b8")
        buf.write("\u00c1\u00c5\u00c7\u00cd\u00d1\u00d7\u00e4\u00ee\u00f6")
        buf.write("\u00fe\u0100\u0109\u0110\u0118\u0120\u0129\u012f\u0132")
        buf.write("\u013b\u0140\u0143\u0148\u014d\u0151\u0163\u016e\u0175")
        buf.write("\u017e\u018b\u0199\u01a7\u01b0\u01ba\u01c3\u01cf\u01d4")
        buf.write("\u01da\u01de\u01e3\u01ea\u01f9\u020c\u0216\u021d\u0224")
        buf.write("\u0228\u022e\u0235\u023c")
        return buf.getvalue()


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
    RULE_foward_func = 2
    RULE_define = 3
    RULE_inner_scope = 4
    RULE_lines = 5
    RULE_line = 6
    RULE_def_line = 7
    RULE_assign_line = 8
    RULE_expr_line = 9
    RULE_statement = 10
    RULE_type_def = 11
    RULE_implicit_type_def = 12
    RULE_var_def = 13
    RULE_value_init = 14
    RULE_static_var_def = 15
    RULE_dynamic_var_def = 16
    RULE_var_assign = 17
    RULE_dim_list = 18
    RULE_dim_list_tail = 19
    RULE_array_dim = 20
    RULE_array_def = 21
    RULE_array_identifier = 22
    RULE_array_static_def = 23
    RULE_array_implicit_def = 24
    RULE_array_init = 25
    RULE_array_value_init = 26
    RULE_array_asign = 27
    RULE_param_def_list = 28
    RULE_param_def_list_tail = 29
    RULE_param = 30
    RULE_param_def = 31
    RULE_func_def = 32
    RULE_foward_func_def = 33
    RULE_expressions = 34
    RULE_expression = 35
    RULE_string_expr = 36
    RULE_string_op = 37
    RULE_relation_expr = 38
    RULE_relational_op = 39
    RULE_logic_expr = 40
    RULE_logic_op = 41
    RULE_add_expr = 42
    RULE_add_op = 43
    RULE_multi_expr = 44
    RULE_multi_op = 45
    RULE_negate_expr = 46
    RULE_negate_op = 47
    RULE_primary_expression = 48
    RULE_array_expr = 49
    RULE_indexer = 50
    RULE_index_op = 51
    RULE_term = 52
    RULE_if_statement = 53
    RULE_if_clause = 54
    RULE_elif_clause = 55
    RULE_else_clause = 56
    RULE_if_condition = 57
    RULE_for_statement = 58
    RULE_for_clause = 59
    RULE_condition_clause = 60
    RULE_update_clause = 61
    RULE_break_statement = 62
    RULE_continue_statement = 63
    RULE_return_statement = 64
    RULE_passing_arg = 65
    RULE_passing_list = 66
    RULE_passing_list_tail = 67
    RULE_func_call = 68
    RULE_block_statement = 69
    RULE_sign_number = 70
    RULE_literal = 71
    RULE_boolean = 72
    RULE_end_line = 73

    ruleNames =  [ "program", "main_def", "foward_func", "define", "inner_scope", 
                   "lines", "line", "def_line", "assign_line", "expr_line", 
                   "statement", "type_def", "implicit_type_def", "var_def", 
                   "value_init", "static_var_def", "dynamic_var_def", "var_assign", 
                   "dim_list", "dim_list_tail", "array_dim", "array_def", 
                   "array_identifier", "array_static_def", "array_implicit_def", 
                   "array_init", "array_value_init", "array_asign", "param_def_list", 
                   "param_def_list_tail", "param", "param_def", "func_def", 
                   "foward_func_def", "expressions", "expression", "string_expr", 
                   "string_op", "relation_expr", "relational_op", "logic_expr", 
                   "logic_op", "add_expr", "add_op", "multi_expr", "multi_op", 
                   "negate_expr", "negate_op", "primary_expression", "array_expr", 
                   "indexer", "index_op", "term", "if_statement", "if_clause", 
                   "elif_clause", "else_clause", "if_condition", "for_statement", 
                   "for_clause", "condition_clause", "update_clause", "break_statement", 
                   "continue_statement", "return_statement", "passing_arg", 
                   "passing_list", "passing_list_tail", "func_call", "block_statement", 
                   "sign_number", "literal", "boolean", "end_line" ]

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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_def(self):
            return self.getTypedRuleContext(ZCodeParser.Main_defContext,0)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.EOF)
            else:
                return self.getToken(ZCodeParser.EOF, i)

        def foward_func_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Foward_func_defContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Foward_func_defContext,i)


        def define(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DefineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DefineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 148
                    self.foward_func_def() 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    self.define() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 160
            self.main_def()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FUNC))) != 0):
                self.state = 161
                self.define()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(ZCodeParser.EOF)
            self.state = 168
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

        def inner_scope(self):
            return self.getTypedRuleContext(ZCodeParser.Inner_scopeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_def" ):
                return visitor.visitMain_def(self)
            else:
                return visitor.visitChildren(self)




    def main_def(self):

        localctx = ZCodeParser.Main_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ZCodeParser.KW_FUNC)
            self.state = 171
            self.match(ZCodeParser.MAIN_TOKEN)
            self.state = 172
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 173
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
            self.state = 174
            self.inner_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foward_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def foward_func_def(self):
            return self.getTypedRuleContext(ZCodeParser.Foward_func_defContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_foward_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFoward_func" ):
                return visitor.visitFoward_func(self)
            else:
                return visitor.visitChildren(self)




    def foward_func(self):

        localctx = ZCodeParser.Foward_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_foward_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.foward_func_def()
            self.state = 177
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


        def foward_func(self):
            return self.getTypedRuleContext(ZCodeParser.Foward_funcContext,0)


        def def_line(self):
            return self.getTypedRuleContext(ZCodeParser.Def_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_define

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine" ):
                return visitor.visitDefine(self)
            else:
                return visitor.visitChildren(self)




    def define(self):

        localctx = ZCodeParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_define)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.func_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.foward_func()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.def_line()
                pass


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


        def lines(self):
            return self.getTypedRuleContext(ZCodeParser.LinesContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_inner_scope

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_scope" ):
                return visitor.visitInner_scope(self)
            else:
                return visitor.visitChildren(self)




    def inner_scope(self):

        localctx = ZCodeParser.Inner_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inner_scope)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.block_statement()
                self.state = 185
                self.end_line()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.lines()
                self.state = 188
                self.return_statement()
                self.state = 189
                self.end_line()
                pass


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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLines" ):
                return visitor.visitLines(self)
            else:
                return visitor.visitChildren(self)




    def lines(self):

        localctx = ZCodeParser.LinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 195
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING, ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                        self.state = 193
                        self.line()
                        pass
                    elif token in [ZCodeParser.KW_RETURN, ZCodeParser.KW_FOR, ZCodeParser.KW_BREAK, ZCodeParser.KW_CONTINUE, ZCodeParser.KW_IF, ZCodeParser.KW_BEGIN]:
                        self.state = 194
                        self.statement()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_line)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.def_line()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.assign_line()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDef_line" ):
                return visitor.visitDef_line(self)
            else:
                return visitor.visitChildren(self)




    def def_line(self):

        localctx = ZCodeParser.Def_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_def_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 205
                self.var_def()
                pass

            elif la_ == 2:
                self.state = 206
                self.array_def()
                pass


            self.state = 209
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


        def array_asign(self):
            return self.getTypedRuleContext(ZCodeParser.Array_asignContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_line" ):
                return visitor.visitAssign_line(self)
            else:
                return visitor.visitChildren(self)




    def assign_line(self):

        localctx = ZCodeParser.Assign_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 211
                self.var_assign()
                pass

            elif la_ == 2:
                self.state = 212
                self.array_asign()
                pass


            self.state = 215
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_line" ):
                return visitor.visitExpr_line(self)
            else:
                return visitor.visitChildren(self)




    def expr_line(self):

        localctx = ZCodeParser.Expr_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.expression()
            self.state = 218
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

        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_IF]:
                self.state = 220
                self.if_statement()
                pass
            elif token in [ZCodeParser.KW_FOR]:
                self.state = 221
                self.for_statement()
                pass
            elif token in [ZCodeParser.KW_BREAK]:
                self.state = 222
                self.break_statement()
                pass
            elif token in [ZCodeParser.KW_CONTINUE]:
                self.state = 223
                self.continue_statement()
                pass
            elif token in [ZCodeParser.KW_RETURN]:
                self.state = 224
                self.return_statement()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.state = 225
                self.block_statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 228
            self.end_line()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_def" ):
                return visitor.visitType_def(self)
            else:
                return visitor.visitChildren(self)




    def type_def(self):

        localctx = ZCodeParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_type_def" ):
                return visitor.visitImplicit_type_def(self)
            else:
                return visitor.visitChildren(self)




    def implicit_type_def(self):

        localctx = ZCodeParser.Implicit_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_implicit_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.KW_VAR or _la==ZCodeParser.KW_DYNAMIC):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_def" ):
                return visitor.visitVar_def(self)
            else:
                return visitor.visitChildren(self)




    def var_def(self):

        localctx = ZCodeParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_def)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.static_var_def()
                pass
            elif token in [ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_init" ):
                return visitor.visitValue_init(self)
            else:
                return visitor.visitChildren(self)




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 239
            self.expression()
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

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_static_var_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_var_def" ):
                return visitor.visitStatic_var_def(self)
            else:
                return visitor.visitChildren(self)




    def static_var_def(self):

        localctx = ZCodeParser.Static_var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_static_var_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.type_def()
            self.state = 242
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_ASSIGN:
                self.state = 243
                self.value_init()


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

        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_var_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_var_def" ):
                return visitor.visitDynamic_var_def(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_var_def(self):

        localctx = ZCodeParser.Dynamic_var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dynamic_var_def)
        self._la = 0 # Token type
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ZCodeParser.KW_VAR)
                self.state = 247
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 248
                self.value_init()
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 250
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.OP_ASSIGN:
                    self.state = 251
                    self.value_init()


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = ZCodeParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 257
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def dim_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dim_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_list" ):
                return visitor.visitDim_list(self)
            else:
                return visitor.visitChildren(self)




    def dim_list(self):

        localctx = ZCodeParser.Dim_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dim_list)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.expression()
                self.state = 260
                self.dim_list_tail()
                pass
            elif token in [ZCodeParser.SEP_CLOSE_BRACK]:
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


    class Dim_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def dim_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dim_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_list_tail" ):
                return visitor.visitDim_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def dim_list_tail(self):

        localctx = ZCodeParser.Dim_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dim_list_tail)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.SEP_COMA)
                self.state = 266
                self.expression()
                self.state = 267
                self.dim_list_tail()
                pass
            elif token in [ZCodeParser.SEP_CLOSE_BRACK]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dim" ):
                return visitor.visitArray_dim(self)
            else:
                return visitor.visitChildren(self)




    def array_dim(self):

        localctx = ZCodeParser.Array_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 273
            self.dim_list()
            self.state = 274
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


        def array_implicit_def(self):
            return self.getTypedRuleContext(ZCodeParser.Array_implicit_defContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_def" ):
                return visitor.visitArray_def(self)
            else:
                return visitor.visitChildren(self)




    def array_def(self):

        localctx = ZCodeParser.Array_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_def)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.array_static_def()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.array_implicit_def()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_identifier" ):
                return visitor.visitArray_identifier(self)
            else:
                return visitor.visitChildren(self)




    def array_identifier(self):

        localctx = ZCodeParser.Array_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 281
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


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_static_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_static_def" ):
                return visitor.visitArray_static_def(self)
            else:
                return visitor.visitChildren(self)




    def array_static_def(self):

        localctx = ZCodeParser.Array_static_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_static_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.type_def()
            self.state = 284
            self.array_identifier()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_ASSIGN:
                self.state = 285
                self.array_init()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_implicit_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def array_identifier(self):
            return self.getTypedRuleContext(ZCodeParser.Array_identifierContext,0)


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_implicit_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_implicit_def" ):
                return visitor.visitArray_implicit_def(self)
            else:
                return visitor.visitChildren(self)




    def array_implicit_def(self):

        localctx = ZCodeParser.Array_implicit_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_implicit_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.KW_VAR)
            self.state = 289
            self.array_identifier()
            self.state = 290
            self.array_init()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.state = 293
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 294
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


    class Array_value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_BRACK(self):
            return self.getToken(ZCodeParser.SEP_OPEN_BRACK, 0)

        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def array_value_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Array_value_initContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Array_value_initContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_init" ):
                return visitor.visitArray_value_init(self)
            else:
                return visitor.visitChildren(self)




    def array_value_init(self):

        localctx = ZCodeParser.Array_value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_value_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 299 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 298
                    self.array_value_init()
                    self.state = 301 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.SEP_OPEN_BRACK):
                        break

                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 303
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 306
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_asignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_asign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_asign" ):
                return visitor.visitArray_asign(self)
            else:
                return visitor.visitChildren(self)




    def array_asign(self):

        localctx = ZCodeParser.Array_asignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_asign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 309
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


        def param_def_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_list_tailContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def_list" ):
                return visitor.visitParam_def_list(self)
            else:
                return visitor.visitChildren(self)




    def param_def_list(self):

        localctx = ZCodeParser.Param_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param_def_list)
        self._la = 0 # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.param()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEW_LINE:
                    self.state = 312
                    self.end_line()


                self.state = 315
                self.param_def_list_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEW_LINE:
                    self.state = 317
                    self.end_line()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def_list_tail" ):
                return visitor.visitParam_def_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_def_list_tail(self):

        localctx = ZCodeParser.Param_def_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param_def_list_tail)
        self._la = 0 # Token type
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(ZCodeParser.SEP_COMA)
                self.state = 324
                self.param()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEW_LINE:
                    self.state = 325
                    self.end_line()


                self.state = 328
                self.param_def_list_tail()
                pass
            elif token in [ZCodeParser.SEP_CLOSE_PAREN]:
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

        def array_def(self):
            return self.getTypedRuleContext(ZCodeParser.Array_defContext,0)


        def var_def(self):
            return self.getTypedRuleContext(ZCodeParser.Var_defContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.array_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.var_def()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def" ):
                return visitor.visitParam_def(self)
            else:
                return visitor.visitChildren(self)




    def param_def(self):

        localctx = ZCodeParser.Param_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_param_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 338
            self.param_def_list()
            self.state = 339
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


        def inner_scope(self):
            return self.getTypedRuleContext(ZCodeParser.Inner_scopeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)




    def func_def(self):

        localctx = ZCodeParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZCodeParser.KW_FUNC)
            self.state = 342
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 343
            self.param_def()
            self.state = 344
            self.inner_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foward_func_defContext(ParserRuleContext):
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
            return ZCodeParser.RULE_foward_func_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFoward_func_def" ):
                return visitor.visitFoward_func_def(self)
            else:
                return visitor.visitChildren(self)




    def foward_func_def(self):

        localctx = ZCodeParser.Foward_func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_foward_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZCodeParser.KW_FUNC)
            self.state = 347
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 348
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = ZCodeParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_TRUE) | (1 << ZCodeParser.KW_FALSE) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.SEP_OPEN_PAREN) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 350
                self.expression()
                self.state = 355
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.string_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.relation_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.logic_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 359
                self.add_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 360
                self.multi_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 361
                self.negate_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 362
                self.primary_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 363
                self.array_expr(0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = ZCodeParser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_string_expr)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.relation_expr()
                self.state = 367
                self.string_op()
                self.state = 368
                self.relation_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_op" ):
                return visitor.visitString_op(self)
            else:
                return visitor.visitChildren(self)




    def string_op(self):

        localctx = ZCodeParser.String_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_string_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_expr" ):
                return visitor.visitRelation_expr(self)
            else:
                return visitor.visitChildren(self)




    def relation_expr(self):

        localctx = ZCodeParser.Relation_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_relation_expr)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.logic_expr(0)
                self.state = 376
                self.relational_op()
                self.state = 377
                self.logic_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_op" ):
                return visitor.visitRelational_op(self)
            else:
                return visitor.visitChildren(self)




    def relational_op(self):

        localctx = ZCodeParser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_EQUAL) | (1 << ZCodeParser.OP_NOT_EQUAL) | (1 << ZCodeParser.OP_SMALLER) | (1 << ZCodeParser.OP_GREATER) | (1 << ZCodeParser.OP_SMALLER_EQUAL) | (1 << ZCodeParser.OP_GREATER_EQUAL) | (1 << ZCodeParser.OP_STRING_EQUAL))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_expr" ):
                return visitor.visitLogic_expr(self)
            else:
                return visitor.visitChildren(self)



    def logic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    self.logic_op()
                    self.state = 389
                    self.add_expr(0) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_op" ):
                return visitor.visitLogic_op(self)
            else:
                return visitor.visitChildren(self)




    def logic_op(self):

        localctx = ZCodeParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.OP_AND or _la==ZCodeParser.OP_OR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_add_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.multi_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 401
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 402
                    self.add_op()
                    self.state = 403
                    self.multi_expr(0) 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = ZCodeParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.OP_ADD or _la==ZCodeParser.OP_SUBTRACT):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_expr" ):
                return visitor.visitMulti_expr(self)
            else:
                return visitor.visitChildren(self)



    def multi_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multi_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_multi_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.negate_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multi_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multi_expr)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    self.multi_op()
                    self.state = 417
                    self.negate_expr() 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_op" ):
                return visitor.visitMulti_op(self)
            else:
                return visitor.visitChildren(self)




    def multi_op(self):

        localctx = ZCodeParser.Multi_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_multi_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_MULTI) | (1 << ZCodeParser.OP_DIVIDE) | (1 << ZCodeParser.OP_REMAINDER))) != 0)):
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


        def primary_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Primary_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_negate_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate_expr" ):
                return visitor.visitNegate_expr(self)
            else:
                return visitor.visitChildren(self)




    def negate_expr(self):

        localctx = ZCodeParser.Negate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_negate_expr)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.negate_op()
                self.state = 427
                self.negate_expr()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.primary_expression()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate_op" ):
                return visitor.visitNegate_op(self)
            else:
                return visitor.visitChildren(self)




    def negate_op(self):

        localctx = ZCodeParser.Negate_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_negate_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(ZCodeParser.OP_NOT)
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


        def array_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_primary_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = ZCodeParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_primary_expression)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(ZCodeParser.SEP_OPEN_PAREN)
                self.state = 435
                self.expression()
                self.state = 436
                self.match(ZCodeParser.SEP_CLOSE_PAREN)
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.literal()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.array_expr(0)
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


        def array_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_exprContext,0)


        def indexer(self):
            return self.getTypedRuleContext(ZCodeParser.IndexerContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expr" ):
                return visitor.visitArray_expr(self)
            else:
                return visitor.visitChildren(self)



    def array_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Array_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_array_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Array_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_expr)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 446
                    self.indexer() 
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexer" ):
                return visitor.visitIndexer(self)
            else:
                return visitor.visitChildren(self)




    def indexer(self):

        localctx = ZCodeParser.IndexerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_indexer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 453
            self.index_op()
            self.state = 454
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


        def SEP_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEP_COMA)
            else:
                return self.getToken(ZCodeParser.SEP_COMA, i)

        def index_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Index_opContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Index_opContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.expression()
            self.state = 461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 457
                    self.match(ZCodeParser.SEP_COMA)
                    self.state = 458
                    self.index_op() 
                self.state = 463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_term)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
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


        def elif_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_clauseContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_clauseContext,i)


        def else_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.if_clause()
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.KW_ELIF:
                self.state = 469
                self.elif_clause()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.KW_ELSE:
                self.state = 475
                self.else_clause()


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


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_clause" ):
                return visitor.visitIf_clause(self)
            else:
                return visitor.visitChildren(self)




    def if_clause(self):

        localctx = ZCodeParser.If_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_if_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(ZCodeParser.KW_IF)
            self.state = 479
            self.if_condition()
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEW_LINE:
                self.state = 480
                self.end_line()


            self.state = 483
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


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_clause" ):
                return visitor.visitElif_clause(self)
            else:
                return visitor.visitChildren(self)




    def elif_clause(self):

        localctx = ZCodeParser.Elif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_elif_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(ZCodeParser.KW_ELIF)
            self.state = 486
            self.if_condition()
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEW_LINE:
                self.state = 487
                self.end_line()


            self.state = 490
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = ZCodeParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(ZCodeParser.KW_ELSE)
            self.state = 493
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = ZCodeParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 496
            self.expression()
            self.state = 497
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


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.for_clause()
            self.state = 500
            self.condition_clause()
            self.state = 501
            self.update_clause()
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEW_LINE:
                self.state = 502
                self.end_line()


            self.state = 505
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_clause" ):
                return visitor.visitFor_clause(self)
            else:
                return visitor.visitChildren(self)




    def for_clause(self):

        localctx = ZCodeParser.For_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_for_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(ZCodeParser.KW_FOR)
            self.state = 508
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_clause" ):
                return visitor.visitCondition_clause(self)
            else:
                return visitor.visitChildren(self)




    def condition_clause(self):

        localctx = ZCodeParser.Condition_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_condition_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 511
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_clause" ):
                return visitor.visitUpdate_clause(self)
            else:
                return visitor.visitChildren(self)




    def update_clause(self):

        localctx = ZCodeParser.Update_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_update_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(ZCodeParser.KW_BY)
            self.state = 514
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(ZCodeParser.KW_RETURN)
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_TRUE) | (1 << ZCodeParser.KW_FALSE) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.SEP_OPEN_PAREN) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 521
                self.expression()


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


        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_passing_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassing_arg" ):
                return visitor.visitPassing_arg(self)
            else:
                return visitor.visitChildren(self)




    def passing_arg(self):

        localctx = ZCodeParser.Passing_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_passing_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 525
            self.passing_list()
            self.state = 526
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassing_list" ):
                return visitor.visitPassing_list(self)
            else:
                return visitor.visitChildren(self)




    def passing_list(self):

        localctx = ZCodeParser.Passing_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_passing_list)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.expression()
                self.state = 529
                self.passing_list_tail()
                pass
            elif token in [ZCodeParser.SEP_CLOSE_BRACK]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassing_list_tail" ):
                return visitor.visitPassing_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def passing_list_tail(self):

        localctx = ZCodeParser.Passing_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_passing_list_tail)
        try:
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(ZCodeParser.SEP_COMA)
                self.state = 535
                self.expression()
                self.state = 536
                self.passing_list_tail()
                pass
            elif token in [ZCodeParser.SEP_CLOSE_BRACK]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 542
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

        def lines(self):
            return self.getTypedRuleContext(ZCodeParser.LinesContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def end_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.End_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.End_lineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 545
                self.end_line()


            self.state = 548
            self.lines()
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEW_LINE:
                self.state = 549
                self.end_line()


            self.state = 552
            self.match(ZCodeParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def OP_SUBTRACT(self):
            return self.getToken(ZCodeParser.OP_SUBTRACT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_number" ):
                return visitor.visitSign_number(self)
            else:
                return visitor.visitChildren(self)




    def sign_number(self):

        localctx = ZCodeParser.Sign_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_sign_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_SUBTRACT]:
                self.state = 554
                self.match(ZCodeParser.OP_SUBTRACT)
                pass
            elif token in [ZCodeParser.NUMBER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 558
            self.match(ZCodeParser.NUMBER)
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

        def sign_number(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_numberContext,0)


        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def boolean(self):
            return self.getTypedRuleContext(ZCodeParser.BooleanContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_literal)
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_SUBTRACT, ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.sign_number()
                pass
            elif token in [ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
                self.match(ZCodeParser.STRING)
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 562
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = ZCodeParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.KW_TRUE or _la==ZCodeParser.KW_FALSE):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_line" ):
                return visitor.visitEnd_line(self)
            else:
                return visitor.visitChildren(self)




    def end_line(self):

        localctx = ZCodeParser.End_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_end_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 567
                    self.match(ZCodeParser.NEW_LINE)

                else:
                    raise NoViableAltException(self)
                self.state = 570 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self._predicates[40] = self.logic_expr_sempred
        self._predicates[42] = self.add_expr_sempred
        self._predicates[44] = self.multi_expr_sempred
        self._predicates[49] = self.array_expr_sempred
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
         

    def array_expr_sempred(self, localctx:Array_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




