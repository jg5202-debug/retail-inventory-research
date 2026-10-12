# 汇报讲解稿

英文幻灯片配中文讲解。第1–14页为主讲，约10–15分钟；第15–17页为问答附录。

## 第1页：Inventory Growth and Subsequent Operating Performance

开场约40秒：我研究零售企业存货增长超过收入增长时，下一年的毛利率和经营现金流表现是否更容易下降。项目结合SEC年度数据、会计口径核对、回归和年报案例。目前分析和报告已完成，但人工年报审核仍只覆盖部分记录。今天重点讲研究逻辑、主要证据，以及结论可以支持到什么程度。

来源：Final research report, 2026-10-11

## 第2页：Research question

这一页约50秒。核心假设是库存增长超过销售可能意味着备货超过需求，之后需要折扣或占用更多现金。但增长也可能来自开店、收购或补库存。因此这里检验关联，并结合年报区分经营背景。不能把正的存货增长差直接称为经营恶化。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第3页：Measures and annual timing

这页约60秒。存货增长差是存货增长率减收入增长率，例如存货增长30%、收入增长10%，差值是20个百分点。毛利率等于披露毛利除以分析收入，现金流比率等于经营现金流除以收入。每条记录依赖三个年度：用上一年和当年计算增长，用当年和下一年计算比率变化。存货和资产是期末余额，收入与现金流是期间发生额。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第4页：Candidate universe and usable samples

约60秒。候选池是人工选择的42家公司，覆盖五个研究者定义的业务组，它不是美国零售公司的完整总体或随机样本。共有656个年度记录，毛利率与现金流分别形成401和490条配对，两个结果共同可用的记录是399条。每家公司历史长度不同，构成不平衡面板。公司数量和年度记录数量应区分。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第5页：Research workflow

约60秒。十三个模块可以归纳为四个阶段：1到6先用AEO、ANF、URBN搭通流程；7到9扩大样本、检查覆盖并核对会计差异；10和11进行描述统计、敏感性和控制变量回归；12和13把年报证据落实到数据，再整理最终报告。最终运行顺序让12在10和11之前，保证审核决定能够进入统计结果。附录提供各模块的具体作用。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第6页：Accounting comparability and disclosure timing

约60秒。相同财务标签未必意味着相同费用范围。Module9解释了13条会计差额，包括四条DDS记录采用核对后的净销售额分母，并保留原始值。已知拆分、终止经营等变化会影响相邻年度配对。时间上，当期年报在目标财年开始后38至134天才披露，因此这是历史年度关联设计，不能视为目标年开始前形成的预测。

来源：Source: Module 9 reconciliation and Module 12 pairing audit

## 第7页：Descriptive differences

约60秒。左图比较毛利率次年变化，右图比较现金流比率次年变化。正差组与非正差组的毛利率平均变化接近，但现金流比率正差组表现更正向。这是按公司年度等权的描述结果，还未纳入充分控制。其方向与最初预期并不一致，需要检查起点和公司、年份因素。
图表数据来自expanded_inventory_group_summary.csv，增长差和比率变化单位都是百分点。

来源：Source: Module 10 pooled group summaries. Means are in percentage points

## 第8页：Regression specification

约60秒。主模型解释下一年的比率，控制当期比率、收入增长、对数资产、公司固定效应和目标年度固定效应。当期比率用于处理起点差异和回归常态；公司效应处理固定公司差异；年份效应处理共同年度影响。标准误按公司聚类，因为一家公司的多年记录可能相关。基期控制后的变化模型与水平模型有代数对应，并不是独立重复实验。高R平方也不等于预测准确率。

来源：Source: Module 11 model specifications and firm-clustered inference

## 第9页：Adjusted intervals include zero

约75秒。充分控制后，存货增长差每增加10个百分点，下一年毛利率关联约为负0.166个百分点，现金流比率关联约为正0.196个百分点。两者的95%区间都包含零，因此证据不足以支持稳定关联。这不能证明真实效应为零，也不能说明库存信息毫无价值。读数字时注意它是比率的百分点变化，不是收益率或下降概率。

来源：Source: Module 11 fully adjusted models. Firm-clustered 95% intervals

## 第10页：Adjusted sensitivity estimates

约70秒。四种样本条件分别为全部配对、没有明显年度长度变化的记录、两个结果共同可用的记录，以及存货增长差中间98%的记录。八条充分控制后的区间都包含零。敏感性既改变样本构成，也改变精度，所以不能当作八个独立实验。这里保留所有预先安排的条件，不按显著性挑选结果。

