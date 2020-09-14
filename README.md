## selenium的持续集成演示demo

### 说明
此demo仅为了演示selenium的持续集成

使用pytest测试框架，yaml文件作为数据驱动，通过selenium技术在百度搜索词汇

- driver.ini：chromedriver路径配置文件

- data.yml：参数化文件

- test_simple_show.py：测试用例

访问[演示网站](http://www.heng.show:8080)，登录演示账号（用户名：guest、密码：password），任务列表中的SeleniumDemo为本项目，在项目中点击Build with Parameters选项，通过is_headless参数控制是否采用无头模式