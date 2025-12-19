import sys

from .db import create_all_tables


def cmd_init():
    create_all_tables()
    print("Database tables created.")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m {{ cookiecutter.project_slug }}.run init")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        cmd_init()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
