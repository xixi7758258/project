from app.confs.config import Config

# Get_network_address.
# @params: <addr: str>, <fid: str>
# @return: <url: str>
def Get_network_address(addr, fid):
    
    url = "http://" + Config.FLIE_SROTAGE_URL[addr]["URL"] \
        + ":" + addr + "/" + fid

    return url