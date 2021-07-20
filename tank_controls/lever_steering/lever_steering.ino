int pushbutton = A0;
int leftLever = A1;
int rightLever = A2;
int fireButton = A3;
int buttonVal;
int fireVal;
String leftVal;
String rightVal;
String fire;

void setup() {
  // put your setup code here, to run once:
  pinMode(pushbutton, INPUT);
  pinMode(leftLever, INPUT);
  pinMode(rightLever, INPUT);
  pinMode(fireButton, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  buttonVal = analogRead(A0);
  fireVal = analogRead(A3);

  if (fireVal > 0)
  {
    fire = "HOLD";
  }
  else
  {
    fire = "FIRE";
  }
  
  if (buttonVal > 0)
  {
    Serial.println(fire + "-1" + ", " + "-1");
  }
  else
  {
    leftVal = String(analogRead(A1));
    rightVal = String(analogRead(A2));
    Serial.println(fire + leftVal + ", " + rightVal);

  }
  delay(500);
}
