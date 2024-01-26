grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : (decl)+ EOF ;

decl:  line_var_decl | funcdecl;
line_var_decl: (vardecl SEMICOLON);
type_def: KW_INT | KW_FLOAT;

vardecl: type_def id_list;
id_list: ID id_list_tail;
id_list_tail:COMMA ID id_list_tail | ;

funcdecl: type_def ID param body;

param: L_BRACK param_list R_BRACK;
param_list: vardecl param_list_tail | ;
param_list_tail: SEMICOLON vardecl param_list_tail | ;

body: L_PAREN inner_scope R_PAREN;
inner_scope: 
	(line)*
	;
line:
	line_var_decl
	| statement
	;
statement:
	(assignment_stmt
	|call_stmt
	|return_stmt) 
	SEMICOLON
	;

assignment_stmt: ID ASSIGN expr;

call_stmt: ID passing;
passing: L_BRACK passing_list R_BRACK;
passing_list: expr passing_list_tail | ;
passing_list_tail: COMMA expr passing_list_tail | ;
return_stmt: KW_RETURN expr;

expr: 
	add_expr
	| sub_expr
	| mult_expr
	;
add_expr: sub_expr ADD add_expr | sub_expr; //right assoc lowest
sub_expr: mult_expr SUBTRACT mult_expr | mult_expr; //non assoc
mult_expr: primary_expr mult_op mult_expr | primary_expr; //left assoc highest
mult_op: MULTI | DIV;
primary_expr: 
	INT_LIT 
	| FLOAT_LIT 
	| ID
	| call_stmt
	| L_BRACK expr R_BRACK 
	;



KW_INT: 'int';
KW_FLOAT: 'float';
KW_RETURN: 'return';


ID: [a-zA-Z]+; // includes a sequence of alphabetic characters.
INT_LIT: [0-9]+;

fragment FLOATING: DOT INT_LIT ;
FLOAT_LIT:INT_LIT FLOATING;

SEMICOLON: ';';
COMMA:',';
L_BRACK: '(';
R_BRACK: ')';
L_PAREN: '{';
R_PAREN: '}';
ASSIGN: '=';
ADD: '+';
SUBTRACT: '-'; 
MULTI: '*';
DIV: '/';
DOT: '.';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

