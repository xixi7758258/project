import requests

# ObtainFileStorageAddr
# @params: <file_url: str>
# @return: <fid: str>, <url: stty>
def ObtainFileStorageAddr(file_url):
    url = "http://" + file_url + "/dir/assign"
    rsp = requests.get(url)
    rsp_json = rsp.json()
    return rsp_json["fid"],rsp_json["url"]

def UploadFile(file_storage_url, fid, file_name, file):
    url = "http://" + file_storage_url + "/" + fid
    print("url", url)
    files = {file_name: file}
    rsp = requests.post(url=url, files=files)
    return rsp.status_code

def DeleteFile(file_storage_url, fid):
    url = "http://" + file_storage_url + "/" + fid
    requests.delete(url)
    return