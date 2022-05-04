import random
from socket import AF_INET, SOCK_STREAM, socket

from PyRoxy import ProxyUtiles
from .core import logger, cl, PROXIES_URLS
from .system import read_or_fetch, fetch


# @formatter:off
_globals_before = set(globals().keys()).union({'_globals_before'})
# noinspection PyUnresolvedReferences
from .load_proxies import *
decrypt_proxies = globals()[set(globals().keys()).difference(_globals_before).pop()]
# @formatter:on


class _NoProxy:
    def asRequest(self):
        return None

    def open_socket(self, family=AF_INET, type=SOCK_STREAM, proto=-1, fileno=None):
        return socket(family, type, proto, fileno)


NoProxy = _NoProxy()


def update_proxies(proxies_file, previous_proxies):
    if proxies_file:
        proxies = load_provided_proxies(proxies_file)
    else:
        proxies = load_system_proxies()

    if not proxies:
        if previous_proxies:
            proxies = previous_proxies
            logger.warning(f'{cl.MAGENTA}The previous proxy list will be used{cl.RESET}')
        else:
            logger.error(f'{cl.RED}No working proxies found - attack stopping{cl.RESET}')
            exit()

    return proxies


def load_provided_proxies(proxies_file):
    content = read_or_fetch(proxies_file)
    if content is None:
        logger.warning(f'{cl.RED}Could not read proxy from file {proxies_file}{cl.RESET}')
        return None

    proxies = ProxyUtiles.parseAll([prox for prox in content.split()])
    if not proxies:
        logger.warning(f'{cl.RED}У {proxies_file} no proxy found - check file format and try again.{cl.RESET}')
    else:
        logger.info(f'{cl.YELLOW}Read {cl.BLUE}{len(proxies)}{cl.YELLOW} proxy{cl.RESET}')
    return proxies


def load_system_proxies():
    raw = fetch(random.choice(PROXIES_URLS))
    try:
        proxies = ProxyUtiles.parseAll(decrypt_proxies(raw))
    except Exception:
        proxies = []
    if proxies:
        logger.info(
            f'{cl.YELLOW}Sample received {cl.BLUE}{len(proxies):,}{cl.YELLOW} proxy '
            f'from the list {cl.BLUE}25.000+{cl.YELLOW} workers{cl.RESET}'
        )
    else:
        logger.warning(f'{cl.RED}Failed to get personal proxy sample{cl.RESET}')
    return proxies
