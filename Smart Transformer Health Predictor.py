class SmartTransformerHealthPredictor:
    def __init__(self, temperature, oil_level, load_percentage,
                 voltage, vibration):
        self.temperature = temperature
        self.oil_level = oil_level
        self.load_percentage = load_percentage
        self.voltage = voltage
        self.vibration = vibration

    def calculate_health_score(self):
        score = 100

        # Temperature condition
        if self.temperature > 90:
            score -= 25
        elif self.temperature > 75:
            score -= 10

        # Oil level condition
        if self.oil_level < 50:
            score -= 20
        elif self.oil_level < 70:
            score -= 10

        # Load condition
        if self.load_percentage > 100:
            score -= 25
        elif self.load_percentage > 85:
            score -= 10

        # Voltage condition
        if self.voltage < 210 or self.voltage > 250:
            score -= 15
        elif self.voltage < 220 or self.voltage > 240:
            score -= 5

        # Vibration condition
        if self.vibration > 8:
            score -= 15
        elif self.vibration > 5:
            score -= 5

        return max(score, 0)

    def predict_health(self):
        score = self.calculate_health_score()

        if score >= 80:
            return "HEALTHY"
        elif score >= 60:
            return "WARNING"
        else:
            return "CRITICAL"

    def display_result(self):
        score = self.calculate_health_score()
        status = self.predict_health()

        print("----- Smart Transformer Health Predictor -----")
        print(f"Temperature       : {self.temperature:.2f} °C")
        print(f"Oil Level         : {self.oil_level:.2f} %")
        print(f"Load Percentage   : {self.load_percentage:.2f} %")
        print(f"Voltage           : {self.voltage:.2f} V")
        print(f"Vibration         : {self.vibration:.2f} mm/s")
        print(f"Health Score      : {score:.2f} / 100")
        print(f"Transformer Status: {status}")


# Example input values
temperature = 70
oil_level = 80
load_percentage = 75
voltage = 230
vibration = 3

transformer = SmartTransformerHealthPredictor(
    temperature,
    oil_level,
    load_percentage,
    voltage,
    vibration
)

transformer.display_result()
