from collections import Counter

# 把你题目里的项目原文粘到这里（保持一行一个即可）
raw_text = """
智能学习平台，点评

鱼皮ai超级智能体和智能云图库
黑马点评plus、大麦
xfg拼团_商城_agent
xfg抽奖，ai代码评审，正在做holis的两个项目
ai知识库 规则引擎
多模态测试智能体
魔改点评
字节青训营电商项目
知光平台

12306
学校上线项目、Agent 正在看

点评，agent
魔改点评、Agent

点评 外卖
点评，mit6.530数据库
知光➕点评
知光 + agent


点评 + agent
知光和点评
知光

知光，短链接
知光，agent

点评+小林的agent
点评+知光
天机 点评
魔改点评+知光
业务项目+知光+想再做个agent
xfg的拼团
zhiguang xfg的aiagent
教育商城项目 + 再做个agent
二哥的rag 知光
点评+知光
牛券
api开放平台
点评+小林agent
短链接+知光
xfg拼团、小型商场
点评，知光
点评，知光
外卖、点评、微服务商城、简易慕课
外卖 实习项目
定时器微服务项目+xfg智能体
黑马点评plus+实习项目
点评，外卖
魔改商城项目+agent
xfg拼团以及AIAgent
知光+手撕rpc框架
自己的rpc框架+AI面试系统
点评 高考志愿ai平台
12306+agent
点评+知光
点评➕Agent(正在做)

rpc＋商城
天机 点评
短链 点评
xfg拼团交易系统，智能体station 
外卖，天机，点评，hollis刚开始
php，javaweb
xfg大营销，agent智能体
点评 
外卖＋头条＋商城
知光+一个agent项目
点评外卖，还有个仿Claudecode的项目在学
点评+agent
外卖，开源项目，Agent项目
天机智能体，云岚
PC客户端
ai智能刷题
agent项目
两个hollis项目，有一个还在写
一个综合天机和agent技术自己写的项目。一个学校上线用的项目
自研玩具+12306
云图库，还有一个agent项目正在学
知光+点评
IM+ai
个人博客
大麦+天机学堂
点评+agent
短链+12306
云岚，AI的agent项目
鱼皮智能体和云图库
天机+im
xfg拼团_商城_agent
组件库+低代码
IM+天幕
外卖点评，正在做xfg的拼团


一个ai一个实习项目

外卖点评，一个仿Claude Code项目
自己写的演唱会购票系统+ 鱼皮聚搜项目
鱼皮的零代码项目
知识星球二哥两个项目（可能替换其中一个为外卖点评）
外卖点评，一个短链接项目
外卖点评
点评+代驾
点评+agent（正在学）
点评+外卖
点评+agent
点评 + 鱼皮ai超级智能体
cpp聊天项目+java正在自学
外卖
xfg的拼团agent + 自研deep research
无
和别人接的几个外包项目 + 鱼皮的ai零代码
外卖、点评
12306+点评
小兔鲜，工业故障，微信小程序（正在）
外卖
点评
天机学堂+xfg agent（在学）
天机AI、二哥派聪明
""".strip("\n")

# 1. 预处理成行列表
lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
total = len(lines)
print(f"总条目数: {total}\n")

# 2. 定义一些粗粒度的“项目类别 -> 关键词”
categories = {
    "点评类": ["点评", "黑马点评", "外卖点评", "魔改点评"],
    "外卖类": ["外卖"],
    "Agent/智能体": ["agent", "Agent", "智能体", "deep research"],
    "知光": ["知光", "zhiguang"],
    "xfg 系列": ["xfg"],
    "12306/购票": ["12306", "演唱会购票"],
    "天机/天机学堂": ["天机", "天机学堂"],
    "云图库/零代码": ["云图库", "零代码"],
    "IM/聊天": ["IM", "聊天"],
    "短链/短链接": ["短链", "短链接"],
    "商城/电商": ["商城", "电商", "小兔鲜", "大麦", "微服务商城"],
    "RAG/知识库": ["rag", "RAG", "知识库"],
    "RPC/中间件": ["rpc", "RPC"],
    "个人/博客": ["博客", "个人博客"],
    "实习/外包": ["实习", "外包"],
}

# 3. 统计：一行可以命中多个类别
cat_counter = Counter()
unmatched_lines = []

for line in lines:
    matched = False
    for cat, kws in categories.items():
        if any(kw in line for kw in kws):
            cat_counter[cat] += 1
            matched = True
    if not matched:
        unmatched_lines.append(line)

# 4. 输出结果：按出现次数排序
print("按项目类别统计：")
for cat, cnt in cat_counter.most_common():
    ratio = cnt / total * 100
    print(f"- {cat}: {cnt} 条 ({ratio:.1f}%)")

# 5. 也可以看看没被任何类别命中的条目，方便你调整关键词
print("\n未命中任何预设类别的条目示例（最多展示 15 条）：")
for line in unmatched_lines[:15]:
    print("  -", line)