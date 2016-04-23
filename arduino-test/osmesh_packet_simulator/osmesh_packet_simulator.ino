/*
    OpenSmartMesh packet simulator sending osm strings on serial 
 */

// String declaration for msg
String msg0, msg;

void setup() {
  // initialize serial at 115200 bps
  Serial.begin(115200);
  while (!Serial) {
    ; // wait needed for native USB port only
  }


  msg0 = String("id:");
  msg  = String();
}

void loop() {
  long dTime = 0;
  while (true)
  {
    dTime = millis() + 5000;
    msg = msg0 + dTime + ",dataA2X:";
    msg = msg + (millis() - dTime) + "\r\n";
    Serial.print(msg);
    while (millis() < dTime)
    {
     ;// do nothing, wait
    }
  }
  

}
