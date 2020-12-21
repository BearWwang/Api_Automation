# API_Automation
基于Pytest+request+Allure的接口自动化开源框架

----
### Common 公共包
  >> #### 公共包模块类设计      
  > >`Request.py` 封装request方法，可以支持多协议扩展（get\post\put）
>>
   > >`Config.py`读取配置文件，包括：不同环境的配置，email相关配置
>   >
   >>`Log.py` 封装记录log方法，分为：debug、info、warning、error、critical
>   >
   > >`Email.py`封装smtplib方法，运行结果发送邮件通知
>   >
   > >`Assert.py` 封装assert方法
>    >
   > >`Hash.py` 封装常用加密方法
>    >
   >> `Session.py` 封装获取登录cookies方法
>  > 
  > >`GToken.py` 封装跨文件全局变量方法
>>
  > >`Methodes.py` 封装接口 path 过滤方法
>>
 >  >`Mysql_operate.py` 封装MySQL操作方法
### Config 配置包
  >>#### 模块类设计
>>
  >>`Config.ini` 环境配置文件
>>
 > > `Config.py` 封装配置文件读写方法
### Log 日志包
 >>日志文件路径，用于存储error 及info 及log文件    
### Mode body_data 参数处理包
>>`body_data.py` 封装request请求参数处理方法
### Params 数据驱动核心包
>>#### 模块类设计
>>Param  测试用例集 路径包
>>
>>`params.py` 封装测试用例集解析方法
>>
>> `tools.py` 封装测试用例集读取方法 
### Repoty Html报告路径包
### TestCase 测试用例执行包
>>#### 模块类设计
>>`xx_test.py` 封装测试用例执行方法
>
`conftest.py` 封装pytest 钩子及 html 修改 方法

`run.py` 核心代码。定义并执行用例集，生成报告 

### 流程图TD
```mermaid
graph TD
A[run.py] -- start--> B{Config};
S[Log 记录log];
R{SMTP};
B  --> D{pytest.allure} --NO-->H[无有效用例];
H-->R;
D --&--> E[allure 定义用例集];
D --Yes--> F{pytest 执行};
F -->G{pytest.fixture 初始化测试数据 };
G--No-->S
G --Yes -->I[定义运行环境];
I -- xx.yaml--params.py-->K{ 解析yaml 文件};
K--No-->S;
K--Yes-->L[tools.py 转换测试用例] -->M[Requesty 运行];
M -->N{Asser断言};
N--Yse-->Q[pytest_html]
Q -->R;
N--Fail-->S;
N--Success-->O[Allure];
H -->  S;
R --Fail -->S;
R--Yes-->T(end);



```

