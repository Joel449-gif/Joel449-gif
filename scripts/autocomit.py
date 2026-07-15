#!/usr/bin/env python3
import random
import datetime
import subprocess
import os

def git_commit(message, timestamp):
    """Create a commit with specific timestamp."""
    with open("activity_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    
    subprocess.run(["git", "add", "activity_log.txt"], check=True)
    
    # Set commit date for realism
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = timestamp
    env["GIT_COMMITTER_DATE"] = timestamp
    
    subprocess.run(
        ["git", "commit", "-m", message],
        env=env,
        check=True
    )

def main():
    today = datetime.date.today()
    
    # Skip weekends (optional - remove if you want weekend commits)
    if today.weekday() >= 5:  # Saturday=5, Sunday=6
        print("Weekend detected. Skipping.")
        return
    
    # Randomize commit count (weighted for realism)
    # 40% chance of 0 commits (rest day), 60% chance of 1-4 commits
    num_commits = random.choices(
        [0, 1, 2, 3, 4],
        weights=[40, 30, 15, 10, 5],
        k=1
    )[0]
    
    if num_commits == 0:
        print("Rest day - no commits.")
        return
    
    print(f"Creating {num_commits} commits today.")
    
    # Realistic commit messages
    messages = [
        "fix: resolve edge case in validation logic",
        "docs: update API documentation",
        "refactor: improve error handling",
        "chore: update dependencies",
        "feat: add input sanitization",
        "fix: handle null pointer exception",
        "style: format code consistently",
        "test: add unit tests for utils",
        "perf: optimize database queries",
        "fix: correct timestamp formatting",
        "docs: clarify usage examples",
        "refactor: extract helper functions",
        "chore: clean up unused imports",
        "feat: implement caching layer",
        "fix: resolve race condition",
    ]
    
    # Create commits with random timestamps throughout the day
    now = datetime.datetime.now()
    base_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    
    for i in range(num_commits):
        # Random time between 9 AM and 6 PM
        random_hour = random.randint(9, 17)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)
        
        commit_time = base_time.replace(
            hour=random_hour,
            minute=random_minute,
            second=random_second
        )
        
        timestamp = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        message = random.choice(messages)
        
        git_commit(message, timestamp)
        print(f"Commit {i+1}/{num_commits}: {message}")

if __name__ == "__main__":
    main()
