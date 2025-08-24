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

def grep_lines_counter(keyword, path_to_file):
    try:
        return run_local_command(f'grep "{keyword}" {path_to_file} | wc -l')
    
    except Exception as e:
        return f"Error: {e}"

def main():
    data = {}
    info_count = grep_lines_counter("INFO", "/var/log/syslog")
    warn_count = grep_lines_counter("WARN", "/var/log/syslog")
    error_count = grep_lines_counter("ERROR", "/var/log/syslog")
    data["INFO"] = int(info_count[0])
    data["WARN"] = int(warn_count[0])
    data["ERROR"] = int(error_count[0])
    data["timestamp"] = int(time.time())
    data = json.dumps(data)
    print(data)
    #return data

if __name__ == "__main__":
    main()
