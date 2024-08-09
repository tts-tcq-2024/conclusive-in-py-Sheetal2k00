import unittest
from unittest.mock import patch
from monitor_battery import classify_temperature_breach, AlertTarget

class BatteryMonitoringTest(unittest.TestCase):
    def test_classify_temperature_breach(self):
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', 36), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', -1), 'TOO_LOW')
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', 39), 'NORMAL')

@patch('builtins.print')
def test_alert_methods(self, mock_print):
    AlertTarget.send_alert('TO_CONTROLLER', 'TOO_HIGH')
    mock_print.assert_called_with('65261, TOO_HIGH')  # Match the integer value

    AlertTarget.send_alert('TO_EMAIL', 'TOO_LOW')
    mock_print.assert_any_call('To: a.b@c.com')
    mock_print.assert_any_call('Hi, the temperature is too low')

if __name__ == "__main__":
    unittest.main()

