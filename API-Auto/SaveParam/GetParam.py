

"""获取登录后产生的hesytoken"""
def UserLoginToken():
    with open('F:/pyhcarm/hezongyy/API-Auto/SaveParam/UserLoginToken.txt', 'r', encoding='utf-8') as f:
        hesytoken = f.read()  # 获取cookies
        f.close()
        return hesytoken

"""登录业务员APP后产生的salesman_token"""
def SalesmanToken():
    with open('F:/pyhcarm/hezongyy/API-Auto/SaveParam/SalesmanToken.txt', 'r', encoding='utf-8') as f:
        hesytoken = f.read()  # 获取cookies
        f.close()
        return hesytoken




# print(UserLoginToken())