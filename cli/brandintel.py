import argparse
import requests


def main() -> None:
    parser = argparse.ArgumentParser(prog="brandintel")
    sub = parser.add_subparsers(dest="cmd", required=True)

    scan = sub.add_parser("scan")
    scan.add_argument("url")

    mon = sub.add_parser("monitor")
    mon.add_argument("brand")

    enr = sub.add_parser("enrich")
    enr.add_argument("domain")

    sub.add_parser("export")

    args = parser.parse_args()

    if args.cmd == "scan":
        print(requests.post("http://localhost:8000/v1/scan", json={"url": args.url}, timeout=20).json())
    elif args.cmd == "monitor":
        print({"status": "queued", "brand": args.brand})
    elif args.cmd == "enrich":
        print({"status": "queued", "domain": args.domain})
    else:
        print({"status": "exported"})


if __name__ == "__main__":
    main()
