import webbrowser
import sys
import os

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

    for d in domains:
        webbrowser.get("firefox").open("https://" + d)
        print(f"✅ Opened: {d}")
    
    print(f"\n🔥 All {len(domains)} domains opened in Firefox!")

except Exception as e:
    print(f"❌ Error: {e}")