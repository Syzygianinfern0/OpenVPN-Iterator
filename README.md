<div align="center">

# 🔐 OpenVPN-Iterator 🔓

"Brute Force(?)" Credentials against an OpenVPN Config

| **🚧 Disclaimer: This is not intended to be used, nor has been created for any malpractices 🚧** |
|:------------------------------------------------------------------------------------------------:|

---

</div>

## Usage 👨‍💻

- `creds.txt`: Credentials in the format of `username:pass`, each one separated in a new line.
- `*.ovpn`: OpenVPN config file. NordVPN Demonstrated here.

### Python 🐍
Checks if the credential works. If it does, prints it in green, else in red (there is also a yellow case when it times out - I don't know why that happens). 
You will have to manually connect using these credentials (or just save them for later/to share). If you don't want to do that, try the bash way. 

```shell
python main.py --config us8245.nordvpn.com.udp.ovpn --creds creds.txt
```

### Bash #️⃣
This command requires `sudo` and if yo momma didn't raise no quitter you would run it. If it just hangs, it means it is connected (fite me or send a PR which I would gladly close cause you're a cheap shit anyways to use this repo in the first place 💩 /S)

```shell
sudo ./main.sh us8245.nordvpn.com.udp.ovpn creds.txt
```

## TODO
- [ ] Maybe integrate [this](https://github.com/mrzool/nordvpn-server-find) or [this](https://sleeplessbeastie.eu/2019/02/18/how-to-use-public-nordvpn-api)
- [ ] Maybe make the bash way more elegant - as a gnome extension?

Please ~~like, share, and subscribe~~ star, fork, and follow if you found this useful. 