来源：Source: expanded_adjusted_regression_sensitivity.csv. Estimates and intervals are pp per 10pp gap

## 第11页：URBN: expansion and markdown pressure

约60秒。这条URBN案例当期存货增长差约为正5.98个百分点，次年毛利率下降约6.40个百分点，现金流比率下降约5.51个百分点。管理层提到新店和直接面向消费者渠道扩张影响了库存增长，次年滞销服饰降价与固定门店费用影响毛利。现金流下降主要与净利润下降有关，库存现金吸收反而较前一年减少。因此即使案例方向符合最初假设，也不能把所有现金流下降归因于库存。
来源：https://www.sec.gov/Archives/edgar/data/912615/000119312511085784/d10k.htm
https://www.sec.gov/Archives/edgar/data/912615/000119312512146029/d276682d10k.htm

来源：Source: URBN filings for periods ending 2011-01-31 and 2012-01-31

## 第12页：SPWH: demand and replenishment cycles

约75秒。疫情期间需求大增，存货下降，形成非常负的增长差。随后公司补库存、应付账款减少，现金流比率下降。库存大增后的下一年，库存占用现金的增量明显减少，物流成本也下降，毛利率和现金流比率改善。FY2021还收到5500万美元一次性并购终止款，影响现金流起点。两个案例都保留，说明同一个指标必须结合需求周期和现金流构成解释。
来源：https://www.sec.gov/Archives/edgar/data/1132105/000155837021003940/spwh-20210130x10k.htm
https://www.sec.gov/Archives/edgar/data/1132105/000155837022004698/spwh-20220129x10k.htm
https://www.sec.gov/Archives/edgar/data/1132105/000155837022004698/spwh-20220129x10k.htm
https://www.sec.gov/Archives/edgar/data/1132105/000095017023012621/spwh-20230128.htm

来源：Source: SPWH FY2020–FY2022 filings. All table values are percentage points

## 第13页：Review coverage and research limits

约70秒。目前完成两家公司资格、七个年度以及七条选定案例中的三条审核。整体样本仍为provisional。剩余四条案例是AKA、ARHS、ULTA和KSS，且多数公司历史尚未核查。其他限制包括人工候选名单、不平衡面板、费用口径差异和缺失字段。项目没有完成样本外预测、股票收益回测或因果识别。我们应如实交付有边界的结果。

来源：Source: Module 12 review readiness and applied review tables

## 第14页：Research contribution and next work

结尾约60秒。项目的价值在于把基本面分析中的库存问题整理成可追溯的流程，帮助确定优先研究哪些公司，并把指标与年报背景连接起来。当前证据不足以给出稳定预测关系，因此实际定位是研究筛选和证据组织。下一版先完成四条待审核案例，再考虑同店销售、开店和收购等变量。如果要开展预测，应重新定义披露日之后的预测窗口并做样本外验证。最后可邀请导师讨论样本边界和后续研究方向。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第15页：Appendix: Modules 1–6

附录按需要使用，不必在主讲逐行读。Module1确认候选公司和CIK；2用三家公司下载和缓存数据；3匹配同一申报与年度形成六指标面板；4检查口径并计算信号；5建立三年依赖和次年结果；6通过图表、分组和敏感性了解试点数据。每一步都解决一个研究依赖问题。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第16页：Appendix: Modules 7–13

附录按需要使用。Module7扩大候选覆盖；8按结果分别处理缺失；9解释会计差额并重建配对；10检查样本、权重和极端值；11控制基期与公司年度因素；12审核证据并应用决定；13生成报告与复现清单。完成报告与完成所有历史审核是不同进度，本项目明确保留后者的剩余工作。

来源：Source: SEC Company Facts and the project report, 11 October 2026

## 第17页：Appendix: sources and discussion

讨论时可以回答：区间包含零说明目前估计不够精确，并不证明效果不存在；42家公司是人工候选池，因此不能宣称行业总体结论；项目不使用预测准确率来描述R平方。参考文献Gaur、Fisher、Raman研究零售库存周转与毛利、资本强度和销售意外，提供经营背景，但本项目的增长差和次年结果问题不同。
SEC：https://www.sec.gov/search-filings/edgar-application-programming-interfaces
Gaur et al.：https://pubsonline.informs.org/doi/10.1287/mnsc.1040.0298

来源：Sources: SEC EDGAR APIs, original annual filings and Gaur, Fisher and Raman (2005)

