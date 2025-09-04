%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int yylex(void);
int yyerror(const char *s);
extern FILE *yyin;
%}

%union {
    double fval;
}

%token <fval> NUM
%type <fval> expr

%%

input:
      /* vacío */
    | input expr '\n'
    | input expr
    ;

expr:
    NUM   { printf("Raíz cúbica: %.2f\n", cbrt($1)); }
    ;

%%

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror("No se pudo abrir archivo");
        return 1;
    }
    yyin = f;
    yyparse();
    fclose(f);
    return 0;
}
