from selenium import webdriver
import time

'''在这个地方我遇到错误了,之前是把bin后面的路径和exe程序我都没有加上,后面单单只加bin的话,提示没有把phantomJS加到PATH中,
后续我也没有加,因为\b被转义了,我在前面加r问题解决,加r就是不转义,按照原本的符号来弄显示的,
后面就行了
'''
driver = webdriver.PhantomJS(executable_path=r'D:\Program\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
