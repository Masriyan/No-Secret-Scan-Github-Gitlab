import re
import requests
from tqdm import tqdm

# Define your regular expressions for detecting secrets
SECRET_PATTERNS = [
    re.compile(r'AKIA[0-9A-Z]{16}'),  # AWS Access Key
    re.compile(r'(?i)secret(.{0,20})?[0-9a-zA-Z]{32,45}'),  # Generic secret
    re.compile(r'(?i)token(.{0,20})?[0-9a-zA-Z]{32,45}'),  # Generic token
    re.compile(r'(?i)password(.{0,20})?[0-9a-zA-Z]{8,}'),  # Generic password
    # Add more patterns as needed
]

def is_secret(line):
    """Check if a line contains a secret."""
    for pattern in SECRET_PATTERNS:
        if pattern.search(line):
            return True
    return False

def scan_github_repo(owner, repo, token):
    """Scan a GitHub repository for secrets."""
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/repos/{owner}/{repo}/contents'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    files = response.json()

    secrets_found = []

    for file in tqdm(files, desc="Scanning GitHub repo"):
        if file['type'] == 'file':
            file_response = requests.get(file['download_url'])
            file_response.raise_for_status()
            content = file_response.text.split('\n')
            for line in content:
                if is_secret(line):
                    secrets_found.append((file['path'], line))

    return secrets_found

def scan_gitlab_repo(owner, repo, token):
    """Scan a GitLab repository for secrets."""
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://gitlab.com/api/v4/projects/{owner}%2F{repo}/repository/tree'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    files = response.json()

    secrets_found = []

    for file in tqdm(files, desc="Scanning GitLab repo"):
        if file['type'] == 'blob':
            file_url = f"https://gitlab.com/api/v4/projects/{owner}%2F{repo}/repository/files/{file['path']}/raw?ref=master"
            file_response = requests.get(file_url, headers=headers)
            file_response.raise_for_status()
            content = file_response.text.split('\n')
            for line in content:
                if is_secret(line):
                    secrets_found.append((file['path'], line))

    return secrets_found

def get_repo_details():
    """Get repository details from the user."""
    print("Select repository type:")
    print("1. GitHub")
    print("2. GitLab")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return get_repo_details()
    
    repo_url = input("Enter the repository URL: ").strip()
    token = input("Enter your access token: ").strip()
    
    return choice, repo_url, token

def parse_repo_url(url):
    """Parse the repository URL to extract owner and repo name."""
    parts = url.rstrip('/').split('/')
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo

# Main function
if __name__ == "__main__":
    banner = """
    **************************************
    *                                    *
    *   No Secret Scan for GitHub &      *
    *       GitLab by sudo3rs            *
    *                                    *
    **************************************
    """
    print(banner)

    choice, repo_url, token = get_repo_details()
    owner, repo = parse_repo_url(repo_url)

    if choice == '1':
        print("Scanning GitHub repository...")
        secrets = scan_github_repo(owner, repo, token)
    else:
        print("Scanning GitLab repository...")
        secrets = scan_gitlab_repo(owner, repo, token)
    
    print(f"Found {len(secrets)} secrets in the repository.")
    for path, secret in secrets:
        print(f"File: {path}, Secret: {secret}")

