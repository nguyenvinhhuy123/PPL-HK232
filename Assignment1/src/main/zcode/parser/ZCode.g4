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
fragment DIGIT: [0-9];
fragment FLOATING_POINT: [.]DIGIT+;
NUMBER: DIGIT+ (FLOATING_POINT)?;

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

//!might not need KW declare for these can be declare as operator fix later if needed
KW_NOT: 'not';
KW_AND: 'and';
KW_OR: 'or';
//
//*Operator */
//*Operator token naming rule: OP_operator_name */
OP_ADD: '+';
OP_SUBTRACT: '-';
OP_MULTI: '*';
OP_DIVIDE: '/';
OP_REMAINDER: '%';
OP_NOT: KW_NOT;
OP_AND: KW_AND;
OP_OR: KW_OR;
OP_EQUAL: '=';
OP_LEFT_ARROW: '<-';
OP_NOT_EQUAL: '!=';
OP_SMALLER: '<';
OP_GREATER: '>';
OP_SMALLER_EQUAL: '<=';
OP_GREATER_EQUAL: '>=';
OP_EQUAL_COMPARE: '==';
OP_TRIPLE_DOT: '...';



//*Bracket */

//*Comment
fragment COMMENT_HEAD: '##';
COMMENT: COMMENT_HEAD NOT_NEW_LINE* (NEW_LINE|EOF) -> Skip; 
//Skip any character not a newline character after comment start fragment end a comment with newline/eof token

//*Whitespace and newline */
WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

NEW_LINE: '\n';
NOT_NEW_LINE: ~'\n';

//*error handling
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;