import urllib.request
import json
import ssl
import google.protobuf

context = ssl._create_unverified_context()

url = 'https://api.openlanguage.com/ez/studentapp/v15/lessonDialogue?lesson_id=6660291531066327307&iid=65893088191&device_id=11070134136&ac=wifi&channel=meizu&aid=1335&app_name=open_language&version_code=410&version_name=4.1.0&device_platform=android&ssmix=a&device_type=MX5&device_brand=Meizu&language=zh&os_api=22&os_version=5.1&uuid=868746020333604&openudid=16ffe5defeeb2180&manifest_version_code=410&resolution=1080*1920&dpi=480&update_version_code=4101&_rticket=1552467168324&ez_version=12&timezone=Asia%2FShanghai&timezone_offset=28800000'
req = urllib.request.Request(url)
with urllib.request.urlopen(req,context=context) as response:
    detail_data = response.read()
    print(detail_data)
