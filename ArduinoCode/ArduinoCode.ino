
int j = 1;
int LEDState = 0;
int LEDPin = 13;
int buttonPin = 11;
int buttonNew;
int whiteButton;
int redButton;
int yellowButton;
int blueButton;
int greenButton;
int buttonOld = 1;
int test = 10;
int dt = 100;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LEDPin, OUTPUT);
  pinMode(buttonPin, OUTPUT);
  //pinMode(6, OUTPUT);
  //pinMode(buttonPin, OUTPUT);
  pinMode(2, INPUT_PULLUP); // white
  pinMode(9, INPUT_PULLUP); // red
  pinMode(4, INPUT_PULLUP); // blue
  pinMode(12, INPUT_PULLUP); // green
  pinMode(7, INPUT_PULLUP); // yellow
  pinMode(test,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEDPin, HIGH);
  analogWrite(buttonPin, 255);
  analogWrite(test,120);
  //analogWrite(6, 255);
  //Serial.println("Start");
  whiteButton = digitalRead(2);
  redButton = digitalRead(9);
  blueButton = digitalRead(4);
  greenButton = digitalRead(12);
  yellowButton = digitalRead(7);


  if (whiteButton == LOW) {
    Serial.print("W");

  }
  if (redButton == LOW) {
    Serial.print("R");

  }
  if (blueButton == LOW) {
    Serial.print("B");

  }
    if (greenButton == LOW) {                                                                                                                                                   
    Serial.print("G");

  }
    if (yellowButton == LOW) {
    Serial.print("Y");

  }
  Serial.println("E");
  delay(50);


}
