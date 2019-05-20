import json
import urllib.request

config = {
    "qq": "",
    "token": "",
    "g_tk": "",
    "cookie": "",
}

qq = config["qq"]
token = config["token"]
g_tk = config["g_tk"]
cookie = config["cookie"]

query_url = f"https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin={qq}&ftype=0&sort=0&pos=0&num=200&replynum=100&g_tk={g_tk}&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken={token}"
delete_url = f"https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_delete_v6?qzonetoken={token}&g_tk={g_tk}"

opener = urllib.request.build_opener()
opener.addheaders.clear()
opener.addheaders.append(("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"))
opener.addheaders.append(("cookie", cookie))
opener.addheaders.append(("referer", f"https://user.qzone.qq.com/{qq}"))
opener.addheaders.append(("origin", "https://user.qzone.qq.com"))

try:
    while True:
        result = opener.open(query_url).read().decode()[17:-2]
        result = json.loads(result)
        msg_list = result["msglist"]
        for msg in msg_list:
            content = msg["content"]
            create_time = msg["createTime"]
            print(f"deleting {create_time}: {content}")
            tid = msg["tid"]
            data = f"hostuin={qq}&tid={tid}&t1_source=1&code_version=1&format=fs&qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F{qq}"
            result = opener.open(delete_url, data.encode()).read().decode()
except TypeError as e:
        print("done")

