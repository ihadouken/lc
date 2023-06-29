import subprocess

cmd = ['git', 'status', '-s']
output = subprocess.run(cmd, capture_output=True, text=True)
changes = output.stdout.splitlines()

for change in changes:
    if change.startswith('??'):
        fname = change.split(' ')[-1].removesuffix('\n')
        id, pname, ext = fname.split('.')

        if ext == 'py':
            lang = 'Python'
        elif ext == 'java':
            lang = 'Java'
        elif ext == 'cpp':
            lang = 'C++'
        elif ext == 'c':
            lang = 'C'
        else:
            print(f'Unknown extension {ext} in {fname}. Skipping ...')
            continue

        cmd = f'git add {fname} && git commit -m "Add solution for #{id} in {lang}"'
        subprocess.run(cmd, shell=True)
