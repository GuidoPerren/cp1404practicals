#Constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


print("Electricity bill estimator 2.0")
tariff_number = int(input("Which tariff? 11 or 31: "))

#cents_per_kw = float(input("Enter cents per kWh: "))
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

if tariff_number == 11:
    estimated_bill = (number_of_billing_days * daily_use_in_kwh * (TARIFF_11 * 100)) / 100
    print(f"Estimated bill: ${estimated_bill:.2f}")
elif tariff_number == 31:
    estimated_bill = (number_of_billing_days * daily_use_in_kwh * (TARIFF_31 * 100)) / 100
    print(f"Estimated bill: ${estimated_bill:.2f}")
else:
    print(f"Invalid tariff!")
