import readConfig as readConfig

readconfig = readConfig.ReadConfig()

class geturlParams():# 定义一个方法，将从配置文件中读取的进行拼接
    """通过票据获取平台用户信息"""
    def get_Url1_1(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':38080' + '/SingleSignOn/find'
        #logger.info('new_url'+new_url)
        return new_url

    """用户登录"""
    def get_Url1_3(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':38080' + '/UserLogin/login'
        #logger.info('new_url'+new_url)
        return new_url

    """添加商品到购物车"""
    def get_Url2_1(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':10070' + '/goodsCart/addGoodsCart'
        # logger.info('new_url'+new_url)
        return new_url

if __name__ == '__main__':# 验证拼接后的正确性
    print(geturlParams().get_Url2_1())
