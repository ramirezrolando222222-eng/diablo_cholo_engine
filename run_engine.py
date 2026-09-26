import sys
from brain import EngineXBrain

ENGINE_SPEC = {
    "engine_name": "VibeEngine Core X",
    "version": "3.0.0-X"
}

class VibeEngine:
    def __init__(self, spec):
        self.spec = spec
        self.brain = EngineXBrain()

    def execute(self):
        artist = self.brain.state["artist_profile"]
        pipeline = self.brain.state["runtime"]["audio_pipeline"]
        
        sys.stdout.write(f"\n[+] {self.spec['engine_name']} ONLINE v{self.spec['version']}\n")
        sys.stdout.write(f"[+] ARTIST: {artist['alias']} ({artist['origin']})\n")
        sys.stdout.write(f"[+] SOUND MATRIX: {', '.join(artist['sonic_identity'])}\n")
        sys.stdout.write(f"[+] PIPELINE TARGET: {pipeline['pitch_shift_algorithm']} @ {pipeline['bpm_target']} BPM\n")
        sys.stdout.write(f"[+] MINI-ALGOS: Dynamic Pitch Ratio & Auto-Tagging Matrix Ready\n\n")

if __name__ == "__main__":
    VibeEngine(ENGINE_SPEC).execute()
