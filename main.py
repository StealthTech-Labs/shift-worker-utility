import csv
import os

# THE STEALTH TECH GROUP - INDUSTRIAL CORE WITH PERSISTENT STORAGE
class StealthTechMasterEngine:
    def __init__(self, business_name="The Stealth Tech Group"):
        self.company = business_name
        self.db_file = "billing_ledger.csv"
        self._initialize_database()
        print(f"=== {self.company} Unified Core with Storage Engaged ===")

    def _initialize_database(self):
        # Creates the spreadsheet file with headers if it does not exist yet
        if not os.path.exists(self.db_file):
            with open(self.db_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Client Name", "USD Amount", "Naira Total"])

    def process_and_log_transaction(self, client_name, usd_amount):
        print("🛡️ Initializing Security Data Integrity Scan...")
        if usd_amount <= 0:
            print("❌ ERROR: Security violation caught! Invalidation quarantined.")
            return False
            
        print("🚀 Processing Valid Files Through Multi-Currency Multipliers...")
        naira_total = usd_amount * 1650
        
        print("💾 Accessing Persistent Storage Ledger...")
        with open(self.db_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([client_name, f"${usd_amount}", f"₦{naira_total:,}"])
            
        print(f"✅ SUCCESS: Record for {client_name} safely written to disk database!")
        print(f"💰 Transformed: ${usd_amount} USD ---> ₦{naira_total:,} Naira")
        return True

def launch_executive_dashboard():
    engine = StealthTechMasterEngine()
    
    print("\n==================================================")
    print("🏢 SYSTEM ONLINE: THE STEALTH TECH GROUP CORE v1.2")
    print("==================================================")
    
    while True:
        print("\n[DASHBOARD MENU]")
        print("1. Process & Log New Transaction")
        print("2. Shut Down System Securely")
        
        user_choice = input("\nEnter selection (1-2): ")
        
        if user_choice == "1":
            client_name = input("Enter client name: ")
            try:
                amount = float(input("Enter transaction amount in USD ($): "))
                engine.process_and_log_transaction(client_name, amount)
            except ValueError:
                print("❌ ERROR: Invalid character input string.")
        elif user_choice == "2":
            print("🔒 Closing database channels. Station secured.")
            break
        else:
            print("⚠️ INVALID SELECTION. Please try again.")

if __name__ == "__main__":
    launch_executive_dashboard()
