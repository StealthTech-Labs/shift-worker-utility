import csv
import os

# THE STEALTH TECH GROUP - UNIFIED MASTER ENTERPRISE CORE v4.0 (GEEGPAY NODE)
class StealthTechUltimateEngine:
    def __init__(self, business_name="The Stealth Tech Group"):
        self.company = business_name
        self.db_file = "billing_ledger.csv"
        # Primary Treasury Wallet (Replicating the Dangote Offshore Model)
        self.geegpay_usd_vault = 0.00
        self._initialize_database()
        print(f"=== {self.company} Master Core v4.0 engaged ===")

    def _initialize_database(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Client Name", "USD Amount", "Naira Total"])

    def process_and_settle_to_geegpay(self, client_name, usd_amount):
        if usd_amount <= 0:
            print("❌ SECURITY ERROR: Negative or zero validation anomaly quarantined.")
            return None
            
        # Settle funds directly into the offshore USD wallet vault
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

    def generate_client_email_receipt(self, client_name, usd_amount, naira_total):
        email_template = f"""
======================================================================
📧 OUTBOUND DISPATCH: THE STEALTH TECH GROUP OPERATIONS DESK
======================================================================
To: Operations Director <contact@clientagency.com>
Subject: Verification Complete - Audit Ledger Account: {client_name}

Dear Partner,

Our data engineering systems have successfully processed your weekly 
contract logs with 100% precision. 

Your verified ledger statistics are formatted below:
----------------------------------------------------------------------
💼 Client Account Node:        {client_name}
📊 Raw Ingestion Volume:       ${usd_amount:,.2f} USD
🇳🇬 Consolidated Local Value:   ₦{naira_total:,} NGN
----------------------------------------------------------------------
Status: 100% Secure. Settled to Branded Geegpay Corporate USD Vault.

A portion of our net profit overflow from this transaction is routed 
to local orphanage infrastructure updates via The Stealth Tech Foundation.
You can monitor our open-source codebase storefront live on the web:
👉 ://github.com

Thank you for your partnership.

Sincerely,
Operations Desk
The Stealth Tech Group
======================================================================
"""
        print(email_template)
        return email_template

def launch_executive_dashboard():
    engine = StealthTechUltimateEngine()
    print("\n==================================================")
    print("🏢 SYSTEM ONLINE: THE STEALTH TECH GROUP CORE v4.0")
    print("==================================================")
    
    while True:
        print("\n[DASHBOARD MENU]")
        print("1. Ingest Transaction & Route to Geegpay USD Wallet")
        print("2. Close Corporate Channels Securely")
        
        user_choice = input("\nEnter selection (1-2): ")
        if user_choice == "1":
            client_name = input("Enter client name: ")
            try:
                amount = float(input("Enter transaction amount in USD ($): "))
                naira_result = engine.process_and_settle_to_geegpay(client_name, amount)
                if naira_result:
                    engine.generate_client_email_receipt(client_name, amount, naira_result)
            except ValueError:
                print("❌ ERROR: Invalid character input string.")
        elif user_choice == "2":
            print("🔒 Closing database channels. Station secured.")
            break

if __name__ == "__main__":
    launch_executive_dashboard()
