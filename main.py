import csv
import os

# THE STEALTH TECH GROUP - COMPLETE ENTERPRISE CORE v5.0 (WITH DATA DEDUPLICATION)
class StealthTechUltimateEngine:
    def __init__(self, business_name="The Stealth Tech Group"):
        self.company = business_name
        self.db_file = "billing_ledger.csv"
        self.geegpay_usd_vault = 0.00
        self._initialize_database()
        print(f"=== {self.company} Master Core v5.0 Online ===")

    def _initialize_database(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Client Name", "USD Amount", "Naira Total"])

    def remove_duplicate_records(self, raw_data_list):
        print("🧹 [DEDUPLICATION] Initializing Database Deduplication Scan...")
        unique_records = []
        duplicate_count = 0
        for record in raw_data_list:
            if record in unique_records:
                duplicate_count += 1
            else:
                unique_records.append(record)
        print(f"✅ Clean Complete: Removed {duplicate_count} duplicate files.")
        return unique_records

    def process_and_settle_to_geegpay(self, client_name, usd_amount):
        if usd_amount <= 0:
            print("❌ SECURITY ERROR: Negative or zero validation anomaly quarantined.")
            return None
            
        self.geegpay_usd_vault += usd_amount
        naira_equivalent = usd_amount * 1650
        
        with open(self.db_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([client_name, f"${usd_amount}", f"₦{naira_equivalent:,}"])
            
        print("\n==================================================")
        print("🔒 GEEGPAY OFFSHORE ROUTING MATRIX ACTIVE")
        print(f"💼 Source Client:        {client_name}")
        print(f"📥 Settled Asset Ledger:  ${usd_amount:,.2f} USD")
        print(f"📈 Total Wallet Reserves: ${self.geegpay_usd_vault:,.2f} USD")
        print("==================================================")
        return naira_equivalent

def launch_executive_dashboard():
    engine = StealthTechUltimateEngine()
    print("\n==================================================")
    print("🏢 SYSTEM ONLINE: THE STEALTH TECH GROUP CORE v5.0")
    print("==================================================")
    
    while True:
        print("\n[DASHBOARD MENU]")
        print("1. Process New Transaction to Geegpay USD Wallet")
        print("2. Run Bulk Data Deduplication Clean")
        print("3. Close Corporate Channels Securely")
        
        user_choice = input("\nEnter selection (1-3): ")
        if user_choice == "1":
            client_name = input("Enter client name: ")
            try:
                amount = float(input("Enter transaction amount in USD ($): "))
                engine.process_and_settle_to_geegpay(client_name, amount)
            except ValueError:
                print("❌ ERROR: Invalid character input string.")
        elif user_choice == "2":
            # Running a live test array of messy client records
            test_list = ["info@ukshop.com", "sales@london.com", "info@ukshop.com", "admin@scot.com"]
            engine.remove_duplicate_records(test_list)
        elif user_choice == "3":
            print("🔒 Closing database channels. Station secured.")
            break

if __name__ == "__main__":
    launch_executive_dashboard()
