#!/usr/bin/python3
"""0. Log parsing"""
import sys
from dateutil import parser
import signal


list_of_log_data = {}
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
line_count = 0
total_file_size = 0


def validate_ip(s):
    """Check if IP is valid"""
    # check number of periods
    if s.count('.') != 3:
        return False

    ip_list = list(map(str, s.split('.')))

    # check range of each number between periods
    for element in ip_list:
        if int(element) < 0 or int(element) > 255\
                or (element[0] == '0' and len(element) != 1):
            return False

    return True


def display_all_logs(signum=None, frame=None):
    """Function to display logs"""
    print(f"File size: {total_file_size}")
    myKeys = list(list_of_log_data.keys())
    myKeys.sort()
    sorted_dict = {i: list_of_log_data[i] for i in myKeys}
    for k, v in sorted_dict.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    for line in sys.stdin:
        my_split_line = line.split()
        sdate = " ".join(my_split_line[2:4]).split('[')
        sddate = sdate[1].split("]")
        if len(my_split_line) == 9:
            if " ".join(my_split_line[4:7]) == '"GET /projects/260 HTTP/1.1"'\
                and my_split_line[1] == "-"\
                and my_split_line[8].isnumeric()\
                and my_split_line[7].isnumeric()\
                and validate_ip(my_split_line[0])\
                and bool(parser.parse(sddate[0]))\
                    and my_split_line[7] in status_codes:
                if my_split_line[7] in list_of_log_data.keys():
                    list_of_log_data[my_split_line[7]] += 1
                else:
                    list_of_log_data[my_split_line[7]] = 1
                total_file_size += int(my_split_line[8])

        line_count += 1

        if line_count == 10:
            display_all_logs()
            line_count = 0

        signal.signal(signal.SIGINT, display_all_logs)
