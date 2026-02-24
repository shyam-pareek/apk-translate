import os
import sys
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator

# --- COLORS ---
G, Y, R, C, W, B, END = '\033[92m', '\033[93m', '\033[91m', '\033[96m', '\033[97m', '\033[1m', '\033[0m'

# --- CONFIGURATION ---
SIGNER_JAR = "uber-apk-signer.jar"

LANG_MAP = {
    "ja": "ja", "jp": "ja", "zh": "zh-CN", "ko": "ko",
    "hi": "hi", "bn": "bn", "pa": "pa", "ta": "ta", "te": "te", 
    "ml": "ml", "mr": "mr", "vi": "vi", "th": "th", "id": "id",
    "ar": "ar", "fa": "fa", "ur": "ur", "he": "iw", "sw": "sw",
    "es": "es", "fr": "fr", "de": "de", "ru": "ru", "it": "it", 
    "pt": "pt", "nl": "nl", "pl": "pl", "tr": "tr", "ro": "ro"
}

def is_target_lang(text, lang_code):
    if not text: return False
    for char in text:
        cp = ord(char)
        if lang_code in ["ja", "jp"]:
            if (0x3040 <= cp <= 0x309F) or (0x30A0 <= cp <= 0x30FF) or (0x4E00 <= cp <= 0x9FAF): return True
        elif lang_code == "zh":
            if (0x4E00 <= cp <= 0x9FFF): return True
        elif lang_code == "ko":
            if (0xAC00 <= cp <= 0xD7A3) or (0x1100 <= cp <= 0x11FF): return True
        elif lang_code in ["ar", "fa", "ur"]:
            if (0x0600 <= cp <= 0x06FF): return True
        elif lang_code == "hi":
            if (0x0900 <= cp <= 0x097F): return True
        else:
            try: text.encode('ascii')
            except UnicodeEncodeError: return True
    return False

def run_cmd(cmd, step_name):
    print(f"\n{B}{C}>>> [EXEC]{END} Starting: {step_name}...")
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"{G}>>> [SUCCESS] {step_name} completed.{END}")
    except subprocess.CalledProcessError:
        print(f"\n{R}{B}[!!!] FATAL ERROR during {step_name}.{END}")
        sys.exit(1)

def translate_xml(file_path, source_lang, user_flag):
    if not os.path.exists(file_path): return 0
    tree = ET.parse(file_path)
    root = tree.getroot()
    all_elements = root.findall('string')
    total = len(all_elements)
    
    if total == 0: return 0
    folder = os.path.basename(os.path.dirname(file_path))
    print(f"\n{B}[*] Scanning Path:{END} {folder}/strings.xml")
    
    translator = GoogleTranslator(source=source_lang, target='en')
    translated_count = 0
    
    for i, string in enumerate(all_elements):
        if string.text and is_target_lang(string.text, user_flag):
            try:
                original = string.text.strip()
                translated = translator.translate(original)
                
                # VERBOSE: Show words being translated
                disp_orig = (original[:25] + '..') if len(original) > 25 else original
                disp_trans = (translated[:25] + '..') if len(translated) > 25 else translated
                print(f"    {W}[{i+1}/{total}]{END} {Y}{disp_orig}{END} -> {G}{disp_trans}{END}")
                
                string.text = translated.replace("'", "\\'").replace('"', '\\"')
                translated_count += 1
            except: continue
        
        # PROGRESS: Constant line update for current file
        percent = int((i + 1) / total * 100)
        sys.stdout.write(f"\r    {C}File Progress: {percent}% ({i+1}/{total}){END}")
        sys.stdout.flush()
    
    print(f"\n{G}[*] Done: {folder}/strings.xml{END}")
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    return translated_count

def main():
    if len(sys.argv) != 3:
        print(f"\n{R}{B}[!] ERROR: Code required.{END}\n{Y}Usage:{END} python3 translate_apk.py <file.apk> <lang_code>")
        sys.exit(1)

    start_time = time.time()
    input_apk = sys.argv[1]
    user_flag = sys.argv[2].lower().replace("-", "")
    source_lang = LANG_MAP.get(user_flag)

    if not source_lang:
        print(f"{R}Error: '{user_flag}' not found in Wiki codes.{END}")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(input_apk))[0]
    work_dir, rebuilt_apk = f"temp_{base_name}", f"rebuilt_{base_name}.apk"
    output_final = f"{base_name}_translated.apk"

    run_cmd(["apktool", "d", input_apk, "-o", work_dir, "-f"], "Decompilation")

    total_translated = 0
    res_path = os.path.join(work_dir, "res")
    for root_dir, dirs, files in os.walk(res_path):
        if "values" in root_dir and "strings.xml" in files:
            total_translated += translate_xml(os.path.join(root_dir, "strings.xml"), source_lang, user_flag)

    run_cmd(["apktool", "b", work_dir, "-o", rebuilt_apk], "Rebuilding")

    if os.path.exists(SIGNER_JAR):
        out_temp = f"out_{base_name}"
        run_cmd(["java", "-jar", SIGNER_JAR, "--apks", rebuilt_apk, "--out", out_temp], "Signing")
        for file in os.listdir(out_temp):
            if file.endswith(".apk"):
                shutil.move(os.path.join(out_temp, file), output_final)
        shutil.rmtree(work_dir); shutil.rmtree(out_temp)
        if os.path.exists(rebuilt_apk): os.remove(rebuilt_apk)
    
    m, s = divmod(time.time() - start_time, 60)
    print(f"\n{B}{G}" + "-"*40 + f"\n🏁  SUMMARY: {user_flag.upper()} -> EN\n" + "-"*40)
    print(f"✅ Strings: {total_translated} | 🕒 Time: {int(m)}m {int(s)}s\n📦 Output: {output_final}\n" + "-"*40 + f"{END}")

if __name__ == "__main__":
    main()
