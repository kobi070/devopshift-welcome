import subprocess

print("Before running")
p = subprocess.run(["wsl", "ls", "-a", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("After running")

(output_bytes_stdout, output_bytes_stderr) = (p.stdout, p.stderr)
(output_str_stdout, output_bytes_stderr) = (output_bytes_stdout.decode(), output_bytes_stderr.decode())
print(f"Output stdout:\n{output_str_stdout}")
print(f"Output stderr:\n{output_bytes_stderr}")

print(f"p code {p.returncode}\n")

print("Before running p1")
p1 = subprocess.Popen(["wsl", "ls", "-a", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE);
p1.wait()
# p1.kill()
print("After running p1")