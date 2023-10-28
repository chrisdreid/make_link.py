import os
import re
import subprocess
import argparse

def create_hard_links(src_directory, dest_directory, regexes=None,endswith=None):
    regexes = regexes or []
    endswith = endswith or []

    # Ensure the destination directory exists
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # Iterate through files in the source directory
    for root, _, files in os.walk(src_directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            ok = True
            for ew in endswith:
                if not file_path.endswith(ew):
                    ok = False
                    break
            for rx in regexes:
                if not rx.match(filename):
                    ok = False
                    break
            
            if ok:
                # Construct the destination path
                dest_path = os.path.join(dest_directory, filename)

                # Create a hard link using mklink /H
                try:
                    cmd = ["mklink", "/H", dest_path, file_path]
                    # print('CMD: ', cmd)
                    subprocess.run(cmd, shell=True, check=True)
                    print(f"Created hard link: {dest_path} -> {file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to create hard link: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

def main(args):
    ret = 0
    parser = argparse.ArgumentParser(description="Create hard links for files matching regex patterns.")
    parser.add_argument("--src-directory", required=True, help="Source directory path")
    parser.add_argument("--dest-directory", required=True, help="Destination directory path")
    parser.add_argument("--regexes", nargs="+", required=False, help="List of regex patterns to filter files")
    parser.add_argument("--endswith", nargs="+", required=False, help="List of endswith patterns to filter files")

    args = parser.parse_args(args)
    src_directory = args.src_directory.replace('/','\\')
    dest_directory = args.dest_directory.replace('/','\\')
    # Split the provided filter string into separate regex patterns
    regexes = None
    if args.regexes:
        regexes = [re.compile(pattern) for pattern in args.regexes]
    endswith =  args.endswith

    create_hard_links(src_directory, dest_directory, regexes, endswith)
    return ret

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    sys.exit(main(args))
