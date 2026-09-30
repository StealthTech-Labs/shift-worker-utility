# THE STEALTH TECH GROUP - COMPLETE ENTERPRISE PROCESSING CORE
class StealthTechMasterEngine:
    def __init__(self, business_name="The Stealth Tech Group"):
        self.company = business_name
        print(f"=== {self.company} Unified System Core Engaged ===")

    def process_weekly_agency_batch(self, raw_data_stream):
        print("🛡️ Step 1: Initializing Security Data Integrity Scan...")
        clean_records = []
        flagged_errors = []
        
        for record in raw_data_stream:
            if record <= 0:
                flagged_errors.append(record)
            else:
                clean_records.append(record)
                
        print("🚀 Step 2: Processing Valid Files Through Multi-Currency Loops...")
        for amount in clean_records:
            naira_total = amount * 1650
            print(f"💰 Processed Transaction: ${amount} USD ---> ₦{naira_total:,} Naira")
            
        return {
            "Status": "Batch Processing 100% Successful",
            "Secure Records Logged": len(clean_records),
            "Security Threats Neutralized": len(flagged_errors)
        }

# Initializing Master Core
if __name__ == "__main__":
    engine = StealthTechMasterEngine()
    test_stream = [100, 250, -50, 400, 0]
    results = engine.process_weekly_agency_batch(test_stream)
    print(results)

# THE STEALTH TECH GROUP - INTERACTIVE USER DASHBOARD
def launch_executive_dashboard():
    print("\n==================================================")
    print("🏢 SYSTEM ONLINE: THE STEALTH TECH GROUP CORE v1.0")
    print("==================================================")
    
    while True:
        print("\n[DASHBOARD MENU]")
        print("1. Process New Weekly Transaction")
        print("2. Shut Down System Securely")
        
        user_choice = input("\nEnter selection (1-2): ")
        
        if user_choice == "1":
            try:
                amount = float(input("Enter transaction amount in USD ($): "))
                if amount <= 0:
                    print("❌ ERROR: Security violation caught! Invalidation quarantined.")
                else:
                    naira_total = amount * 1650
                    print(f"✅ SUCCESS: Processed ${amount} USD ---> ₦{naira_total:,} Naira")
            except ValueError:
                print("❌ ERROR: Invalid character input string.")
        elif user_choice == "2":
            print("🔒 Closing dashboard channels. Station secured.")
            break
        else:
            print("⚠️ INVALID SELECTION. Please try again.")

# Active System Trigger Configuration
if __name__ == "__main__":
    launch_executive_dashboard()

