import os
import sys
import shutil
import subprocess
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator


SIGNER_JAR = "uber-apk-signer.jar"


def run_cmd(cmd, step_name):
    print(f"\n>>> [EXEC] Starting: {step_name}")
    try:
        
        subprocess.run(cmd, check=True)
        print(f">>> [SUCCESS] {step_name} completed.")
    except subprocess.CalledProcessError:
        print(f"\n[!!!] FATAL ERROR during {step_name}. Verify Apktool and Java are in your PATH.")
        sys.exit(1)

def should_translate(text):
    """Universal detection: returns True if text contains non-ASCII characters."""
    if not text: return False
    try:
        text.encode('ascii')
        return False  
    except UnicodeEncodeError:
        return True   

def escape_android_xml(text):
    if not text: return text
    
    return text.replace("'", "\\'").replace('"', '\\"')

def translate_xml(file_path):
    if not os.path.exists(file_path): return
    print(f"[*] Scanning: {file_path}")
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    translator = GoogleTranslator(source='auto', target='en')
    
    count = 0
    for string in root.findall('string'):
        if should_translate(string.text):
            try:
                translated = translator.translate(string.text)
                string.text = escape_android_xml(translated)
                count += 1
            except: continue
            
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"[*] Translated {count} strings in this file.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 translate_apk.py <file.apk>")
        sys.exit(1)

    input_apk = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(input_apk))[0]
    work_dir = f"temp_{base_name}"
    rebuilt_apk = f"rebuilt_{base_name}.apk"
    output_final_name = f"{base_name}_translated.apk"

    
    run_cmd(["apktool", "d", input_apk, "-o", work_dir, "-f"], "Decompilation")

    
    print(f"\n>>> Scanning all resource folders for {base_name}...")
    res_path = os.path.join(work_dir, "res")
    for root_dir, dirs, files in os.walk(res_path):
        if "values" in root_dir and "strings.xml" in files:
            translate_xml(os.path.join(root_dir, "strings.xml"))

    
    run_cmd(["apktool", "b", work_dir, "-o", rebuilt_apk], "Rebuilding")

    
    if os.path.exists(SIGNER_JAR):
        out_temp = f"out_{base_name}"
        run_cmd(["java", "-jar", SIGNER_JAR, "--apks", rebuilt_apk, "--out", out_temp], "Signing")
        for file in os.listdir(out_temp):
            if file.endswith(".apk"):
                shutil.move(os.path.join(out_temp, file), output_final_name)
                break
        
        
        shutil.rmtree(work_dir)
        shutil.rmtree(out_temp)
        if os.path.exists(rebuilt_apk): os.remove(rebuilt_apk)
        print(f"\n[DONE] Success! Your universal APK is ready: {output_final_name}")
    else:
        print(f"\n[!] Signer missing. Your unsigned APK is: {rebuilt_apk}")

if __name__ == "__main__":
    main()
