import os
import shutil
import json

def package_release():
    print("==================================================")
    print(" PACKAGING DIABLO CHOLO ENGINE v6.0.0-ENTERPRISE ")
    print("==================================================")
    
    base_dir = os.path.expanduser("~/diablo_cholo_engine")
    dist_dir = os.path.join(base_dir, "dist")
    os.makedirs(dist_dir, exist_ok=True)
    
    archive_name = "diablo_cholo_engine_v6_enterprise"
    archive_path = os.path.join(dist_dir, archive_name)
    
    # Create a clean release folder structure
    release_src = os.path.join(dist_dir, archive_name)
    if os.path.exists(release_src):
        shutil.rmtree(release_src)
    os.makedirs(release_src)
    
    # Folders to copy
    folders_to_copy = ["vault", "config", "adapters", "pipelines", "scripts"]
    for folder in folders_to_copy:
        src_folder = os.path.join(base_dir, folder)
        if os.path.exists(src_folder):
            shutil.copytree(src_folder, os.path.join(release_src, folder))
            print(f" -> Packed folder: {folder}")
            
    # Create a distribution ZIP
    shutil.make_archive(archive_path, 'zip', release_src)
    print(f"\n[SUCCESS] Enterprise release package created at: {archive_path}.zip")
    
    # Output manifest
    manifest = {
        "release_package": f"{archive_name}.zip",
        "version": "6.0.0-ENTERPRISE",
        "owner": "Rolando H Ramirez Jr",
        "alias": "Diablo Cholo",
        "status": "READY_FOR_GUMROAD_UPLOAD"
    }
    
    manifest_path = os.path.join(dist_dir, "release_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"[SUCCESS] Release manifest written to: {manifest_path}")

if __name__ == "__main__":
    package_release()
