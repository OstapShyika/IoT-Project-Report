import requests
import json
import time


class HttpAPI:

    def __init__(self):
        self.send_error = 0
        self.send_text = ""
        self.send_response = ""

    def write_log(self, log_data):

        cur_log = time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime()) + log_data + "\r\n"
        try:
            with open("log.txt", "a+") as log:
                log.write(cur_log)
        except BaseException:
            print("lan_eWeLink_api_error")

    def post_request(self, url=None, data=None):

        ret = {}

        json_str = json.dumps(data)
        print("send ING", json_str)
        self.send_text = json_str
        self.write_log("send ING")
        self.write_log(self.send_text)
        response = requests.post(url=url, data=json.dumps(data), timeout=10)
        self.send_response = response
        print("RETURN response：", response.text)
        self.write_log("RETURN response")
        self.write_log(response.text)
        ret["result"] = True
        ret["text"] = response.text
        return ret


class SendCommand:

    def __init__(self, parent=None, **func_task):

        self.http = HttpAPI()

    def send_data(self, send_url, send_data):

        print("send", send_url, str(send_data))
        response = self.http.post_request(send_url, send_data)
        print("response：", str(response))
        if response["result"]:
            return json.loads(response["text"])
        else:
            return 1

    def set_wifi_connection(self, **info):

        ssid = info["ssid"]
        password = info["password"]
        data = {}

        url = "https://" + info["ip"] + ":" + \
              str(info["port"]) + "/zeroconf/wifi"

        data["sequence"] = str(int(time.time()))
        sub_id = info["sub_id"]
        data["device_id"] = sub_id
        data["data"] = {"ssid": ssid, "password": password}

        return self.send_data(send_url=url, send_data=data)

    def set_power_up_state(self, **info):
        state = info["state"]
        data = {}

        url = "https://" + info["ip"] + ":" + \
              str(info["port"]) + "/zeroconf/startup"

        data["sequence"] = str(int(time.time()))
        sub_id = info["sub_id"]
        data["device_id"] = sub_id
        if state == 0:
            data["data"] = {"startup": "off"}
        elif state == 1:
            data["data"] = {"startup": "on"}
        elif state == 2:
            data["data"] = {"startup": "stay"}

        return self.send_data(send_url=url, send_data=data)

    def set_on_off(self, **info):

        # out_state == true -> set the device on
        # out_state == false -> set the device off

        out_state = info["OUT"]
        data = {}

        url = "https://" + info["ip"] + ":" + \
              str(info["port"]) + "/zeroconf/switch"

        data["sequence"] = str(int(time.time()))
        sub_id = info["sub_id"]
        data["device_id"] = sub_id
        if out_state:
            data["data"] = {"switch": "on"}
        else:
            data["data"] = {"switch": "off"}

        return self.send_data(send_url=url, send_data=data)


# Info setter
def set_info(out):
    info = {"OUT": out}
    print("Enter the device's IP-adress")
    info["ip"] = str(input())
    print("Enter the port number")
    info["port"] = int(input())
    print("Enter the device's id")
    info["sub_id"] = str(input())
    return info


sonoff_manager = SendCommand()
current_info = set_info(False)
sonoff_manager.set_on_off(current_info)
