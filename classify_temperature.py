class CoolingType:
    PASSIVE_COOLING = ("PASSIVE_COOLING", 0, 35)
    HI_ACTIVE_COOLING = ("HI_ACTIVE_COOLING", 0, 45)
    MED_ACTIVE_COOLING = ("MED_ACTIVE_COOLING", 0, 40)

def classify_temperature(temp, cooling_type):
    _, lower_limit, upper_limit = cooling_type
    if temp < lower_limit:
        return "TOO_LOW"
    elif temp > upper_limit:
        return "TOO_HIGH"
    return "NORMAL"
