import webbrowser,  sys , os , requests


print("""

                                                                   
    ███████╗ ██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
    ██╔════╝██╔════╝ ██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
    ███████╗██║  ███╗███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
    ╚════██║██║   ██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
    ███████║╚██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                

""")
try:
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as f:
                domains = [line.strip() for line in f if line.strip()]
            print(f"📂 Loaded {len(domains)} domains from {sys.argv[1]}")
        else:
            domains = sys.argv[1:]
            print(f"📝 Loaded {len(domains)} domains from arguments")
    else:
        domains = input("Domains (space separated): ").split()
        print(f"📝 Loaded {len(domains)} domains from input")

    if not domains:
        print("❌ No domains found!")
        sys.exit(1)

    for i,d in enumerate(domains,1):
        url = d if d.startswith(("https://","http://")) else "https://"+ d
        webbrowser.get("firefox").open(url)
        try: 
            status = f"({requests.get(url,timeout=3).status_code})"
        except:
            status = "(Down)"
        print(f"[{i:3}]{status:>10} -> {d}")
        
    
    print(f"\n🔥 All {len(domains)} domains opened in Firefox!")

except Exception as e:
    print(f"❌ Error: {e}") 