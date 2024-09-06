grammar CSP;

cspFile: (processDefinition | channelDefinition)+ ;

processDefinition: ID '('? parameters? ')'? '=' expression ;

channelDefinition: 'channel' ID (',' ID)* ':' '{' INT ('..' INT)? '}' ;

parameters: ID (',' ID)* ;

expression
    : BOOL '&' expression  // Guarded expression
    | expression '[]' expression  // External choice
    | expression '[' '{' eventList '}' '||' '{' eventList '}' ']' expression // Alphabetised Parallel
    | expression '[|' '{' eventList '}' '|]' expression  // Generalised Parallel
    | expression '|||' expression  // Interleave
    | expression ';' expression  // Sequential Composition
    | prefixExpression
    | baseExpression
    ;

prefixExpression: event '->' expression ;

baseExpression
    : STOP_RULE
    | SKIP_RULE
    | ID
    | '(' expression ')'
    ;

eventList: event (',' event)* ;  // 事件集

event: ID ('.' INT)* ;  // 事件允许通道名称加上具体的值

STOP_RULE: 'STOP' ;

SKIP_RULE: 'SKIP' ;

BOOL: 'true' | 'false' ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;  // 标识符规则

INT: [0-9]+ ;  // 数字规则

WS: [ \t\r\n]+ -> skip ;
