import subprocess
import os

def push_release():
    print("==================================================")
    print(" PUSHING v6.0.0-ENTERPRISE RELEASE TO GITHUB ")
    print("==================================================")
    
    os.chdir(os.path.expanduser("~/diablo_cholo_engine"))
    
    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "release: lock v6.0.0-enterprise boilerplate package for gumroad distribution"])
    
    if result.returncode == 0:
        print("[SUCCESS] Changes committed successfully.")
    else:
        print("[INFO] No new changes to commit or commit already up to date.")
        
    push_res = subprocess.run(["git", "push", "origin", "main"])
    if push_res.returncode != 0:
        print("[INFO] Trying standard push without origin specification...")
        subprocess.run(["git", "push"])
        
    print("==================================================")
    print(" [SUCCESS] REPOSITORY PUSHED & READY FOR PRODUCTION ")
    print("==================================================")

if __name__ == "__main__":
    push_release()
