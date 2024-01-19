grammar ZCode;

@lexer::header {
from lexererr import *
#MSSV: 2152597
}

options {
	language=Python3;
}

program:.;
//*PARSER RULES */
main_derclaration: KW_FUNC MAIN_TOKEN SEP_OPEN_PAREN SEP_CLOSE_BRACK code_block;

//*function */
function: KW_FUNC IDENTIFIER SEP_OPEN_PAREN SEP_CLOSE_BRACK code_block;

code_block:;


//*variable */
var_declaration:.;
var_assign: IDENTIFIER OP_LEFT_ARROW expression;

//*expression */
expression: NUMBER | IDENTIFIER operation expression;
operation: OP_ADD | OP_AND | OP_SUBTRACT | OP_REMAINDER | OP_DIVIDE;


//*LEXER RULES */
//*main func */
MAIN_TOKEN: 'main';

//*Identifier */
fragment IDENTIFIER_HEAD: [_a-zA-Z];
IDENTIFIER: IDENTIFIER_HEAD+[a-zA-Z0-9]*;

//*Number */
fragment ZERO: '0';
fragment NON_ZERO_DIGIT: [1-9];
fragment DIGIT: ZERO | NON_ZERO_DIGIT;
fragment FLOATING_POINT: '.'DIGIT*;
fragment EXPONENTIAL: [eE]('+'|'-')? NON_ZERO_DIGIT DIGIT*;
NUMBER: NON_ZERO_DIGIT DIGIT* FLOATING_POINT* EXPONENTIAL* | ZERO;


//*String */
fragment STRING_CHAR: ~[\\\b\f\r\n\t'"]; //*Any character that not a escape seq char and quote*/
fragment ESCAPE_SIGN:. [\\];
fragment ESCAPE_SEQUENCE:. ESCAPE_SIGN ~["]; 
//*Any char with escape sign prefix and not a double quote count as esc_seq*/
fragment DOUBLE_QUOTE_IN_STRING: [']["];
fragment STRING_LITTERAL: ESCAPE_SEQUENCE | DOUBLE_QUOTE_IN_STRING | STRING_CHAR;
STRING: ["] STRING_LITTERAL* ["] 
	{self.text = self.text[1:-1]} ;

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
COMMENT: COMMENT_HEAD NOT_NEW_LINE* -> skip; 
//Skip any character not a newline character after comment start fragment end a comment with newline/eof token

//*Whitespace and newline */
WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

NEW_LINE: '\n' -> channel(HIDDEN);
fragment NOT_NEW_LINE: ~'\n';

//*error handling
ERROR_CHAR: . 
{raise ErrorToken(self.text)};

UNCLOSE_STRING: ["] STRING_LITTERAL* EOF 
	{raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: ["] STRING_LITTERAL* ESCAPE_SIGN STRING_LITTERAL* ["]
	{raise IllegalEscape(self.text[1:-1])};
//TODO: Walkthough this lexeme?

