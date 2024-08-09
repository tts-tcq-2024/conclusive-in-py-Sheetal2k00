class CoolingTypeLimits:
    LIMITS = {
        'PASSIVE_COOLING': (0, 35),
        'HI_ACTIVE_COOLING': (0, 45),
        'MED_ACTIVE_COOLING': (0, 40)
    }

    @staticmethod
    def get_limits(coolingType):
        if coolingType in CoolingTypeLimits.LIMITS:
            return CoolingTypeLimits.LIMITS[coolingType]
        raise ValueError(f"Unknown cooling type: {coolingType}")

def infer_breach(value, lowerLimit, upperLimit):
    if value < lowerLimit:
        return 'TOO_LOW'
    if value > upperLimit:
        return 'TOO_HIGH'
    return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
    lowerLimit, upperLimit = CoolingTypeLimits.get_limits(coolingType)
    return infer_breach(temperatureInC, lowerLimit, upperLimit)

class AlertTarget:
    @staticmethod
    def to_controller(breachType):
        header = 0xfeed
        print(f'{header}, {breachType}')

    @staticmethod
    def to_email(breachType):
        recipient = "a.b@c.com"
        breach_messages = {
            'TOO_LOW': 'Hi, the temperature is too low',
            'TOO_HIGH': 'Hi, the temperature is too high'
        }
        print(f'To: {recipient}')
        print(breach_messages[breachType])

    ALERT_METHODS = {
        'TO_CONTROLLER': to_controller,
        'TO_EMAIL': to_email
    }

    @staticmethod
    def send_alert(alertTarget, breachType):
        if alertTarget in AlertTarget.ALERT_METHODS:
            AlertTarget.ALERT_METHODS[alertTarget](breachType)
        else:
            raise ValueError(f"Unknown alert target: {alertTarget}")

def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    AlertTarget.send_alert(alertTarget, breachType)
