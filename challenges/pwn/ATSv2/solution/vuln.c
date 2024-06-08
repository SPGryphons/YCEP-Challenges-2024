#include <stdio.h>
#include <unistd.h>

void slow_type( char * msg ) {
    /*
    thanks @Elma!
    */
	int i = 0;

	while ( 1 ) {
		if ( ! msg[ i ] ) {
            return;
        }

		putchar( msg[ i ] );
		usleep( 5000 );
		i += 1;
	}
}

void printWelcome() {
    char * line1 = "========================================\n";
    char * line2 = " Welcome to Singapore Polytechnic\n";
    char * line3 = "      Attendance System\n";
    char * line4 = "========================================\n";

    slow_type( line1 );
    slow_type( line2 );
    slow_type( line3 );
    slow_type( line4 );
}

void printWin() {
    char * line1 = "========================================\n";
    char * line2 = " Congratulations! You have won the game!\n";
    char * line3 = "========================================\n";

    slow_type( line1 );
    slow_type( line2 );
    slow_type( line3 );
}


void win() {
    
    /*
        Secret endpoint for administrator users!
    **/

    printf( "\n\n" );

    char * welcomeLine1 = "========================================\n";
    char * welcomeLine2 = " Admin Access: Secure Shell Activated\n";
    char * welcomeLine3 = "========================================\n";

    slow_type( welcomeLine1 );
    slow_type( welcomeLine2 );
    slow_type( welcomeLine3 );

    char * argv[] = { "/bin/sh", NULL }; 
    char * envp[] = { NULL };

    execve( "/bin/sh", argv, envp ); 
}

int main( int argc, char *argv[] ) {

    setbuf( stdin, 0 );
    setbuf( stdout, 0 );

    printWelcome();

    char ATS [ 6 ];

    printf( "Enter your ATS code >> " );

    gets( ATS );

    printf( "\nATS successfully entered, enjoy your class!~\n" );

    return 0;
}