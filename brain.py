import json
import os
import sys
from datetime import datetime

STATE_FILE = "brain_engine.json"

class EngineXBrain:
    def __init__(self, state_path=STATE_FILE):
        self.state_path = state_path
        self.state = self._load()

    def _load(self):
        if not os.path.exists(self.state_path):
            sys.stderr.write(f"[!] Critical: {self.state_path} missing.\n")
            sys.exit(1)
        with open(self.state_path, "r") as f:
            return json.load(f)

    def _sync(self):
        with open(self.state_path, "w") as f:
            json.dump(self.state, f, indent=2)

    def calc_pitch_ratio(self, input_bpm: float) -> float:
        """Mini-Algo 1: Pitch/Tempo Shift Ratio"""
        target_bpm = self.state["runtime"]["audio_pipeline"]["bpm_target"]
        if input_bpm <= 0:
            return 1.0
        ratio = round(target_bpm / input_bpm, 4)
        return ratio

    def infer_tags(self, text: str) -> list:
        """Mini-Algo 2: Semantic Auto-Tagging Matrix"""
        text_lower = text.lower()
        matched_tags = []
        rules = self.state.get("mini_algorithms", {}).get("auto_tagger", {})
        
        for genre, keywords in rules.items():
            if any(kw in text_lower for kw in keywords):
                matched_tags.append(genre)
                
        return matched_tags if matched_tags else ["unclassified"]

    def process_track(self, title: str, original_bpm: float):
        """Mini-Algo 3: Track Processing Pipeline Execution"""
        ratio = self.calc_pitch_ratio(original_bpm)
        tags = self.infer_tags(title)
        
        record = {
            "timestamp": datetime.now().isoformat(),
            "title": title,
            "original_bpm": original_bpm,
            "target_bpm": self.state["runtime"]["audio_pipeline"]["bpm_target"],
            "speed_ratio": ratio,
            "tags": tags
        }
        
        self.state["memory_vault"].append(record)
        self._sync()
        return record

if __name__ == "__main__":
    brain = EngineXBrain()
    
    # Example execution via CLI args or default test track
    track_title = sys.argv[1] if len(sys.argv) > 1 else "Houston Baytown Screw Cumbia"
    in_bpm = float(sys.argv[2]) if len(sys.argv) > 2 else 105.0
    
    res = brain.process_track(track_title, in_bpm)
    print(f"\n[ENGINE X BRAIN PROCESSOR]")
    print(f" Track       : {res['title']}")
    print(f" Speed Ratio : {res['speed_ratio']}x ({res['original_bpm']} -> {res['target_bpm']} BPM)")
    print(f" Inferred    : {', '.join(res['tags'])}")
    print(f" State Sync  : brain_engine.json updated\n")
