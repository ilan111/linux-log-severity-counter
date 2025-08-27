import subprocess
import time
import json

def run_local_command(command):
    try:
        # Run the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr

    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error output: {e.stderr}")

def main():
    data = {}
    info_count = 0
    warn_count = 0
    error_count = 0
    with open("/var/log/syslog", "r") as log:
        for line in log:
            if "INFO" in line:
                info_count += 1
            elif "WARN" in line:
                warn_count += 1
            elif "ERROR" in line:
                error_count += 1

    data["INFO"] = info_count
    data["WARN"] = warn_count
    data["ERROR"] = error_count
    data["timestamp"] = int(time.time())
    data = json.dumps(data)
    print(data)

if __name__ == "__main__":
    main()
