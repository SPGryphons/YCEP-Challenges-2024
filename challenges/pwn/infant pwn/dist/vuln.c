#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void win() {

    printf( "\n[+] buffer overflow detected, congrats\n" );

    int     fd;
    char *  flag;
    ssize_t read_bytes;

    if ( ( fd = open( "./flag.txt", O_RDONLY ) ) == -1 ) {
        printf( "couldn't open flag.txt file\n" );
        exit( 1 );
    }

    if ( ( flag = (char *)calloc( 0x50, sizeof( char ) ) ) == NULL ) {
        printf( "calloc failed\n" );
        close( fd );
        exit( 1 );
    }

    if ( ( read_bytes = read( fd, flag, 0x50 ) ) == -1 ) {
        printf( "couldn't read flag.txt file\n" );
        free( flag );
        close( fd );
        exit( 1 );
    }

    close( fd );
    printf( "congrats: %s\n", flag );
    free( flag );
    exit( 0 );
}

void lose() {
    printf( "Sorry, try again\n" );
    exit( 1 );
}

void vuln() {
    int  canary = 0xdeadbeef;
    char overflow_me[100];

    printf( "[-] canary set to: %p\n", canary );
    printf( "overflow me plz: " );

    gets( overflow_me );

    printf( "value of canary now: %p\n", canary );
    if ( canary != 0xdeadbeef ) {
        win();
    } else {
        lose();
    }
}

int main( int argc, char ** argv ) {

    setbuf( stdin, 0 );
    setbuf( stdout, 0 );

    vuln();

    return 0;
}