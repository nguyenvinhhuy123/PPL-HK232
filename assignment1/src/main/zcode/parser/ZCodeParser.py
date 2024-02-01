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
        buf.write("\u024d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("V\3\2\3\2\3\2\7\2\u00b0\n\2\f\2\16\2\u00b3\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\5\5\u00c4\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00cc\n\6\3")
        buf.write("\7\3\7\7\7\u00d0\n\7\f\7\16\7\u00d3\13\7\3\b\3\b\3\b\5")
        buf.write("\b\u00d8\n\b\3\t\3\t\5\t\u00dc\n\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\5\n\u00e3\n\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f4\n\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\5\20\u00fc\n\20\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\23\3\23\5\23\u0106\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0112\n\25\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u011e")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0133")
        buf.write("\n\36\3\37\3\37\5\37\u0137\n\37\3 \3 \3 \3!\3!\3!\5!\u013f")
        buf.write("\n!\3\"\3\"\5\"\u0143\n\"\3#\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0157\n\'\3(\3(\3(")
        buf.write("\3(\3(\5(\u015e\n(\3)\3)\5)\u0162\n)\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3,\3,\3,\3,\3-\7-\u0173\n-\f-\16-\u0176")
        buf.write("\13-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0180\n.\3/\3/\3/\3/\3")
        buf.write("/\5/\u0187\n/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u0190\n\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\7\63\u019b\n\63\f\63\16\63\u019e\13\63\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u01a9\n\65\f\65")
        buf.write("\16\65\u01ac\13\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u01b7\n\67\f\67\16\67\u01ba\13\67\38\3")
        buf.write("8\39\39\39\39\59\u01c2\n9\3:\3:\3;\3;\3;\5;\u01c9\n;\3")
        buf.write("<\3<\5<\u01cd\n<\3=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\5?\u01da")
        buf.write("\n?\3@\3@\3@\3@\3@\3@\5@\u01e2\n@\3A\3A\5A\u01e6\nA\3")
        buf.write("B\3B\3B\3B\7B\u01ec\nB\fB\16B\u01ef\13B\3B\3B\3B\3B\5")
        buf.write("B\u01f5\nB\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3E\3E\3E\3E\3")
        buf.write("F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3H\3H\3H\5H\u0212\nH\3I\3")
        buf.write("I\3I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3M\5M\u0221\nM\3N\3N\3")
        buf.write("N\3N\3O\3O\3O\3O\5O\u022b\nO\3P\3P\3P\3P\3P\5P\u0232\n")
        buf.write("P\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3S\3S\5S\u0240\nS\3T\3")
        buf.write("T\3U\3U\5U\u0246\nU\3V\6V\u0249\nV\rV\16V\u024a\3V\2\5")
        buf.write("dhlW\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6")
        buf.write("\u00a8\u00aa\2\t\3\2\6\b\3\2\n\13\4\2\37\37!&\3\2\35\36")
        buf.write("\3\2\27\30\3\2\31\33\3\2\4\5\2\u0232\2\u00ac\3\2\2\2\4")
        buf.write("\u00b6\3\2\2\2\6\u00bd\3\2\2\2\b\u00c3\3\2\2\2\n\u00cb")
        buf.write("\3\2\2\2\f\u00d1\3\2\2\2\16\u00d7\3\2\2\2\20\u00db\3\2")
        buf.write("\2\2\22\u00e2\3\2\2\2\24\u00e6\3\2\2\2\26\u00e9\3\2\2")
        buf.write("\2\30\u00f3\3\2\2\2\32\u00f5\3\2\2\2\34\u00f7\3\2\2\2")
        buf.write("\36\u00fb\3\2\2\2 \u00fd\3\2\2\2\"\u0100\3\2\2\2$\u0105")
        buf.write("\3\2\2\2&\u0107\3\2\2\2(\u0111\3\2\2\2*\u0113\3\2\2\2")
        buf.write(",\u0116\3\2\2\2.\u011d\3\2\2\2\60\u011f\3\2\2\2\62\u0123")
        buf.write("\3\2\2\2\64\u0125\3\2\2\2\66\u0128\3\2\2\28\u012b\3\2")
        buf.write("\2\2:\u012f\3\2\2\2<\u0136\3\2\2\2>\u0138\3\2\2\2@\u013e")
        buf.write("\3\2\2\2B\u0142\3\2\2\2D\u0144\3\2\2\2F\u0148\3\2\2\2")
        buf.write("H\u014b\3\2\2\2J\u014e\3\2\2\2L\u0156\3\2\2\2N\u015d\3")
        buf.write("\2\2\2P\u0161\3\2\2\2R\u0163\3\2\2\2T\u0167\3\2\2\2V\u016d")
        buf.write("\3\2\2\2X\u0174\3\2\2\2Z\u017f\3\2\2\2\\\u0186\3\2\2\2")
        buf.write("^\u0188\3\2\2\2`\u018f\3\2\2\2b\u0191\3\2\2\2d\u0193\3")
        buf.write("\2\2\2f\u019f\3\2\2\2h\u01a1\3\2\2\2j\u01ad\3\2\2\2l\u01af")
        buf.write("\3\2\2\2n\u01bb\3\2\2\2p\u01c1\3\2\2\2r\u01c3\3\2\2\2")
        buf.write("t\u01c8\3\2\2\2v\u01cc\3\2\2\2x\u01ce\3\2\2\2z\u01d1\3")
        buf.write("\2\2\2|\u01d5\3\2\2\2~\u01e1\3\2\2\2\u0080\u01e5\3\2\2")
        buf.write("\2\u0082\u01e7\3\2\2\2\u0084\u01f6\3\2\2\2\u0086\u01fb")
        buf.write("\3\2\2\2\u0088\u0200\3\2\2\2\u008a\u0204\3\2\2\2\u008c")
        buf.write("\u0208\3\2\2\2\u008e\u0211\3\2\2\2\u0090\u0213\3\2\2\2")
        buf.write("\u0092\u0216\3\2\2\2\u0094\u0219\3\2\2\2\u0096\u021b\3")
        buf.write("\2\2\2\u0098\u021d\3\2\2\2\u009a\u0222\3\2\2\2\u009c\u022a")
        buf.write("\3\2\2\2\u009e\u0231\3\2\2\2\u00a0\u0233\3\2\2\2\u00a2")
        buf.write("\u0236\3\2\2\2\u00a4\u023f\3\2\2\2\u00a6\u0241\3\2\2\2")
        buf.write("\u00a8\u0245\3\2\2\2\u00aa\u0248\3\2\2\2\u00ac\u00b1\5")
        buf.write("\u00a8U\2\u00ad\u00b0\5\6\4\2\u00ae\u00b0\5\b\5\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3")
        buf.write("\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\2\2\3\u00b5\3")
        buf.write("\3\2\2\2\u00b6\u00b7\7\f\2\2\u00b7\u00b8\7\3\2\2\u00b8")
        buf.write("\u00b9\7(\2\2\u00b9\u00ba\7)\2\2\u00ba\u00bb\5\u00a8U")
        buf.write("\2\u00bb\u00bc\5\n\6\2\u00bc\5\3\2\2\2\u00bd\u00be\5V")
        buf.write(",\2\u00be\u00bf\5\u00aaV\2\u00bf\7\3\2\2\2\u00c0\u00c4")
        buf.write("\5T+\2\u00c1\u00c4\5\20\t\2\u00c2\u00c4\5\4\3\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2")
        buf.write("\u00c4\t\3\2\2\2\u00c5\u00c6\5\u00a2R\2\u00c6\u00c7\5")
        buf.write("\u00aaV\2\u00c7\u00cc\3\2\2\2\u00c8\u00c9\5\u0098M\2\u00c9")
        buf.write("\u00ca\5\u00aaV\2\u00ca\u00cc\3\2\2\2\u00cb\u00c5\3\2")
        buf.write("\2\2\u00cb\u00c8\3\2\2\2\u00cc\13\3\2\2\2\u00cd\u00d0")
        buf.write("\5\16\b\2\u00ce\u00d0\5\26\f\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\r\3\2\2\2\u00d3\u00d1\3\2\2")
        buf.write("\2\u00d4\u00d8\5\20\t\2\u00d5\u00d8\5\22\n\2\u00d6\u00d8")
        buf.write("\5\24\13\2\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\17\3\2\2\2\u00d9\u00dc\5\36\20\2")
        buf.write("\u00da\u00dc\5\62\32\2\u00db\u00d9\3\2\2\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\5\u00aaV\2\u00de")
        buf.write("\21\3\2\2\2\u00df\u00e3\5*\26\2\u00e0\u00e3\5F$\2\u00e1")
        buf.write("\u00e3\5H%\2\u00e2\u00df\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\5\u00aa")
        buf.write("V\2\u00e5\23\3\2\2\2\u00e6\u00e7\5Z.\2\u00e7\u00e8\5\u00aa")
        buf.write("V\2\u00e8\25\3\2\2\2\u00e9\u00ea\5\30\r\2\u00ea\u00eb")
        buf.write("\5\u00aaV\2\u00eb\27\3\2\2\2\u00ec\u00f4\5\u0082B\2\u00ed")
        buf.write("\u00f4\5\u008cG\2\u00ee\u00f4\5\u0094K\2\u00ef\u00f4\5")
        buf.write("\u0096L\2\u00f0\u00f4\5\u0098M\2\u00f1\u00f4\5\u00a2R")
        buf.write("\2\u00f2\u00f4\5\u00a0Q\2\u00f3\u00ec\3\2\2\2\u00f3\u00ed")
        buf.write("\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f3")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2")
        buf.write("\u00f4\31\3\2\2\2\u00f5\u00f6\t\2\2\2\u00f6\33\3\2\2\2")
        buf.write("\u00f7\u00f8\t\3\2\2\u00f8\35\3\2\2\2\u00f9\u00fc\5&\24")
        buf.write("\2\u00fa\u00fc\5(\25\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa")
        buf.write("\3\2\2\2\u00fc\37\3\2\2\2\u00fd\u00fe\5\32\16\2\u00fe")
        buf.write("\u00ff\7\60\2\2\u00ff!\3\2\2\2\u0100\u0101\7 \2\2\u0101")
        buf.write("\u0102\5Z.\2\u0102#\3\2\2\2\u0103\u0106\5\"\22\2\u0104")
        buf.write("\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2")
        buf.write("\u0106%\3\2\2\2\u0107\u0108\5\32\16\2\u0108\u0109\7\60")
        buf.write("\2\2\u0109\u010a\5$\23\2\u010a\'\3\2\2\2\u010b\u010c\7")
        buf.write("\n\2\2\u010c\u010d\7\60\2\2\u010d\u0112\5\"\22\2\u010e")
        buf.write("\u010f\7\13\2\2\u010f\u0110\7\60\2\2\u0110\u0112\5$\23")
        buf.write("\2\u0111\u010b\3\2\2\2\u0111\u010e\3\2\2\2\u0112)\3\2")
        buf.write("\2\2\u0113\u0114\7\60\2\2\u0114\u0115\5\"\22\2\u0115+")
        buf.write("\3\2\2\2\u0116\u0117\7\61\2\2\u0117\u0118\5.\30\2\u0118")
        buf.write("-\3\2\2\2\u0119\u011a\7,\2\2\u011a\u011b\7\61\2\2\u011b")
        buf.write("\u011e\5.\30\2\u011c\u011e\3\2\2\2\u011d\u0119\3\2\2\2")
        buf.write("\u011d\u011c\3\2\2\2\u011e/\3\2\2\2\u011f\u0120\7*\2\2")
        buf.write("\u0120\u0121\5,\27\2\u0121\u0122\7+\2\2\u0122\61\3\2\2")
        buf.write("\2\u0123\u0124\58\35\2\u0124\63\3\2\2\2\u0125\u0126\5")
        buf.write("\32\16\2\u0126\u0127\5\66\34\2\u0127\65\3\2\2\2\u0128")
        buf.write("\u0129\7\60\2\2\u0129\u012a\5\60\31\2\u012a\67\3\2\2\2")
        buf.write("\u012b\u012c\5\32\16\2\u012c\u012d\5\66\34\2\u012d\u012e")
        buf.write("\5<\37\2\u012e9\3\2\2\2\u012f\u0132\7 \2\2\u0130\u0133")
        buf.write("\5Z.\2\u0131\u0133\5D#\2\u0132\u0130\3\2\2\2\u0132\u0131")
        buf.write("\3\2\2\2\u0133;\3\2\2\2\u0134\u0137\5:\36\2\u0135\u0137")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137")
        buf.write("=\3\2\2\2\u0138\u0139\5B\"\2\u0139\u013a\5@!\2\u013a?")
        buf.write("\3\2\2\2\u013b\u013c\7,\2\2\u013c\u013f\5> \2\u013d\u013f")
        buf.write("\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("A\3\2\2\2\u0140\u0143\5D#\2\u0141\u0143\5Z.\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0141\3\2\2\2\u0143C\3\2\2\2\u0144\u0145")
        buf.write("\7*\2\2\u0145\u0146\5> \2\u0146\u0147\7+\2\2\u0147E\3")
        buf.write("\2\2\2\u0148\u0149\7\60\2\2\u0149\u014a\5:\36\2\u014a")
        buf.write("G\3\2\2\2\u014b\u014c\5x=\2\u014c\u014d\5J&\2\u014dI\3")
        buf.write("\2\2\2\u014e\u014f\7 \2\2\u014f\u0150\5Z.\2\u0150K\3\2")
        buf.write("\2\2\u0151\u0152\5P)\2\u0152\u0153\5\u00a8U\2\u0153\u0154")
        buf.write("\5N(\2\u0154\u0157\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0151")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157M\3\2\2\2\u0158\u0159")
        buf.write("\7,\2\2\u0159\u015a\5P)\2\u015a\u015b\5N(\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u0158\3\2\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015eO\3\2\2\2\u015f\u0162\5\64\33\2\u0160")
        buf.write("\u0162\5 \21\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2")
        buf.write("\u0162Q\3\2\2\2\u0163\u0164\7(\2\2\u0164\u0165\5L\'\2")
        buf.write("\u0165\u0166\7)\2\2\u0166S\3\2\2\2\u0167\u0168\7\f\2\2")
        buf.write("\u0168\u0169\7\60\2\2\u0169\u016a\5R*\2\u016a\u016b\5")
        buf.write("\u00a8U\2\u016b\u016c\5\n\6\2\u016cU\3\2\2\2\u016d\u016e")
        buf.write("\7\f\2\2\u016e\u016f\7\60\2\2\u016f\u0170\5R*\2\u0170")
        buf.write("W\3\2\2\2\u0171\u0173\5Z.\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175Y\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0180\5\\/\2")
        buf.write("\u0178\u0180\5`\61\2\u0179\u0180\5d\63\2\u017a\u0180\5")
        buf.write("h\65\2\u017b\u0180\5l\67\2\u017c\u0180\5p9\2\u017d\u0180")
        buf.write("\5~@\2\u017e\u0180\5v<\2\u017f\u0177\3\2\2\2\u017f\u0178")
        buf.write("\3\2\2\2\u017f\u0179\3\2\2\2\u017f\u017a\3\2\2\2\u017f")
        buf.write("\u017b\3\2\2\2\u017f\u017c\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u017e\3\2\2\2\u0180[\3\2\2\2\u0181\u0182\5`\61")
        buf.write("\2\u0182\u0183\5^\60\2\u0183\u0184\5`\61\2\u0184\u0187")
        buf.write("\3\2\2\2\u0185\u0187\5`\61\2\u0186\u0181\3\2\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187]\3\2\2\2\u0188\u0189\7\'\2\2\u0189")
        buf.write("_\3\2\2\2\u018a\u018b\5d\63\2\u018b\u018c\5b\62\2\u018c")
        buf.write("\u018d\5d\63\2\u018d\u0190\3\2\2\2\u018e\u0190\5d\63\2")
        buf.write("\u018f\u018a\3\2\2\2\u018f\u018e\3\2\2\2\u0190a\3\2\2")
        buf.write("\2\u0191\u0192\t\4\2\2\u0192c\3\2\2\2\u0193\u0194\b\63")
        buf.write("\1\2\u0194\u0195\5h\65\2\u0195\u019c\3\2\2\2\u0196\u0197")
        buf.write("\f\4\2\2\u0197\u0198\5f\64\2\u0198\u0199\5h\65\2\u0199")
        buf.write("\u019b\3\2\2\2\u019a\u0196\3\2\2\2\u019b\u019e\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019de\3\2\2")
        buf.write("\2\u019e\u019c\3\2\2\2\u019f\u01a0\t\5\2\2\u01a0g\3\2")
        buf.write("\2\2\u01a1\u01a2\b\65\1\2\u01a2\u01a3\5l\67\2\u01a3\u01aa")
        buf.write("\3\2\2\2\u01a4\u01a5\f\4\2\2\u01a5\u01a6\5j\66\2\u01a6")
        buf.write("\u01a7\5l\67\2\u01a7\u01a9\3\2\2\2\u01a8\u01a4\3\2\2\2")
        buf.write("\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3")
        buf.write("\2\2\2\u01abi\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae")
        buf.write("\t\6\2\2\u01aek\3\2\2\2\u01af\u01b0\b\67\1\2\u01b0\u01b1")
        buf.write("\5p9\2\u01b1\u01b8\3\2\2\2\u01b2\u01b3\f\4\2\2\u01b3\u01b4")
        buf.write("\5n8\2\u01b4\u01b5\5p9\2\u01b5\u01b7\3\2\2\2\u01b6\u01b2")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9m\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bc\t\7\2\2\u01bco\3\2\2\2\u01bd\u01be\5r:\2\u01be")
        buf.write("\u01bf\5p9\2\u01bf\u01c2\3\2\2\2\u01c0\u01c2\5t;\2\u01c1")
        buf.write("\u01bd\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2q\3\2\2\2\u01c3")
        buf.write("\u01c4\7\34\2\2\u01c4s\3\2\2\2\u01c5\u01c6\7\30\2\2\u01c6")
        buf.write("\u01c9\5t;\2\u01c7\u01c9\5v<\2\u01c8\u01c5\3\2\2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9u\3\2\2\2\u01ca\u01cd\5x=\2\u01cb")
        buf.write("\u01cd\5~@\2\u01cc\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("w\3\2\2\2\u01ce\u01cf\5\u0080A\2\u01cf\u01d0\5z>\2\u01d0")
        buf.write("y\3\2\2\2\u01d1\u01d2\7*\2\2\u01d2\u01d3\5|?\2\u01d3\u01d4")
        buf.write("\7+\2\2\u01d4{\3\2\2\2\u01d5\u01d9\5Z.\2\u01d6\u01d7\7")
        buf.write(",\2\2\u01d7\u01da\5|?\2\u01d8\u01da\3\2\2\2\u01d9\u01d6")
        buf.write("\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da}\3\2\2\2\u01db\u01dc")
        buf.write("\7(\2\2\u01dc\u01dd\5Z.\2\u01dd\u01de\7)\2\2\u01de\u01e2")
        buf.write("\3\2\2\2\u01df\u01e2\5\u00a4S\2\u01e0\u01e2\5\u0080A\2")
        buf.write("\u01e1\u01db\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e0\3")
        buf.write("\2\2\2\u01e2\177\3\2\2\2\u01e3\u01e6\7\60\2\2\u01e4\u01e6")
        buf.write("\5\u00a0Q\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6")
        buf.write("\u0081\3\2\2\2\u01e7\u01ed\5\u0084C\2\u01e8\u01e9\5\u00aa")
        buf.write("V\2\u01e9\u01ea\5\u0086D\2\u01ea\u01ec\3\2\2\2\u01eb\u01e8")
        buf.write("\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01f4\3\2\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01f0\u01f1\5\u00aaV\2\u01f1\u01f2\5\u0088E\2\u01f2\u01f5")
        buf.write("\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5\u0083\3\2\2\2\u01f6\u01f7\7\22\2")
        buf.write("\2\u01f7\u01f8\5\u008aF\2\u01f8\u01f9\5\u00a8U\2\u01f9")
        buf.write("\u01fa\5\30\r\2\u01fa\u0085\3\2\2\2\u01fb\u01fc\7\24\2")
        buf.write("\2\u01fc\u01fd\5\u008aF\2\u01fd\u01fe\5\u00a8U\2\u01fe")
        buf.write("\u01ff\5\30\r\2\u01ff\u0087\3\2\2\2\u0200\u0201\7\23\2")
        buf.write("\2\u0201\u0202\5\u00a8U\2\u0202\u0203\5\30\r\2\u0203\u0089")
        buf.write("\3\2\2\2\u0204\u0205\7(\2\2\u0205\u0206\5Z.\2\u0206\u0207")
        buf.write("\7)\2\2\u0207\u008b\3\2\2\2\u0208\u0209\5\u008eH\2\u0209")
        buf.write("\u020a\5\u0090I\2\u020a\u020b\5\u0092J\2\u020b\u020c\5")
        buf.write("\u00a8U\2\u020c\u020d\5\30\r\2\u020d\u008d\3\2\2\2\u020e")
        buf.write("\u020f\7\r\2\2\u020f\u0212\7\60\2\2\u0210\u0212\5\66\34")
        buf.write("\2\u0211\u020e\3\2\2\2\u0211\u0210\3\2\2\2\u0212\u008f")
        buf.write("\3\2\2\2\u0213\u0214\7\16\2\2\u0214\u0215\5Z.\2\u0215")
        buf.write("\u0091\3\2\2\2\u0216\u0217\7\17\2\2\u0217\u0218\5Z.\2")
        buf.write("\u0218\u0093\3\2\2\2\u0219\u021a\7\20\2\2\u021a\u0095")
        buf.write("\3\2\2\2\u021b\u021c\7\21\2\2\u021c\u0097\3\2\2\2\u021d")
        buf.write("\u0220\7\t\2\2\u021e\u0221\5Z.\2\u021f\u0221\3\2\2\2\u0220")
        buf.write("\u021e\3\2\2\2\u0220\u021f\3\2\2\2\u0221\u0099\3\2\2\2")
        buf.write("\u0222\u0223\7(\2\2\u0223\u0224\5\u009cO\2\u0224\u0225")
        buf.write("\7)\2\2\u0225\u009b\3\2\2\2\u0226\u0227\5Z.\2\u0227\u0228")
        buf.write("\5\u009eP\2\u0228\u022b\3\2\2\2\u0229\u022b\3\2\2\2\u022a")
        buf.write("\u0226\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u009d\3\2\2\2")
        buf.write("\u022c\u022d\7,\2\2\u022d\u022e\5Z.\2\u022e\u022f\5\u009e")
        buf.write("P\2\u022f\u0232\3\2\2\2\u0230\u0232\3\2\2\2\u0231\u022c")
        buf.write("\3\2\2\2\u0231\u0230\3\2\2\2\u0232\u009f\3\2\2\2\u0233")
        buf.write("\u0234\7\60\2\2\u0234\u0235\5\u009aN\2\u0235\u00a1\3\2")
        buf.write("\2\2\u0236\u0237\7\25\2\2\u0237\u0238\5\u00a8U\2\u0238")
        buf.write("\u0239\5\f\7\2\u0239\u023a\5\u00a8U\2\u023a\u023b\7\26")
        buf.write("\2\2\u023b\u00a3\3\2\2\2\u023c\u0240\7\61\2\2\u023d\u0240")
        buf.write("\7\62\2\2\u023e\u0240\5\u00a6T\2\u023f\u023c\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u023f\u023e\3\2\2\2\u0240\u00a5\3\2\2\2")
        buf.write("\u0241\u0242\t\b\2\2\u0242\u00a7\3\2\2\2\u0243\u0246\5")
        buf.write("\u00aaV\2\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2\u0245")
        buf.write("\u0244\3\2\2\2\u0246\u00a9\3\2\2\2\u0247\u0249\7/\2\2")
        buf.write("\u0248\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0248\3")
        buf.write("\2\2\2\u024a\u024b\3\2\2\2\u024b\u00ab\3\2\2\2-\u00af")
        buf.write("\u00b1\u00c3\u00cb\u00cf\u00d1\u00d7\u00db\u00e2\u00f3")
        buf.write("\u00fb\u0105\u0111\u011d\u0132\u0136\u013e\u0142\u0156")
        buf.write("\u015d\u0161\u0174\u017f\u0186\u018f\u019c\u01aa\u01b8")
        buf.write("\u01c1\u01c8\u01cc\u01d9\u01e1\u01e5\u01ed\u01f4\u0211")
        buf.write("\u0220\u022a\u0231\u023f\u0245\u024a")
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
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FUNC))) != 0):
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 171
                    self.forward_func()
                    pass

                elif la_ == 2:
                    self.state = 172
                    self.define()
                    pass


                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
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
            self.state = 180
            self.match(ZCodeParser.KW_FUNC)
            self.state = 181
            self.match(ZCodeParser.MAIN_TOKEN)
            self.state = 182
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 183
            self.match(ZCodeParser.SEP_CLOSE_PAREN)
            self.state = 184
            self.optional_end_line()
            self.state = 185
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
            self.state = 187
            self.forward_func_def()
            self.state = 188
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


        def main_def(self):
            return self.getTypedRuleContext(ZCodeParser.Main_defContext,0)


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
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.func_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.def_line()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.main_def()
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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.block_statement()
                self.state = 196
                self.end_line()
                pass
            elif token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.return_statement()
                self.state = 199
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
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_TRUE) | (1 << ZCodeParser.KW_FALSE) | (1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_RETURN) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FOR) | (1 << ZCodeParser.KW_BREAK) | (1 << ZCodeParser.KW_CONTINUE) | (1 << ZCodeParser.KW_IF) | (1 << ZCodeParser.KW_BEGIN) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.SEP_OPEN_PAREN) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 204
                    self.statement_line()
                    pass


                self.state = 209
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
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.def_line()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.assign_line()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
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
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 215
                self.var_def()
                pass

            elif la_ == 2:
                self.state = 216
                self.array_def()
                pass


            self.state = 219
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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 221
                self.var_assign()
                pass

            elif la_ == 2:
                self.state = 222
                self.array_assign()
                pass

            elif la_ == 3:
                self.state = 223
                self.array_elem_assign()
                pass


            self.state = 226
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
            self.state = 228
            self.expression()
            self.state = 229
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
            self.state = 231
            self.statement()
            self.state = 232
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
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 234
                self.if_statement()
                pass

            elif la_ == 2:
                self.state = 235
                self.for_statement()
                pass

            elif la_ == 3:
                self.state = 236
                self.break_statement()
                pass

            elif la_ == 4:
                self.state = 237
                self.continue_statement()
                pass

            elif la_ == 5:
                self.state = 238
                self.return_statement()
                pass

            elif la_ == 6:
                self.state = 239
                self.block_statement()
                pass

            elif la_ == 7:
                self.state = 240
                self.func_call()
                pass


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
            self.state = 243
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
            self.state = 245
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
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.static_var_def()
                pass
            elif token in [ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
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
            self.state = 251
            self.type_def()
            self.state = 252
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
            self.state = 254
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 255
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
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
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
            self.state = 261
            self.type_def()
            self.state = 262
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 263
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
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.KW_VAR)
                self.state = 266
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 267
                self.value_init()
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 269
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 270
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
            self.state = 273
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 274
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
            self.state = 276
            self.match(ZCodeParser.NUMBER)
            self.state = 277
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
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(ZCodeParser.SEP_COMA)
                self.state = 280
                self.match(ZCodeParser.NUMBER)
                self.state = 281
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
            self.state = 285
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 286
            self.dim_list()
            self.state = 287
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
            self.state = 289
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
            self.state = 291
            self.type_def()
            self.state = 292
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
            self.state = 294
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 295
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
            self.state = 297
            self.type_def()
            self.state = 298
            self.array_identifier()
            self.state = 299
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
            self.state = 301
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 302
                self.expression()
                pass
            elif token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 303
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
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
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
            self.state = 310
            self.array_value()
            self.state = 311
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
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(ZCodeParser.SEP_COMA)
                self.state = 314
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
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 318
                self.array_value_init()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 319
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
            self.state = 322
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 323
            self.array_value_init_list()
            self.state = 324
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
            self.state = 326
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 327
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
            self.state = 329
            self.array_element_expr()
            self.state = 330
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
            self.state = 332
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 333
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
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.param()
                self.state = 336
                self.optional_end_line()
                self.state = 337
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
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(ZCodeParser.SEP_COMA)
                self.state = 343
                self.param()
                self.state = 344
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
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.array_def_for_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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
            self.state = 353
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 354
            self.param_def_list()
            self.state = 355
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
            self.state = 357
            self.match(ZCodeParser.KW_FUNC)
            self.state = 358
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 359
            self.param_def()
            self.state = 360
            self.optional_end_line()
            self.state = 361
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
            self.state = 363
            self.match(ZCodeParser.KW_FUNC)
            self.state = 364
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 365
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
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_TRUE) | (1 << ZCodeParser.KW_FALSE) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.SEP_OPEN_PAREN) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 367
                self.expression()
                self.state = 372
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
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.string_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.relation_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.logic_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
                self.add_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 377
                self.multi_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 378
                self.negate_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 379
                self.primary_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 380
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
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.relation_expr()
                self.state = 384
                self.string_op()
                self.state = 385
                self.relation_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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
            self.state = 390
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
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.logic_expr(0)
                self.state = 393
                self.relational_op()
                self.state = 394
                self.logic_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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
            self.state = 399
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
            self.state = 402
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 404
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 405
                    self.logic_op()
                    self.state = 406
                    self.add_expr(0) 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 413
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
            self.state = 416
            self.multi_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    self.add_op()
                    self.state = 420
                    self.multi_expr(0) 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 427
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
            self.state = 430
            self.negate_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multi_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multi_expr)
                    self.state = 432
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 433
                    self.multi_op()
                    self.state = 434
                    self.negate_expr() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
            self.state = 441
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
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.negate_op()
                self.state = 444
                self.negate_expr()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
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
            self.state = 449
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
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.match(ZCodeParser.OP_SUBTRACT)
                self.state = 452
                self.sign_expr()
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
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
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.array_element_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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
            self.state = 460
            self.term()
            self.state = 461
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
            self.state = 463
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 464
            self.index_op()
            self.state = 465
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
            self.state = 467
            self.expression()
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.state = 468
                self.match(ZCodeParser.SEP_COMA)
                self.state = 469
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
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(ZCodeParser.SEP_OPEN_PAREN)
                self.state = 474
                self.expression()
                self.state = 475
                self.match(ZCodeParser.SEP_CLOSE_PAREN)
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.literal()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 478
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
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
            self.state = 485
            self.if_clause()
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 486
                    self.end_line()
                    self.state = 487
                    self.elif_clause() 
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 494
                self.end_line()
                self.state = 495
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
            self.state = 500
            self.match(ZCodeParser.KW_IF)
            self.state = 501
            self.if_condition()
            self.state = 502
            self.optional_end_line()
            self.state = 503
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
            self.state = 505
            self.match(ZCodeParser.KW_ELIF)
            self.state = 506
            self.if_condition()
            self.state = 507
            self.optional_end_line()
            self.state = 508
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
            self.state = 510
            self.match(ZCodeParser.KW_ELSE)
            self.state = 511
            self.optional_end_line()
            self.state = 512
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
            self.state = 514
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 515
            self.expression()
            self.state = 516
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
            self.state = 518
            self.for_clause()
            self.state = 519
            self.condition_clause()
            self.state = 520
            self.update_clause()
            self.state = 521
            self.optional_end_line()
            self.state = 522
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

        def array_identifier(self):
            return self.getTypedRuleContext(ZCodeParser.Array_identifierContext,0)


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
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(ZCodeParser.KW_FOR)
                self.state = 525
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.array_identifier()
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
            self.state = 529
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 530
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
            self.state = 532
            self.match(ZCodeParser.KW_BY)
            self.state = 533
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
            self.state = 535
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
            self.state = 537
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
            self.state = 539
            self.match(ZCodeParser.KW_RETURN)
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 540
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
            self.state = 544
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 545
            self.passing_list()
            self.state = 546
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
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE, ZCodeParser.OP_SUBTRACT, ZCodeParser.OP_NOT, ZCodeParser.SEP_OPEN_PAREN, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.expression()
                self.state = 549
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
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.match(ZCodeParser.SEP_COMA)
                self.state = 555
                self.expression()
                self.state = 556
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
            self.state = 561
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 562
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
            self.state = 564
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 565
            self.optional_end_line()
            self.state = 566
            self.lines()
            self.state = 567
            self.optional_end_line()
            self.state = 568
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
            self.state = 573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 571
                self.match(ZCodeParser.STRING)
                pass
            elif token in [ZCodeParser.KW_TRUE, ZCodeParser.KW_FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 572
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
            self.state = 575
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
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 577
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
            self.state = 582 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 581
                    self.match(ZCodeParser.NEW_LINE)

                else:
                    raise NoViableAltException(self)
                self.state = 584 
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
         




