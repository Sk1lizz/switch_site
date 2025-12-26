import platform

def get_path(*args, **kwargs):
    path = None
    
    if platform.system() == "Windows":
        path = r"C:\Windows\System32\drivers\etc\hosts"
    else: 
        path = None

    return path

def filter_website(site: str): 

    site_end = (site.replace("https://", "")).replace("http://", "")

    if site_end[0] == "w" and site_end[1] == "w" and site_end[2] == "w" and site_end[3] == ".":
        site_end=site_end.replace("www.", "")

    return site_end

    


def switch_add(site_start):
    ip_block = "0.0.0.0"
    path_to_local_hosts_file = r"files\datafile\Windows\hosts\hosts"

    site = filter_website(site_start)

    text = [
        f"\n\n# Blocking access to the website: {site} (by skilizz)",
        f"{ip_block} {site}"
    ]

    try:
        with open(path_to_local_hosts_file, "a", encoding='utf-8') as file:
            file.write("\n".join(text))
            return f"Website {site} added"
        
    except Exception as e:
        return f"Error: {e}"

    
def switch_on(site):
    path = get_path()
    if path == None: return "This platform is not supported."


def switch_off():
    pass
