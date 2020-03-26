alert_system = 'console' # other value can be 'email'
error_severity = 'critical' # other values : 'medium' or 'low'
error_message = 'OMG! Somthing terrible happend!'

if alert_system == 'console' :
    print(error_message) # 1
elif alert_system == 'email' :
    send_email('admin@example.com', error_message) # 2
    elif error_severity == 'medium' :
        send_email('support_1@example.com', error_severity) # 3
    else : 
        send_email('support_2@example.com', error_message) # 4