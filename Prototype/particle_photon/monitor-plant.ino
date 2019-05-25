const int MOISTURE_SENSOR = A0;
const int WATER_VALVE = D0; //This is actually just an LED...
const int MEAN_N = 4000;
bool needs_watering = false;
double mean_moisture;

int waterPlant(String command){
    Serial.println(command);
    //cloud function
    if(command=="water"){
        //return if water signal has already been sent before so the user isnt spammed by notifications
        if(needs_watering == true)
            return 1;
    
        needs_watering = true;
        digitalWrite(WATER_VALVE, HIGH);
        Particle.publish("waterPlant", "water");
    }
    if(command=="stop"){
        needs_watering = false;
        digitalWrite(WATER_VALVE, LOW);
        Particle.publish("waterPlant", "stop");
    }
    return 0;   //return 0 if watering succeeds
}

void setup() {
    pinMode(MOISTURE_SENSOR, INPUT);
    pinMode(WATER_VALVE, OUTPUT);
    
    Particle.variable("moisture", mean_moisture); //allow raspi to access moisture variable over api
    Particle.function("waterPlant", waterPlant);  //allow raspi to water the plant remotely
    Serial.begin(9600);
}

void loop() {
    // Calculate mean moisture from MEAN_N samples
    long int sum = 0;
    for(int i = 0; i < MEAN_N; i++)
        sum += analogRead(MOISTURE_SENSOR);
    mean_moisture = float(sum) / float(MEAN_N);
    
    delay(1000);    // wait 1 second between loops
}