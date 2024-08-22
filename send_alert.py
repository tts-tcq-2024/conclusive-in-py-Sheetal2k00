def send_alert_to_controller(message):
    print(f"Sending to controller: {message}")

def send_alert_via_email(message):
    print(f"Sending email: {message}")

def send_alert(alert_target, alert_message):
    alert_methods = {
        "CONTROLLER": send_alert_to_controller,
        "EMAIL": send_alert_via_email,
    }
    alert_method = alert_methods.get(alert_target, lambda msg: print(f"Unknown alert target: {msg}"))
    alert_method(alert_message)
