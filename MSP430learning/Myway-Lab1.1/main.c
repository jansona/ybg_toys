#include <msp430.h> 


/**
 * main.c
 */
int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer
	P1DIR|=(BIT0+BIT6);
	P1OUT&=~BIT0;
	P1OUT|=BIT6;
	P1REN|=BIT3;
//	P1OUT|=BIT3;
	P1IES&=~BIT3;
	P1IFG&=~BIT3;
	P1IE|=BIT3;

	__bis_SR_register(LPM4_bits + GIE);
	__no_operation();
	return 0;
}

#pragma vector=PORT1_VECTOR
__interrupt void Port_1(void)
{
    __delay_cycles(100000);
    P1OUT^=(BIT0+BIT6);
    P1IFG&=~BIT3;
}
