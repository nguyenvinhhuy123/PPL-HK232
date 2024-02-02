grammar ZCode;

@lexer::header {
from lexererr import *
#MSSV: 2152597
}

options {
	language=Python3;
}

program:optional_end_line (forward_func | define)* EOF;
//? Should main func be the last function tho?

//*PARSER RULES */
main_def: KW_FUNC MAIN_TOKEN SEP_OPEN_PAREN SEP_CLOSE_PAREN optional_end_line inner_scope;

forward_func: forward_func_def end_line;
define: func_def | decl end_line | main_def;

inner_scope: 
	block_statement end_line
	| return_statement end_line
	;

lines: (line|statement_line)*;
line: (decl | assign) end_line ;

decl: (var_def | array_def);

assign: (var_assign | array_assign | array_elem_assign);

statement_line: statement end_line;
statement: 
	(if_statement
	| for_statement
	| break_statement
	| continue_statement
	| return_statement
	| block_statement
	| func_call
	| decl
	| assign)
	; //TODO: all statement type together

//*type def */
type_def: KW_NUMBER | KW_STRING | KW_BOOL;
implicit_type_def: KW_VAR | KW_DYNAMIC;

//*variable */
var_def: static_var_def | dynamic_var_def ;
var_def_for_param: type_def IDENTIFIER;

value_init: OP_ASSIGN expression;
optional_val_init: value_init |;
static_var_def: (type_def IDENTIFIER optional_val_init);
dynamic_var_def:
	(KW_VAR IDENTIFIER value_init)
	| (KW_DYNAMIC IDENTIFIER optional_val_init)
	; //? Should value_init be obligatory for dynamic variables?
var_assign: IDENTIFIER value_init;

//*Array */
dim_list: NUMBER dim_list_tail;
dim_list_tail: SEP_COMA NUMBER dim_list_tail |;
array_dim: SEP_OPEN_BRACK dim_list SEP_CLOSE_BRACK;

array_def: array_static_def ;
array_def_for_param: type_def array_identifier;

array_identifier: IDENTIFIER array_dim;
array_static_def: type_def array_identifier optional_array_init;

array_init: OP_ASSIGN (expression | array_value);
optional_array_init: array_init |;

array_value_init_list: array_value_elem array_value_init_tail;
array_value_init_tail: (SEP_COMA array_value_init_list) | ;
array_value_elem: (expression);
array_value: SEP_OPEN_BRACK array_value_init_list SEP_CLOSE_BRACK;

array_assign: IDENTIFIER array_init;
array_elem_assign: array_element_expr array_elem_init;
array_elem_init: OP_ASSIGN expression ;
//*function */
param_def_list: param optional_end_line param_def_list_tail |;
param_def_list_tail: SEP_COMA param param_def_list_tail|;
param: array_def_for_param | var_def_for_param;

param_def: SEP_OPEN_PAREN param_def_list SEP_CLOSE_PAREN;

func_def: KW_FUNC IDENTIFIER param_def optional_end_line inner_scope;

forward_func_def: KW_FUNC IDENTIFIER param_def;

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

negate_expr: negate_op negate_expr | sign_expr;
negate_op: OP_NOT;

sign_expr: (OP_SUBTRACT) sign_expr | array_expr;

array_expr: array_element_expr | primary_expression;
array_element_expr: term indexer;
indexer: SEP_OPEN_BRACK index_op SEP_CLOSE_BRACK;
index_op: expression (SEP_COMA index_op | );

primary_expression:
	SEP_OPEN_PAREN expression SEP_CLOSE_PAREN
	| literal
	| term
	;

term: IDENTIFIER | func_call ;

//*Statements */
//*if stmt */
if_statement: if_clause (end_line elif_clause)* (end_line else_clause | );

if_clause: KW_IF if_condition optional_end_line statement;
elif_clause: KW_ELIF if_condition optional_end_line statement;
else_clause: KW_ELSE optional_end_line statement;

if_condition: SEP_OPEN_PAREN expression SEP_CLOSE_PAREN;

//*for stmt */
for_statement: for_clause condition_clause update_clause optional_end_line statement;

