grammar ZCode;

@lexer::header {
from lexererr import *
#MSSV: 2152597
}

options {
	language=Python3;
}

program: foward_func_def* define* main_def define*;
//? Should main func be the last function tho?

//*PARSER RULES */
main_def: KW_FUNC MAIN_TOKEN SEP_OPEN_PAREN SEP_CLOSE_PAREN code_block;

define: func_def | var_def | array_def;

code_block:.;
line:;
statement:;

//*type def */
type_def: KW_NUMBER | KW_STRING | KW_BOOL;
implicit_type_def: KW_VAR | KW_DYNAMIC;

//*variable */
value_init: OP_ASSIGN expression;
var_def:(type_def IDENTIFIER value_init? NEW_LINE)
		| (KW_VAR IDENTIFIER value_init NEW_LINE)
		| (KW_DYNAMIC IDENTIFIER value_init? NEW_LINE); //? Should value_init be obligatory for dynamic variables?
var_assign: IDENTIFIER value_init NEW_LINE;

//*Array */
number_list: NUMBER number_list_tail?;
number_list_tail: SEP_COMA NUMBER number_list_tail?;
array_dim_list: SEP_OPEN_BRACK number_list SEP_CLOSE_BRACK;

array_def: type_def IDENTIFIER  array_dim_list array_init? NEW_LINE;
array_init: OP_ASSIGN (IDENTIFIER 
			| array_value_init);

array_value_init: SEP_OPEN_BRACK (array_value_init+|literal) SEP_CLOSE_BRACK;

//*function */
param_list:IDENTIFIER param_list_tail?;
param_list_tail: SEP_COMA IDENTIFIER param_list_tail?;

param_def_list: (type_def IDENTIFIER) param_def_list?;
param_def_list_tail: SEP_COMA (type_def IDENTIFIER) param_def_list_tail?;
param_def: SEP_OPEN_PAREN param_def_list? SEP_CLOSE_PAREN;

func_def: KW_FUNC IDENTIFIER param_def code_block;

foward_func_def: KW_FUNC IDENTIFIER param_def NEW_LINE;

func_call: IDENTIFIER SEP_OPEN_PAREN param_def_list? SEP_CLOSE_BRACK;

//*expression */
expression:
	SEP_OPEN_PAREN expression SEP_CLOSE_PAREN
	| expression SEP_OPEN_BRACK index_op SEP_CLOSE_BRACK
	| sign_number
	| <assoc=right> negate_op expression
	| expression multi_op expression
	| expression add_op expression
	| expression logic_op expression
	| expression relational_op expression
	| expression string_op expression
	| IDENTIFIER
	| literal;

index_op: expression (SEP_COMA index_op)*;

negate_op: OP_NOT;

multi_op: (OP_MULTI | OP_DIVIDE | OP_REMAINDER);

add_op: (OP_ADD | OP_SUBTRACT);

logic_op: (OP_AND | OP_OR);

relational_op: (OP_GREATER | OP_GREATER_EQUAL | OP_EQUAL | OP_NOT_EQUAL | OP_SMALLER | OP_SMALLER_EQUAL | OP_STRING_EQUAL );

string_op: OP_STRING_CONCAT;

//*Literal */
sign_number: <assoc=right> OP_SUBTRACT? NUMBER;
literal: NUMBER | STRING | BOOL ;




//*LEXER RULES */
//*main func */
MAIN_TOKEN: 'main';

//*Boolen */
BOOL: KW_TRUE | KW_FALSE;

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
OP_ASSIGN: '<-';
OP_NOT_EQUAL: '!=';
OP_SMALLER: '<';
OP_GREATER: '>';
OP_SMALLER_EQUAL: '<=';
OP_GREATER_EQUAL: '>=';
OP_STRING_EQUAL: '==';
OP_STRING_CONCAT: '...';

//*Separator */
SEP_OPEN_PAREN: '(';
SEP_CLOSE_PAREN: ')';
SEP_OPEN_BRACK: '[';
SEP_CLOSE_BRACK: ']';
SEP_COMA: ',';	


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


//*Comment
fragment COMMENT_HEAD: '##';
COMMENT: COMMENT_HEAD NOT_NEW_LINE* -> skip; 
//Skip any character not a newline character after comment start fragment end a comment with newline/eof token

//*Whitespace and newline */
WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

NEW_LINE: '\n';
fragment NOT_NEW_LINE: ~'\n';

//*error handling
ERROR_CHAR: . 
{raise ErrorToken(self.text)};

UNCLOSE_STRING: ["] STRING_LITTERAL* EOF 
	{raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: ["] STRING_LITTERAL* ESCAPE_SIGN STRING_LITTERAL* ["]
	{raise IllegalEscape(self.text[1:-1])};
//TODO: Walkthough this lexeme?

