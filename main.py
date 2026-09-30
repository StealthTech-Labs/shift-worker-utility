import csv
import os

# THE STEALTH TECH GROUP - COMPLETE ENTERPRISE CORE WITH ADVANCED REPORTING
class StealthTechMasterEngine:
    def __init__(self, business_name="The Stealth Tech Group"):
        self.company = business_name
        self.db_file = "billing_ledger.csv"
        self._initialize_database()
        print(f"=== {self.company} Unified Core with Advanced Reporting Engaged ===")

    def _initialize_database(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Client Name", "USD Amount", "Naira Total"])

    def process_and_log_transaction(self, client_name, usd_amount):
        if usd_amount <= 0:
            print("❌ ERROR: Security violation caught! Invalidation quarantined.")
            return False
            
        naira_total = usd_amount * 1650
        with open(self.db_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([client_name, f"${usd_amount}", f"₦{naira_total:,}"])
            
        print(f"✅ SUCCESS: Record for {client_name} safely written to disk database!")
        print(f"💰 Transformed: ${usd_amount} USD ---> ₦{naira_total:,} Naira")
        return True

    def generate_executive_revenue_report(self):
        print("\n📊 Compiling Global Financial Aggregates...")
        if not os.path.exists(self.db_file):
            print("⚠️ DATABASE EMPTY: No records found to aggregate.")
            return
            
        total_usd = 0
        record_count = 0
        
        with open(self.db_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row:
                    try:
                        usd_value = float(row[1].replace("$", "").replace(",", ""))
                        total_usd += usd_value
                        record_count += 1
                    except (ValueError, IndexError):
                        continue
                        
        print("--------------------------------------------------")
        print(f"📈 Total Agency Files Processed: {record_count}")
        print(f"💰 Cumulative System Revenue:   ${total_usd:,.2f} USD")
        print(f"🇳🇬 Equivalent Local Liquidity:  ₦{total_usd * 1650:,.2f} NGN")
        print("--------------------------------------------------")

def launch_executive_dashboard():
    engine = StealthTechMasterEngine()
    
    print("\n==================================================")
    print("🏢 SYSTEM ONLINE: THE STEALTH TECH GROUP CORE v1.5")
    print("==================================================")
    
    while True:
        print("\n[DASHBOARD MENU]")
        print("1. Process & Log New Transaction")
        print("2. Generate Executive Financial Report")
        print("3. Shut Down System Securely")
        
        user_choice = input("\nEnter selection (1-3): ")
        
        if user_choice == "1":
            client_name = input("Enter client name: ")
            try:
                amount = float(input("Enter transaction amount in USD ($): "))
                engine.process_and_log_transaction(client_name, amount)
            except ValueError:
                print("❌ ERROR: Invalid character input string.")
        elif user_choice == "2":
            engine.generate_executive_revenue_report()
        elif user_choice == "3":
            print("🔒 Closing database channels. Station secured.")
            break
        else:
            print("⚠️ INVALID SELECTION. Please try again.")

if __name__ == "__main__":
    launch_executive_dashboard()
