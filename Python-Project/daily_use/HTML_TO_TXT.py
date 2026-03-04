from bs4 import BeautifulSoup

# 将你的 HTML 代码放入这个变量
html_data = """<div class="video-pod__list multip list" data-v-dac4fbd2=""><div data-key="27660389247" class="simple-base-item video-pod__item active normal" data-v-dac4fbd2="" data-scrolled="true"><div title="01.Web开发-导学视频" class="title"><div class="playing-gif" style="display:;"></div> <div class="title-txt">01.Web开发-导学视频</div></div> <div class="stats"><div class="stat-item duration">
        22:35
      </div></div></div><div data-key="27660389450" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="02.Web前端开发初识" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">02.Web前端开发初识</div></div> <div class="stats"><div class="stat-item duration">
        13:16
      </div></div></div><div data-key="27660389786" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="03.HTML-CSS-入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">03.HTML-CSS-入门程序</div></div> <div class="stats"><div class="stat-item duration">
        26:27
      </div></div></div><div data-key="27090487468" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="04. HTML-CSS-VsCode开发工具" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">04. HTML-CSS-VsCode开发工具</div></div> <div class="stats"><div class="stat-item duration">
        31:31
      </div></div></div><div data-key="26421496424" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="05. HTML-CSS-常见标签和样式-央视新闻-标题-排版" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">05. HTML-CSS-常见标签和样式-央视新闻-标题-排版</div></div> <div class="stats"><div class="stat-item duration">
        16:44
      </div></div></div><div data-key="26421559438" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="06. HTML-CSS-常见标签和样式-央视新闻-标题-样式" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">06. HTML-CSS-常见标签和样式-央视新闻-标题-样式</div></div> <div class="stats"><div class="stat-item duration">
        26:01
      </div></div></div><div data-key="26421560327" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="07. HTML-CSS-常见标签和样式-央视新闻-标题-样式(选择器)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">07. HTML-CSS-常见标签和样式-央视新闻-标题-样式(选择器)</div></div> <div class="stats"><div class="stat-item duration">
        15:45
      </div></div></div><div data-key="26421560897" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="08. HTML-CSS-常见标签和样式-央视新闻-正文-排版" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">08. HTML-CSS-常见标签和样式-央视新闻-正文-排版</div></div> <div class="stats"><div class="stat-item duration">
        27:51
      </div></div></div><div data-key="26421562568" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="09. HTML-CSS-常见标签和样式-央视新闻-正文-样式" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">09. HTML-CSS-常见标签和样式-央视新闻-正文-样式</div></div> <div class="stats"><div class="stat-item duration">
        11:31
      </div></div></div><div data-key="26421563173" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="10. HTML-CSS-常见标签和样式-央视新闻-整体布局" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">10. HTML-CSS-常见标签和样式-央视新闻-整体布局</div></div> <div class="stats"><div class="stat-item duration">
        31:04
      </div></div></div><div data-key="26421625536" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="11. HTML-CSS-常见标签和样式-tlias案例-顶部导航栏" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">11. HTML-CSS-常见标签和样式-tlias案例-顶部导航栏</div></div> <div class="stats"><div class="stat-item duration">
        30:00
      </div></div></div><div data-key="26421626224" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="12. HTML-CSS-常见标签和样式-表单标签" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">12. HTML-CSS-常见标签和样式-表单标签</div></div> <div class="stats"><div class="stat-item duration">
        17:57
      </div></div></div><div data-key="26421626574" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="13. HTML-CSS-常见标签和样式-表单项标签" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">13. HTML-CSS-常见标签和样式-表单项标签</div></div> <div class="stats"><div class="stat-item duration">
        17:37
      </div></div></div><div data-key="26421627311" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="14. HTML-CSS-常见标签和样式-tlias案例-搜索表单区域" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">14. HTML-CSS-常见标签和样式-tlias案例-搜索表单区域</div></div> <div class="stats"><div class="stat-item duration">
        17:01
      </div></div></div><div data-key="26421628020" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="15. HTML-CSS-常见标签和样式-tlias案例-底部版权区域" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">15. HTML-CSS-常见标签和样式-tlias案例-底部版权区域</div></div> <div class="stats"><div class="stat-item duration">
        25:59
      </div></div></div><div data-key="26421628756" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="16. HTML-CSS-课程总结" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">16. HTML-CSS-课程总结</div></div> <div class="stats"><div class="stat-item duration">
        10:01
      </div></div></div><div data-key="26421690556" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="17. JS-课程介绍" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">17. JS-课程介绍</div></div> <div class="stats"><div class="stat-item duration">
        06:07
      </div></div></div><div data-key="26421690715" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="18. JS-核心语法-引入方式" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">18. JS-核心语法-引入方式</div></div> <div class="stats"><div class="stat-item duration">
        10:27
      </div></div></div><div data-key="26421691123" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="19. JS-核心语法-变量&amp;数据类型" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">19. JS-核心语法-变量&amp;数据类型</div></div> <div class="stats"><div class="stat-item duration">
        22:32
      </div></div></div><div data-key="26421691521" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="20. JS-核心语法-函数" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">20. JS-核心语法-函数</div></div> <div class="stats"><div class="stat-item duration">
        12:18
      </div></div></div><div data-key="26421691821" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="21. JS-核心语法-自定义对象&amp;JSON" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">21. JS-核心语法-自定义对象&amp;JSON</div></div> <div class="stats"><div class="stat-item duration">
        21:01
      </div></div></div><div data-key="26421692096" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="22. JS-核心语法-DOM" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">22. JS-核心语法-DOM</div></div> <div class="stats"><div class="stat-item duration">
        18:47
      </div></div></div><div data-key="26421692940" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="23. JS-事件监听-语法&amp;常见事件" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">23. JS-事件监听-语法&amp;常见事件</div></div> <div class="stats"><div class="stat-item duration">
        31:03
      </div></div></div><div data-key="26421693959" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="24. JS-事件监听-常见事件(优化-JS模块化)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">24. JS-事件监听-常见事件(优化-JS模块化)</div></div> <div class="stats"><div class="stat-item duration">
        13:14
      </div></div></div><div data-key="26421694324" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="25. Vue-快速入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">25. Vue-快速入门</div></div> <div class="stats"><div class="stat-item duration">
        26:10
      </div></div></div><div data-key="26421756798" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="26. Vue-常用指令-v-for" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">26. Vue-常用指令-v-for</div></div> <div class="stats"><div class="stat-item duration">
        25:08
      </div></div></div><div data-key="26421757767" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="27. Vue-常用指令-v-bind&amp;v-if&amp;v-show" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">27. Vue-常用指令-v-bind&amp;v-if&amp;v-show</div></div> <div class="stats"><div class="stat-item duration">
        19:37
      </div></div></div><div data-key="26421758127" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="28. Vue-常用指令-v-model与v-on" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">28. Vue-常用指令-v-model与v-on</div></div> <div class="stats"><div class="stat-item duration">
        25:33
      </div></div></div><div data-key="26421758844" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="29. Ajax-入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">29. Ajax-入门</div></div> <div class="stats"><div class="stat-item duration">
        25:23
      </div></div></div><div data-key="26421759802" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="30. Ajax-案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">30. Ajax-案例</div></div> <div class="stats"><div class="stat-item duration">
        24:43
      </div></div></div><div data-key="26421821884" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="31. Maven-课程介绍" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">31. Maven-课程介绍</div></div> <div class="stats"><div class="stat-item duration">
        17:35
      </div></div></div><div data-key="26421822380" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="32. Maven-概述-介绍&amp;安装" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">32. Maven-概述-介绍&amp;安装</div></div> <div class="stats"><div class="stat-item duration">
        21:55
      </div></div></div><div data-key="26421822998" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="33. Maven-IDEA集成" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">33. Maven-IDEA集成</div></div> <div class="stats"><div class="stat-item duration">
        23:58
      </div></div></div><div data-key="26421823579" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="34. Maven-依赖管理" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">34. Maven-依赖管理</div></div> <div class="stats"><div class="stat-item duration">
        26:18
      </div></div></div><div data-key="26421824446" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="35. 单元测试-概述&amp;入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">35. 单元测试-概述&amp;入门</div></div> <div class="stats"><div class="stat-item duration">
        23:09
      </div></div></div><div data-key="26436567686" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="36. 单元测试-断言&amp;常见注解" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">36. 单元测试-断言&amp;常见注解</div></div> <div class="stats"><div class="stat-item duration">
        27:35
      </div></div></div><div data-key="26436567925" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="37. 单元测试-企业开发规范&amp;AI生成生成单元测试" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">37. 单元测试-企业开发规范&amp;AI生成生成单元测试</div></div> <div class="stats"><div class="stat-item duration">
        28:31
      </div></div></div><div data-key="26421887616" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="38. 单元测试-Maven依赖范围" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">38. 单元测试-Maven依赖范围</div></div> <div class="stats"><div class="stat-item duration">
        10:12
      </div></div></div><div data-key="26421888170" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="39. Maven-常见问题解决方案" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">39. Maven-常见问题解决方案</div></div> <div class="stats"><div class="stat-item duration">
        05:38
      </div></div></div><div data-key="26421888286" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="40. Web基础-课程安排" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">40. Web基础-课程安排</div></div> <div class="stats"><div class="stat-item duration">
        09:22
      </div></div></div><div data-key="26421888764" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="41. Web基础-SpringBootWeb入门-入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">41. Web基础-SpringBootWeb入门-入门程序</div></div> <div class="stats"><div class="stat-item duration">
        28:16
      </div></div></div><div data-key="26421889513" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="42. Web基础-SpringBootWeb入门-入门解析" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">42. Web基础-SpringBootWeb入门-入门解析</div></div> <div class="stats"><div class="stat-item duration">
        11:32
      </div></div></div><div data-key="26421889968" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="43. Web基础-HTTP协议-概述" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">43. Web基础-HTTP协议-概述</div></div> <div class="stats"><div class="stat-item duration">
        10:11
      </div></div></div><div data-key="26421890251" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="44. Web基础-HTTP协议-请求协议" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">44. Web基础-HTTP协议-请求协议</div></div> <div class="stats"><div class="stat-item duration">
        20:39
      </div></div></div><div data-key="26421890640" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="45. Web基础-HTTP协议-响应协议" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">45. Web基础-HTTP协议-响应协议</div></div> <div class="stats"><div class="stat-item duration">
        25:41
      </div></div></div><div data-key="26421953249" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="46. Web基础-SpringBootWeb案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">46. Web基础-SpringBootWeb案例</div></div> <div class="stats"><div class="stat-item duration">
        38:42
      </div></div></div><div data-key="26421954779" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="47. Web基础-分层解耦-三层架构" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">47. Web基础-分层解耦-三层架构</div></div> <div class="stats"><div class="stat-item duration">
        22:28
      </div></div></div><div data-key="26421955703" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="48. Web基础-分层解耦-IOC与DI入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">48. Web基础-分层解耦-IOC与DI入门</div></div> <div class="stats"><div class="stat-item duration">
        18:17
      </div></div></div><div data-key="26562464314" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="49. Web基础-分层解耦-IOC&amp;DI详解" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">49. Web基础-分层解耦-IOC&amp;DI详解</div></div> <div class="stats"><div class="stat-item duration">
        41:53
      </div></div></div><div data-key="26422018284" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="50. MySQL-课程介绍" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">50. MySQL-课程介绍</div></div> <div class="stats"><div class="stat-item duration">
        13:30
      </div></div></div><div data-key="26422018852" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="51. MySQL-概述-安装&amp;数据模型" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">51. MySQL-概述-安装&amp;数据模型</div></div> <div class="stats"><div class="stat-item duration">
        27:06
      </div></div></div><div data-key="26562464644" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="52. MySQL-SQL-DDL-数据库操作&amp;图形化工具" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">52. MySQL-SQL-DDL-数据库操作&amp;图形化工具</div></div> <div class="stats"><div class="stat-item duration">
        30:48
      </div></div></div><div data-key="26562464694" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="53. MySQL-SQL-DDL-表操作-创建表" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">53. MySQL-SQL-DDL-表操作-创建表</div></div> <div class="stats"><div class="stat-item duration">
        30:27
      </div></div></div><div data-key="26422020727" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="54. MySQL-SQL-DDL-表操作-数据类型" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">54. MySQL-SQL-DDL-表操作-数据类型</div></div> <div class="stats"><div class="stat-item duration">
        20:25
      </div></div></div><div data-key="26562464816" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="55. MySQL-SQL-DDL-表操作-设计表案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">55. MySQL-SQL-DDL-表操作-设计表案例</div></div> <div class="stats"><div class="stat-item duration">
        26:46
      </div></div></div><div data-key="26422083689" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="56. MySQL-SQL-DDL-表操作-查询-修改-删除" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">56. MySQL-SQL-DDL-表操作-查询-修改-删除</div></div> <div class="stats"><div class="stat-item duration">
        15:42
      </div></div></div><div data-key="26422083958" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="57. MySQL-SQL-DML-insert&amp;update&amp;delete" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">57. MySQL-SQL-DML-insert&amp;update&amp;delete</div></div> <div class="stats"><div class="stat-item duration">
        30:20
      </div></div></div><div data-key="26422084703" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="58. MySQL-SQL-DQL-基本查询" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">58. MySQL-SQL-DQL-基本查询</div></div> <div class="stats"><div class="stat-item duration">
        18:43
      </div></div></div><div data-key="26422085275" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="59. MySQL-SQL-DQL-条件查询" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">59. MySQL-SQL-DQL-条件查询</div></div> <div class="stats"><div class="stat-item duration">
        21:26
      </div></div></div><div data-key="26422086084" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="60. MySQL-SQL-DQL-分组查询" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">60. MySQL-SQL-DQL-分组查询</div></div> <div class="stats"><div class="stat-item duration">
        23:28
      </div></div></div><div data-key="26422086726" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="61. MySQL-SQL-DQL-排序查询&amp;分页查询" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">61. MySQL-SQL-DQL-排序查询&amp;分页查询</div></div> <div class="stats"><div class="stat-item duration">
        19:59
      </div></div></div><div data-key="26422087322" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="62. JDBC-入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">62. JDBC-入门程序</div></div> <div class="stats"><div class="stat-item duration">
        22:50
      </div></div></div><div data-key="26422149701" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="63. JDBC-执行DQL语句" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">63. JDBC-执行DQL语句</div></div> <div class="stats"><div class="stat-item duration">
        21:09
      </div></div></div><div data-key="26422150530" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="64. JDBC-预编译SQL" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">64. JDBC-预编译SQL</div></div> <div class="stats"><div class="stat-item duration">
        21:51
      </div></div></div><div data-key="26422151280" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="65. Mybatis-入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">65. Mybatis-入门程序</div></div> <div class="stats"><div class="stat-item duration">
        26:13
      </div></div></div><div data-key="26422152354" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="66. Mybatis-辅助配置&amp;JDBC VS Mybatis" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">66. Mybatis-辅助配置&amp;JDBC VS Mybatis</div></div> <div class="stats"><div class="stat-item duration">
        15:51
      </div></div></div><div data-key="26422152594" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="67. Mybatis-数据库连接池" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">67. Mybatis-数据库连接池</div></div> <div class="stats"><div class="stat-item duration">
        15:41
      </div></div></div><div data-key="26422153162" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="68. Mybatis-增删改查-删除操作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">68. Mybatis-增删改查-删除操作</div></div> <div class="stats"><div class="stat-item duration">
        16:07
      </div></div></div><div data-key="26422215381" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="69. Mybatis-增删改查-新增操作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">69. Mybatis-增删改查-新增操作</div></div> <div class="stats"><div class="stat-item duration">
        09:12
      </div></div></div><div data-key="26422215505" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="70. Mybatis-增删改查-更新操作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">70. Mybatis-增删改查-更新操作</div></div> <div class="stats"><div class="stat-item duration">
        06:44
      </div></div></div><div data-key="26422215875" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="71. Mybatis-增删改查-查询操作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">71. Mybatis-增删改查-查询操作</div></div> <div class="stats"><div class="stat-item duration">
        20:49
      </div></div></div><div data-key="26422216994" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="72. Mybatis-XML映射配置" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">72. Mybatis-XML映射配置</div></div> <div class="stats"><div class="stat-item duration">
        28:53
      </div></div></div><div data-key="26422217895" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="73. SpringBoot项目配置文件" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">73. SpringBoot项目配置文件</div></div> <div class="stats"><div class="stat-item duration">
        23:20
      </div></div></div><div data-key="26562334515" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="74. 准备工作-开发规范-开发模式" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">74. 准备工作-开发规范-开发模式</div></div> <div class="stats"><div class="stat-item duration">
        18:51
      </div></div></div><div data-key="26562397023" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="75. 准备工作-开发规范-Restful" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">75. 准备工作-开发规范-Restful</div></div> <div class="stats"><div class="stat-item duration">
        21:02
      </div></div></div><div data-key="26562397602" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="76. 准备工作-工程搭建" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">76. 准备工作-工程搭建</div></div> <div class="stats"><div class="stat-item duration">
        22:25
      </div></div></div><div data-key="26562398951" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="77. 部门管理-列表查询-接口开发" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">77. 部门管理-列表查询-接口开发</div></div> <div class="stats"><div class="stat-item duration">
        30:38
      </div></div></div><div data-key="26562461855" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="78. 部门管理-列表查询-结果封装" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">78. 部门管理-列表查询-结果封装</div></div> <div class="stats"><div class="stat-item duration">
        10:35
      </div></div></div><div data-key="26562462360" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="79. 部门管理-列表查询-前后端联调测试" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">79. 部门管理-列表查询-前后端联调测试</div></div> <div class="stats"><div class="stat-item duration">
        23:24
      </div></div></div><div data-key="26562463169" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="80. 部门管理-删除部门-接口开发" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">80. 部门管理-删除部门-接口开发</div></div> <div class="stats"><div class="stat-item duration">
        32:05
      </div></div></div><div data-key="26562464347" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="81. 部门管理-新增部门-接口开发" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">81. 部门管理-新增部门-接口开发</div></div> <div class="stats"><div class="stat-item duration">
        21:07
      </div></div></div><div data-key="26562593330" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="82. 部门管理-修改部门-查询回显" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">82. 部门管理-修改部门-查询回显</div></div> <div class="stats"><div class="stat-item duration">
        19:26
      </div></div></div><div data-key="26562594054" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="83. 部门管理-修改部门-修改数据" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">83. 部门管理-修改部门-修改数据</div></div> <div class="stats"><div class="stat-item duration">
        20:58
      </div></div></div><div data-key="26664307070" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="84. 日志技术-Logback入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">84. 日志技术-Logback入门程序</div></div> <div class="stats"><div class="stat-item duration">
        21:22
      </div></div></div><div data-key="26664307739" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="85. 日志技术-Logback配置文件&amp;日志级别" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">85. 日志技术-Logback配置文件&amp;日志级别</div></div> <div class="stats"><div class="stat-item duration">
        30:59
      </div></div></div><div data-key="26664370423" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="86. 多表关系-一对多" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">86. 多表关系-一对多</div></div> <div class="stats"><div class="stat-item duration">
        33:13
      </div></div></div><div data-key="26664371670" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="87. 多表关系-一对一&amp;多对多" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">87. 多表关系-一对一&amp;多对多</div></div> <div class="stats"><div class="stat-item duration">
        16:29
      </div></div></div><div data-key="26664372091" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="88. 多表关系-多表设计案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">88. 多表关系-多表设计案例</div></div> <div class="stats"><div class="stat-item duration">
        18:17
      </div></div></div><div data-key="26664372790" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="89. 多表查询-概述" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">89. 多表查询-概述</div></div> <div class="stats"><div class="stat-item duration">
        13:44
      </div></div></div><div data-key="26664373854" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="90. 多表查询-内连接&amp;外连接" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">90. 多表查询-内连接&amp;外连接</div></div> <div class="stats"><div class="stat-item duration">
        26:59
      </div></div></div><div data-key="26664436009" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="91. 多表查询-子查询" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">91. 多表查询-子查询</div></div> <div class="stats"><div class="stat-item duration">
        27:15
      </div></div></div><div data-key="26664436877" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="92. 多表查询-案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">92. 多表查询-案例</div></div> <div class="stats"><div class="stat-item duration">
        22:00
      </div></div></div><div data-key="26769690398" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="93. 员工管理-准备工作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">93. 员工管理-准备工作</div></div> <div class="stats"><div class="stat-item duration">
        12:29
      </div></div></div><div data-key="26769752543" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="94. 员工管理-分页查询-原理分析" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">94. 员工管理-分页查询-原理分析</div></div> <div class="stats"><div class="stat-item duration">
        23:07
      </div></div></div><div data-key="26769753383" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="95. 员工管理-分页查询-代码实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">95. 员工管理-分页查询-代码实现</div></div> <div class="stats"><div class="stat-item duration">
        32:56
      </div></div></div><div data-key="26769754887" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="96. 员工管理-分页查询-PageHelper分页插件" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">96. 员工管理-分页查询-PageHelper分页插件</div></div> <div class="stats"><div class="stat-item duration">
        30:33
      </div></div></div><div data-key="26769818124" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="97. 员工管理-条件分页查询-基本实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">97. 员工管理-条件分页查询-基本实现</div></div> <div class="stats"><div class="stat-item duration">
        33:58
      </div></div></div><div data-key="26769819815" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="98. 员工管理-条件分页查询-程序优化" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">98. 员工管理-条件分页查询-程序优化</div></div> <div class="stats"><div class="stat-item duration">
        36:35
      </div></div></div><div data-key="26769821170" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="99. 员工管理-新增员工-保存员工基本信息" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">99. 员工管理-新增员工-保存员工基本信息</div></div> <div class="stats"><div class="stat-item duration">
        30:16
      </div></div></div><div data-key="26769883718" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="100. 员工管理-新增员工-批量保存员工工作经历" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">100. 员工管理-新增员工-批量保存员工工作经历</div></div> <div class="stats"><div class="stat-item duration">
        32:25
      </div></div></div><div data-key="26769885011" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="101. 事务管理-介绍与操作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">101. 事务管理-介绍与操作</div></div> <div class="stats"><div class="stat-item duration">
        19:36
      </div></div></div><div data-key="26769886170" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="102. 事务管理-Spring事务管理-介绍" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">102. 事务管理-Spring事务管理-介绍</div></div> <div class="stats"><div class="stat-item duration">
        15:52
      </div></div></div><div data-key="26769886822" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="103. 事务管理-Spring事务管理-进阶&amp;事务四大特性" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">103. 事务管理-Spring事务管理-进阶&amp;事务四大特性</div></div> <div class="stats"><div class="stat-item duration">
        38:56
      </div></div></div><div data-key="26769949571" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="104. 文件上传-介绍" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">104. 文件上传-介绍</div></div> <div class="stats"><div class="stat-item duration">
        26:05
      </div></div></div><div data-key="26769951002" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="105. 文件上传-本地存储" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">105. 文件上传-本地存储</div></div> <div class="stats"><div class="stat-item duration">
        19:48
      </div></div></div><div data-key="26769951903" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="106. 文件上传-阿里云OSS-准备工作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">106. 文件上传-阿里云OSS-准备工作</div></div> <div class="stats"><div class="stat-item duration">
        26:26
      </div></div></div><div data-key="26770014322" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="107. 文件上传-阿里云OSS-入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">107. 文件上传-阿里云OSS-入门程序</div></div> <div class="stats"><div class="stat-item duration">
        15:51
      </div></div></div><div data-key="26770015006" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="108. 文件上传-阿里云OSS-案例集成" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">108. 文件上传-阿里云OSS-案例集成</div></div> <div class="stats"><div class="stat-item duration">
        21:18
      </div></div></div><div data-key="26781093114" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="109. 文件上传-阿里云OSS-程序优化(@Value&amp;@ConfigurationProperties)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">109. 文件上传-阿里云OSS-程序优化(@Value&amp;@ConfigurationProperties)</div></div> <div class="stats"><div class="stat-item duration">
        21:18
      </div></div></div><div data-key="26893551142" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="110. 员工管理-删除员工-请求参数接收" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">110. 员工管理-删除员工-请求参数接收</div></div> <div class="stats"><div class="stat-item duration">
        16:50
      </div></div></div><div data-key="26893551962" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="111. 员工管理-删除员工-逻辑实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">111. 员工管理-删除员工-逻辑实现</div></div> <div class="stats"><div class="stat-item duration">
        13:29
      </div></div></div><div data-key="26893552908" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="112. 员工管理-修改员工-查询回显" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">112. 员工管理-修改员工-查询回显</div></div> <div class="stats"><div class="stat-item duration">
        31:36
      </div></div></div><div data-key="26893616889" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="113. 员工管理-修改员工-修改数据" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">113. 员工管理-修改员工-修改数据</div></div> <div class="stats"><div class="stat-item duration">
        22:09
      </div></div></div><div data-key="26893618568" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="114. 员工管理-修改员工-程序优化(动态更新)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">114. 员工管理-修改员工-程序优化(动态更新)</div></div> <div class="stats"><div class="stat-item duration">
        12:40
      </div></div></div><div data-key="26893681015" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="115. 全局异常处理器" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">115. 全局异常处理器</div></div> <div class="stats"><div class="stat-item duration">
        26:23
      </div></div></div><div data-key="26893682996" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="116. 员工信息统计-职位统计-分析" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">116. 员工信息统计-职位统计-分析</div></div> <div class="stats"><div class="stat-item duration">
        18:48
      </div></div></div><div data-key="26893684163" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="117. 员工信息统计-职位统计-实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">117. 员工信息统计-职位统计-实现</div></div> <div class="stats"><div class="stat-item duration">
        20:25
      </div></div></div><div data-key="26893746819" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="118. 员工信息统计-性别统计" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">118. 员工信息统计-性别统计</div></div> <div class="stats"><div class="stat-item duration">
        15:40
      </div></div></div><div data-key="26893747735" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="119. 项目实战-需求说明" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">119. 项目实战-需求说明</div></div> <div class="stats"><div class="stat-item duration">
        08:59
      </div></div></div><div data-key="27090488891" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="120. 登录认证-登录功能-实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">120. 登录认证-登录功能-实现</div></div> <div class="stats"><div class="stat-item duration">
        26:51
      </div></div></div><div data-key="27090551469" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="121. 登录认证-登录校验-会话技术-介绍" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">121. 登录认证-登录校验-会话技术-介绍</div></div> <div class="stats"><div class="stat-item duration">
        13:16
      </div></div></div><div data-key="27090551951" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="122. 登录认证-登录校验-会话技术-Cookie" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">122. 登录认证-登录校验-会话技术-Cookie</div></div> <div class="stats"><div class="stat-item duration">
        18:59
      </div></div></div><div data-key="27090552453" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="123. 登录认证-登录校验-会话技术-Session" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">123. 登录认证-登录校验-会话技术-Session</div></div> <div class="stats"><div class="stat-item duration">
        15:00
      </div></div></div><div data-key="27090553203" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="124. 登录认证-登录校验-会话技术-令牌方案" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">124. 登录认证-登录校验-会话技术-令牌方案</div></div> <div class="stats"><div class="stat-item duration">
        05:05
      </div></div></div><div data-key="27090553409" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="125. 登录认证-登录校验-JWT-生成与校验" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">125. 登录认证-登录校验-JWT-生成与校验</div></div> <div class="stats"><div class="stat-item duration">
        28:13
      </div></div></div><div data-key="27090554521" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="126. 登录认证-登录校验-JWT-登录成功后下发令牌" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">126. 登录认证-登录校验-JWT-登录成功后下发令牌</div></div> <div class="stats"><div class="stat-item duration">
        12:47
      </div></div></div><div data-key="27090616610" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="127. 登录认证-登录校验-Filter-入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">127. 登录认证-登录校验-Filter-入门</div></div> <div class="stats"><div class="stat-item duration">
        21:12
      </div></div></div><div data-key="27090617519" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="128. 登录认证-登录校验-Filter-令牌校验Filter" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">128. 登录认证-登录校验-Filter-令牌校验Filter</div></div> <div class="stats"><div class="stat-item duration">
        27:50
      </div></div></div><div data-key="27090618550" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="129. 登录认证-登录校验-Filter-详解" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">129. 登录认证-登录校验-Filter-详解</div></div> <div class="stats"><div class="stat-item duration">
        19:57
      </div></div></div><div data-key="27090619472" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="130. 登录认证-登录校验-Interceptor-入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">130. 登录认证-登录校验-Interceptor-入门</div></div> <div class="stats"><div class="stat-item duration">
        19:06
      </div></div></div><div data-key="27090681868" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="131. 登录认证-登录校验-Interceptor-令牌校验Interceptor" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">131. 登录认证-登录校验-Interceptor-令牌校验Interceptor</div></div> <div class="stats"><div class="stat-item duration">
        11:54
      </div></div></div><div data-key="27090682679" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="132. 登录认证-登录校验-Interceptor-详解" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">132. 登录认证-登录校验-Interceptor-详解</div></div> <div class="stats"><div class="stat-item duration">
        19:34
      </div></div></div><div data-key="27205109109" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="133. SpringAOP-基础-AOP入门程序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">133. SpringAOP-基础-AOP入门程序</div></div> <div class="stats"><div class="stat-item duration">
        28:18
      </div></div></div><div data-key="27205110761" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="134. SpringAOP-基础-核心概念" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">134. SpringAOP-基础-核心概念</div></div> <div class="stats"><div class="stat-item duration">
        17:34
      </div></div></div><div data-key="27205173253" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="135. SpringAOP-进阶-通知类型" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">135. SpringAOP-进阶-通知类型</div></div> <div class="stats"><div class="stat-item duration">
        22:04
      </div></div></div><div data-key="27205174447" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="136. SpringAOP-进阶-通知顺序" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">136. SpringAOP-进阶-通知顺序</div></div> <div class="stats"><div class="stat-item duration">
        09:03
      </div></div></div><div data-key="27205174888" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="137. SpringAOP-进阶-切入点表达式" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">137. SpringAOP-进阶-切入点表达式</div></div> <div class="stats"><div class="stat-item duration">
        28:31
      </div></div></div><div data-key="27205175783" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="138. SpringAOP-进阶-连接点JoinPoint" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">138. SpringAOP-进阶-连接点JoinPoint</div></div> <div class="stats"><div class="stat-item duration">
        10:57
      </div></div></div><div data-key="27205176208" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="139. SpringAOP-案例-记录操作日志" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">139. SpringAOP-案例-记录操作日志</div></div> <div class="stats"><div class="stat-item duration">
        27:47
      </div></div></div><div data-key="27205238989" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="140. SpringAOP-案例-获取当前登录员工" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">140. SpringAOP-案例-获取当前登录员工</div></div> <div class="stats"><div class="stat-item duration">
        31:02
      </div></div></div><div data-key="27321044067" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="141. 原理篇-SpringBoot配置优先级" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">141. 原理篇-SpringBoot配置优先级</div></div> <div class="stats"><div class="stat-item duration">
        22:13
      </div></div></div><div data-key="27957528126" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="142. 原理篇-Bean管理" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">142. 原理篇-Bean管理</div></div> <div class="stats"><div class="stat-item duration">
        39:32
      </div></div></div><div data-key="27321107848" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="143. 原理篇-SpringBoot原理-起步依赖原理" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">143. 原理篇-SpringBoot原理-起步依赖原理</div></div> <div class="stats"><div class="stat-item duration">
        04:02
      </div></div></div><div data-key="27321108199" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="144. 原理篇-SpringBoot原理-自动配置-两种方案" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">144. 原理篇-SpringBoot原理-自动配置-两种方案</div></div> <div class="stats"><div class="stat-item duration">
        34:27
      </div></div></div><div data-key="27321110200" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="145. 原理篇-SpringBoot原理-自动配置-源码跟踪" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">145. 原理篇-SpringBoot原理-自动配置-源码跟踪</div></div> <div class="stats"><div class="stat-item duration">
        22:30
      </div></div></div><div data-key="27321173398" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="146. 原理篇-SpringBoot原理-自动配置-源码跟踪(@Conditional)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">146. 原理篇-SpringBoot原理-自动配置-源码跟踪(@Conditional)</div></div> <div class="stats"><div class="stat-item duration">
        18:07
      </div></div></div><div data-key="27321174468" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="147. 原理篇-SpringBoot原理-自动配置-自定义starter" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">147. 原理篇-SpringBoot原理-自动配置-自定义starter</div></div> <div class="stats"><div class="stat-item duration">
        37:04
      </div></div></div><div data-key="27321237549" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="148. Maven高级-分模块设计与开发" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">148. Maven高级-分模块设计与开发</div></div> <div class="stats"><div class="stat-item duration">
        25:46
      </div></div></div><div data-key="27321238898" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="149. Maven高级-继承" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">149. Maven高级-继承</div></div> <div class="stats"><div class="stat-item duration">
        37:22
      </div></div></div><div data-key="27321240568" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="150. Maven高级-聚合" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">150. Maven高级-聚合</div></div> <div class="stats"><div class="stat-item duration">
        13:25
      </div></div></div><div data-key="27321241050" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="151. Maven高级-私服" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">151. Maven高级-私服</div></div> <div class="stats"><div class="stat-item duration">
        29:33
      </div></div></div><div data-key="27321303577" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="152. Web后端开发-总结" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">152. Web后端开发-总结</div></div> <div class="stats"><div class="stat-item duration">
        06:39
      </div></div></div><div data-key="27739424182" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="153. Vue工程化-介绍&amp;环境准备" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">153. Vue工程化-介绍&amp;环境准备</div></div> <div class="stats"><div class="stat-item duration">
        18:03
      </div></div></div><div data-key="27739424602" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="154. Vue工程化-vue项目介绍&amp;开发流程" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">154. Vue工程化-vue项目介绍&amp;开发流程</div></div> <div class="stats"><div class="stat-item duration">
        36:44
      </div></div></div><div data-key="27739424898" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="155. Vue工程化-API风格&amp;案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">155. Vue工程化-API风格&amp;案例</div></div> <div class="stats"><div class="stat-item duration">
        40:49
      </div></div></div><div data-key="27739425492" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="156. ElementPlus-快速入门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">156. ElementPlus-快速入门</div></div> <div class="stats"><div class="stat-item duration">
        22:31
      </div></div></div><div data-key="27739426215" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="157. ElementPlus-常见组件-表格组件&amp;分页组件" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">157. ElementPlus-常见组件-表格组件&amp;分页组件</div></div> <div class="stats"><div class="stat-item duration">
        31:48
      </div></div></div><div data-key="27739426710" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="158. ElementPlus-常见组件-对话框组件&amp;表单组件" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">158. ElementPlus-常见组件-对话框组件&amp;表单组件</div></div> <div class="stats"><div class="stat-item duration">
        28:39
      </div></div></div><div data-key="27739488357" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="159. ElementPlus-案例" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">159. ElementPlus-案例</div></div> <div class="stats"><div class="stat-item duration">
        38:42
      </div></div></div><div data-key="27789690482" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="160. Tlias案例-准备工作" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">160. Tlias案例-准备工作</div></div> <div class="stats"><div class="stat-item duration">
        23:52
      </div></div></div><div data-key="27789691032" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="161. Tlias案例-整体布局-动态菜单(VueRouter)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">161. Tlias案例-整体布局-动态菜单(VueRouter)</div></div> <div class="stats"><div class="stat-item duration">
        43:06
      </div></div></div><div data-key="27789692631" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="162. Tlias案例-整体布局-动态菜单(VueRouter-嵌套路由)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">162. Tlias案例-整体布局-动态菜单(VueRouter-嵌套路由)</div></div> <div class="stats"><div class="stat-item duration">
        21:51
      </div></div></div><div data-key="27789754832" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="163. Tlias案例-部门管理-列表查询" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">163. Tlias案例-部门管理-列表查询</div></div> <div class="stats"><div class="stat-item duration">
        34:02
      </div></div></div><div data-key="27789755744" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="164. Tlias案例-部门管理-列表查询-程序优化" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">164. Tlias案例-部门管理-列表查询-程序优化</div></div> <div class="stats"><div class="stat-item duration">
        35:32
      </div></div></div><div data-key="27789756386" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="165. Tlias案例-部门管理-新增部门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">165. Tlias案例-部门管理-新增部门</div></div> <div class="stats"><div class="stat-item duration">
        51:05
      </div></div></div><div data-key="27789757843" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="166. Tlias案例-部门管理-修改&amp;删除部门" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">166. Tlias案例-部门管理-修改&amp;删除部门</div></div> <div class="stats"><div class="stat-item duration">
        29:12
      </div></div></div><div data-key="27857521749" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="167. Tlias案例-员工管理-列表查询-页面布局(搜索栏)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">167. Tlias案例-员工管理-列表查询-页面布局(搜索栏)</div></div> <div class="stats"><div class="stat-item duration">
        21:12
      </div></div></div><div data-key="27857584131" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="168. Tlias案例-员工管理-列表查询-页面布局(搜索栏-watch侦听)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">168. Tlias案例-员工管理-列表查询-页面布局(搜索栏-watch侦听)</div></div> <div class="stats"><div class="stat-item duration">
        26:53
      </div></div></div><div data-key="27857584905" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="169. Tlias案例-员工管理-列表查询-页面布局(表格)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">169. Tlias案例-员工管理-列表查询-页面布局(表格)</div></div> <div class="stats"><div class="stat-item duration">
        24:33
      </div></div></div><div data-key="27857585812" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="170. Tlias案例-员工管理-列表查询-页面交互" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">170. Tlias案例-员工管理-列表查询-页面交互</div></div> <div class="stats"><div class="stat-item duration">
        19:18
      </div></div></div><div data-key="27857586477" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="171. Tlias案例-员工管理-新增员工-页面布局(引入)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">171. Tlias案例-员工管理-新增员工-页面布局(引入)</div></div> <div class="stats"><div class="stat-item duration">
        18:44
      </div></div></div><div data-key="27857588034" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="172. Tlias案例-员工管理-新增员工-页面布局(展示优化)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">172. Tlias案例-员工管理-新增员工-页面布局(展示优化)</div></div> <div class="stats"><div class="stat-item duration">
        25:52
      </div></div></div><div data-key="27857650060" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="173. Tlias案例-员工管理-新增员工-页面交互(工作经历)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">173. Tlias案例-员工管理-新增员工-页面交互(工作经历)</div></div> <div class="stats"><div class="stat-item duration">
        30:01
      </div></div></div><div data-key="27857651215" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="174. Tlias案例-员工管理-新增员工-页面交互(保存员工)" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">174. Tlias案例-员工管理-新增员工-页面交互(保存员工)</div></div> <div class="stats"><div class="stat-item duration">
        32:28
      </div></div></div><div data-key="27917486352" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="175. Tlias案例-员工管理-修改员工-修改数据" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">175. Tlias案例-员工管理-修改员工-修改数据</div></div> <div class="stats"><div class="stat-item duration">
        22:07
      </div></div></div><div data-key="27917487251" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="176. Tlias案例-员工管理-删除员工-批量删除" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">176. Tlias案例-员工管理-删除员工-批量删除</div></div> <div class="stats"><div class="stat-item duration">
        24:45
      </div></div></div><div data-key="27917549764" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="177. Tlias案例-登录-登录功能实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">177. Tlias案例-登录-登录功能实现</div></div> <div class="stats"><div class="stat-item duration">
        22:00
      </div></div></div><div data-key="27917550555" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="178. Tlias案例-登录-携带令牌访问服务端" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">178. Tlias案例-登录-携带令牌访问服务端</div></div> <div class="stats"><div class="stat-item duration">
        24:56
      </div></div></div><div data-key="27917551384" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="179. Tlias案例-登录-响应401跳转登录页面" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">179. Tlias案例-登录-响应401跳转登录页面</div></div> <div class="stats"><div class="stat-item duration">
        13:03
      </div></div></div><div data-key="27917552129" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="180. Tlias案例-退出-功能实现" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">180. Tlias案例-退出-功能实现</div></div> <div class="stats"><div class="stat-item duration">
        15:12
      </div></div></div><div data-key="27917552564" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="181. Tlias案例-打包部署" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">181. Tlias案例-打包部署</div></div> <div class="stats"><div class="stat-item duration">
        20:23
      </div></div></div><div data-key="28307491491" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="182. Linux-概述-介绍&amp;系统安装" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">182. Linux-概述-介绍&amp;系统安装</div></div> <div class="stats"><div class="stat-item duration">
        27:49
      </div></div></div><div data-key="28307492281" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="183. Linux-概述-远程连接&amp;目录结构" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">183. Linux-概述-远程连接&amp;目录结构</div></div> <div class="stats"><div class="stat-item duration">
        14:25
      </div></div></div><div data-key="28307492661" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="184. Linux-常用命令-目录&amp;文件操作命令" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">184. Linux-常用命令-目录&amp;文件操作命令</div></div> <div class="stats"><div class="stat-item duration">
        37:23
      </div></div></div><div data-key="28307555691" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="185. Linux-常用命令-拷贝移动&amp;打包压缩命令" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">185. Linux-常用命令-拷贝移动&amp;打包压缩命令</div></div> <div class="stats"><div class="stat-item duration">
        24:31
      </div></div></div><div data-key="28307556350" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="186. Linux-常用命令-文本编辑&amp;查找命令" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">186. Linux-常用命令-文本编辑&amp;查找命令</div></div> <div class="stats"><div class="stat-item duration">
        26:42
      </div></div></div><div data-key="28307557520" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="187. Linux-软件安装-JDK安装" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">187. Linux-软件安装-JDK安装</div></div> <div class="stats"><div class="stat-item duration">
        16:06
      </div></div></div><div data-key="28307558123" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="188. Linux-软件安装-MySQL安装&amp;防火墙" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">188. Linux-软件安装-MySQL安装&amp;防火墙</div></div> <div class="stats"><div class="stat-item duration">
        34:25
      </div></div></div><div data-key="28307621150" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="189. Linux-软件安装-Nginx安装" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">189. Linux-软件安装-Nginx安装</div></div> <div class="stats"><div class="stat-item duration">
        12:20
      </div></div></div><div data-key="28307621678" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="190. Linux-项目部署" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">190. Linux-项目部署</div></div> <div class="stats"><div class="stat-item duration">
        34:49
      </div></div></div><div data-key="28385479419" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="191. Docker-入门-MySQL安装" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">191. Docker-入门-MySQL安装</div></div> <div class="stats"><div class="stat-item duration">
        28:03
      </div></div></div><div data-key="28385544026" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="192. Docker-入门-命令解读" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">192. Docker-入门-命令解读</div></div> <div class="stats"><div class="stat-item duration">
        11:25
      </div></div></div><div data-key="28385545542" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="193. Docker-核心-常见命令" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">193. Docker-核心-常见命令</div></div> <div class="stats"><div class="stat-item duration">
        28:47
      </div></div></div><div data-key="28385610389" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="194. Docker-核心-数据卷挂载" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">194. Docker-核心-数据卷挂载</div></div> <div class="stats"><div class="stat-item duration">
        25:01
      </div></div></div><div data-key="28385674391" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="195. Docker-核心-本地目录挂载" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">195. Docker-核心-本地目录挂载</div></div> <div class="stats"><div class="stat-item duration">
        23:24
      </div></div></div><div data-key="28385676179" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="196. Docker-核心-自定义镜像" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">196. Docker-核心-自定义镜像</div></div> <div class="stats"><div class="stat-item duration">
        31:49
      </div></div></div><div data-key="28385738850" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="197. Docker-核心-网络" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">197. Docker-核心-网络</div></div> <div class="stats"><div class="stat-item duration">
        16:06
      </div></div></div><div data-key="28385739789" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="198. Docker-部署-服务端&amp;前端部署" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">198. Docker-部署-服务端&amp;前端部署</div></div> <div class="stats"><div class="stat-item duration">
        31:52
      </div></div></div><div data-key="28385741153" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="199. Docker-部署-DockerCompose" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">199. Docker-部署-DockerCompose</div></div> <div class="stats"><div class="stat-item duration">
        30:01
      </div></div></div><div data-key="28385742454" class="simple-base-item video-pod__item normal" data-v-dac4fbd2=""><div title="200. Web开发-完结" class="title"><div class="playing-gif" style="display:none;"></div> <div class="title-txt">200. Web开发-完结</div></div> <div class="stats"><div class="stat-item duration">
        02:19
      </div></div></div></div>"""


def extract_bilibili_catalog(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 查找所有的视频条目容器
    items = soup.find_all('div', class_='video-pod__item')

    catalog_list = []

    for item in items:
        # 提取标题
        title_tag = item.find('div', class_='title-txt')
        title = title_tag.get_text(strip=True) if title_tag else "未知标题"

        # 提取时长
        duration_tag = item.find('div', class_='duration')
        duration = duration_tag.get_text(strip=True) if duration_tag else "00:00"

        catalog_list.append(f"{title}  ({duration})")

    return catalog_list


# 执行提取
results = extract_bilibili_catalog(html_data)

# 打印结果
for line in results:
    print(line)