import json, sys

ENGINE_SPEC = '''
{
  "brain_engine": {
    "version": "2.1.0",
    "architecture": "vibe_coding_core",
    "artist_profile": {
      "alias": "Diablo Cholo",
      "legal_name": "Rolando H. Ramirez Jr.",
      "origin": "Baytown/Houston, TX",
      "sonic_identity": ["cholo_rap", "cumbia_rebajada", "chopped_and_screwed"]
    },
    "runtime": {
      "mode": "silent_execution",
      "tts_talking": false,
      "audio_pipeline": {
        "transcription": "whisper_stt",
        "pitch_shift_algorithm": "rebajada_slow_down",
        "bpm_target": 80
      },
      "hud_overlay": {
        "active": true,
        "theme": "matrix_dark",
        "bg_color": "#000000",
        "text_color": "#00FF00"
      },
      "targets": ["local_disk", "youtube_studio"]
    }
  }
}
'''

class VibeEngine:
    def __init__(self, raw_json):
        self.state = json.loads(raw_json)["brain_engine"]

    def execute(self):
        artist = self.state["artist_profile"]
        runtime = self.state["runtime"]

        with open("brain_engine.json", "w") as f:
            json.dump(self.state, f, indent=2)

        sys.stdout.write(f"\n[+] VIBE ENGINE CORE ACTIVE v{self.state['version']}\n")
        sys.stdout.write(f"[+] ARTIST: {artist['alias']} ({artist['origin']})\n")
        sys.stdout.write(f"[+] SOUND: {', '.join(artist['sonic_identity'])}\n")
        sys.stdout.write(f"[+] TTS TALK: {runtime['tts_talking']}\n")
        sys.stdout.write(f"[+] HUD CONFIG: {runtime['hud_overlay']['theme']} ({runtime['hud_overlay']['text_color']})\n")
        sys.stdout.write(f"[+] PIPELINE TARGET: {runtime['audio_pipeline']['pitch_shift_algorithm']} @ {runtime['audio_pipeline']['bpm_target']} BPM\n")
        sys.stdout.write(f"[+] STATE LOADED: brain_engine.json ready\n\n")

if __name__ == "__main__":
    VibeEngine(ENGINE_SPEC).execute()
