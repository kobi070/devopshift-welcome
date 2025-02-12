import subprocess

# Lab 1
def task1():
    command = "wsl ls -l /var/log".split()
    try:
        proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (output_str_stdout, output_str_stderr) = (proc.stdout.decode(), proc.stderr.decode())
        code = proc.returncode
        if(code == 0):
            print(f"Output:\n{output_str_stdout}")
        else:
            print(f"Error: {output_str_stderr}")
    except FileNotFoundError:
        print(f"File not found: {output_str_stdout}")
    except PermissionError:
        print(f"Permission denied: {output_str_stderr}")

# Lab2
def task2(service: str):
    command = f"wsl systemctl status {service}".split()
    try:
        proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (output_str_stdout, output_str_stderr) = (proc.stdout.decode(), proc.stderr.decode())
        code = proc.returncode
        if(code):
            if("running" in output_str_stdout):
                print(f"{service} is Running")
            else:
                print(f"{service} is not running trying to restart")
                command = "wsl systemctl start apache2".split()
                proc = subprocess.run(command, stderr=subprocess.PIPE)
                output_str_stderr = proc.stderr.decode()
                if proc.returncode:
                    print(f"Restarting {service} was successful !")
                else:
                    print(f"Failed to restart service: {service} - {output_str_stdout}")
        else:
            print(f"Error: {service} encountered an error")
    except FileNotFoundError:
        print(f"File not found: {output_str_stdout}")
    except PermissionError:
        print(f"Permission denied: {output_str_stderr}")

task2(service="apache2")