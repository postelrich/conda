
def parse_links(actions):
    links = (l.split(' ') for l in actions['LINK'])
    return {l[0]: l[1:] for l in links}


def print_actions(actions):
    print(actions)


def no_javascript(actions):
    links = parse_links(actions)
    bad_packages = [p for p in links.keys() if 'js' in p or 'javascript' in p]
    print(bad_packages)
    if bad_packages:
        raise ValueError("I'm afraid I can't let you install javascript.")


def post_installed(actions):
    import socket
    import os
    packages = list(parse_links(actions).keys())
    hostname = socket.gethostname()
    user = os.getegid()
    for p in packages:
        print("POST /admin/monitor/packages: {{ user: {0}, hostname: {1}, package: {2} }}".format(user, hostname, p))
