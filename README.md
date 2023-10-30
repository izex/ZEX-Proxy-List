# 🚀 ZEX Proxy List v1.0

A Python script to fetch and test SOCKS4 and SOCKS5 proxy lists. This script is designed to retrieve free proxies.


## ⚙️ Requirements

- Python 3.x
- Required Python libraries: `requests`, `rich`, `socket`

## 📥 Installation & Setup

1. First, clone the repository:
    ```bash
    git clone https://github.com/izex/zex-proxy-list.git
    cd zex-proxy-list
    ```

2. Install the required Python libraries:
    ```bash
    pip install requests rich
    ```

## 🚀 Usage

Run the script using Python 3:

    ```bash
    python3 proxy.py
    ```

Follow the on-screen prompts to choose the type of proxies (SOCKS4 or SOCKS5), the number of proxies you want to test, and whether you want to test them or not.

## 📝 Notes

- The script fetches proxy lists from predefined URLs and optionally tests their validity.
- Tested proxies are saved to a file named either `socks4_zex.txt` or `socks5_zex.txt` depending on the chosen proxy type.

## 📜 License

This project is open source. Feel free to fork, modify, and distribute as you see fit.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
