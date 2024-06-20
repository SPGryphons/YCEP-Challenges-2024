#include <stdio.h>
#include <stdlib.h>

int main( int argc, char * argv[] ) {

    setbuf( stdin, 0 );
    setbuf( stdout, 0 );

    char buffer[20];
    printf( "here's a printf: %llx, say thank you\n", printf );
    gets( buffer );
    printf( "you're welcome\n" );
    return 0;
}