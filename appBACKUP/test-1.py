import unittest
import requests

class TestDevelopAPI(unittest.TestCase):
    def __init__(self):
        # self.base_url_localhost = 'http://192.168.0.109:8081/api/LEJ/v2'
        self.base_url_localhost = 'http://127.0.0.1:8000'
        self.base_url_test = 'https://test.edallianz.net/api/LEJ/v2'
        self.base_url_release = 'https://api2.lejourneyapp.com/api/LEJ/v2'
        # self.base_url = 'http://127.0.0.1:9999'

    def test_get_version(self):
        url = f'{self.base_url}/version/1'
        response = requests.get(url)
        print(response.text)
            
    def test_check_customer_email(self):
        email = 'cm08051985@gmail.com'
        url = f'{self.base_url}/customer/checkEmailExist/{email}'
        response = requests.get(url)
        print(response.text)
    
    def test_guest_paynow(self):
        url = f'{self.base_url_localhost}/payment/guestpaynow/'
        params = {
            'customer_email': 'edtai@rd.edallianz.com',
            'customer_firstname': 'fisdgfrstname',
            'customer_lastname': 'lastsdgfsdgfname',
            'customer_mobile': '96093859',
            'learners': [{
                # "profile_id": "",
                "profile_name": "Candy Yo",
                "profile_dob": "2016/3/28",
                'profile_note': '',
            },{
                # "profile_id": "",
                "profile_name": "Candys Yo",
                "profile_dob": "2016/3/28",
                'profile_note': 'cc',
            }],
            'schedule_id': 'zpeexbynq0lazeymm4rs',
            # 'stripe_token': 'tok_visa_debit',
            # 'currency': 'SGD',
            # 'grand_total': '0',
            'auto_create_account': '0',
        }
        print ("I'm here")
        print(url)
        response = requests.get(url, json=params)
        # print(response.status_code)
        print(response.text)
    def test_customer_login(self):
        url = f'{self.base_url_test}/login'
        data = {
            # 'customer_email': 'jamesho@edallianz.com',
            # 'customer_password': '123456',
            'customer_email': 'rd01@classlogy.com',
            'customer_password': '123456',
            'appid': 4,
            'deviceType': 1,
        }
       
        response = requests.post(url, data=data)
        print(response.text)
    
    def test_customer_paynow(self):
        url = f'{self.base_url_test}/payment/paynow/futpm'
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImFiMjM3N2MxZmFkMGVhYTdjYWU1MDQzZWEzYjM0NThiYjVlMjM3OGU2NzA0MzE1ODc0OGY4YzMyNDcwNTU2ZDkzY2JlYTBiNzk4OWNlYmFjIn0.eyJhdWQiOiIxIiwianRpIjoiYWIyMzc3YzFmYWQwZWFhN2NhZTUwNDNlYTNiMzQ1OGJiNWUyMzc4ZTY3MDQzMTU4NzQ4ZjhjMzI0NzA1NTZkOTNjYmVhMGI3OTg5Y2ViYWMiLCJpYXQiOjE1NTYxNTg3MTIsIm5iZiI6MTU1NjE1ODcxMiwiZXhwIjoxNTg3NzgxMTEyLCJzdWIiOiIyNTAiLCJzY29wZXMiOlsiY3VzdG9tZXIiXX0.G_T_HYDjt5otjwRnxzXlUa1yiMn5R75Lb2V_wOzyW6i1yawgcqEKZljSglvZVlDNLwlWVaF-JiNPacGVsPK5HiK7GoFJbafXUqvrFQf25W8CRBUrj5eUrgeWvjJGJUpZ4q8XpHV59y4FyrAff55LCjJiSpSDdV68s7qcyaJMHFbD4N5TGr8scsuycXg_tttZTIsa53iqIHxiepZqFytoBd5off_Jf2flRqvr-oYI4YJXuGSyXMqozBBR3jpXEB-EpJpACLH_dHcC_4FRsPxt5wWmsOjjEu-GEaqhCvvo83Wi-80l0xgO9hO8cRsx9tL2RraS_LboHVAmcU3DDSMBzVphHFqCy6MZ7s6ixsRnJDHxzPwZb6EQNAmvEwb7XxkCX8lSUfG4gnlnFwtZmgYSr-eR8GiPXXJDu-EfNDyVFHrKAlknd96RPgXEnKIm1NaV3_9CNd5w7h-TRa4ZmpypCyN9qxgwR1IWEED1ZB6f5prampLxKtpLeZw7LMj0OVQwHAtFHMQDTbCqXGehbDmjjGmyVqSNNjXAaxGIDMGzg2UlW6Ck2-2ZT4cS6lf9Jvi9geZeow4gtbtOZgO8UkqQP8GmhV45l23vB0h5ZacwLypTsQCGxnp2uHRvBolq2F6B8Roqj4KqxOnC9qEIv54hxLNV0K7szXnHepN5rZ7L3MQ',
        }
        params = {
            'price_prefix': 'SGD',
            'ground_total': 222,
        }
        response = requests.post(url, headers=headers, json=params)
        # print(url)
        # print(response.status_code)
        print(response.text)

    def test_get_customer_ecredits_and_option_limit(self):
        url = f'{self.base_url_release}/cart/ecredits/003fb'
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNkZmZiODAwMTUzYTMzNWIxZDc1MTIyMTQwMmVjYzQxNzlkOTFjNmNmYTJlMGEwYTIzNWIwOWNiZjIyNDI4YmNjZmE0MGE3YzYzMjJhYzMzIn0.eyJhdWQiOiIxIiwianRpIjoiM2RmZmI4MDAxNTNhMzM1YjFkNzUxMjIxNDAyZWNjNDE3OWQ5MWM2Y2ZhMmUwYTBhMjM1YjA5Y2JmMjI0MjhiY2NmYTQwYTdjNjMyMmFjMzMiLCJpYXQiOjE1NTU5ODUyNDQsIm5iZiI6MTU1NTk4NTI0NCwiZXhwIjoxNTg3NjA3NjQ0LCJzdWIiOiI2Iiwic2NvcGVzIjpbImN1c3RvbWVyIl19.C957EjXTFAKz9jJrJOuctJRbXeAMjBf0xp9TzivJhAzlq-ibWAWwTE4kSlRMUu8oOrQ7o9VVuuhZxmY3qF27Vk7mwBQxvUd4YRlOxu4cAR6I9jLnJrC7WFUI-PuuEV_FqcERA-b5DWNei5NnU3YPUG0kh6Ld3lbGX0g0Xm07pC0XruUc4o-pTp546Kv9Al71MHPqlHS3z0WYAHQHfbU61cqcNWcUzPUgHtr7ESUMhEgW2oETCqRUYr7QVHbgO2zUlBwKf-oT8645KLUNOC2rCPchZBz-iZWrmozZ0H7n88zpHIgwk31YZryJe_KsKc8Cg7crnv2uQ7dG1ABdXLzD3Ot98LCiw7lBIxJXFrjv-17503eYBQnEiQ-iM5DboA6BXr2HvOfySgQFkepta3mVCJp7SAF7BaRm613pEJGvbfdSgq6GxQS8VhlpMNJ9Cwil0IQpHvtYDemIvgF8YrTYpTvBVQ1Jeyp4C3dAvrcGw5jQSvxt3SK5gDIvdfuRWu8YsLF-C9P47YaPx_zeyrn8LXSmlfpZrsVwuYV6WlnvN8J14wGIGg4-b3AbI9d2wbaxl7TMpo6oLFnwA9y_s5ZcSglEIxlOJkPchh6ZsPXhugrIj2TDB3xkMna2GKDO3uTC7ccNhmWN_anReNd-bS8Juf541gI_9BRwY0fsCpF7yBU',
        }
       
        response = requests.get(url, headers=headers)
        print(response.text)

    def test_get_ecredits_carts_limit(self):
        url = f'{self.base_url_release}/cart/ecredits/003fb'
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQyZWU2YTVlM2JiYzM3NDgyMTlkYTdmMjdhZDUyMjBlMWE0MjAzYjMzMDZmYTI3ZWY2NjMwMmZmNjA4N2Q2MjA5N2E4Zjc4OTFjYmEzYmQ4In0.eyJhdWQiOiIxIiwianRpIjoiZDJlZTZhNWUzYmJjMzc0ODIxOWRhN2YyN2FkNTIyMGUxYTQyMDNiMzMwNmZhMjdlZjY2MzAyZmY2MDg3ZDYyMDk3YThmNzg5MWNiYTNiZDgiLCJpYXQiOjE1NTU5ODYyMjEsIm5iZiI6MTU1NTk4NjIyMSwiZXhwIjoxNTg3NjA4NjIxLCJzdWIiOiI2Iiwic2NvcGVzIjpbImN1c3RvbWVyIl19.XxLPIuYFp2u9PNYwRRfkDgQWqBtGKcz8FaJ6Uud3BYdgyiqHbFtONhnWvj-LchfLUChBh0mD6TACqMuAe6RyGM4pyMpssfLidLcK4WPFW2ArxRe79R-QJgzM3XrFIQfikJ5cNVZjwgofc2SBI4wF2akF9DPth3IN6FfTf0LMRbp5ds6rqMHIbcPtCmXlSHZuJhfqX3_aC2Lf6_w_qxWRxJxUmzY17JBKe5Ibm0H7feQlCeuFpeVqayJKCSxsja21fbqFXVYOKGwnENBzQ3nxQ8xj3yU0wOgCB8IwbCK_IH05-3MIg8ARGJBKCR3pg_isnVd_SCjilbLZSgII49pe60CLO1wtxsEukSKLxezP3H4ks2oBVCA2D8JKL429WbaNRznAuw5inp_W4G05jZjR8s2vlPyiOjnfheoTnce5rG43N7rAGnGZhurBN5auLrJND6Kg806p9_O_Ue_Qefnff_G58b557ySIprknsuaI7YbnoQ0VxbMVh2TDmAkZ7rnA_KDiIDitLDafQ8xCNwZh8j0La4fx94GTKlWhJgjzhptnW9gBH3FJ0eBVxOstJWZ_yDcnFFjEFdH_1AcLfrFB65kYFhHI0_i9L7SldJtAKeiyX9sDV4ZRjxuPbhypd9TmLRqACttl_xxun3KQcQZnejIs4BA2fIT5IZgKrxw1SUI',
        }

        data = {
            'shoppingcart_ids': [
                "omiw1qywqaqhq700kfb7", 
                "w5py33cv2tnivycxa319"
            ],
            'customerId': '003fb',
        }
       
        response = requests.post(url, headers=headers, json=data)
        print(response.text)
    
    def get_transaction_detail(self):
        url = f'{self.base_url_localhost}/customer/transactiondetail/003fb'
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQyZWU2YTVlM2JiYzM3NDgyMTlkYTdmMjdhZDUyMjBlMWE0MjAzYjMzMDZmYTI3ZWY2NjMwMmZmNjA4N2Q2MjA5N2E4Zjc4OTFjYmEzYmQ4In0.eyJhdWQiOiIxIiwianRpIjoiZDJlZTZhNWUzYmJjMzc0ODIxOWRhN2YyN2FkNTIyMGUxYTQyMDNiMzMwNmZhMjdlZjY2MzAyZmY2MDg3ZDYyMDk3YThmNzg5MWNiYTNiZDgiLCJpYXQiOjE1NTU5ODYyMjEsIm5iZiI6MTU1NTk4NjIyMSwiZXhwIjoxNTg3NjA4NjIxLCJzdWIiOiI2Iiwic2NvcGVzIjpbImN1c3RvbWVyIl19.XxLPIuYFp2u9PNYwRRfkDgQWqBtGKcz8FaJ6Uud3BYdgyiqHbFtONhnWvj-LchfLUChBh0mD6TACqMuAe6RyGM4pyMpssfLidLcK4WPFW2ArxRe79R-QJgzM3XrFIQfikJ5cNVZjwgofc2SBI4wF2akF9DPth3IN6FfTf0LMRbp5ds6rqMHIbcPtCmXlSHZuJhfqX3_aC2Lf6_w_qxWRxJxUmzY17JBKe5Ibm0H7feQlCeuFpeVqayJKCSxsja21fbqFXVYOKGwnENBzQ3nxQ8xj3yU0wOgCB8IwbCK_IH05-3MIg8ARGJBKCR3pg_isnVd_SCjilbLZSgII49pe60CLO1wtxsEukSKLxezP3H4ks2oBVCA2D8JKL429WbaNRznAuw5inp_W4G05jZjR8s2vlPyiOjnfheoTnce5rG43N7rAGnGZhurBN5auLrJND6Kg806p9_O_Ue_Qefnff_G58b557ySIprknsuaI7YbnoQ0VxbMVh2TDmAkZ7rnA_KDiIDitLDafQ8xCNwZh8j0La4fx94GTKlWhJgjzhptnW9gBH3FJ0eBVxOstJWZ_yDcnFFjEFdH_1AcLfrFB65kYFhHI0_i9L7SldJtAKeiyX9sDV4ZRjxuPbhypd9TmLRqACttl_xxun3KQcQZnejIs4BA2fIT5IZgKrxw1SUI',
        }

        data = {
            'shoppingcart_ids': [
                "omiw1qywqaqhq700kfb7", 
                "w5py33cv2tnivycxa319"
            ],
            'customerId': '003fb',
        }
       
        response = requests.get(url, headers=headers, json=data)
        print(response.text)

    def get_guest_transaction_detail(self):
        url = f'{self.base_url_test}/guest/transactiondetail/8hzux48axjgp3i1m9mkg'
        # headers = {
        #     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQyZWU2YTVlM2JiYzM3NDgyMTlkYTdmMjdhZDUyMjBlMWE0MjAzYjMzMDZmYTI3ZWY2NjMwMmZmNjA4N2Q2MjA5N2E4Zjc4OTFjYmEzYmQ4In0.eyJhdWQiOiIxIiwianRpIjoiZDJlZTZhNWUzYmJjMzc0ODIxOWRhN2YyN2FkNTIyMGUxYTQyMDNiMzMwNmZhMjdlZjY2MzAyZmY2MDg3ZDYyMDk3YThmNzg5MWNiYTNiZDgiLCJpYXQiOjE1NTU5ODYyMjEsIm5iZiI6MTU1NTk4NjIyMSwiZXhwIjoxNTg3NjA4NjIxLCJzdWIiOiI2Iiwic2NvcGVzIjpbImN1c3RvbWVyIl19.XxLPIuYFp2u9PNYwRRfkDgQWqBtGKcz8FaJ6Uud3BYdgyiqHbFtONhnWvj-LchfLUChBh0mD6TACqMuAe6RyGM4pyMpssfLidLcK4WPFW2ArxRe79R-QJgzM3XrFIQfikJ5cNVZjwgofc2SBI4wF2akF9DPth3IN6FfTf0LMRbp5ds6rqMHIbcPtCmXlSHZuJhfqX3_aC2Lf6_w_qxWRxJxUmzY17JBKe5Ibm0H7feQlCeuFpeVqayJKCSxsja21fbqFXVYOKGwnENBzQ3nxQ8xj3yU0wOgCB8IwbCK_IH05-3MIg8ARGJBKCR3pg_isnVd_SCjilbLZSgII49pe60CLO1wtxsEukSKLxezP3H4ks2oBVCA2D8JKL429WbaNRznAuw5inp_W4G05jZjR8s2vlPyiOjnfheoTnce5rG43N7rAGnGZhurBN5auLrJND6Kg806p9_O_Ue_Qefnff_G58b557ySIprknsuaI7YbnoQ0VxbMVh2TDmAkZ7rnA_KDiIDitLDafQ8xCNwZh8j0La4fx94GTKlWhJgjzhptnW9gBH3FJ0eBVxOstJWZ_yDcnFFjEFdH_1AcLfrFB65kYFhHI0_i9L7SldJtAKeiyX9sDV4ZRjxuPbhypd9TmLRqACttl_xxun3KQcQZnejIs4BA2fIT5IZgKrxw1SUI',
        # }

        # data = {
        #     'shoppingcart_ids': [
        #         "omiw1qywqaqhq700kfb7", 
        #         "w5py33cv2tnivycxa319"
        #     ],
        #     'customerId': '003fb',
        # }
       
        response = requests.get(url)
        print(response.text)

if __name__ == '__main__':
    process = TestDevelopAPI()
    # process.test_get_version()
    # process.test_check_customer_email()
    # process.test_customer_login()
    # process.test_customer_paynow()
    process.test_guest_paynow()
    # process.test_get_customer_ecredits_and_option_limit()
    # process.test_get_ecredits_carts_limit()
    # process.get_guest_transaction_detail()

