%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"
%}
%%
"open"      	{return START;}
"close"     	{return FINISH;}
"<"         	{return BEGINBLOCK;}
">"         	{return FINISHBLOCK;}
"."         	{return ENDLINE;}
"{"         	{return OPENPAR;}
"}"         	{return CLOSEPAR;}
"++"        	{return PLUS;}
"--"        	{return MINUS;}
"//"        	{return DIVIDE;}
"**"        	{return MULTIPLY;}
"=="        	{return EQUAL;}
"not=="     	{return NOTEQUAL;}
"^"         	{return AND;}
"v"         	{return OR;}
"smaller"   	{return SMALLER;}
"bigger"    	{return BIGGER;}
"when"      	{return WHILE;}
"do"		{return DO;}
"whether"   	{return IF;}
"times"  	{return FOR;}
"write"      	{return WRITE;}
"let"      	{return ASSIGN;}
[&][a-z][a-zA-Z0-9]+   {return VARIABLE;}
[1-9][0-9]*      	{return INTEGER;}
[ \t\n]         ;
.		{printf("syntax error \n"); exit(1);}
%%
