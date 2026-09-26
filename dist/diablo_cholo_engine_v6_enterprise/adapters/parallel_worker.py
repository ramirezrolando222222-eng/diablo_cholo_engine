import json
import sys
import os
import time

ENGINE_DIR = os.path.expanduser("~/diablo_cholo_engine")
RIGHTS_FILE = os.path.join(ENGINE_DIR, "config/system_rights.json")

class ParallelWorkerEngine:
    def __init__(self, rights_path=RIGHTS_FILE):
        self.rights_path = rights_path
        self.rights = self._load_rights()

    def _load_rights(self):
        if os.path.exists(self.rights_path):
            with open(self.rights_path, "r") as f:
                return json.load(f)
        return {"system_rights": {"copyright_holder": "Rolando H Ramirez Jr"}}

    def process_job(self, job_payload):
        try:
            data = json.loads(job_payload) if isinstance(job_payload, str) else job_payload
        except Exception as e:
            return {
                "status": "ERROR",
                "error_type": "INVALID_JSON_INPUT",
                "details": str(e)
            }

        domain = data.get("domain", "ERROR_RECOVERY")
        tenant_id = data.get("tenant_id", "default_tenant")
        workspace_id = data.get("workspace_id", "default_ws")
        payload = data.get("payload", {})

        job_log = {
            "execution_id": data.get("execution_id", f"exec_{int(time.time())}"),
            "tenant_id": tenant_id,
            "workspace_id": workspace_id,
            "domain": domain,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "result": {}
        }

        # Domain Execution Routing Matrix
        if domain == "SYSTEM_EXECUTION":
            action = payload.get("action")
            bpm = payload.get("target_bpm", 80)
            job_log["result"] = {
                "action_executed": action,
                "target_bpm": bpm,
                "status": "SUCCESS"
            }
        elif domain == "LEAD_SCORE":
            score = payload.get("score", 0)
            job_log["result"] = {
                "lead_score": score,
                "qualification": "HIGH_PRIORITY" if score >= 80 else "STANDARD",
                "status": "ROUTED_TO_CRM"
            }
        elif domain == "CONTENT_ENGINE":
            job_log["result"] = {
                "published_platforms": payload.get("platform", "multi_channel"),
                "status": "QUEUED_FOR_PUBLISHING"
            }
        else:
            job_log["result"] = {
                "status": "HANDLED_BY_FALLBACK",
                "error_handler": "NO_MATCHING_DOMAIN"
            }

        # Save tenant-isolated execution log
        log_file = os.path.join(ENGINE_DIR, f"logs/{job_log['execution_id']}.json")
        with open(log_file, "w") as f:
            json.dump(job_log, f, indent=2)

        return job_log

if __name__ == "__main__":
    worker = ParallelWorkerEngine()
    input_str = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else '{"domain":"SYSTEM_EXECUTION","tenant_id":"tenant_01","workspace_id":"ws_01","payload":{"action":"rebajada_slow_down","target_bpm":80}}'
    output = worker.process_job(input_str)
    print(json.dumps(output, indent=2))
