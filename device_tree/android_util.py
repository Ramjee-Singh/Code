from ppadb.client import Client as AdbClient
import xml.etree.ElementTree as ET

def list_directory_content(device, path, parent_element):
    # Execute 'ls -l' command on the given path
    result = device.shell(f"ls -l {path}")

    # Process the result
    lines = result.splitlines()
    for line in lines:
        line = line.strip()
        if line:
            # Split the line into file/directory name and attributes
            parts = line.split(None, 8)
            print(parts)
            if len(parts) >= 8:
                file_name = parts[-1]
                attributes = parts[0]

                # Create XML element for the file/directory
                element = ET.SubElement(parent_element, "entry")
                element.set("name", file_name)

                # Recursively list the content if it's a directory
                if attributes.startswith("d"):
                    sub_path = f"{path}/{file_name}"
                    print(sub_path)
                    list_directory_content(device, sub_path, element)

# Connect to ADB server
adb = AdbClient(host="127.0.0.1", port=5037)

# Get the list of connected devices
devices = adb.devices()

if len(devices) == 0:
    print("No devices connected.")
else:
    # Get the first device from the list
    device = devices[0]
    # device.shell("su")

    # Start listing the content recursively from /proc/device-tree
    root_element = ET.Element("directory")
    # listing from storage path for example
    list_directory_content(device, "/storage", root_element)

    # Create XML tree and write it to a file
    tree = ET.ElementTree(root_element)
    tree.write("directory_content.xml", encoding="utf-8", xml_declaration=True)
    print("XML file generated: directory_content.xml")
