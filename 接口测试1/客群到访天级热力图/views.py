

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from md5_generater.md5_util import generate_arg_md5



# 测试请求类
class HotMap(APIView):


    def get(self, request):

        #在这里调用一个动态生成arg_md5参数的函数
        # arg_md5 = generate_arg_md5()
        # print(arg_md5)
        arg_md5 = '752a5a0d49195348c4b882bae9e3a9f2'
        try:
            url_para_str = f"salt=0.234153348&argMd5={arg_md5}&access-key=moxi-oa-ak-huashiTest"
            data = {"urlParaStr": url_para_str,"sk": "046A752BE25BCE2D"}
            url = 'http://39.102.128.14:8080/mx-data/sign/get'
            # 调用外部接口
            response = requests.request("GET",url, json=data)
            response.raise_for_status()  # 检查请求是否成功
            print("First Response Content:", response.text)
            data_value = response.json().get('data')
            if data_value:
                print(data_value)  # 确认数据是否打印

                # 将 `data_value` 进行 URL 编码
                # encoded_data_value = quote(data_value)
                url2 = f"http://39.102.128.14:8080/mx-data/api/request/v1/tfDheat?{data_value}"
            # 直接将获取到的数据返回给前端
                headers = {
                    "Content-Type": "application/json"  # 确保服务器理解为 JSON 请求
                }
                # 和上面的to_sign的内容要保持一致
                data2 = '{"projectId":2024012301,"type":3,"id":"9022603","data":{"length":7,"date":1713283200}}'
                response2 = requests.post(url2,headers=headers,data=data2)
                response2.raise_for_status()
                return Response(response2.json(), status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No data returned from first GET request'}, status=status.HTTP_400_BAD_REQUEST)

        except requests.RequestException as e:
            # 请求失败时返回错误响应
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


