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
        buf.write("\u0256\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\3\2\3\2\7\2\u00af\n\2\f\2\16\2\u00b2\13\2\3\2\7\2\u00b5")
        buf.write("\n\2\f\2\16\2\u00b8\13\2\3\2\3\2\7\2\u00bc\n\2\f\2\16")
        buf.write("\2\u00bf\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\5\5\u00cf\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00d7\n\6\3\7\3\7\7\7\u00db\n\7\f\7\16\7\u00de\13")
        buf.write("\7\3\b\3\b\3\b\5\b\u00e3\n\b\3\t\3\t\5\t\u00e7\n\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\5\n\u00ee\n\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ff\n\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\5\20\u0107\n\20\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\23\3\23\5\23\u0111\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u011d")
        buf.write("\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0129\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\5\36\u013e\n\36\3\37\3\37\5\37\u0142\n\37\3 \3 ")
        buf.write("\3 \3!\3!\3!\5!\u014a\n!\3\"\3\"\5\"\u014e\n\"\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u0162\n\'\3(\3(\3(\3(\3(\5(\u0169\n(\3)\3)\5)\u016d")
        buf.write("\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\7-\u017e")
        buf.write("\n-\f-\16-\u0181\13-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u018b")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u0192\n/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u019b\n\61\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\7\63\u01a6\n\63\f\63\16\63\u01a9\13")
        buf.write("\63\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65")
        buf.write("\u01b4\n\65\f\65\16\65\u01b7\13\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\7\67\u01c2\n\67\f\67\16\67\u01c5")
        buf.write("\13\67\38\38\39\39\39\39\59\u01cd\n9\3:\3:\3;\3;\3;\5")
        buf.write(";\u01d4\n;\3<\3<\5<\u01d8\n<\3=\3=\3=\3>\3>\3>\3>\3?\3")
        buf.write("?\3?\3?\5?\u01e5\n?\3@\3@\3@\3@\3@\3@\5@\u01ed\n@\3A\3")
        buf.write("A\5A\u01f1\nA\3B\3B\3B\3B\7B\u01f7\nB\fB\16B\u01fa\13")
        buf.write("B\3B\3B\3B\3B\5B\u0200\nB\3C\3C\3C\3C\3C\3D\3D\3D\3D\3")
        buf.write("D\3E\3E\3E\3E\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3H\3H\3H\3")
        buf.write("I\3I\3I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3M\5M\u022a\nM\3N\3")
        buf.write("N\3N\3N\3O\3O\3O\3O\5O\u0234\nO\3P\3P\3P\3P\3P\5P\u023b")
        buf.write("\nP\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3S\3S\5S\u0249\nS\3")
        buf.write("T\3T\3U\3U\5U\u024f\nU\3V\6V\u0252\nV\rV\16V\u0253\3V")
        buf.write("\2\5dhlW\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write("\u00a6\u00a8\u00aa\2\t\3\2\6\b\3\2\n\13\4\2\37\37!&\3")
        buf.write("\2\35\36\3\2\27\30\3\2\31\33\3\2\4\5\2\u023a\2\u00ac\3")
        buf.write("\2\2\2\4\u00c2\3\2\2\2\6\u00c9\3\2\2\2\b\u00ce\3\2\2\2")
        buf.write("\n\u00d6\3\2\2\2\f\u00dc\3\2\2\2\16\u00e2\3\2\2\2\20\u00e6")
        buf.write("\3\2\2\2\22\u00ed\3\2\2\2\24\u00f1\3\2\2\2\26\u00f4\3")
        buf.write("\2\2\2\30\u00fe\3\2\2\2\32\u0100\3\2\2\2\34\u0102\3\2")
        buf.write("\2\2\36\u0106\3\2\2\2 \u0108\3\2\2\2\"\u010b\3\2\2\2$")
        buf.write("\u0110\3\2\2\2&\u0112\3\2\2\2(\u011c\3\2\2\2*\u011e\3")
        buf.write("\2\2\2,\u0121\3\2\2\2.\u0128\3\2\2\2\60\u012a\3\2\2\2")
        buf.write("\62\u012e\3\2\2\2\64\u0130\3\2\2\2\66\u0133\3\2\2\28\u0136")
        buf.write("\3\2\2\2:\u013a\3\2\2\2<\u0141\3\2\2\2>\u0143\3\2\2\2")
        buf.write("@\u0149\3\2\2\2B\u014d\3\2\2\2D\u014f\3\2\2\2F\u0153\3")
        buf.write("\2\2\2H\u0156\3\2\2\2J\u0159\3\2\2\2L\u0161\3\2\2\2N\u0168")
        buf.write("\3\2\2\2P\u016c\3\2\2\2R\u016e\3\2\2\2T\u0172\3\2\2\2")
        buf.write("V\u0178\3\2\2\2X\u017f\3\2\2\2Z\u018a\3\2\2\2\\\u0191")
        buf.write("\3\2\2\2^\u0193\3\2\2\2`\u019a\3\2\2\2b\u019c\3\2\2\2")
        buf.write("d\u019e\3\2\2\2f\u01aa\3\2\2\2h\u01ac\3\2\2\2j\u01b8\3")
        buf.write("\2\2\2l\u01ba\3\2\2\2n\u01c6\3\2\2\2p\u01cc\3\2\2\2r\u01ce")
        buf.write("\3\2\2\2t\u01d3\3\2\2\2v\u01d7\3\2\2\2x\u01d9\3\2\2\2")
        buf.write("z\u01dc\3\2\2\2|\u01e0\3\2\2\2~\u01ec\3\2\2\2\u0080\u01f0")
        buf.write("\3\2\2\2\u0082\u01f2\3\2\2\2\u0084\u0201\3\2\2\2\u0086")
        buf.write("\u0206\3\2\2\2\u0088\u020b\3\2\2\2\u008a\u020f\3\2\2\2")
        buf.write("\u008c\u0213\3\2\2\2\u008e\u0219\3\2\2\2\u0090\u021c\3")
        buf.write("\2\2\2\u0092\u021f\3\2\2\2\u0094\u0222\3\2\2\2\u0096\u0224")
        buf.write("\3\2\2\2\u0098\u0226\3\2\2\2\u009a\u022b\3\2\2\2\u009c")
        buf.write("\u0233\3\2\2\2\u009e\u023a\3\2\2\2\u00a0\u023c\3\2\2\2")
        buf.write("\u00a2\u023f\3\2\2\2\u00a4\u0248\3\2\2\2\u00a6\u024a\3")
        buf.write("\2\2\2\u00a8\u024e\3\2\2\2\u00aa\u0251\3\2\2\2\u00ac\u00b0")
        buf.write("\5\u00a8U\2\u00ad\u00af\5\6\4\2\u00ae\u00ad\3\2\2\2\u00af")
        buf.write("\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00b6\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\5")
        buf.write("\b\5\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b9\u00bd\5\4\3\2\u00ba\u00bc\5\b\5\2")
        buf.write("\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3")
        buf.write("\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00c0\u00c1\7\2\2\3\u00c1\3\3\2\2\2\u00c2\u00c3")
        buf.write("\7\f\2\2\u00c3\u00c4\7\3\2\2\u00c4\u00c5\7(\2\2\u00c5")
        buf.write("\u00c6\7)\2\2\u00c6\u00c7\5\u00a8U\2\u00c7\u00c8\5\n\6")
        buf.write("\2\u00c8\5\3\2\2\2\u00c9\u00ca\5V,\2\u00ca\u00cb\5\u00aa")
        buf.write("V\2\u00cb\7\3\2\2\2\u00cc\u00cf\5T+\2\u00cd\u00cf\5\20")
        buf.write("\t\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\t\3")
        buf.write("\2\2\2\u00d0\u00d1\5\u00a2R\2\u00d1\u00d2\5\u00aaV\2\u00d2")
        buf.write("\u00d7\3\2\2\2\u00d3\u00d4\5\u0098M\2\u00d4\u00d5\5\u00aa")
        buf.write("V\2\u00d5\u00d7\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6\u00d3")
        buf.write("\3\2\2\2\u00d7\13\3\2\2\2\u00d8\u00db\5\16\b\2\u00d9\u00db")
        buf.write("\5\26\f\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\r\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e3\5\20")
        buf.write("\t\2\u00e0\u00e3\5\22\n\2\u00e1\u00e3\5\24\13\2\u00e2")
        buf.write("\u00df\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2")
        buf.write("\u00e3\17\3\2\2\2\u00e4\u00e7\5\36\20\2\u00e5\u00e7\5")
        buf.write("\62\32\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8\u00e9\5\u00aaV\2\u00e9\21\3\2\2\2")
        buf.write("\u00ea\u00ee\5*\26\2\u00eb\u00ee\5F$\2\u00ec\u00ee\5H")
        buf.write("%\2\u00ed\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\5\u00aaV\2\u00f0")
        buf.write("\23\3\2\2\2\u00f1\u00f2\5Z.\2\u00f2\u00f3\5\u00aaV\2\u00f3")
        buf.write("\25\3\2\2\2\u00f4\u00f5\5\30\r\2\u00f5\u00f6\5\u00aaV")
        buf.write("\2\u00f6\27\3\2\2\2\u00f7\u00ff\5\u0082B\2\u00f8\u00ff")
        buf.write("\5\u008cG\2\u00f9\u00ff\5\u0094K\2\u00fa\u00ff\5\u0096")
        buf.write("L\2\u00fb\u00ff\5\u0098M\2\u00fc\u00ff\5\u00a2R\2\u00fd")
        buf.write("\u00ff\5\u00a0Q\2\u00fe\u00f7\3\2\2\2\u00fe\u00f8\3\2")
        buf.write("\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fb")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("\31\3\2\2\2\u0100\u0101\t\2\2\2\u0101\33\3\2\2\2\u0102")
        buf.write("\u0103\t\3\2\2\u0103\35\3\2\2\2\u0104\u0107\5&\24\2\u0105")
        buf.write("\u0107\5(\25\2\u0106\u0104\3\2\2\2\u0106\u0105\3\2\2\2")
        buf.write("\u0107\37\3\2\2\2\u0108\u0109\5\32\16\2\u0109\u010a\7")
        buf.write("\60\2\2\u010a!\3\2\2\2\u010b\u010c\7 \2\2\u010c\u010d")
        buf.write("\5Z.\2\u010d#\3\2\2\2\u010e\u0111\5\"\22\2\u010f\u0111")
        buf.write("\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111")
        buf.write("%\3\2\2\2\u0112\u0113\5\32\16\2\u0113\u0114\7\60\2\2\u0114")
        buf.write("\u0115\5$\23\2\u0115\'\3\2\2\2\u0116\u0117\7\n\2\2\u0117")
        buf.write("\u0118\7\60\2\2\u0118\u011d\5\"\22\2\u0119\u011a\7\13")
        buf.write("\2\2\u011a\u011b\7\60\2\2\u011b\u011d\5$\23\2\u011c\u0116")
        buf.write("\3\2\2\2\u011c\u0119\3\2\2\2\u011d)\3\2\2\2\u011e\u011f")
        buf.write("\7\60\2\2\u011f\u0120\5\"\22\2\u0120+\3\2\2\2\u0121\u0122")
        buf.write("\7\61\2\2\u0122\u0123\5.\30\2\u0123-\3\2\2\2\u0124\u0125")
        buf.write("\7,\2\2\u0125\u0126\7\61\2\2\u0126\u0129\5.\30\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u0124\3\2\2\2\u0128\u0127\3\2\2\2")
        buf.write("\u0129/\3\2\2\2\u012a\u012b\7*\2\2\u012b\u012c\5,\27\2")
        buf.write("\u012c\u012d\7+\2\2\u012d\61\3\2\2\2\u012e\u012f\58\35")
        buf.write("\2\u012f\63\3\2\2\2\u0130\u0131\5\32\16\2\u0131\u0132")
        buf.write("\5\66\34\2\u0132\65\3\2\2\2\u0133\u0134\7\60\2\2\u0134")
        buf.write("\u0135\5\60\31\2\u0135\67\3\2\2\2\u0136\u0137\5\32\16")
        buf.write("\2\u0137\u0138\5\66\34\2\u0138\u0139\5<\37\2\u01399\3")
        buf.write("\2\2\2\u013a\u013d\7 \2\2\u013b\u013e\5Z.\2\u013c\u013e")
        buf.write("\5D#\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e;")
        buf.write("\3\2\2\2\u013f\u0142\5:\36\2\u0140\u0142\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142=\3\2\2\2\u0143")
        buf.write("\u0144\5B\"\2\u0144\u0145\5@!\2\u0145?\3\2\2\2\u0146\u0147")
        buf.write("\7,\2\2\u0147\u014a\5> \2\u0148\u014a\3\2\2\2\u0149\u0146")
        buf.write("\3\2\2\2\u0149\u0148\3\2\2\2\u014aA\3\2\2\2\u014b\u014e")
        buf.write("\5D#\2\u014c\u014e\5Z.\2\u014d\u014b\3\2\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014eC\3\2\2\2\u014f\u0150\7*\2\2\u0150\u0151")
        buf.write("\5> \2\u0151\u0152\7+\2\2\u0152E\3\2\2\2\u0153\u0154\7")
        buf.write("\60\2\2\u0154\u0155\5:\36\2\u0155G\3\2\2\2\u0156\u0157")
        buf.write("\5x=\2\u0157\u0158\5J&\2\u0158I\3\2\2\2\u0159\u015a\7")
        buf.write(" \2\2\u015a\u015b\5Z.\2\u015bK\3\2\2\2\u015c\u015d\5P")
        buf.write(")\2\u015d\u015e\5\u00a8U\2\u015e\u015f\5N(\2\u015f\u0162")
        buf.write("\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u015c\3\2\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162M\3\2\2\2\u0163\u0164\7,\2\2\u0164")
        buf.write("\u0165\5P)\2\u0165\u0166\5N(\2\u0166\u0169\3\2\2\2\u0167")
        buf.write("\u0169\3\2\2\2\u0168\u0163\3\2\2\2\u0168\u0167\3\2\2\2")
        buf.write("\u0169O\3\2\2\2\u016a\u016d\5\64\33\2\u016b\u016d\5 \21")
        buf.write("\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016dQ\3\2")
        buf.write("\2\2\u016e\u016f\7(\2\2\u016f\u0170\5L\'\2\u0170\u0171")
        buf.write("\7)\2\2\u0171S\3\2\2\2\u0172\u0173\7\f\2\2\u0173\u0174")
        buf.write("\7\60\2\2\u0174\u0175\5R*\2\u0175\u0176\5\u00a8U\2\u0176")
        buf.write("\u0177\5\n\6\2\u0177U\3\2\2\2\u0178\u0179\7\f\2\2\u0179")
        buf.write("\u017a\7\60\2\2\u017a\u017b\5R*\2\u017bW\3\2\2\2\u017c")
        buf.write("\u017e\5Z.\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180Y\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u018b\5\\/\2\u0183\u018b\5`\61\2")
        buf.write("\u0184\u018b\5d\63\2\u0185\u018b\5h\65\2\u0186\u018b\5")
        buf.write("l\67\2\u0187\u018b\5p9\2\u0188\u018b\5~@\2\u0189\u018b")
        buf.write("\5v<\2\u018a\u0182\3\2\2\2\u018a\u0183\3\2\2\2\u018a\u0184")
        buf.write("\3\2\2\2\u018a\u0185\3\2\2\2\u018a\u0186\3\2\2\2\u018a")
        buf.write("\u0187\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2")
        buf.write("\u018b[\3\2\2\2\u018c\u018d\5`\61\2\u018d\u018e\5^\60")
        buf.write("\2\u018e\u018f\5`\61\2\u018f\u0192\3\2\2\2\u0190\u0192")
        buf.write("\5`\61\2\u0191\u018c\3\2\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("]\3\2\2\2\u0193\u0194\7\'\2\2\u0194_\3\2\2\2\u0195\u0196")
        buf.write("\5d\63\2\u0196\u0197\5b\62\2\u0197\u0198\5d\63\2\u0198")
        buf.write("\u019b\3\2\2\2\u0199\u019b\5d\63\2\u019a\u0195\3\2\2\2")
        buf.write("\u019a\u0199\3\2\2\2\u019ba\3\2\2\2\u019c\u019d\t\4\2")
        buf.write("\2\u019dc\3\2\2\2\u019e\u019f\b\63\1\2\u019f\u01a0\5h")
        buf.write("\65\2\u01a0\u01a7\3\2\2\2\u01a1\u01a2\f\4\2\2\u01a2\u01a3")
        buf.write("\5f\64\2\u01a3\u01a4\5h\65\2\u01a4\u01a6\3\2\2\2\u01a5")
        buf.write("\u01a1\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8e\3\2\2\2\u01a9\u01a7\3\2\2")
        buf.write("\2\u01aa\u01ab\t\5\2\2\u01abg\3\2\2\2\u01ac\u01ad\b\65")
        buf.write("\1\2\u01ad\u01ae\5l\67\2\u01ae\u01b5\3\2\2\2\u01af\u01b0")
        buf.write("\f\4\2\2\u01b0\u01b1\5j\66\2\u01b1\u01b2\5l\67\2\u01b2")
        buf.write("\u01b4\3\2\2\2\u01b3\u01af\3\2\2\2\u01b4\u01b7\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6i\3\2\2")
        buf.write("\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\t\6\2\2\u01b9k\3\2")
        buf.write("\2\2\u01ba\u01bb\b\67\1\2\u01bb\u01bc\5p9\2\u01bc\u01c3")
        buf.write("\3\2\2\2\u01bd\u01be\f\4\2\2\u01be\u01bf\5n8\2\u01bf\u01c0")
        buf.write("\5p9\2\u01c0\u01c2\3\2\2\2\u01c1\u01bd\3\2\2\2\u01c2\u01c5")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4")
        buf.write("m\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\t\7\2\2\u01c7")
        buf.write("o\3\2\2\2\u01c8\u01c9\5r:\2\u01c9\u01ca\5p9\2\u01ca\u01cd")
        buf.write("\3\2\2\2\u01cb\u01cd\5t;\2\u01cc\u01c8\3\2\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cdq\3\2\2\2\u01ce\u01cf\7\34\2\2\u01cfs\3")
        buf.write("\2\2\2\u01d0\u01d1\7\30\2\2\u01d1\u01d4\5t;\2\u01d2\u01d4")
        buf.write("\5v<\2\u01d3\u01d0\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4u")
        buf.write("\3\2\2\2\u01d5\u01d8\5x=\2\u01d6\u01d8\5~@\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8w\3\2\2\2\u01d9\u01da")
        buf.write("\5\u0080A\2\u01da\u01db\5z>\2\u01dby\3\2\2\2\u01dc\u01dd")
        buf.write("\7*\2\2\u01dd\u01de\5|?\2\u01de\u01df\7+\2\2\u01df{\3")
        buf.write("\2\2\2\u01e0\u01e4\5Z.\2\u01e1\u01e2\7,\2\2\u01e2\u01e5")
        buf.write("\5|?\2\u01e3\u01e5\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e5}\3\2\2\2\u01e6\u01e7\7(\2\2\u01e7\u01e8")
        buf.write("\5Z.\2\u01e8\u01e9\7)\2\2\u01e9\u01ed\3\2\2\2\u01ea\u01ed")
        buf.write("\5\u00a4S\2\u01eb\u01ed\5\u0080A\2\u01ec\u01e6\3\2\2\2")
        buf.write("\u01ec\u01ea\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed\177\3\2")
        buf.write("\2\2\u01ee\u01f1\7\60\2\2\u01ef\u01f1\5\u00a0Q\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1\u0081\3\2\2\2")
        buf.write("\u01f2\u01f8\5\u0084C\2\u01f3\u01f4\5\u00aaV\2\u01f4\u01f5")
        buf.write("\5\u0086D\2\u01f5\u01f7\3\2\2\2\u01f6\u01f3\3\2\2\2\u01f7")
        buf.write("\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2")
        buf.write("\u01f9\u01ff\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fc\5")
        buf.write("\u00aaV\2\u01fc\u01fd\5\u0088E\2\u01fd\u0200\3\2\2\2\u01fe")
        buf.write("\u0200\3\2\2\2\u01ff\u01fb\3\2\2\2\u01ff\u01fe\3\2\2\2")
        buf.write("\u0200\u0083\3\2\2\2\u0201\u0202\7\22\2\2\u0202\u0203")
        buf.write("\5\u008aF\2\u0203\u0204\5\u00a8U\2\u0204\u0205\5\30\r")
        buf.write("\2\u0205\u0085\3\2\2\2\u0206\u0207\7\24\2\2\u0207\u0208")
        buf.write("\5\u008aF\2\u0208\u0209\5\u00a8U\2\u0209\u020a\5\30\r")
        buf.write("\2\u020a\u0087\3\2\2\2\u020b\u020c\7\23\2\2\u020c\u020d")
        buf.write("\5\u00a8U\2\u020d\u020e\5\30\r\2\u020e\u0089\3\2\2\2\u020f")
        buf.write("\u0210\7(\2\2\u0210\u0211\5Z.\2\u0211\u0212\7)\2\2\u0212")
        buf.write("\u008b\3\2\2\2\u0213\u0214\5\u008eH\2\u0214\u0215\5\u0090")
        buf.write("I\2\u0215\u0216\5\u0092J\2\u0216\u0217\5\u00a8U\2\u0217")
        buf.write("\u0218\5\30\r\2\u0218\u008d\3\2\2\2\u0219\u021a\7\r\2")
        buf.write("\2\u021a\u021b\7\60\2\2\u021b\u008f\3\2\2\2\u021c\u021d")
        buf.write("\7\16\2\2\u021d\u021e\5Z.\2\u021e\u0091\3\2\2\2\u021f")
        buf.write("\u0220\7\17\2\2\u0220\u0221\5Z.\2\u0221\u0093\3\2\2\2")
        buf.write("\u0222\u0223\7\20\2\2\u0223\u0095\3\2\2\2\u0224\u0225")
        buf.write("\7\21\2\2\u0225\u0097\3\2\2\2\u0226\u0229\7\t\2\2\u0227")
        buf.write("\u022a\5Z.\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2\u0229")
        buf.write("\u0228\3\2\2\2\u022a\u0099\3\2\2\2\u022b\u022c\7(\2\2")
        buf.write("\u022c\u022d\5\u009cO\2\u022d\u022e\7)\2\2\u022e\u009b")
        buf.write("\3\2\2\2\u022f\u0230\5Z.\2\u0230\u0231\5\u009eP\2\u0231")
        buf.write("\u0234\3\2\2\2\u0232\u0234\3\2\2\2\u0233\u022f\3\2\2\2")
        buf.write("\u0233\u0232\3\2\2\2\u0234\u009d\3\2\2\2\u0235\u0236\7")
        buf.write(",\2\2\u0236\u0237\5Z.\2\u0237\u0238\5\u009eP\2\u0238\u023b")
        buf.write("\3\2\2\2\u0239\u023b\3\2\2\2\u023a\u0235\3\2\2\2\u023a")
        buf.write("\u0239\3\2\2\2\u023b\u009f\3\2\2\2\u023c\u023d\7\60\2")
        buf.write("\2\u023d\u023e\5\u009aN\2\u023e\u00a1\3\2\2\2\u023f\u0240")
        buf.write("\7\25\2\2\u0240\u0241\5\u00a8U\2\u0241\u0242\5\f\7\2\u0242")
        buf.write("\u0243\5\u00a8U\2\u0243\u0244\7\26\2\2\u0244\u00a3\3\2")
        buf.write("\2\2\u0245\u0249\7\61\2\2\u0246\u0249\7\62\2\2\u0247\u0249")
        buf.write("\5\u00a6T\2\u0248\u0245\3\2\2\2\u0248\u0246\3\2\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u00a5\3\2\2\2\u024a\u024b\t\b\2\2")
        buf.write("\u024b\u00a7\3\2\2\2\u024c\u024f\5\u00aaV\2\u024d\u024f")
        buf.write("\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024f")
        buf.write("\u00a9\3\2\2\2\u0250\u0252\7/\2\2\u0251\u0250\3\2\2\2")
        buf.write("\u0252\u0253\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3")
        buf.write("\2\2\2\u0254\u00ab\3\2\2\2-\u00b0\u00b6\u00bd\u00ce\u00d6")
        buf.write("\u00da\u00dc\u00e2\u00e6\u00ed\u00fe\u0106\u0110\u011c")
        buf.write("\u0128\u013d\u0141\u0149\u014d\u0161\u0168\u016c\u017f")
        buf.write("\u018a\u0191\u019a\u01a7\u01b5\u01c3\u01cc\u01d3\u01d7")
        buf.write("\u01e4\u01ec\u01f0\u01f8\u01ff\u0229\u0233\u023a\u0248")
        buf.write("\u024e\u0253")
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
                      "SEP_COMA", "COMMENT", "WS", "NEW_LINE", "IDENTIFIER", 
                      "NUMBER", "STRING", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_main_def = 1
    RULE_forward_func = 2
    RULE_define = 3
    RULE_inner_scope = 4
    RULE_lines = 5
    RULE_line = 6
    RULE_def_line = 7
    RULE_assign_line = 8
    RULE_expr_line = 9
    RULE_statement_line = 10
    RULE_statement = 11
    RULE_type_def = 12
    RULE_implicit_type_def = 13
    RULE_var_def = 14
    RULE_var_def_for_param = 15
    RULE_value_init = 16
    RULE_optional_val_init = 17
    RULE_static_var_def = 18
    RULE_dynamic_var_def = 19
    RULE_var_assign = 20
    RULE_dim_list = 21
    RULE_dim_list_tail = 22
    RULE_array_dim = 23
    RULE_array_def = 24
    RULE_array_def_for_param = 25
    RULE_array_identifier = 26
    RULE_array_static_def = 27
    RULE_array_init = 28
    RULE_optional_array_init = 29
    RULE_array_value_init_list = 30
    RULE_array_value_init_tail = 31
    RULE_array_value = 32
    RULE_array_value_init = 33
    RULE_array_assign = 34
    RULE_array_elem_assign = 35
    RULE_array_elem_init = 36
    RULE_param_def_list = 37
    RULE_param_def_list_tail = 38
    RULE_param = 39
    RULE_param_def = 40
    RULE_func_def = 41
    RULE_forward_func_def = 42
    RULE_expressions = 43
    RULE_expression = 44
    RULE_string_expr = 45
    RULE_string_op = 46
    RULE_relation_expr = 47
    RULE_relational_op = 48
    RULE_logic_expr = 49
    RULE_logic_op = 50
    RULE_add_expr = 51
    RULE_add_op = 52
    RULE_multi_expr = 53
    RULE_multi_op = 54
    RULE_negate_expr = 55
    RULE_negate_op = 56
    RULE_sign_expr = 57
    RULE_array_expr = 58
    RULE_array_element_expr = 59
    RULE_indexer = 60
    RULE_index_op = 61
    RULE_primary_expression = 62
    RULE_term = 63
    RULE_if_statement = 64
    RULE_if_clause = 65
    RULE_elif_clause = 66
    RULE_else_clause = 67
    RULE_if_condition = 68
    RULE_for_statement = 69
    RULE_for_clause = 70
    RULE_condition_clause = 71
    RULE_update_clause = 72
    RULE_break_statement = 73
    RULE_continue_statement = 74
    RULE_return_statement = 75
    RULE_passing_arg = 76
    RULE_passing_list = 77
    RULE_passing_list_tail = 78
    RULE_func_call = 79
    RULE_block_statement = 80
    RULE_literal = 81
    RULE_boolean = 82
    RULE_optional_end_line = 83
    RULE_end_line = 84

    ruleNames =  [ "program", "main_def", "forward_func", "define", "inner_scope", 
                   "lines", "line", "def_line", "assign_line", "expr_line", 
                   "statement_line", "statement", "type_def", "implicit_type_def", 
                   "var_def", "var_def_for_param", "value_init", "optional_val_init", 
                   "static_var_def", "dynamic_var_def", "var_assign", "dim_list", 
                   "dim_list_tail", "array_dim", "array_def", "array_def_for_param", 
                   "array_identifier", "array_static_def", "array_init", 
                   "optional_array_init", "array_value_init_list", "array_value_init_tail", 
                   "array_value", "array_value_init", "array_assign", "array_elem_assign", 
                   "array_elem_init", "param_def_list", "param_def_list_tail", 
                   "param", "param_def", "func_def", "forward_func_def", 
                   "expressions", "expression", "string_expr", "string_op", 
                   "relation_expr", "relational_op", "logic_expr", "logic_op", 
                   "add_expr", "add_op", "multi_expr", "multi_op", "negate_expr", 
                   "negate_op", "sign_expr", "array_expr", "array_element_expr", 
                   "indexer", "index_op", "primary_expression", "term", 
                   "if_statement", "if_clause", "elif_clause", "else_clause", 
                   "if_condition", "for_statement", "for_clause", "condition_clause", 
                   "update_clause", "break_statement", "continue_statement", 
                   "return_statement", "passing_arg", "passing_list", "passing_list_tail", 
                   "func_call", "block_statement", "literal", "boolean", 
                   "optional_end_line", "end_line" ]

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
    COMMENT=43
    WS=44
    NEW_LINE=45
    IDENTIFIER=46
    NUMBER=47
    STRING=48
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

        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def main_def(self):
            return self.getTypedRuleContext(ZCodeParser.Main_defContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def forward_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Forward_funcContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Forward_funcContext,i)


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
            self.state = 170
            self.optional_end_line()
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 171
                    self.forward_func() 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 177
                    self.define() 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 183
            self.main_def()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FUNC))) != 0):
                self.state = 184
                self.define()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
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

        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


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
            self.state = 192
            self.match(ZCodeParser.KW_FUNC)
            self.state = 193
            self.match(ZCodeParser.MAIN_TOKEN)
            self.state = 194
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 195
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
            self.state = 196
            self.optional_end_line()
            self.state = 197
            self.inner_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forward_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forward_func_def(self):
            return self.getTypedRuleContext(ZCodeParser.Forward_func_defContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forward_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForward_func" ):
                return visitor.visitForward_func(self)
            else:
                return visitor.visitChildren(self)




    def forward_func(self):

        localctx = ZCodeParser.Forward_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forward_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.forward_func_def()
            self.state = 200
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
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.func_def()
                pass
            elif token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING, ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.def_line()
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


    class Inner_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


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
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.block_statement()
                self.state = 207
                self.end_line()
                pass
            elif token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.return_statement()
                self.state = 210
                self.end_line()
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


        def statement_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Statement_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Statement_lineContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_TRUE) | (1 << ZCodeParser.KW_FALSE) | (1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_RETURN) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FOR) | (1 << ZCodeParser.KW_BREAK) | (1 << ZCodeParser.KW_CONTINUE) | (1 << ZCodeParser.KW_IF) | (1 << ZCodeParser.KW_BEGIN) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.SEP_OPEN_PAREN) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 216
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 214
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 215
                    self.statement_line()
                    pass


                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.def_line()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.assign_line()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 226
                self.var_def()
                pass

            elif la_ == 2:
                self.state = 227
                self.array_def()
                pass


            self.state = 230
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


        def array_assign(self):
            return self.getTypedRuleContext(ZCodeParser.Array_assignContext,0)


        def array_elem_assign(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elem_assignContext,0)


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
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 232
                self.var_assign()
                pass

            elif la_ == 2:
                self.state = 233
                self.array_assign()
                pass

            elif la_ == 3:
                self.state = 234
                self.array_elem_assign()
                pass


            self.state = 237
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
            self.state = 239
            self.expression()
            self.state = 240
            self.end_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_line" ):
                return visitor.visitStatement_line(self)
            else:
                return visitor.visitChildren(self)




    def statement_line(self):

        localctx = ZCodeParser.Statement_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.statement()
            self.state = 243
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


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_IF]:
                self.state = 245
                self.if_statement()
                pass
            elif token in [ZCodeParser.KW_FOR]:
                self.state = 246
                self.for_statement()
                pass
            elif token in [ZCodeParser.KW_BREAK]:
                self.state = 247
                self.break_statement()
                pass
            elif token in [ZCodeParser.KW_CONTINUE]:
                self.state = 248
                self.continue_statement()
                pass
            elif token in [ZCodeParser.KW_RETURN]:
                self.state = 249
                self.return_statement()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.state = 250
                self.block_statement()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.state = 251
                self.func_call()
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
        self.enterRule(localctx, 24, self.RULE_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 26, self.RULE_implicit_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
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
        self.enterRule(localctx, 28, self.RULE_var_def)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.static_var_def()
                pass
            elif token in [ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
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


    class Var_def_for_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_def_for_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_def_for_param" ):
                return visitor.visitVar_def_for_param(self)
            else:
                return visitor.visitChildren(self)




    def var_def_for_param(self):

        localctx = ZCodeParser.Var_def_for_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_def_for_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.type_def()
            self.state = 263
            self.match(ZCodeParser.IDENTIFIER)
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
        self.enterRule(localctx, 32, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 266
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_val_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_val_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_val_init" ):
                return visitor.visitOptional_val_init(self)
            else:
                return visitor.visitChildren(self)




    def optional_val_init(self):

        localctx = ZCodeParser.Optional_val_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_optional_val_init)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.value_init()
                pass
            elif token in [ZCodeParser.NEW_LINE]:
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


    class Static_var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def optional_val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_static_var_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_var_def" ):
                return visitor.visitStatic_var_def(self)
            else:
                return visitor.visitChildren(self)




    def static_var_def(self):

        localctx = ZCodeParser.Static_var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_static_var_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.type_def()
            self.state = 273
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 274
            self.optional_val_init()
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

        def optional_val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_var_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_var_def" ):
                return visitor.visitDynamic_var_def(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_var_def(self):

        localctx = ZCodeParser.Dynamic_var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dynamic_var_def)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(ZCodeParser.KW_VAR)
                self.state = 277
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 278
                self.value_init()
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 280
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 281
                self.optional_val_init()
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
        self.enterRule(localctx, 40, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 285
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

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

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
        self.enterRule(localctx, 42, self.RULE_dim_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ZCodeParser.NUMBER)
            self.state = 288
            self.dim_list_tail()
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

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

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
        self.enterRule(localctx, 44, self.RULE_dim_list_tail)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(ZCodeParser.SEP_COMA)
                self.state = 291
                self.match(ZCodeParser.NUMBER)
                self.state = 292
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
        self.enterRule(localctx, 46, self.RULE_array_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 297
            self.dim_list()
            self.state = 298
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_def" ):
                return visitor.visitArray_def(self)
            else:
                return visitor.visitChildren(self)




    def array_def(self):

        localctx = ZCodeParser.Array_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.array_static_def()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_def_for_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def array_identifier(self):
            return self.getTypedRuleContext(ZCodeParser.Array_identifierContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_def_for_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_def_for_param" ):
                return visitor.visitArray_def_for_param(self)
            else:
                return visitor.visitChildren(self)




    def array_def_for_param(self):

        localctx = ZCodeParser.Array_def_for_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_def_for_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.type_def()
            self.state = 303
            self.array_identifier()
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
        self.enterRule(localctx, 52, self.RULE_array_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 306
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


        def optional_array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_static_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_static_def" ):
                return visitor.visitArray_static_def(self)
            else:
                return visitor.visitChildren(self)




    def array_static_def(self):

        localctx = ZCodeParser.Array_static_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_static_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.type_def()
            self.state = 309
            self.array_identifier()
            self.state = 310
            self.optional_array_init()
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 56, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 313
                self.expression()
                pass
            elif token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 314
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


    class Optional_array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_array_init" ):
                return visitor.visitOptional_array_init(self)
            else:
                return visitor.visitChildren(self)




    def optional_array_init(self):

        localctx = ZCodeParser.Optional_array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_optional_array_init)
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.array_init()
                pass
            elif token in [ZCodeParser.NEW_LINE]:
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


    class Array_value_init_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def array_value_init_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_init_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_init_list" ):
                return visitor.visitArray_value_init_list(self)
            else:
                return visitor.visitChildren(self)




    def array_value_init_list(self):

        localctx = ZCodeParser.Array_value_init_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_value_init_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.array_value()
            self.state = 322
            self.array_value_init_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_init_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def array_value_init_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_init_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_init_tail" ):
                return visitor.visitArray_value_init_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_value_init_tail(self):

        localctx = ZCodeParser.Array_value_init_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_value_init_tail)
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(ZCodeParser.SEP_COMA)
                self.state = 325
                self.array_value_init_list()
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


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_initContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 329
                self.array_value_init()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 330
                self.expression()
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

        def array_value_init_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_init_listContext,0)


        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_init" ):
                return visitor.visitArray_value_init(self)
            else:
                return visitor.visitChildren(self)




    def array_value_init(self):

        localctx = ZCodeParser.Array_value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_array_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 334
            self.array_value_init_list()
            self.state = 335
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_assign" ):
                return visitor.visitArray_assign(self)
            else:
                return visitor.visitChildren(self)




    def array_assign(self):

        localctx = ZCodeParser.Array_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 338
            self.array_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elem_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_exprContext,0)


        def array_elem_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elem_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_elem_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elem_assign" ):
                return visitor.visitArray_elem_assign(self)
            else:
                return visitor.visitChildren(self)




    def array_elem_assign(self):

        localctx = ZCodeParser.Array_elem_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_elem_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.array_element_expr()
            self.state = 341
            self.array_elem_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elem_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_elem_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elem_init" ):
                return visitor.visitArray_elem_init(self)
            else:
                return visitor.visitChildren(self)




    def array_elem_init(self):

        localctx = ZCodeParser.Array_elem_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_elem_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 344
            self.expression()
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


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def param_def_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def_list" ):
                return visitor.visitParam_def_list(self)
            else:
                return visitor.visitChildren(self)




    def param_def_list(self):

        localctx = ZCodeParser.Param_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_param_def_list)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.param()
                self.state = 347
                self.optional_end_line()
                self.state = 348
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def_list_tail" ):
                return visitor.visitParam_def_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_def_list_tail(self):

        localctx = ZCodeParser.Param_def_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_param_def_list_tail)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(ZCodeParser.SEP_COMA)
                self.state = 354
                self.param()
                self.state = 355
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

        def array_def_for_param(self):
            return self.getTypedRuleContext(ZCodeParser.Array_def_for_paramContext,0)


        def var_def_for_param(self):
            return self.getTypedRuleContext(ZCodeParser.Var_def_for_paramContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_param)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.array_def_for_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.var_def_for_param()
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
        self.enterRule(localctx, 80, self.RULE_param_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 365
            self.param_def_list()
            self.state = 366
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


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


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
        self.enterRule(localctx, 82, self.RULE_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.KW_FUNC)
            self.state = 369
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 370
            self.param_def()
            self.state = 371
            self.optional_end_line()
            self.state = 372
            self.inner_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forward_func_defContext(ParserRuleContext):
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
            return ZCodeParser.RULE_forward_func_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForward_func_def" ):
                return visitor.visitForward_func_def(self)
            else:
                return visitor.visitChildren(self)




    def forward_func_def(self):

        localctx = ZCodeParser.Forward_func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_forward_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(ZCodeParser.KW_FUNC)
            self.state = 375
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 376
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
        self.enterRule(localctx, 86, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_TRUE) | (1 << ZCodeParser.KW_FALSE) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.SEP_OPEN_PAREN) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 378
                self.expression()
                self.state = 383
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
        self.enterRule(localctx, 88, self.RULE_expression)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.string_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.relation_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.logic_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.add_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.multi_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
                self.negate_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 390
                self.primary_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 391
                self.array_expr()
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
        self.enterRule(localctx, 90, self.RULE_string_expr)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.relation_expr()
                self.state = 395
                self.string_op()
                self.state = 396
                self.relation_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
        self.enterRule(localctx, 92, self.RULE_string_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
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
        self.enterRule(localctx, 94, self.RULE_relation_expr)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.logic_expr(0)
                self.state = 404
                self.relational_op()
                self.state = 405
                self.logic_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
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
        self.enterRule(localctx, 96, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    self.logic_op()
                    self.state = 417
                    self.add_expr(0) 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 100, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_add_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.multi_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 429
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 430
                    self.add_op()
                    self.state = 431
                    self.multi_expr(0) 
                self.state = 437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_multi_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.negate_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multi_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multi_expr)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 444
                    self.multi_op()
                    self.state = 445
                    self.negate_expr() 
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 108, self.RULE_multi_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
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


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_negate_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate_expr" ):
                return visitor.visitNegate_expr(self)
            else:
                return visitor.visitChildren(self)




    def negate_expr(self):

        localctx = ZCodeParser.Negate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_negate_expr)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.negate_op()
                self.state = 455
                self.negate_expr()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.sign_expr()
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
        self.enterRule(localctx, 112, self.RULE_negate_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(ZCodeParser.OP_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def OP_SUBTRACT(self):
            return self.getToken(ZCodeParser.OP_SUBTRACT, 0)

        def array_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_sign_expr)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(ZCodeParser.OP_SUBTRACT)
                self.state = 463
                self.sign_expr()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.array_expr()
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

        def array_element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_exprContext,0)


        def primary_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Primary_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expr" ):
                return visitor.visitArray_expr(self)
            else:
                return visitor.visitChildren(self)




    def array_expr(self):

        localctx = ZCodeParser.Array_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_array_expr)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.array_element_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.primary_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def indexer(self):
            return self.getTypedRuleContext(ZCodeParser.IndexerContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_expr" ):
                return visitor.visitArray_element_expr(self)
            else:
                return visitor.visitChildren(self)




    def array_element_expr(self):

        localctx = ZCodeParser.Array_element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_array_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.term()
            self.state = 472
            self.indexer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 120, self.RULE_indexer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 475
            self.index_op()
            self.state = 476
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


        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.expression()
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.state = 479
                self.match(ZCodeParser.SEP_COMA)
                self.state = 480
                self.index_op()
                pass
            elif token in [ZCodeParser.SEP_CLOSE_BRACK]:
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


        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_primary_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = ZCodeParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_primary_expression)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(ZCodeParser.SEP_OPEN_PAREN)
                self.state = 485
                self.expression()
                self.state = 486
                self.match(ZCodeParser.SEP_CLOSE_PAREN)
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
                self.literal()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 489
                self.term()
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
        self.enterRule(localctx, 126, self.RULE_term)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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


        def end_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.End_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.End_lineContext,i)


        def else_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Else_clauseContext,0)


        def elif_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_clauseContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_clauseContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.if_clause()
            self.state = 502
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 497
                    self.end_line()
                    self.state = 498
                    self.elif_clause() 
                self.state = 504
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 505
                self.end_line()
                self.state = 506
                self.else_clause()
                pass

            elif la_ == 2:
                pass


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


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_clause" ):
                return visitor.visitIf_clause(self)
            else:
                return visitor.visitChildren(self)




    def if_clause(self):

        localctx = ZCodeParser.If_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_if_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(ZCodeParser.KW_IF)
            self.state = 512
            self.if_condition()
            self.state = 513
            self.optional_end_line()
            self.state = 514
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


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_clause" ):
                return visitor.visitElif_clause(self)
            else:
                return visitor.visitChildren(self)




    def elif_clause(self):

        localctx = ZCodeParser.Elif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_elif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(ZCodeParser.KW_ELIF)
            self.state = 517
            self.if_condition()
            self.state = 518
            self.optional_end_line()
            self.state = 519
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

        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


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
        self.enterRule(localctx, 134, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(ZCodeParser.KW_ELSE)
            self.state = 522
            self.optional_end_line()
            self.state = 523
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
        self.enterRule(localctx, 136, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 526
            self.expression()
            self.state = 527
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


        def optional_end_line(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.for_clause()
            self.state = 530
            self.condition_clause()
            self.state = 531
            self.update_clause()
            self.state = 532
            self.optional_end_line()
            self.state = 533
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
        self.enterRule(localctx, 140, self.RULE_for_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(ZCodeParser.KW_FOR)
            self.state = 536
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
        self.enterRule(localctx, 142, self.RULE_condition_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 539
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
        self.enterRule(localctx, 144, self.RULE_update_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(ZCodeParser.KW_BY)
            self.state = 542
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
        self.enterRule(localctx, 146, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
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
        self.enterRule(localctx, 148, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
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
        self.enterRule(localctx, 150, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(ZCodeParser.KW_RETURN)
            self.state = 551
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 549
                self.expression()
                pass
            elif token in [ZCodeParser.NEW_LINE]:
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


    class Passing_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def passing_list(self):
            return self.getTypedRuleContext(ZCodeParser.Passing_listContext,0)


        def SEP_CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_passing_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassing_arg" ):
                return visitor.visitPassing_arg(self)
            else:
                return visitor.visitChildren(self)




    def passing_arg(self):

        localctx = ZCodeParser.Passing_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_passing_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 554
            self.passing_list()
            self.state = 555
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
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
        self.enterRule(localctx, 154, self.RULE_passing_list)
        try:
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.expression()
                self.state = 558
                self.passing_list_tail()
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
        self.enterRule(localctx, 156, self.RULE_passing_list_tail)
        try:
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.match(ZCodeParser.SEP_COMA)
                self.state = 564
                self.expression()
                self.state = 565
                self.passing_list_tail()
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
        self.enterRule(localctx, 158, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 571
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

        def optional_end_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Optional_end_lineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Optional_end_lineContext,i)


        def lines(self):
            return self.getTypedRuleContext(ZCodeParser.LinesContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 574
            self.optional_end_line()
            self.state = 575
            self.lines()
            self.state = 576
            self.optional_end_line()
            self.state = 577
            self.match(ZCodeParser.KW_END)
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

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

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
        self.enterRule(localctx, 162, self.RULE_literal)
        try:
            self.state = 582
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
                self.match(ZCodeParser.STRING)
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 581
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
        self.enterRule(localctx, 164, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
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


    class Optional_end_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_line(self):
            return self.getTypedRuleContext(ZCodeParser.End_lineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_end_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_end_line" ):
                return visitor.visitOptional_end_line(self)
            else:
                return visitor.visitChildren(self)




    def optional_end_line(self):

        localctx = ZCodeParser.Optional_end_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_optional_end_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 586
                self.end_line()
                pass

            elif la_ == 2:
                pass


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
        self.enterRule(localctx, 168, self.RULE_end_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 590
                    self.match(ZCodeParser.NEW_LINE)

                else:
                    raise NoViableAltException(self)
                self.state = 593 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self._predicates[49] = self.logic_expr_sempred
        self._predicates[51] = self.add_expr_sempred
        self._predicates[53] = self.multi_expr_sempred
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
         




