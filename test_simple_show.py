import configparser
import os
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSimpleShow:

    with open("data.yml") as f:
        data = yaml.safe_load(f)

    def setup_class(self):
        # 通过配置文件获取driver路径
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'driver.ini'))
        path = config.get('driver', 'chrome_driver')

        opt = webdriver.ChromeOptions()

        # 是否无头模式（即是否打开浏览器）
        # true：是（不打开浏览，无界面）
        # false：否（打开浏览器，有界面）
        try:
            is_headless = os.environ["is_headless"]
            if is_headless.lower() == 'true':
                print("参数 is_headless 为 true，使用无界面方式运行")
                opt.add_argument("--headless")
        except KeyError:
            print("没有配置 is_headless 参数，使用有界面方式运行")

        self.driver = webdriver.Chrome(executable_path=path, options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        print("打开百度首页")
        self.driver.get("https://www.baidu.com")
        assert "百度一下" in self.driver.title

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("key", data)
    def test_simple_show(self, key):
        print(f"使用百度搜索关键词：{key}")
        self.driver.find_element(By.ID, "kw").clear()
        self.driver.find_element(By.ID, "kw").send_keys(key)
        self.driver.find_element(By.ID, "su").click()
        sleep(2)
