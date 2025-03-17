![No Secret Scan Banner](https://github.com/Masriyan/No-Secret-Scan-Github-Gitlab/blob/main/banner.png?raw=true)                                                                                                                          
# No Secret Scan for GitHub & GitLab by sudo3rs
## Overview
No Secret Scan is a Python script designed to scan GitHub and GitLab repositories for potential secrets such as API keys, tokens, passwords, and more. The script uses regular expressions to identify these secrets within the repository files and provides a comprehensive report of any findings.

## Features
1. Supports GitHub and GitLab: Choose between scanning a GitHub or GitLab repository.
2. Customizable Secret Patterns: Define your own regular expressions to identify specific types of secrets.
3. Progress Indicator: See the progress of the scan in real-time using the tqdm library.
4. etailed Report: Get a detailed report of all found secrets, including the file path and the secret itself.

## Usage
1. Clone the repository:
-- git clone [https://github.com/Masriyan/no-secret-scan.git](https://github.com/Masriyan/No-Secret-Scan-Github-Gitlab.git)
-- cd no-secret-scan

2. Install the required libraries:
-- pip install requests tqdm

3. Run the script:
-- python no_secret_scan.py

4. Follow the prompts:
-- Select the repository type (GitHub or GitLab).
-- Enter the URL of the repository you want to scan.
-- Provide your access token.

## Example
![No Secret Scan Banner](https://github.com/Masriyan/No-Secret-Scan-Github-Gitlab/blob/main/Screenshot%202024-07-16%20093855.png?raw=true)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/awesome-feature).
3. Commit your changes (git commit -m 'Add some awesome feature').
4. Push to the branch (git push origin feature/awesome-feature).
5. Open a pull request.

## Acknowledgments
-- Inspired by various secret scanning tools and methodologies.
