# make_links.py

## OVERVIEW:
The `make_links.py` tool is designed as a (Windows) symlink generator. It searches for files in the specified `source directory` based on given `regex & endswith` patterns. The script then uses the `mklink` command to create symlinks in the specified `destination directory`.
> **IMPORTANT:** You must run this as admin to create symlinks on Windows.

## USAGE:
```shell
python make_links.py --src-directory [SOURCE_DIRECTORY] --dest-directory [DESTINATION_DIRECTORY] --regexes [REGEX_PATTERN_1] ... --endswith [.EXTENSION_1] ...
```

## PARAMETERS:
- **--src-directory:**  
    Path to the source directory from which files will be fetched.  
    *Example:* `C:\Source`

- **--dest-directory:**  
    Path to the destination directory where the symlinks will be created.  
    *Example:* `D:\Destination`

- **--regexes:**  
    A list of regex patterns to match files in the source directory. The script will search for files matching any of the provided patterns.  
    *Examples:*   
    - `"^.*\.safetensors$"` matches any file with a '.safetensors' extension.  
    - `"^.*\.bin$"` matches any file with a '.bin' extension.

- **--endswith:**  
    A list of file extensions to match files in the source directory. This can be used as an alternative or in addition to the --regexes parameter.  
    *Examples:*  
    - `".txt"` matches any file with a '.txt' extension.  
    - `".doc"` matches any file with a '.doc' extension.

## EXAMPLES:
1. To create symlinks for all files with extensions '.safetensors' and '.bin' from C:\Source to D:\Destination:
```shell
python make_links.py --src-directory C:\Source --dest-directory D:\Destination --regexes "^.*\.safetensors$" "^.*\.bin$"
```

2. To create symlinks for all '.txt' files from C:\Documents to D:\TextFiles:
```shell
python make_links.py --src-directory C:\Documents --dest-directory D:\TextFiles --endswith .txt
```

## NOTE:
Make sure you have the necessary permissions to read from the source directory and write to the destination directory. Ensure your regex patterns and endswith extensions are accurate to avoid unexpected file matches.
