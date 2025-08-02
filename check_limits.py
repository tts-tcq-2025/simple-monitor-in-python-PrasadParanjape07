def is_within_range(value, min_value, max_value, parameter_name):
    if not (min_value <= value <= max_value):
        print(f'{parameter_name} is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (
        is_within_range(temperature, 0, 45, 'Temperature') and
        is_within_range(soc, 20, 80, 'State of Charge') and
        is_within_range(charge_rate, 0, 0.8, 'Charge rate')
    )

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
