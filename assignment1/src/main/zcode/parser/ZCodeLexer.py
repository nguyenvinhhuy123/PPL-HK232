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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u01b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\3\6\3\u0085")
        buf.write("\n\3\r\3\16\3\u0086\3\3\7\3\u008a\n\3\f\3\16\3\u008d\13")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u0095\n\6\3\7\3\7\7\7\u0099")
        buf.write("\n\7\f\7\16\7\u009c\13\7\3\b\3\b\5\b\u00a0\n\b\3\b\3\b")
        buf.write("\7\b\u00a4\n\b\f\b\16\b\u00a7\13\b\3\t\3\t\7\t\u00ab\n")
        buf.write("\t\f\t\16\t\u00ae\13\t\3\t\7\t\u00b1\n\t\f\t\16\t\u00b4")
        buf.write("\13\t\3\t\7\t\u00b7\n\t\f\t\16\t\u00ba\13\t\3\t\5\t\u00bd")
        buf.write("\n\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\5\16\u00ce\n\16\3\17\3\17\7\17\u00d2")
        buf.write("\n\17\f\17\16\17\u00d5\13\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write("9\3:\3:\7:\u0180\n:\f:\16:\u0183\13:\3:\3:\3;\6;\u0188")
        buf.write("\n;\r;\16;\u0189\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\7?\u0197")
        buf.write("\n?\f?\16?\u019a\13?\3?\3?\3?\3@\3@\7@\u01a1\n@\f@\16")
        buf.write("@\u01a4\13@\3@\3@\7@\u01a8\n@\f@\16@\u01ab\13@\3@\5@\u01ae")
        buf.write("\n@\3@\3@\2\2A\3\2\5\3\7\2\t\2\13\2\r\2\17\2\21\4\23\2")
        buf.write("\25\2\27\2\31\2\33\2\35\5\37\6!\7#\b%\t\'\n)\13+\f-\r")
        buf.write("/\16\61\17\63\20\65\21\67\229\23;\24=\25?\26A\27C\30E")
        buf.write("\31G\32I\33K\34M\35O\36Q\37S U!W\"Y#[$]%_&a\'c(e)g*i+")
        buf.write("k,m-o.q\2s/u\60w\61y\2{\62}\63\177\64\3\2\r\5\2C\\aac")
        buf.write("|\5\2\62;C\\c|\3\2\63;\4\2GGgg\4\2--//\7\2\n\f\16\17$")
        buf.write("$))^^\3\2^^\3\2$$\3\2))\5\2\n\13\16\17\"\"\3\2\f\f\2\u01b6")
        buf.write("\2\5\3\2\2\2\2\21\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5")
        buf.write("\u0084\3\2\2\2\7\u008e\3\2\2\2\t\u0090\3\2\2\2\13\u0094")
        buf.write("\3\2\2\2\r\u0096\3\2\2\2\17\u009d\3\2\2\2\21\u00bc\3\2")
        buf.write("\2\2\23\u00be\3\2\2\2\25\u00c0\3\2\2\2\27\u00c3\3\2\2")
        buf.write("\2\31\u00c7\3\2\2\2\33\u00cd\3\2\2\2\35\u00cf\3\2\2\2")
        buf.write("\37\u00d9\3\2\2\2!\u00de\3\2\2\2#\u00e4\3\2\2\2%\u00eb")
        buf.write("\3\2\2\2\'\u00f0\3\2\2\2)\u00f7\3\2\2\2+\u00fe\3\2\2\2")
        buf.write("-\u0102\3\2\2\2/\u010a\3\2\2\2\61\u010f\3\2\2\2\63\u0113")
        buf.write("\3\2\2\2\65\u0119\3\2\2\2\67\u011c\3\2\2\29\u0122\3\2")
        buf.write("\2\2;\u012b\3\2\2\2=\u012e\3\2\2\2?\u0133\3\2\2\2A\u0138")
        buf.write("\3\2\2\2C\u013e\3\2\2\2E\u0142\3\2\2\2G\u0144\3\2\2\2")
        buf.write("I\u0146\3\2\2\2K\u0148\3\2\2\2M\u014a\3\2\2\2O\u014c\3")
        buf.write("\2\2\2Q\u0150\3\2\2\2S\u0154\3\2\2\2U\u0157\3\2\2\2W\u0159")
        buf.write("\3\2\2\2Y\u015c\3\2\2\2[\u015f\3\2\2\2]\u0161\3\2\2\2")
        buf.write("_\u0163\3\2\2\2a\u0166\3\2\2\2c\u0169\3\2\2\2e\u016c\3")
        buf.write("\2\2\2g\u0170\3\2\2\2i\u0172\3\2\2\2k\u0174\3\2\2\2m\u0176")
        buf.write("\3\2\2\2o\u0178\3\2\2\2q\u017a\3\2\2\2s\u017d\3\2\2\2")
        buf.write("u\u0187\3\2\2\2w\u018d\3\2\2\2y\u018f\3\2\2\2{\u0191\3")
        buf.write("\2\2\2}\u0194\3\2\2\2\177\u019e\3\2\2\2\u0081\u0082\t")
        buf.write("\2\2\2\u0082\4\3\2\2\2\u0083\u0085\5\3\2\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u008b\3\2\2\2\u0088\u008a\t\3\2\2")
        buf.write("\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3")
        buf.write("\2\2\2\u008b\u008c\3\2\2\2\u008c\6\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008e\u008f\7\62\2\2\u008f\b\3\2\2\2\u0090\u0091")
        buf.write("\t\4\2\2\u0091\n\3\2\2\2\u0092\u0095\5\7\4\2\u0093\u0095")
        buf.write("\5\t\5\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\f\3\2\2\2\u0096\u009a\7\60\2\2\u0097\u0099\5\13\6\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\16\3\2\2\2\u009c\u009a\3\2")
        buf.write("\2\2\u009d\u009f\t\5\2\2\u009e\u00a0\t\6\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u00a5\5\t\5\2\u00a2\u00a4\5\13\6\2\u00a3\u00a2\3\2\2")
        buf.write("\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a6\20\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00ac")
        buf.write("\5\t\5\2\u00a9\u00ab\5\13\6\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00b2\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\5")
        buf.write("\r\7\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b8\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b5\u00b7\5\17\b\2\u00b6\u00b5\3\2\2")
        buf.write("\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00bd\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00bd\5\7\4\2\u00bc\u00a8\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\22\3\2\2\2\u00be\u00bf\n\7\2\2\u00bf\24\3\2\2\2")
        buf.write("\u00c0\u00c1\13\2\2\2\u00c1\u00c2\t\b\2\2\u00c2\26\3\2")
        buf.write("\2\2\u00c3\u00c4\13\2\2\2\u00c4\u00c5\5\25\13\2\u00c5")
        buf.write("\u00c6\n\t\2\2\u00c6\30\3\2\2\2\u00c7\u00c8\t\n\2\2\u00c8")
        buf.write("\u00c9\t\t\2\2\u00c9\32\3\2\2\2\u00ca\u00ce\5\27\f\2\u00cb")
        buf.write("\u00ce\5\31\r\2\u00cc\u00ce\5\23\n\2\u00cd\u00ca\3\2\2")
        buf.write("\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\34\3")
        buf.write("\2\2\2\u00cf\u00d3\t\t\2\2\u00d0\u00d2\5\33\16\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3")
        buf.write("\2\2\2\u00d6\u00d7\t\t\2\2\u00d7\u00d8\b\17\2\2\u00d8")
        buf.write("\36\3\2\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7t\2\2\u00db")
        buf.write("\u00dc\7w\2\2\u00dc\u00dd\7g\2\2\u00dd \3\2\2\2\u00de")
        buf.write("\u00df\7h\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7n\2\2\u00e1")
        buf.write("\u00e2\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\"\3\2\2\2\u00e4")
        buf.write("\u00e5\7p\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7o\2\2\u00e7")
        buf.write("\u00e8\7d\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7t\2\2\u00ea")
        buf.write("$\3\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed\7q\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7n\2\2\u00ef&\3\2\2\2\u00f0")
        buf.write("\u00f1\7u\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7i\2\2\u00f6")
        buf.write("(\3\2\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\u00fa\7v\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7t\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd*\3\2\2\2\u00fe\u00ff\7x\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7t\2\2\u0101,\3\2\2\2\u0102")
        buf.write("\u0103\7f\2\2\u0103\u0104\7{\2\2\u0104\u0105\7p\2\2\u0105")
        buf.write("\u0106\7c\2\2\u0106\u0107\7o\2\2\u0107\u0108\7k\2\2\u0108")
        buf.write("\u0109\7e\2\2\u0109.\3\2\2\2\u010a\u010b\7h\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7p\2\2\u010d\u010e\7e\2\2\u010e")
        buf.write("\60\3\2\2\2\u010f\u0110\7h\2\2\u0110\u0111\7q\2\2\u0111")
        buf.write("\u0112\7t\2\2\u0112\62\3\2\2\2\u0113\u0114\7w\2\2\u0114")
        buf.write("\u0115\7p\2\2\u0115\u0116\7v\2\2\u0116\u0117\7k\2\2\u0117")
        buf.write("\u0118\7n\2\2\u0118\64\3\2\2\2\u0119\u011a\7d\2\2\u011a")
        buf.write("\u011b\7{\2\2\u011b\66\3\2\2\2\u011c\u011d\7d\2\2\u011d")
        buf.write("\u011e\7t\2\2\u011e\u011f\7g\2\2\u011f\u0120\7c\2\2\u0120")
        buf.write("\u0121\7m\2\2\u01218\3\2\2\2\u0122\u0123\7e\2\2\u0123")
        buf.write("\u0124\7q\2\2\u0124\u0125\7p\2\2\u0125\u0126\7v\2\2\u0126")
        buf.write("\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129\7w\2\2\u0129")
        buf.write("\u012a\7g\2\2\u012a:\3\2\2\2\u012b\u012c\7k\2\2\u012c")
        buf.write("\u012d\7h\2\2\u012d<\3\2\2\2\u012e\u012f\7g\2\2\u012f")
        buf.write("\u0130\7n\2\2\u0130\u0131\7u\2\2\u0131\u0132\7g\2\2\u0132")
        buf.write(">\3\2\2\2\u0133\u0134\7g\2\2\u0134\u0135\7n\2\2\u0135")
        buf.write("\u0136\7k\2\2\u0136\u0137\7h\2\2\u0137@\3\2\2\2\u0138")
        buf.write("\u0139\7d\2\2\u0139\u013a\7g\2\2\u013a\u013b\7i\2\2\u013b")
        buf.write("\u013c\7k\2\2\u013c\u013d\7p\2\2\u013dB\3\2\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141\7f\2\2\u0141")
        buf.write("D\3\2\2\2\u0142\u0143\7-\2\2\u0143F\3\2\2\2\u0144\u0145")
        buf.write("\7/\2\2\u0145H\3\2\2\2\u0146\u0147\7,\2\2\u0147J\3\2\2")
        buf.write("\2\u0148\u0149\7\61\2\2\u0149L\3\2\2\2\u014a\u014b\7\'")
        buf.write("\2\2\u014bN\3\2\2\2\u014c\u014d\7p\2\2\u014d\u014e\7q")
        buf.write("\2\2\u014e\u014f\7v\2\2\u014fP\3\2\2\2\u0150\u0151\7c")
        buf.write("\2\2\u0151\u0152\7p\2\2\u0152\u0153\7f\2\2\u0153R\3\2")
        buf.write("\2\2\u0154\u0155\7q\2\2\u0155\u0156\7t\2\2\u0156T\3\2")
        buf.write("\2\2\u0157\u0158\7?\2\2\u0158V\3\2\2\2\u0159\u015a\7>")
        buf.write("\2\2\u015a\u015b\7/\2\2\u015bX\3\2\2\2\u015c\u015d\7#")
        buf.write("\2\2\u015d\u015e\7?\2\2\u015eZ\3\2\2\2\u015f\u0160\7>")
        buf.write("\2\2\u0160\\\3\2\2\2\u0161\u0162\7@\2\2\u0162^\3\2\2\2")
        buf.write("\u0163\u0164\7>\2\2\u0164\u0165\7?\2\2\u0165`\3\2\2\2")
        buf.write("\u0166\u0167\7@\2\2\u0167\u0168\7?\2\2\u0168b\3\2\2\2")
        buf.write("\u0169\u016a\7?\2\2\u016a\u016b\7?\2\2\u016bd\3\2\2\2")
        buf.write("\u016c\u016d\7\60\2\2\u016d\u016e\7\60\2\2\u016e\u016f")
        buf.write("\7\60\2\2\u016ff\3\2\2\2\u0170\u0171\7*\2\2\u0171h\3\2")
        buf.write("\2\2\u0172\u0173\7+\2\2\u0173j\3\2\2\2\u0174\u0175\7]")
        buf.write("\2\2\u0175l\3\2\2\2\u0176\u0177\7_\2\2\u0177n\3\2\2\2")
        buf.write("\u0178\u0179\7.\2\2\u0179p\3\2\2\2\u017a\u017b\7%\2\2")
        buf.write("\u017b\u017c\7%\2\2\u017cr\3\2\2\2\u017d\u0181\5q9\2\u017e")
        buf.write("\u0180\5y=\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0184\u0185\b:\3\2\u0185t\3\2\2\2")
        buf.write("\u0186\u0188\t\13\2\2\u0187\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018c\b;\3\2\u018cv\3\2\2\2\u018d")
        buf.write("\u018e\7\f\2\2\u018ex\3\2\2\2\u018f\u0190\n\f\2\2\u0190")
        buf.write("z\3\2\2\2\u0191\u0192\13\2\2\2\u0192\u0193\b>\4\2\u0193")
        buf.write("|\3\2\2\2\u0194\u0198\t\t\2\2\u0195\u0197\5\33\16\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019b\u019c\7\2\2\3\u019c\u019d\b?\5\2\u019d~\3")
        buf.write("\2\2\2\u019e\u01a2\t\t\2\2\u019f\u01a1\5\33\16\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u01a2\3")
        buf.write("\2\2\2\u01a5\u01a9\5\25\13\2\u01a6\u01a8\5\33\16\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3")
        buf.write("\2\2\2\u01ac\u01ae\t\t\2\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\b@\6\2\u01b0")
        buf.write("\u0080\3\2\2\2\25\2\u0086\u008b\u0094\u009a\u009f\u00a5")
        buf.write("\u00ac\u00b2\u00b8\u00bc\u00cd\u00d3\u0181\u0189\u0198")
        buf.write("\u01a2\u01a9\u01ad\7\3\17\2\b\2\2\3>\3\3?\4\3@\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    NUMBER = 2
    STRING = 3
    KW_TRUE = 4
    KW_FALSE = 5
    KW_NUMBER = 6
    KW_BOOL = 7
    KW_STRING = 8
    KW_RETURN = 9
    KW_VAR = 10
    KW_DYNAMIC = 11
    KW_FUNC = 12
    KW_FOR = 13
    KW_UNTIL = 14
    KW_BY = 15
    KW_BREAK = 16
    KW_CONTINUE = 17
    KW_IF = 18
    KW_ELSE = 19
    KW_ELIF = 20
    KW_BEGIN = 21
    KW_END = 22
    OP_ADD = 23
    OP_SUBTRACT = 24
    OP_MULTI = 25
    OP_DIVIDE = 26
    OP_REMAINDER = 27
    OP_NOT = 28
    OP_AND = 29
    OP_OR = 30
    OP_EQUAL = 31
    OP_LEFT_ARROW = 32
    OP_NOT_EQUAL = 33
    OP_SMALLER = 34
    OP_GREATER = 35
    OP_SMALLER_EQUAL = 36
    OP_GREATER_EQUAL = 37
    OP_EQUAL_COMPARE = 38
    OP_TRIPLE_DOT = 39
    SEP_OPEN_PAREN = 40
    SEP_CLOSE_PAREN = 41
    SEP_OPEN_BRACK = 42
    SEP_CLOSE_BRACK = 43
    SEP_COMA = 44
    COMMENT = 45
    WS = 46
    NEW_LINE = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

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
            "IDENTIFIER", "NUMBER", "STRING", "KW_TRUE", "KW_FALSE", "KW_NUMBER", 
            "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
            "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", 
            "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", 
            "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", "OP_NOT", 
            "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", "OP_NOT_EQUAL", 
            "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", 
            "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
            "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT", 
            "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER_HEAD", "IDENTIFIER", "ZERO", "NON_ZERO_DIGIT", 
                  "DIGIT", "FLOATING_POINT", "EXPONENTIAL", "NUMBER", "STRING_CHAR", 
                  "ESCAPE_SIGN", "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", 
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
            actions[13] = self.STRING_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
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
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text)
     


