import csv
import os

# THE STEALTH TECH GROUP - COMPLETE ENTERPRISE CORE v6.0 (WITH BUSINESS ANALYTICS)
class StealthTechUltimateEngine:
    def __init__(self, business_name="The Stealth Tech Group"):
        self.company = business_name
        self.db_file = "billing_ledger.csv"
        self.geegpay_usd_vault = 0.00
        self._initialize_database()
        print(f"=== {self.company} Master Core v6.0 Online ===")

    def _initialize_database(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Client Name", "USD Amount", "Naira Total"])

    def remove_duplicate_records(self, raw_data_list):
        unique_records = []
        duplicate_count = 0
        for record in raw_data_list:
            if record in unique_records:
                duplicate_count += 1
            else:
                unique_records.append(record)
        return unique_records, duplicate_count

    def generate_executive_analytics(self, total_ingested, duplicates, malformed):
        clean_retained = total_ingested - (duplicates + malformed)
        purity_rate = (clean_retained / total_ingested) * 100
        
        print("\n==================================================================")
        print(f"📊 EXECUTIVE PERFORMANCE BRIEF - {self.company.upper()}")
        print("==================================================================")
        print(f"📥 Total Data Rows Ingested:    {total_ingested} Records")
        print(f"🧹 Corrupted Elements Cleaned:  {duplicates + malformed} Files")
        print(f"✅ Pristine Records Exported:   {clean_retained} Nodes")
        print(f"📈 Database Yield Purity Rate:  {purity_rate:.2f}%")
        print("==================================================================")
        return clean_retained

def launch_executive_dashboard():
    engine = StealthTechUltimateEngine()
    print("\n==================================================")
    print("🏢 SYSTEM ONLINE: THE STEALTH TECH GROUP CORE v6.0")
    print("==================================================")
    
    while True:
        print("\n[DASHBOARD MENU]")
        print("1. Run Bulk Data Process & Generate Analytics Summary")
        print("2. Close Corporate Channels Securely")
        
        user_choice = input("\nEnter selection (1-2): ")
        if user_choice == "1":
            try:
                total = int(input("Enter total raw records count: "))
                dups = int(input("Enter duplicate rows count found: "))
                bad_mail = int(input("Enter malformed emails count found: "))
                engine.generate_executive_analytics(total, dups, bad_mail)
            except ValueError:
                print("❌ ERROR: Invalid entry string integer.")
        elif user_choice == "2":
            print("🔒 Closing database channels. Station secured.")
            break

if __name__ == "__main__":
    launch_executive_dashboard()
