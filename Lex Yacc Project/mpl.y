%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    int yylex(void);
    void yyerror(){
    	printf("syntax error\n");
    	exit(1);
    }
%}

%start program
%token VARIABLE INTEGER WHILE DO IF FOR WRITE PLUS MINUS DIVIDE MULTIPLY EQUAL NOTEQUAL AND OR SMALLER BIGGER ASSIGN
%token BEGINBLOCK FINISHBLOCK OPENPAR CLOSEPAR ENDLINE START FINISH

%left PLUS MINUS 
%left DIVIDE MULTIPLY 
%left EQUAL NOTEQUAL
%left AND OR 
%left SMALLER BIGGER


%%
    program: START exprs FINISH
    	| START FINISH;

    exprs: expr
    	 | expr exprs;

    expr: VARIABLE ASSIGN arithmetics1 ENDLINE
        | arithmetics1 WRITE ENDLINE
        | IF LOGIC BEGINBLOCK exprs FINISHBLOCK ENDLINE
        | WHILE LOGIC DO BEGINBLOCK exprs FINISHBLOCK ENDLINE
        | INTEGER FOR BEGINBLOCK exprs FINISHBLOCK ENDLINE;


    arithmetics1: arithmetics1 PLUS arithmetics1 
                | arithmetics1 MINUS arithmetics1 
                | arithmetics2;


    arithmetics2: arithmetics2 DIVIDE values
                | arithmetics2 MULTIPLY values
                | values;

    
    values: OPENPAR arithmetics1 CLOSEPAR
        | INTEGER
        | VARIABLE;

    LOGIC: LOGIC AND LOGIC
        | LOGIC OR LOGIC
        | compare
        | OPENPAR LOGIC CLOSEPAR;

    compare: values SMALLER arithmetics1 
            | values BIGGER arithmetics1 
            | values EQUAL arithmetics1 
            | values NOTEQUAL arithmetics1;

%%


int main(){
    yyparse();
    printf("OK\n");
    return 0;
}
