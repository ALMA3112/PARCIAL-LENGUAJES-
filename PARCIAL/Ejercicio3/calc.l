%{
#include "calc.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+(\.[0-9]+)?    { yylval.fval = atof(yytext); return NUM; }
\n                   { return '\n'; }
[ \t\r]+             ;   /* ignorar espacios y tabs */
.                    { return yytext[0]; }

%%

int yywrap(void) {
    return 1;
}
