import subprocess


def run_telnet_command(host, port, command, output_file):
    telnet_cmd = f"telnet {host} {port}"
    full_cmd = f'echo "{command}" | {telnet_cmd} > {output_file}'
    subprocess.call(full_cmd, shell=True)


# Przykładowe użycie
host = "google.com"
port = 23
command = "ls"
output_file = "output.txt"

run_telnet_command(host, port, command, output_file)
