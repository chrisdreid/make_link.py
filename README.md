-----------------------------------------------------
README FOR make_links.py
-----------------------------------------------------

OVERVIEW:
---------
The `make_links.py` tool is designed as a symlink windows generator to search for files in the specified source directory based on given regex patterns and then perform certain operations (assumed to be copying or moving) to the specified destination directory.
** You must run this as admin to create symlinks

USAGE:
------
python make_links.py --src-directory [SOURCE_DIRECTORY] --dest-directory [DESTINATION_DIRECTORY] --regexes [REGEX_PATTERN_1] [REGEX_PATTERN_2] ...

PARAMETERS:
-----------
--src-directory: 
    Path to the source directory from which files will be fetched.
    Example: 
    C:\Source

--dest-directory: 
    Path to the destination directory where the selected files will be placed.
    Example: 
    D:\Destination

--regexes: 
    A list of regex patterns to match files in the source directory. The script will search for files matching any of the provided patterns.
    Examples: 
    ".*\.safetensors" matches any file with a '.safetensors' extension.
    ".*\.bin" matches any file with a '.bin' extension.

EXAMPLES:
---------
1. To search for all files with extensions '.safetensors' and '.bin' in the C:\Source directory and move/copy them to D:\Destination:

    python make_links.py --src-directory C:\Source --dest-directory D:\Destination --regexes ".*\.safetensors" ".*\.bin"

2. If you want to search for all '.txt' files in C:\Documents and move/copy them to D:\TextFiles:

    python make_links.py --src-directory C:\Documents --dest-directory D:\TextFiles --regexes ".*\.txt"

NOTE:
-----
Make sure you have the necessary permissions to read from the source directory and write to the destination directory. Also, ensure your regex patterns are accurate to avoid unexpected file matches.

-----------------------------------------------------
