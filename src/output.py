import os
import time
from typing import Dict

from tabulate import tabulate

from .core import cl, logger, THREADS_PER_CORE, Params, Stats
from .mhddos import Tools


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_statistic(
    statistics: Dict[Params, Stats],
    table,
    use_my_ip,
    proxies_cnt,
    time_left
):
    tabulate_text = []
    total_pps, total_bps = 0, 0
    for params, stats in statistics.items():
        pps, bps = stats.reset()
        total_pps += pps
        total_bps += bps
        if table:
            tabulate_text.append((
                f'{cl.YELLOW}%s' % params.target.url.host, params.target.url.port, params.method,
                Tools.humanformat(pps) + "/s", f'{Tools.humanbits(bps)}/s{cl.RESET}'
            ))
        else:
            logger.info(
                f'{cl.YELLOW}Target:{cl.BLUE} %s,{cl.YELLOW} Port:{cl.BLUE} %s,{cl.YELLOW} Method:{cl.BLUE} %s,'
                f'{cl.YELLOW} Requests:{cl.BLUE} %s/s,{cl.YELLOW} Traffic:{cl.BLUE} %s/s{cl.RESET}' %
                (
                    params.target.url.host,
                    params.target.url.port,
                    params.method,
                    Tools.humanformat(pps),
                    Tools.humanbits(bps),
                )
            )

    if table:
        tabulate_text.append((f'{cl.GREEN}Total', '', '', Tools.humanformat(total_pps) + "/s",
                              f'{Tools.humanbits(total_bps)}/s{cl.RESET}'))

        cls()
        print(tabulate(
            tabulate_text,
            headers=[f'{cl.BLUE}Target', 'Port', 'Method', 'Requests', f'Traffic{cl.RESET}'],
            tablefmt='fancy_grid'
        ))
        print_banner(use_my_ip)
    else:
        logger.info(
            f'{cl.GREEN}Total:{cl.YELLOW} Requests:{cl.GREEN} %s/s,{cl.YELLOW} Traffic:{cl.GREEN} %s/s{cl.RESET}' %
            (
                Tools.humanformat(total_pps),
                Tools.humanbits(total_bps),
            )
        )

    print_progress(time_left, proxies_cnt, use_my_ip)


def print_progress(time_left, proxies_cnt, use_my_ip):
    logger.info(f'{cl.YELLOW}New cycle through: {cl.BLUE}{time_left} seconds{cl.RESET}')
    if proxies_cnt:
        logger.info(f'{cl.YELLOW}Number of proxies: {cl.BLUE}{proxies_cnt}{cl.RESET}')
        if use_my_ip:
            logger.info(f'{cl.YELLOW}The attack also uses {cl.MAGENTA}your IP along with the proxy{cl.RESET}')
    else:
        logger.info(f'{cl.YELLOW}Attack {cl.MAGENTA}without a proxy{cl.YELLOW} - only your IP is used{cl.RESET}')


def print_banner(use_my_ip):
    print(f'''
- {cl.YELLOW}Load (number of flows){cl.RESET} - parameter `-t 3000`, default - CPU * {THREADS_PER_CORE}
- {cl.YELLOW}Statistics in the form of a table or text{cl.RESET} - the `--table` or` --debug` flags
- {cl.YELLOW}Complete documentation{cl.RESET} - https://github.com/porthole-ascend-cinnamon/mhddos_proxy
    ''')

    if not use_my_ip:
        print(
            f'        {cl.MAGENTA}Use your IP or a VPN {cl.YELLOW}in addition to the proxy - flag `--vpn`{cl.RESET}\n')
