from log_analyzer import LogEntry 
import argparse
import csv
from pathlib import Path
from datetime import datetime

# Method to print the first 5 log entries
def print_head(log_entries):
    for entry in log_entries[:5]:
        print(f"{entry.event_time}, {entry.action}, {entry.internal_ip}, {entry.ipv4_class}, {entry.country_name}")


# Method to count the denied log entries
def deny_count(log_entries):
    denied_entries = [entry for entry in log_entries if entry.action == "Deny"]
    print(f"{len(denied_entries)} log entries were denied.")


# Method to count the log entries from a specific country
def country_count(log_entries, country_code):
    country_entries = [entry for entry in log_entries if entry.country == country_code]
    print(f"{len(country_entries)} log entries from {country_code} were recorded.")




def main():
    parser = argparse.ArgumentParser(description="Process firewall logs.")
    parser.add_argument("--filename", required=True, help="CSV file name")
    parser.add_argument("--action", required=True, choices=["head", "deny", "source"], help="Action to perform on the logs")
    parser.add_argument("--country", required=False, help="Two-letter country code for the 'source' action")

    args = parser.parse_args()

    # Load the CSV file and parse it into log entries
    with open(Path(__file__).with_name(args.filename), 'r', encoding='utf-8') as file:
        dict_reader = csv.DictReader(file)
        datadict = list(dict_reader)

    log_entries = []
    for row in datadict:
        log = LogEntry(
            row['event_time'], row['internal_ip'], int(row['port_number']), row['protocol'],
            row['action'], int(row['rule_id']), row['source_ip'], row['country'], row['country_name']
        )
        log_entries.append(log)

    # Check the action and execute accordingly
    if args.action == "head":
        print_head(log_entries)
    elif args.action == "deny":
        deny_count(log_entries)
    elif args.action == "source" and args.country:
        country_count(log_entries, args.country)

if __name__ == "__main__":
    main()

