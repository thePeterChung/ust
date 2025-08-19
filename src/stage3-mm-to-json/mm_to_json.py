import xml.etree.ElementTree as ET
import json
import re
import os
import argparse

convert_count = 0

def extract_metadata(text):
    """Extract structured metadata (tags like <key:value>) from node TEXT."""
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    tags = {}
    matches = re.findall(r"<([^:>]+):([^>]+)>", text)
    for key, value in matches:
        tags[key] = value
    clean_text = re.sub(r"<[^:>]+:[^>]+>", "", text).strip()
    return clean_text, tags

def parse_node_clean(xml_node):
    """Recursively convert an XML Freeplane node to structured JSON, omitting system attributes."""
    node_data = {}
    raw_text = xml_node.attrib.get("TEXT", "")
    clean_text, metadata = extract_metadata(raw_text)

    if clean_text:
        node_data["text"] = clean_text
    node_data.update(metadata)

    children = [parse_node_clean(child) for child in xml_node.findall("node")]
    if children:
        node_data["children"] = children

    return node_data

def mm_to_json(mm_file, json_file, mm_folder_path, json_folder_path):
    global convert_count
    """Convert .mm Freeplane file to JSON."""
    tree = ET.parse(mm_folder_path + "/" + mm_file)
    root = tree.getroot()
    first_node = root.find("node")
    if first_node is None:
        raise ValueError("No <node> element found in the .mm file.")
    clean_json = parse_node_clean(first_node)

    os.makedirs(json_folder_path, exist_ok=True)
    with open(json_folder_path +"/" + json_file, "w", encoding="utf-8") as f:
        json.dump(clean_json, f, indent=2, ensure_ascii=False)
    convert_count += 1
    print(f"[{convert_count}] Convert: {mm_file} -> {json_file}")

def natural_sort_key(s):
    """Sort like macOS Finder: split text and numbers."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def ust_json(mm_folder_path,json_folder_path):
    for filename in sorted(os.listdir(mm_folder_path), key=natural_sort_key):
        if filename.endswith(".mm"):
            mm_file = filename
            json_file = filename.replace(".mm",".json")
            mm_to_json(mm_file,json_file,mm_folder_path,json_folder_path)

def run_pipeline(versionIs):
    if (versionIs == "raw"):
        ust_json("mm-raw","json-raw")
    elif (versionIs == "clean"):
        ust_json("mm-clean","json-clean")

def main():
    parser = argparse.ArgumentParser(description="Run UST pipeline with version and platform options.")

    parser.add_argument(
        "--version",
        required=True,
        choices=["clean", "raw"],
        help="Choose pipeline version: clean or raw."
    )

    args = parser.parse_args()
    print(f"Running version: {args.version}")
    run_pipeline(args.version)
   
if __name__ == "__main__":
    main()