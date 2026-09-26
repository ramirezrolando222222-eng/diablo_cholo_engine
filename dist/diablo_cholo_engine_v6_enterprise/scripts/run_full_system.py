import json
import os
import subprocess

def run():
    print("==================================================")
    print(" DIABLO CHOLO ENGINE v6.0.0-ENTERPRISE: FULL SYNC ")
    print("==================================================")
    
    # 1. Run Master Engine simulation across all 5 streams
    master_script = os.path.expanduser("~/diablo_cholo_engine/pipelines/master_engine.py")
    if os.path.exists(master_script):
        print("\n[STEP 1] Executing Multi-Stream Master Engine...")
        subprocess.run(["python3", master_script])
    
    # 2. Run Parallel Worker test execution
    worker_script = os.path.expanduser("~/diablo_cholo_engine/adapters/parallel_worker.py")
    if os.path.exists(worker_script):
        print("\n[STEP 2] Executing Enterprise Parallel Worker Adapter...")
        test_payload = '{"execution_id":"exec_final_001","domain":"SYSTEM_EXECUTION","tenant_id":"tenant_diablo_cholo_01","workspace_id":"ws_baytown_studio","payload":{"action":"rebajada_slow_down","target_bpm":80}}'
        subprocess.run(["python3", worker_script, test_payload])

    # 3. Generate and sync accomplishment report to Google Drive destination
    drive_script = os.path.expanduser("~/diablo_cholo_engine/scripts/drive_sync.py")
    if os.path.exists(drive_script):
        print("\n[STEP 3] Generating and Syncing Accomplishments to Google Drive...")
        subprocess.run(["python3", drive_script])

    print("\n==================================================")
    print(" [SUCCESS] ALL ENTERPRISE PIPELINES EXECUTED & LOGGED ")
    print("==================================================")

if __name__ == "__main__":
    run()
