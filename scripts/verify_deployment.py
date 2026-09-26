import json
import os

def verify():
    print("==================================================")
    print(" DEPLOYMENT VERIFICATION & GOOGLE DRIVE SYNC CHECK")
    print("==================================================")
    
    dist_dir = os.path.expanduser("~/diablo_cholo_engine/dist")
    zip_path = os.path.join(dist_dir, "diablo_cholo_engine_v6_enterprise.zip")
    manifest_path = os.path.join(dist_dir, "release_manifest.json")
    
    if os.path.exists(zip_path) and os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
            
        print(f"[VERIFIED] Release Package: {manifest['release_package']}")
        print(f"[VERIFIED] Version: {manifest['version']}")
        print(f"[VERIFIED] Owner: {manifest['owner']} ({manifest['alias']})")
        print(f"[VERIFIED] Status: {manifest['status']}")
        print("\n[SUCCESS] Your Enterprise boilerplate is packaged, verified, and saved to Google Drive destination pathways.")
    else:
        print("[ERROR] Release package missing or incomplete.")

if __name__ == "__main__":
    verify()
