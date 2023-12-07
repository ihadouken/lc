#!/usr/bin/env python3
import subprocess

# Query changes in the repo
cmd = ['git', 'status', '-s']
output = subprocess.run(cmd, capture_output=True, text=True)
# One changed file per line
changes = output.stdout.splitlines()

for change in changes:
    # Only interested in new solutions
    if change.startswith('??'):
        # Extract problem info from filename
        filename = change.split(' ')[-1].removesuffix('\n')
        id, problem, ext = filename.split('.')

        # Find programming language of solution
        if ext == 'py':
            lang = 'Python'
        elif ext == 'java':
            lang = 'Java'
        elif ext == 'cpp':
            lang = 'C++'
        elif ext == 'c':
            lang = 'C'
        else:
            print(f'Unknown extension {ext} in {filename}. Skipping ...')
            continue

        # One commit for each new solution.
        cmd = f'git add {filename} && git commit -m "Add solution for #{id} in {lang}"'
        subprocess.run(cmd, shell=True)
