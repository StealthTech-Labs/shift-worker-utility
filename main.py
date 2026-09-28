# THE STEALTH TECH GROUP - MULTI-CURRENCY DATA ENTRY UTILITY
def calculate_shift_invoice(hours_worked, hourly_rate, currency="USD"):
    guaranteed_hours = 40
    overtime_threshold = 45
    
    # Calculate regular and protected hours
    if hours_worked < guaranteed_hours:
        processed_hours = guaranteed_hours
        status = "Guaranteed Base Hours Enforced"
    elif hours_worked > overtime_threshold:
        regular_hours = overtime_threshold
        overtime_hours = hours_worked - overtime_threshold
        return {
            "Total Due": (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5),
            "Currency": currency,
            "Status": f"Overtime Enforced (+{overtime_hours} hrs)"
        }
    else:
        processed_hours = hours_worked
        status = "Standard Hours Processed"
        
    return {
        "Total Due": processed_hours * hourly_rate,
        "Currency": currency,
        "Status": status
    }

print("=== StealthTech Data Processing Engine Online ===")
