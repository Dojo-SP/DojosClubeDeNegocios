def parse_url(url):
    pos = url.find("://")
    if pos == -1:
        raise ValueError("Invalid URL")

    if "?" in url:
        url, query = url.split("?", 1)
    else:
        query = ""

    at = url.find("@")
    if at >= 0:
        dpath = url[at + 1:]
        colon = url.find(":", pos + 1)
        if colon >= 0:
            user = url[pos + 3:colon]
            password = url[colon + 1:at]
            print(pos, colon, at)
        else:
            user = url[pos + 3:at]
            password = ""
    else:
        dpath = url[pos + 3:]
        user = ""
        password = ""

    protocol = url[:pos]
    return {
        "protocol": protocol,
        "dpath": dpath,
        "query": query,
        "user": user,
        "password": password,
    }
