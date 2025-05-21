#!/usr/bin/env python3

"""
Polymathic Cognition Constructs - Prompt CLI Tool
(Placeholder for future enhancements)
"""

import argparse
import os

def list_constructs(path="."):
    """Lists all .prmt.md files."""
    print(f"Available constructs in '{os.path.abspath(path)}':")
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".prmt.md"):
                # Construct a relative path for cleaner output
                relative_root = os.path.relpath(root, path)
                if relative_root == ".":
                    print(f"  - {file}")
                else:
                    print(f"  - {os.path.join(relative_root, file)}")

def main():
    parser = argparse.ArgumentParser(description="CLI tool for managing cognition constructs.")
    parser.add_argument("--list", action="store_true", help="List available constructs in the current directory and subdirectories.")
    parser.add_argument("--path", default=".", help="Path to search for constructs (default: current directory).")
    
    args = parser.parse_args()

    if args.list:
        list_constructs(args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
