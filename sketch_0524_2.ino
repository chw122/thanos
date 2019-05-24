//아날로그 핀
int sensorValue = 0;
int sensorValue2 = 0;
float avg = 0.0;

//안정화
float EMA_a = 0.6;
int EMA_s = 0;
int EMA_s2 = 0;


void setup() {
  Serial.begin(9600);
  EMA_s = sensorValue;
  EMA_s2 = sensorValue2;
}

// the loop routine runs over and over again forever:
void loop() {
  sensorValue = analogRead(A0);
  sensorValue2 = analogRead(A1);
  
  EMA_s = (EMA_a*sensorValue) + ((1-EMA_a)*EMA_s);
  EMA_s2 = (EMA_a*sensorValue2) + ((1-EMA_a)*EMA_s2);

  avg = (EMA_s + EMA_s2) / 2.0;

  
  //float avg = sqrt((pow(sensorValue, 2) + pow(sensorValue2, 2)) / 2.0);
  // print out the value you read:
  Serial.print("팔뚝 : ");
  Serial.print(EMA_s);
  Serial.print("           손목 : ");
  Serial.print(EMA_s2);
  Serial.print("           평균 : ");
  Serial.println(avg);
  delay(50);
} 
