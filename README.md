
# Google Dork Scanner

A Python-based **Google Dork Scanner** that allows you to automate advanced Google searches using custom queries. This tool is designed for ethical purposes to identify potential vulnerabilities or publicly accessible information on web servers.

---

## Features

- **Interactive Console**: Enter your Google dork queries and number of results directly in the terminal.
- **Customizable Output**: Saves only the links from search results in a simple text file.
- **User-Friendly Design**: Includes a colorized banner and prompts for a smooth user experience.
- **Ethical Scanning**: Designed for penetration testing and security auditing purposes with user responsibility in mind.

---

## Banner

The tool displays a colorized banner with the creator's name and website:

```
██████╗     ██████╗  ██████╗ ██████╗ ██╗  ██╗
██╔════╝     ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝
██║  ███╗    ██║  ██║██║   ██║██████╔╝█████╔╝ 
██║   ██║    ██║  ██║██║   ██║██╔══██╗██╔═██╗ 
╚██████╔╝    ██████╔╝╚██████╔╝██║  ██║██║  ██╗
 ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
              Created by: Aung San Oo
             Website: https://aungsanoo.com
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/google-dork-scanner.git
   cd google-dork-scanner
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Script**:
   ```bash
   python3 googledork.py
   ```

---

## Usage

### 1. Interactive Mode
Run the script and follow the prompts:
```bash
python3 googledork.py
```

Example:
```plaintext
[+] Enter the Dork Search Query: intitle:"Index of /" "password"
[+] Enter the Number of Websites to Display: 5
```

### 2. Output
- Results will be saved to a text file (default: `dork_results.txt`).
- The file will contain only the links, one per line:
  ```plaintext
  http://example.com/secure/
  http://example.com/backup/
  ```

---

## Legal Disclaimer

This tool is intended for **educational purposes only**. Use it responsibly and with explicit permission when performing security assessments. The creator, **Aung San Oo**, is not responsible for any misuse of this tool.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

- **Author**: Aung San Oo
- **Website**: [https://aungsanoo.com](https://aungsanoo.com)
- **GitHub**: [https://github.com/yourusername](https://github.com/yourusername)

---

