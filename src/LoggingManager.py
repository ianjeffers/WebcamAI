from datetime import datetime
import os

import dateutil.utils


class LoggingManager():

    path = os.getcwd()
    txt_file_type = ".txt"
    error_path = "/errors/"
    records_path = "records/"
    info_path = "/info/"
    logs_path = "/logs/{}/"

    def __init__(self):
        self.write_path = self.path + self.logs_path.format(dateutil.utils.today())
        if not os.path.exists(self.write_path):
            os.mkdir(self.write_path)

    def log_message(self, message_path, message):
        file_path = self.write_path + message_path
        file_name = file_path + str(datetime.utcnow().hour) + self.txt_file_type

        if not os.path.exists(file_path):
            os.mkdir(file_path)
        else:
            f = open(file_name, "a")
            f.write(str(dateutil.utils.today()) + "\n" + str(datetime.utcnow()) + "\n" + message + "\n")
            f.close()

    def log_error(self, error):
        self.log_message(self.error_path, error)

    def log_records(self, records):
        self.log_message(self.records_path, records)

    def log_info(self, info):
        self.log_message(self.info_path, info)