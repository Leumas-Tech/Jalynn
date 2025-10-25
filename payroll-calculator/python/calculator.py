import json
import os

def calculate_payroll():
    """
    This function calculates an employee's payroll based on a config file.
    """
    default_tax_rates = {
        "fedTaxRate": 0.15,
        "stateTaxRate": 0.05,
        "SSTaxRate": 0.062
    }

    try:
        # Correctly construct the path to config.json relative to the script
        script_dir = os.path.dirname(__file__)
        config_path = os.path.join(script_dir, '..', 'config.json')

        with open(config_path, 'r') as f:
            tax_rates = json.load(f)
    except FileNotFoundError:
        tax_rates = default_tax_rates

    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))

        gross_pay = hours_worked * hourly_rate
        fed_amount = gross_pay * tax_rates['fedTaxRate']
        state_amount = gross_pay * tax_rates['stateTaxRate']
        ss_amount = gross_pay * tax_rates['SSTaxRate']
        net_pay = gross_pay - fed_amount - state_amount - ss_amount

        print(f"\nGross Pay: ${gross_pay:.2f}")
        print(f"Federal Tax: ${fed_amount:.2f}")
        print(f"State Tax: ${state_amount:.2f}")
        print(f"Social Security: ${ss_amount:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")

    except ValueError:
        print("\nPlease enter valid numbers for hours worked and hourly rate.")

if __name__ == "__main__":
    calculate_payroll()