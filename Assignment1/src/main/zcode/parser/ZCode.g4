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
KEYWORD: 'main';
//*Operator */
Operator: '';
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