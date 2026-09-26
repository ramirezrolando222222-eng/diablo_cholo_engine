import json
import os

VAULT_PATH = os.path.expanduser("~/diablo_cholo_engine/vault/vault.json")

def load_vault():
    with open(VAULT_PATH, "r") as f:
        return json.load(f)

def route_job(job):
    domain = job.get("domain")
    payload = job.get("payload", {})
    
    print(f"\n[ORCHESTRATOR] Processing Domain: {domain}")
    
    if domain == "LEAD_SCORE":
        # Revenue Stream 1 & 2: Speed-to-Lead / High-Ticket Agency Prospecting
        company = payload.get("company", "Unknown")
        budget = payload.get("budget", "$0")
        score = payload.get("score", 0)
        print(f" -> [MONETIZATION] Speed-to-Lead Alert! Company: {company} | Budget: {budget} | Score: {score}")
        if score >= 80:
            print(" -> [ACTION] Triggering immediate high-priority SMS/CRM sync for high-ticket close.")

    elif domain == "CONTENT_ENGINE":
        # Revenue Stream 3: Automated Content Syndication / Personal Brand Growth
        platform = payload.get("platform", "general")
        print(f" -> [MONETIZATION] Generating platform-tailored copy for: {platform}")
        print(f" -> [ACTION] Pushing to Buffer/Social APIs for automated organic traffic & monetization.")

    elif domain == "INVOICE_PARSER":
        # Revenue Stream 4: Automated Bookkeeping / Receipt Processing Service
        vendor = payload.get("vendor", "Unknown Vendor")
        total = payload.get("total", 0.00)
        print(f" -> [MONETIZATION] Bookkeeping Automation parsed invoice from {vendor} for ${total}")
        print(f" -> [ACTION] Syncing line items to client QuickBooks / Google Sheets ledger.")

    elif domain == "SYSTEM_EXECUTION":
        # Revenue Stream 5: Automated Audio / Remix Production Service
        action = payload.get("action", "unknown")
        print(f" -> [MONETIZATION] Executing local Python/Sox routine: {action}")
        print(f" -> [ACTION] Processing digital audio product delivery for client/marketplace.")

    else:
        print(f" -> [ERROR_RECOVERY] Routing unhandled payload to Dead-Letter Queue.")

if __name__ == "__main__":
    vault = load_vault()
    print(f"Loaded Vault for: {vault['vault_meta']['owner']} ({vault['vault_meta']['alias']})")
    
    # Simulation of a multi-stream inbound batch
    sample_batch = [
        {"domain": "LEAD_SCORE", "payload": {"company": "Acme Corp", "budget": "$15,000", "score": 95}},
        {"domain": "INVOICE_PARSER", "payload": {"vendor": "Studio Supply Co", "total": 450.00}},
        {"domain": "SYSTEM_EXECUTION", "payload": {"action": "rebajada_slow_down", "target_bpm": 80}}
    ]
    
    for job in sample_batch:
        route_job(job)
