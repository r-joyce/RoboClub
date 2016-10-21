// Constants needed to setup PWM frequency
const float clk = 16000000;
const float prescale = 64;

// Setting pin numbers
const int clockPin = 5;
const int dataPin = 3;
const int latchPin = 4;

// The delay between shifts in the shift register in milliseconds
int period = 30;

void setup()
{
  // Turning on the PWM output
  onPWM_12();
  // Setting the output to 500Hz with a 50% duty cycle
  setPWM_12(500,50);

  // Setting the pins as outputs
  pinMode(clockPin,OUTPUT);
  pinMode(dataPin,OUTPUT);
  pinMode(latchPin,OUTPUT);

  // Beginning serial communication because yolo
  Serial.begin(9600);
}

void loop()
{
  // Main loop
  for(int i = 0;i < 16;i++)
  {
    // i is less than 3 three times in the for loop, so 3 ones are shifted into the system
    if(i < 3)
    {
      shiftOne();
    }
    // Shifting in zeros otherwise to keep the ones in the system moving
    else
    {
      shiftZero();
    }
    // Delaying between shifts
    delay(period);
    // Changing frequency as shifts occur
    setPWM_12(800-(i*40),50);
  }
}

// Function to shift a one into system
void shiftOne()
{
  digitalWrite(latchPin, LOW);
  digitalWrite(dataPin,HIGH); 
  digitalWrite(clockPin,HIGH);
  digitalWrite(clockPin,LOW);
  digitalWrite(dataPin,LOW);
  digitalWrite(latchPin, HIGH);
}

// Function to shift a zero into system
void shiftZero()
{
  digitalWrite(latchPin, LOW);
  digitalWrite(clockPin,HIGH);
  digitalWrite(clockPin,LOW);
  digitalWrite(latchPin, HIGH);
}


// Function to set the frequency and duty cycle of timer associated with pin 12
void setPWM_12(float freq,float duty)
{
  int ocra = round((clk/(prescale*freq))-1);
  int ocrb = round(((clk/(prescale*freq))-1)*(duty/100));
  
  byte ocral = lowByte(ocra);
  byte ocrah = highByte(ocra);
  
  byte ocrbl = lowByte(ocrb);
  byte ocrbh = highByte(ocrb);
  
  TCCR1A = 0x23;
  TCCR1B = 0x1B;
  
  OCR1AH = ocrah;
  OCR1AL = ocral;
  
  OCR1BH = ocrbh;
  OCR1BL = ocrbl;
}

// Function to turn PWM on
void onPWM_12()
{
  DDRB = DDRB & 0b10111111 | 0x40;
  PORTB = PORTB & 0b10111111 | 0x40;
  TCCR1A = 0x23;
}

// Function to turn PWM off
void offPWM_12()
{
  PORTB = PORTB & 0b10111111 | 0x00;
  TCCR1A = 0x03;
}

