import os
import nmap

def run_network_scanner():
    try:
        # تحديد المسار المباشر المكتشف لملف nmap.exe
        nmap_exe = r"C:\Program Files (x86)\Nmap\nmap.exe"
        
        # إضافة المسار لمتغيرات البيئة لضمان التعرف عليه
        nmap_dir = r"C:\Program Files (x86)\Nmap"
        if os.path.exists(nmap_dir) and nmap_dir not in os.environ["PATH"]:
            os.environ["PATH"] += os.pathsep + nmap_dir

        # إخبار المكتبة بمكان الملف مباشرة وبدء أداة الفحص
        scanner = nmap.PortScanner(nmap_search_path=(nmap_exe, "nmap"))
        
        print("=== NetScout-CLI: Automated Scanning & Analysis Tool ===")
        
        # استقبال عنوان الهدف يمكن استخدام هذا IP للتجربة (45.33.32.156)
        target = input("Enter Target IP address or URL to scan: ").strip()
        if not target:
            print("No target entered. Process canceled.")
            return

        # 3. اختيار نوع الفحص
        print("\nSelect the desired scan mode:")
        print("1. Quick Scan (Top 100 ports)")
        print("2. Detailed Scan (Service versions & NSE scripts)")
        choice = input("Enter choice (1 or 2): ").strip()

        # تحديد خيارات الفحص بناءً على اختيار المستخدم
        if choice == '1':
            options = "-F"
        else:
            options = "-sV -sC"

        # 4. بدء عملية الفحص
        print(f"\n[+] Scanning target: {target} ... Please wait.")
        scanner.scan(target, arguments=options)

        # 5. استخراج النتائج وعرضها
        output_results = []
        for host in scanner.all_hosts():
            host_info = f"\nHost: {host} ({scanner[host].hostname()})\nState: {scanner[host].state()}"
            print(host_info)
            output_results.append(host_info)

            for protocol in scanner[host].all_protocols():
                proto_info = f"\nProtocol: {protocol.upper()}"
                print(proto_info)
                output_results.append(proto_info)

                ports = scanner[host][protocol]
                for port, port_data in ports.items():
                    service_name = port_data.get('name', 'Unknown')
                    port_line = f"Port: {port}\tState: {port_data['state']}\tService: {service_name}"
                    print(port_line)
                    output_results.append(port_line)

        # 6. خيار حفظ التقرير في ملف نصي
        save = input("\nDo you want to save the report to a text file? (y/n): ").strip().lower()
        if save == 'y':
            with open("scan_report.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(output_results))
            print("[+] Report saved successfully to scan_report.txt")

    except nmap.PortScannerError:
        print("[-] Error: Nmap is not installed or was not found on your system.")
    except Exception as error:
        print(f"[-] An unexpected error occurred: {error}")

# تشغيل الدالة الرئيسية
if __name__ == "__main__":
    run_network_scanner()
    