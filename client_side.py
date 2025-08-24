from SshToServer import SshToServer
import json
import pandas as pd
import os

# Enter the relevant details
PEM_FILE_PATH = ""
SERVER_SIDE_SCRIPT_PATH = ""
CSV_FILE_PATH = ""
HOST_IP = ""
HOST_USERNAME = ""
REMOTE_COMMAND = f"python3 {SERVER_SIDE_SCRIPT_PATH}"

def append_to_csv(file_path, data):
    df_new = pd.DataFrame([data])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_csv(file_path, index=False)

my_ssh = SshToServer(PEM_FILE_PATH, HOST_IP, HOST_USERNAME)
stdout, stderr = my_ssh.runRemoteCommand(REMOTE_COMMAND)
if stdout:
    stdout = json.loads(stdout)
    append_to_csv(CSV_FILE_PATH, stdout)
