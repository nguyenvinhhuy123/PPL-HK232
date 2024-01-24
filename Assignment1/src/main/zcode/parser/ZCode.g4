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

code_block: 
	KW_BEGIN lines KW_END
	| lines return_statement
	;
lines: (line|statement)*;
line: var_def | var_assign | array_def | array_asign ;
statement:; //TODO: all statement type together

//*type def */
type_def: KW_NUMBER | KW_STRING | KW_BOOL;
implicit_type_def: KW_VAR | KW_DYNAMIC;

//*variable */
var_def: static_var_def | dynamic_var_def ;

value_init: OP_ASSIGN expression;
static_var_def: (type_def IDENTIFIER value_init?);
dynamic_var_def:
	(KW_VAR IDENTIFIER value_init)
	| (KW_DYNAMIC IDENTIFIER value_init?)
	; //? Should value_init be obligatory for dynamic variables?
var_assign: IDENTIFIER value_init;

//*Array */
number_list: NUMBER number_list_tail |;
number_list_tail: SEP_COMA NUMBER number_list_tail |;
array_dim_list: SEP_OPEN_BRACK number_list SEP_CLOSE_BRACK;

array_def: type_def IDENTIFIER  array_dim_list array_init? NEW_LINE;

array_init: OP_ASSIGN (IDENTIFIER | array_value_init);
array_value_init: SEP_OPEN_BRACK (array_value_init+|literal) SEP_CLOSE_BRACK;

array_asign: IDENTIFIER array_asign;

//*function */
param_list:IDENTIFIER param_list_tail | ;
param_list_tail: SEP_COMA IDENTIFIER param_list_tail | ;

param_def_list: param param_def_list_tail | ;
param_def_list_tail: SEP_COMA param param_def_list_tail|;
param: type_def IDENTIFIER;

param_def: SEP_OPEN_PAREN param_def_list SEP_CLOSE_PAREN;

func_def: KW_FUNC IDENTIFIER param_def code_block;

foward_func_def: KW_FUNC IDENTIFIER param_def;

func_call: IDENTIFIER SEP_OPEN_PAREN param_def_list SEP_CLOSE_BRACK;

//*expression */
expressions: (expression)*;
expression: string_expr
	| relation_expr
	| logic_expr
	| add_expr
	| multi_expr
	| negate_expr
	| primary_expression
	| array_expr;

string_expr: relation_expr string_op relation_expr | relation_expr;
string_op: OP_STRING_CONCAT;

relation_expr: logic_expr relational_op logic_expr | logic_expr;
relational_op: (OP_GREATER | OP_GREATER_EQUAL | OP_EQUAL | OP_NOT_EQUAL | OP_SMALLER | OP_SMALLER_EQUAL | OP_STRING_EQUAL);

logic_expr: logic_expr logic_op add_expr | add_expr;
logic_op: (OP_AND | OP_OR);

add_expr: add_expr add_op multi_expr | multi_expr;
add_op: (OP_ADD | OP_SUBTRACT);

multi_expr: multi_expr multi_op negate_expr | negate_expr;
multi_op: (OP_MULTI | OP_DIVIDE | OP_REMAINDER);

negate_expr: negate_op negate_expr | primary_expression;
negate_op: OP_NOT;

primary_expression:
	SEP_OPEN_PAREN expression SEP_CLOSE_PAREN
	| literal
	| array_expr
	;

array_expr: array_expr  indexer | term;
indexer: SEP_OPEN_BRACK index_op SEP_CLOSE_BRACK;
index_op: expression (SEP_COMA index_op)*;

term: IDENTIFIER | func_call;


//*Literal */
sign_number: (OP_SUBTRACT| ) NUMBER;
literal: sign_number | STRING | boolean;
//*Boolen */
boolean: KW_TRUE | KW_FALSE;

comment: NEW_LINE COMMENT NEW_LINE;




//*LEXER RULES */
//*main func */
MAIN_TOKEN: 'main';


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

