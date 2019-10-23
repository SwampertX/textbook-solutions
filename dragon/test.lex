delim [ \t\n]
ws {delim}+
non_ws [^{delim}]*

%%

{ws} {return(' ');}

%%
