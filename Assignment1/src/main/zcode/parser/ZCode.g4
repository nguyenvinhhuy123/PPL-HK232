grammar ZCode;

@lexer::header {
from lexererr import *
#MSSV: 2152597
}

options {
	language=Python3;
}

program:;

//*Identifier */
fragment IDENTIFIER_HEAD: [_a-zA-Z];
IDENTIFIER: IDENTIFIER_HEAD+[a-zA-Z0-9]*;

//*Number */
fragment ZERO: '0';
fragment NON_ZERO_DIGIT: [1-9];
fragment DIGIT: ZERO | NON_ZERO_DIGIT;
fragment FLOATING_POINT: '.'DIGIT*;
fragment EXPONENTIAL: [eE]('+'|'-')* NON_ZERO_DIGIT DIGIT*;
NUMBER: NON_ZERO_DIGIT DIGIT* FLOATING_POINT* EXPONENTIAL* | ZERO;

//*Boolen */
BOOLEN: KW_TRUE | KW_FALSE;


//*String */
fragment STRING_CHAR: ~[\\\b\f\r\n\t'"]; //*Any character that not a escape seq char and quote*/
fragment ESCAPE_SIGN:. '\\';
fragment ESCAPE_SEQUENCE:. ESCAPE_SIGN ~'"' | ESCAPE_SIGN NEW_LINE; 
//*Any char with escape sign prefix and not a double quote count as esc_seq*/
fragment DOUBLE_QUOTE_IN_STRING: '\'''"';
fragment STRING_LITTERAL: ESCAPE_SEQUENCE | DOUBLE_QUOTE_IN_STRING | STRING_CHAR;
STRING: '"' STRING_LITTERAL* '"';

//*Keyword */
//*Keyword token naming rule: KW_Keyname */
KW_TRUE: 'true';
KW_FALSE: 'false';
KW_NUMBER: 'number';
KW_BOOL: 'bool';
KW_STRING:'string';
KW_RETURN: 'return';
KW_VAR: 'var';
KW_DYNAMIC: 'dynamic';
KW_FUNC: 'func';
KW_FOR: 'for';
KW_UNTIL: 'until';
KW_BY: 'by';
KW_BREAK: 'break';
KW_CONTINUE: 'continue';
KW_IF: 'if';
KW_ELSE: 'else';
KW_ELIF: 'elif';
KW_BEGIN: 'begin';
KW_END: 'end';

//
//*Operator */
//*Operator token naming rule: OP_operator_name */
OP_ADD: '+';
OP_SUBTRACT: '-';
OP_MULTI: '*';
OP_DIVIDE: '/';
OP_REMAINDER: '%';
OP_NOT: 'not';
OP_AND: 'and';
OP_OR: 'or';
OP_EQUAL: '=';
OP_LEFT_ARROW: '<-';
OP_NOT_EQUAL: '!=';
OP_SMALLER: '<';
OP_GREATER: '>';
OP_SMALLER_EQUAL: '<=';
OP_GREATER_EQUAL: '>=';
OP_EQUAL_COMPARE: '==';
OP_TRIPLE_DOT: '...';

//*Separator */
SEP_OPEN_PAREN: '(';
SEP_CLOSE_PAREN: ')';
SEP_OPEN_BRACK: '[';
SEP_CLOSE_BRACK: ']';
SEP_COMA: ',';	

//*Comment
fragment COMMENT_HEAD: '##';
COMMENT: COMMENT_HEAD NOT_NEW_LINE* (NEW_LINE|EOF); 
//Skip any character not a newline character after comment start fragment end a comment with newline/eof token

//*Whitespace and newline */
WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

NEW_LINE: '\n';
NOT_NEW_LINE: ~'\n';

//*error handling
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;