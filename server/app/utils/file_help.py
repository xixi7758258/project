import requests

# ObtainFileStorageAddr
# @params: <file_url: str>
# @return: <fid: str>, <url: stty>
def ObtainFileStorageAddr(master_url):
    url = "http://" + master_url + "/dir/assign"
    rsp = requests.get(url)
    rsp_json = rsp.json()
    return rsp_json["fid"],str(rsp_json["url"])[str(rsp_json["url"]).find(":")+1:]

def UploadFile(file_storage_url, port, fid, file_name, file):
    url = "http://" + file_storage_url + ":"+ port + "/" + fid
    files = {file_name: file}
    rsp = requests.post(url=url, files=files)
    return rsp.status_code

def DeleteFile(file_storage_url, fid):
    url = "http://" + file_storage_url + "/" + fid
    requests.delete(url)
    return