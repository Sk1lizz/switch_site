import platform
import json

ip_block = "0.0.0.0"
path_to_local_hosts_file = r"files\datafile\Windows\hosts\hosts"

def get_path(*args, **kwargs) -> str:
    path = None
    
    if platform.system() == "Windows":
        path = r"C:\Windows\System32\drivers\etc\hosts"
    else: 
        path = None

    return path

def filter_website(site: str) -> str: 

    site_end = (site.replace("https://", "")).replace("http://", "")

    if site_end[0] == "w" and site_end[1] == "w" and site_end[2] == "w" and site_end[3] == ".":
        site_end=site_end.replace("www.", "")

    return site_end

    


def switch_add(site_start) -> str:
    site = filter_website(site_start)

    text = [
        f"\n\n# Blocking access to the website: {site} (by skilizz)",
        f"{ip_block} {site}"
    ]

    with open(r"files\datafile\Windows\hosts\sites.json", "r", encoding='utf-8') as file:
        sitejson = json.load(file)

    count = 0
    for i in sitejson.keys():
        count += 1    

    with open(r"files\datafile\Windows\hosts\sites.json", "w+", encoding='utf-8') as file:
        sitejson[f"{count}"] = f"{site}"
        json.dump(sitejson, file, indent=4)

    try:
        with open(path_to_local_hosts_file, "a", encoding='utf-8') as file:
            file.write("\n".join(text))
            return f"Website {site} added"
        
    except Exception as e:
        return f"Error: {e}"
    

def switch_delete(site_start) -> str:
    site = filter_website(site_start)

    with open(r"files\datafile\Windows\hosts\sites.json", "r", encoding='utf-8') as file:
        sitejson = json.load(file)
    
    count = 0
    count_break = 0
    
    for i in sitejson.keys():
        if sitejson[f"{i}"] == site:
            count = i 
            break

    for i in sitejson.keys():
        if i <= count:
            continue
        sitejson[f"{int(i)-1}"] = sitejson[f"{int(i)}"]
        try: temp = sitejson[f"{int(i)+1}"]
        except KeyError: count_break = i
    
    sitejson.pop(f"{count_break}", None)
    
    with open(r"files\datafile\Windows\hosts\sites.json", "w+", encoding='utf-8') as file:
        json.dump(sitejson, file, indent=4)

    try:
        with open(path_to_local_hosts_file, "r", encoding='utf-8') as file:
            sites_hosts = file.read()
        
        text = f"""\n\n# Blocking access to the website: {site} (by skilizz)
{ip_block} {site}"""
        
        sites_hosts_file = sites_hosts.replace(str(text), "")

        with open(path_to_local_hosts_file, "w", encoding='utf-8') as file:
            file.write(sites_hosts_file)

        return f"Website {site} deleted"
        
    except Exception as e:
        return f"Error: {e}"


def switch_on(site):
    path = get_path()
    if path == None: return "This platform is not supported."


def switch_off():
    path = get_path()
    if path == None: return "This platform is not supported."
 