for_clause:KW_FOR IDENTIFIER | array_identifier;
condition_clause:KW_UNTIL expression;
update_clause:KW_BY expression;

//*break stmt */
break_statement: KW_BREAK;

//*cont stmt */
continue_statement:KW_CONTINUE;

//*return stmt*/
return_statement: KW_RETURN (expression| );

//*function call/invoke */
passing_arg: SEP_OPEN_PAREN passing_list SEP_CLOSE_PAREN;
passing_list: expression passing_list_tail | ;
passing_list_tail: SEP_COMA expression passing_list_tail | ;

func_call: IDENTIFIER passing_arg;

//*block stmt */
block_statement: KW_BEGIN end_line lines optional_end_line KW_END;

//*Literal */
literal: NUMBER | STRING | boolean | array_value;
//*Boolen */
boolean: KW_TRUE | KW_FALSE;

optional_end_line: (end_line |);
end_line: (NEW_LINE)+;
//*LEXER RULES */

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

//*Comment
fragment COMMENT_HEAD: '##';
COMMENT: COMMENT_HEAD NOT_NEW_LINE* -> skip; 
//Skip any character not a newline character after comment start fragment end a comment with newline/eof token

//*Whitespace and newline */
WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs, and whitespace tok

NEW_LINE: (WINDOW_NEW_LINE | '\n'  | '\r') {self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")};
fragment WINDOW_NEW_LINE: '\r\n' ;
fragment NOT_NEW_LINE: ~[\r\n];

//*Identifier */
fragment IDENTIFIER_HEAD: [_a-zA-Z];
fragment IDENTIFIER_TAIL: [_a-zA-Z0-9]*;
IDENTIFIER: IDENTIFIER_HEAD IDENTIFIER_TAIL | MAIN_TOKEN;

//*main func */
MAIN_TOKEN: 'main';

//*Number */
fragment ZERO: '0';
fragment NON_ZERO_DIGIT: [1-9];
fragment DIGIT: ZERO | NON_ZERO_DIGIT;
fragment DECIMAL: DIGIT+;
fragment FLOATING_POINT: '.'DIGIT* | ;
fragment EXPONENTIAL: [eE]('+'|'-'|)DIGIT+ | ;
NUMBER: DECIMAL FLOATING_POINT EXPONENTIAL | ZERO;


//*String */
fragment ESCAPE_SIGN: [\\];
fragment ESCAPE_SEQUENCE: ESCAPE_SIGN ESCAPE_REP;
fragment ESCAPE_REP: [bfrnt'\\]; //[\bfrnt'] : escape seq representation char 
fragment NOT_ESCAPE_REP: ~[bfrnt'\\];
fragment ILLEGAL_ESCAPE_SEQ: ESCAPE_SIGN NOT_ESCAPE_REP;
fragment STRING_CHAR: ~[\\\r\n"] ; //*Any character that not a escape seq char and quote*/

fragment DOUBLE_QUOTE_IN_STRING: [']["];
fragment STRING_LITTERAL: ESCAPE_SEQUENCE | DOUBLE_QUOTE_IN_STRING | STRING_CHAR ;
//*Why NEW_LINE here: Put NL in stirng_char and tto it like this is nearly the same, 
//*however, when we do this way, we can count the number of NL even when it in string
//*Thus will be helpful for count line for frontend to be able to give the exatc error line
//*Ex: string: "a\na\na\n" -> should be count as 4 different line in parser, not 1*/
STRING: ["] (NEW_LINE | STRING_LITTERAL )* ["]
	{self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
self.text = self.text[1:-1]} ;

//*error handling
ERROR_CHAR:. 
 	{raise ErrorToken(self.text)};

UNCLOSE_STRING: ["] (STRING_LITTERAL|NEW_LINE)* EOF 
	{self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: ["] (STRING_LITTERAL|NEW_LINE )* ILLEGAL_ESCAPE_SEQ 
	{self.text = self.text.replace("\r\n", "\n").replace("\r", "\n")
raise IllegalEscape(self.text[1:])};


