// Firmware for Python Class Board over serial
// Python Class Board is (effectively) a small Arduino Leonardo clone

// Pin defines for peripherals
#define SWITCH_ONE 2
#define SWITCH_TWO 3
#define SWITCH_THREE 4
#define BUZZER 5
#define LED_RED 6
#define LED_YELLOW 7
#define LED_GREEN  8
#define TEMP_SENSOR A0
#define TRIM_POT A1

// Defines for serial functions case statement characters
#define LED_CONTROL 'L'
#define BUZZER_CONTROL 'B'
#define GET_SWITCH 'S'
#define GET_TEMP 'T'
#define GET_POTENTIOMETER 'P'

// Setup serial message options
char message_buffer[21]; // null terminated char array,fits 20 characters + null
int message_index = 0;

// Set up pins, and serial communication
void setup() {
  // Configure pins
  pinMode(SWITCH_ONE, INPUT);
  pinMode(SWITCH_TWO, INPUT);
  pinMode(SWITCH_THREE, INPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(TEMP_SENSOR, INPUT);
  pinMode(TRIM_POT, INPUT);

  Serial.begin(57600);

  memset(message_buffer, 0, sizeof(message_buffer));
}

// Handle incoming messages
void loop() {
  if (message_get()) {
    byte operation = message_buffer[0];
    switch (operation) {
      case LED_CONTROL:
        set_led();
        break;
      case BUZZER_CONTROL:
        set_buzzer();
        break;
      case GET_SWITCH:
        get_switch();
        break;
      case GET_TEMP:
        get_temperature();
        break;
      case GET_POTENTIOMETER:
        get_potentiometer();
        break;
      default:
        Serial.print("ERROR: COMMAND CHARACTER: \"");
        Serial.print((char)operation);
        Serial.println("\" INVALID. VALID COMMANDS ARE: LED CONTROL (L), BUZZER CONTROL (B), GET SWITCH STATE (S), GET TEMPERATURE (T), GET POTENTIOMETER VOLTAGE (P).");
        break;
    }
  }
}

// Set target LED to 1 (on) or 0 (off)
void set_led() {
  char led = message_buffer[1];
  char state = message_buffer[2];
  if ((led == 'R' || led == 'Y' || led == 'G') && (state == '0' || state == '1')) {
    bool output_state = LOW;
    if (state == '1') {
      output_state = HIGH;
    }
    switch (led) {
      case 'R':
        digitalWrite(LED_RED, output_state);
        break;
      case 'Y':
        digitalWrite(LED_YELLOW, output_state);
        break;
      case 'G':
        digitalWrite(LED_GREEN, output_state);
        break;
    }
    return;
  }
  else {
    Serial.print("ERROR: ");
    if (led != 'R' && led != 'Y' && led != 'G') {
      Serial.print(" LED VALUE OF: \"");
      Serial.print((char)led);
      Serial.print("\" INVALID. VALID LED'S ARE: RED (R), YELLOW (Y), GREEN (G).");
    }
    if (state != '0' && state != '1') {
      Serial.print(" LED STATE VALUE OF: \"");
      Serial.print((char)state);
      Serial.print("\" INVALID. VALID LED STATES ARE: ON (1), OFF (0).");
    }
    Serial.println();
  }
  return;
}

// Set buzzer to 1 (on) or 0 (off)
void set_buzzer() {
  char state = message_buffer[1];
  if (state == '0' || state == '1') {
    bool output_state = LOW;
    if (state == '1') {
      output_state = HIGH;
    }
    digitalWrite(BUZZER, output_state);
    return;
  }
  else {
    Serial.print("ERROR: BUZZER STATE VALUE OF: \"");
    Serial.print((char)state);
    Serial.println("\" INVALID. VALID BUZZER STATES ARE: ON (1), OFF (0).");
  }
  return;
}

// Returns 1 (enabled) or 0 (disabled) for a given switch input
void get_switch() {
  char sw = message_buffer[1];
  if (sw == '1' || sw == '2' || sw == '3') {
    bool switch_status = false;
    switch (sw) {
      case '1':
        switch_status = digitalRead(SWITCH_ONE);
        break;
      case '2':
        switch_status = digitalRead(SWITCH_TWO);
        break;
      case '3':
        switch_status = digitalRead(SWITCH_THREE);
        break;
    }
    Serial.println(switch_status);
  }
  else {
    Serial.print("ERROR: SWITCH VALUE OF: \"");
    Serial.print((char)sw);
    Serial.println("\" INVALID. VALID SWITCH INPUTS ARE: SW1 (1), SW2 (2), SW3 (3).");
  }
}

// Returns temperature calculated from TMP36 in Fahrenheit
// Note: I should have used the 3.3V line, temperature values are wacky for this but oh well
void get_temperature() {
  // Celsius temperature = [(analog voltage in mV) - 500] / 10
  // Fahrenheit temperature = (Celsius value × 9/5) + 32
  int sensor_reading = analogRead(TEMP_SENSOR);
  // ADC is 0-1024 for 0-5V, convert to volts
  float voltage = sensor_reading * 5.0 / 1024;
  // Convert to Celsius
  float temperature_c = ((voltage *1000) - 500) /10 ;
  // Convert to Fahrenheit
  float temperature_f = (temperature_c * 9.0 / 5.0) + 32.0;
  Serial.println(temperature_f);
}

// Returns voltage coming off potentiometer from 0-5V
void get_potentiometer() {
  int sensor_reading = analogRead(TRIM_POT);
  // ADC is 0-1024 for 0-5V, convert to volts
  float voltage = sensor_reading * 5.0 / 1024;
  Serial.println(voltage);
}

//Takes bytes off the serial port until a start of packet is found, and a delimiter (or buffer overrun)
bool message_get() {
  while (Serial.available()) {
    if (Serial.read() == '!') { //look for start of packet
      message_buffer[0] = '\0';
      message_index = 0;
      memset(message_buffer, 0, sizeof(message_buffer));
      while (message_index < 20) {
        while (Serial.available()) {
          message_buffer[message_index++] = Serial.read();
          message_buffer[message_index + 1] = '\0';
          if ((message_buffer[message_index - 2] == '\r') && (message_buffer[message_index - 1] == '\n' )) {
            //Serial.println(message_buffer);
            return (true);
          }
          else if (message_index >= 20) {
            Serial.println("ERROR: BUFFER EXCEEDED BEFORE DELIMITER FOUND");
            return (false);
          }
        }
      }
    }
    else {
      return (false);
    }
  }
  return (false);
}
