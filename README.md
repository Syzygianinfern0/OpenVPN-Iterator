# OpenVPN-Iterator
🔒 "Brute Force(?)" Credentials against an OpenVPN Config

## Usage
- `creds.txt`: Credentials in the format of `username:pass`, each one separated in 
a new line.
- `*.ovpn`: OpenVPN config file. NordVPN Demonstrated here. 

```shell
python main.py --config us8245.nordvpn.com.udp.ovpn --creds creds.txt
```

Disclaimer: This is not intended to be used, nor has been created for any malpractices. 
