from datetime import datetime

try:
    file = open("E:Hindi.txt", "r")
    content = file.read()
    print(content + "\nEndOfFile\n---------")
except ZeroDivisionError:
    print("divide by zeror error")
except Exception as e:
    print(f"Exception occured. {repr(e)} @{ datetime.now().strftime("%Y-%m-%d %H:%M:%S") }")
else:
    print(f"no exception occured @{ datetime.now().strftime("%Y-%m-%d %H:%M:%S") }")
finally:
    print("success.Great man.")
