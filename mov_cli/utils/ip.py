import re

__all__ = ("hide_ip",)

def hide_ip(text: str, hide_it: bool) -> str:
    ipv4_re = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ipv6_re = "([a-f0-9:]+:+)+[a-f0-9]+"

    if hide_it:
        text = re.sub(ipv4_re, "{the-cat-snatched-your-ip-address}", text)
        text = re.sub(ipv6_re, "{the-cat-snatched-your-ip-address}", text)

    return text