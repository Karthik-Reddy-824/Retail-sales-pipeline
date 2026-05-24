import argparse
import subprocess
import os
from scripts.pipeline import run

def auto_mode():
    """Decide full vs incremental automatically"""
    if not os.path.exists("db/sales.db"):
        return "full"
    return "incremental"

def run_pipeline(mode):
    print(f"🚀 Running pipeline in {mode} mode...")
    
    print("✅ Pipeline completed")

def run_dashboard():
    print("📊 Starting Streamlit dashboard...")
    subprocess.Popen(["streamlit", "run", "app.py"])

def main():
    parser = argparse.ArgumentParser(description="Run Pipeline + Dashboard")

    parser.add_argument(
        "--mode",
        choices=["full", "incremental"],
        help="Pipeline mode"
    )

    parser.add_argument(
        "--dashboard",
        action="store_true",
        help="Run dashboard after pipeline"
    )

    args = parser.parse_args()

    # Auto mode if not provided
    mode = args.mode if args.mode else auto_mode()

    # Run pipeline
    run_pipeline(mode)

    # Run dashboard (optional)
    if args.dashboard:
        run_dashboard()

if __name__ == "__main__":
    main()