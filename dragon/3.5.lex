%{
/* definitions of manifest constants
LT, LE, EQ, NE, GT, GE,
IF, THEN, ELSE, ID, NUMBER, RELOP, WHILE, STRING */
%}

/* regular definitions */
delim       [ \t\n]
ws          {delim}+
letter      [A-Za-z]
letter_     {letter}_
digit       [0-9]
digit_      {digit}_
id          {letter_}({letter_}|{digit_})*
number      {digit}+(\.{digit}+)?(E[+-]?{digit }+)?
doubleq     \"
inside_str  [^"]*|\\"
str_lit     {doubleq}{inside_str}*{doubleq}

%%
{ws}        {/* no action and no return */}
if          {return (IF); }
while       {return (WHILE); /* Exercise 3.5.1 - a) */ }
then        {return (THEN); }
else        {return (ELSE) ; }
{id}        {yylval = (int) installID(); return (ID); }
{str_lit}   {/* yylval = (int) installString();*/ return (STRING); /* Exercise 3.5.1 - d) */}
{number}    {yylval = (int) installNum(); return (NUMBER); }
"<"         {yylval = LT; return (RELOP); }
"<="        {yylval = LE; return (RELOP);}
"=="        {yylval = EQ; return (RELOP); /* Exercise 3.5.1 - b) */ }
"!="        {yylval = NE; return (RELOP); /* Exercise 3.5.1 - b) */ }
">"         {yylval = GT; return (RELOP); }
">="        {yylval = GE; return (RELOP); }

%%

int installID() { /* function to install the lexeme, whose first character is pointed to bu yytext,
and whose length is yyleng, into the symbol table and return a pointer thereto */
}

int installNum() { /* similar to installID, but puts numerical constants into a seperate table */
}

int installString() {
/* ... */
}

