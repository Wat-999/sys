# [店铺数据运营](https://github.com/Wat-999/sys/tree/main/%E5%BA%97%E9%93%BA%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5)

1、[竞品调价预警](https://github.com/Wat-999/sys/blob/main/%E5%BA%97%E9%93%BA%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5/%E7%AB%9E%E5%93%81%E8%B0%83%E4%BB%B7%E9%A2%84%E8%AD%A6/%E7%AB%9E%E5%93%81%E8%B0%83%E4%BB%B7%E9%A2%84%E8%AD%A6.py)

- 项目简介：运营人员想确定可删除替换的词根，删除表现差的词根不会对整体数据带来太大的影响。
- 作用：找出数据反馈差的词根。
- 实现思路：
- 1.设置词根列表；
- 2.用for循环判断关键词中是否包含某个词根；
- 3.统计词根的数据；
- 4.绘制柱状图。

2、[推广方案最优解](https://github.com/Wat-999/sys/blob/main/%E5%BA%97%E9%93%BA%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5/%E6%8E%A8%E5%B9%BF%E6%96%B9%E6%A1%88%E6%9C%80%E4%BC%98%E8%A7%A3/%E6%9C%80%E4%BC%98%E8%A7%A3.py)

- 项目简介：做推广方案
- 作用：可以制定出最佳的投放方案
- 实现思路：
- 1.梳理任务条件，转变成数学表达式;
- 2.分别计算渠道和品类投放预算的最优解;
- 3.计算各个品类在不同渠道投放预算的最优解。

3、[SEO(搜索引擎)](https://github.com/Wat-999/sys/blob/main/%E5%BA%97%E9%93%BA%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5/SEO(%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E)/SEO(%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E).py)

- 项目简介：批量获取天猫单个商品的评价标签关键词。
- 作用：可以从商品标签词中统计出每个商品在买家评论中的优点和缺点，可以帮助商家快速的整改评论不好的商品，提升商品DSR。
- 实现思路：
- 1.设置词根列表;
- 2.用for循环判断关键词中是否包含某个词根;
- 3.统计词根数据;
- 4.绘制柱状图。


# [数字营销](https://github.com/Wat-999/sys/tree/main/%E6%95%B0%E5%AD%97%E8%90%A5%E9%94%80)

1、[消费者舆情分析](https://github.com/Wat-999/sys/blob/main/%E6%95%B0%E5%AD%97%E8%90%A5%E9%94%80/%E6%B6%88%E8%B4%B9%E8%80%85%E8%88%86%E6%83%85%E5%88%86%E6%9E%90/%E6%B6%88%E8%B4%B9%E8%80%85%E8%88%86%E6%83%85%E5%88%86%E6%9E%90.py)

- 项目简介：品牌方想通过消费者调研，掌握消费者对该品牌对态度，从而找出正确对改造方向。
- 作用：找出正确对改造方向。
-  数据说明: 
-  1.评价：来自某电商平台对消费者对该品牌商品对评论;
-  2.词根：根据评价切分出来对最小词语单位;
-  3.词频：指某个词根出现对次数。
- 实现思路：
- 1.通过情感分析提取情感得分，区分正面评价和负面评价；
- 2.分别分析正面评价和负面评价对词云；
- 3.通过词云掌握消费者对品牌对态度。

2、[基于关联规则的产品推荐](https://github.com/Wat-999/sys/blob/main/%E6%95%B0%E5%AD%97%E8%90%A5%E9%94%80/%E5%9F%BA%E4%BA%8E%E5%85%B3%E8%81%94%E8%A7%84%E5%88%99%E7%9A%84%E4%BA%A7%E5%93%81%E6%8E%A8%E8%8D%90/%E5%9F%BA%E4%BA%8E%E5%85%B3%E8%81%94%E8%A7%84%E5%88%99%E7%9A%84%E4%BA%A7%E5%93%81%E6%8E%A8%E8%8D%90.py)

- 项目简介：做产品推荐
- 作用：可以制定出最佳的产品推荐
- 实现思路：
- 1.关联规则需要先创建商品项集，商品项集类似超市购物后得到的小票，每一条项集就是一张小票的商品的列表;
- 2.计算频繁项集;
- 3.编写关联规则算法，挖掘关联规则。

3、[基于聚类算法的商品推荐](https://github.com/Wat-999/sys/blob/main/%E6%95%B0%E5%AD%97%E8%90%A5%E9%94%80/%E5%9F%BA%E4%BA%8E%E8%81%9A%E7%B1%BB%E7%AE%97%E6%B3%95%E7%9A%84%E5%95%86%E5%93%81%E6%8E%A8%E8%8D%90/%E5%9F%BA%E4%BA%8E%E8%81%9A%E7%B1%BB%E7%AE%97%E6%B3%95%E7%9A%84%E5%95%86%E5%93%81%E6%8E%A8%E8%8D%90.py)

- 项目简介：正确地推荐商品可以提高企业的销售额，关联规则则是物与物之间的关系，可以通过商品之间的连带关系寻找商品至之间的关联规则
- 作用：可基于聚类结果为消费者推荐产品。
- 实现思路：
- 1.提取消费者特征;
- 2.使用sklearn.cluster库中的Kmeans函数对消费者分类;
- 3.基于聚类结果为消费者推荐产品。

4、[基于协同过滤算法的产品推荐](https://github.com/Wat-999/sys/blob/main/%E6%95%B0%E5%AD%97%E8%90%A5%E9%94%80/%E5%9F%BA%E4%BA%8E%E5%8D%8F%E5%90%8C%E8%BF%87%E6%BB%A4%E7%AE%97%E6%B3%95%E7%9A%84%E4%BA%A7%E5%93%81%E6%8E%A8%E8%8D%90/%E5%9F%BA%E4%BA%8E%E5%8D%8F%E5%90%8C%E8%BF%87%E6%BB%A4%E7%AE%97%E6%B3%95%E7%9A%84%E4%BA%A7%E5%93%81%E6%8E%A8%E8%8D%90.py)

- 项目简介：给消费者推荐商品，提高转化率。
- 作用：给消费者推荐商品，提高转化率。
- 实现思路：使用sklearn.metrics.pairwise库中的pairwise_distances()函数构建协同过滤模型。

# [销售预测](https://github.com/Wat-999/sys/tree/main/%E9%94%80%E5%94%AE%E9%A2%84%E6%B5%8B)

1、[用户成单预测](https://github.com/Wat-999/sys/blob/main/%E9%94%80%E5%94%AE%E9%A2%84%E6%B5%8B/%E7%94%A8%E6%88%B7%E6%88%90%E5%8D%95%E9%A2%84%E6%B5%8B/%E7%94%A8%E6%88%B7%E6%88%90%E5%8D%95%E9%A2%84%E6%B5%8B.py)

- 项目简介：精品旅行服务成单预测，即希望通过分析用户的行为，了解不同用户的需求，对它们下一次是否购买精品服务进行预测。
- 作用：预测用户是否会为精品服务买单,从而改进精品服务。
-  数据说明: 
- 1.表一保存了用户个人信息，主要以个人生物属性为主，其中部分字段缺失比例较高，在分析过程中需要对其进行缺失值处理;
-  2.表二保存了用户历史订单数据，详细记录了发生交易行为的用户订单相关信息，其信息为后续分析预测工作起到了至关重要的作用;
-  3.表三保存了用户行为信息，详细记录了用户在使用APP过程中的相关信息，包括唤醒APP、浏览产品、填写表单等相关信息。
- 实现思路：
* (一)准备阶段，在用户基本资料、用户订单资料、用户APP行为资料中选取并变换出与目标相关的指标货特征，做出一系列的数值处理。具体包括以下6步。
- 1、导入与导出数据表
- 2、用户基本资料分析处理，主要是缺失值填补
- 3、用户订单资料分析处理，主要是新特征的分析与产生
- 4、用户APP行为的分析处理，主要是新特征的分析与产生、缺失值调整、极值调整
- 5、基于用户订单资料与用户APP行为的整合分析处理，强调基于已产生的特征进行再此特征发现
- 6、汇总所有特征，并处理缺失值(本项目有大量的特征需要从原始资料中提取，过程比较烦琐，可结合代码调试)
- (二)数据挖掘阶段，主要是技能型成单预测，要先将前整理汇总的特征与目标组合成能进行分析的格式，而后通过分析工具(分类器)对用户是否会购买服务进行预测
并将预测结果与实际结果进行比较，测试模型的准确程度。具体包括以下两步
- 1、将特含恶搞与目标数据表进行合并，产生新的数据集用于数据挖掘
- 2、以XGBoost为例对精品旅行服务成单进行预测

2、[用户流失预测](https://github.com/Wat-999/sys/blob/main/%E9%94%80%E5%94%AE%E9%A2%84%E6%B5%8B/%E7%94%A8%E6%88%B7%E6%B5%81%E5%A4%B1%E9%A2%84%E6%B5%8B/%E7%94%A8%E6%88%B7%E6%B5%81%E5%A4%B1%E9%A2%84%E6%B5%8B.py)

- 算法原理: 
- 流失用户是指那些曾经使用过产品或服务，由于对产品失去兴趣等种种原因，不再使用产品或服务对用户;根据流失用户所处对用户关系生命周期阶段可以将流失用户分为4类，即考察阶段流失用户、形成阶段流失用户、稳定阶段流失用户和衰退阶段流失用户。
- 项目简介：分析用户的行为数据来挖掘潜在的信息资源,客户流失率是考虑业务成绩的一个非常关键的指标。
- 作用：深入了解使用者画像及行为偏好，找到最优算法，挖掘出影响用户流失的关键因素;从而更好地完善产品设计、提升用户体验。
-  实现思路：
- (一)准备阶段
- 1.导入与导出数据表
- 2.客户基本数据分析处理、缺失值填补
- 3.询问与入住日期的转换，产生新特征的分析与数据清理
- 4.缺失值处理与归一化，新特征的分析与产生、缺失值调整、极值调整
-  (二)数据挖掘阶段
- 1.将特征与目标数据表进行合并的动作，产生新的数据集用于数据挖掘
- 2.以GBM、XGBoost为例对客户流失概率进行预测。


3、[基于时序算法预测库存](https://github.com/Wat-999/sys/blob/main/%E9%94%80%E5%94%AE%E9%A2%84%E6%B5%8B/%E5%9F%BA%E4%BA%8E%E6%97%B6%E5%BA%8F%E6%B3%95%E9%A2%84%E6%B5%8B%E5%BA%93%E5%AD%98/%E5%9F%BA%E4%BA%8E%E6%97%B6%E5%BA%8F%E7%AE%97%E6%B3%95%E9%A2%84%E6%B5%8B%E5%BA%93%E5%AD%98.py)

- 算法原理: 
- 时间序列是一种统计分析方法，在营销工作中根据一定时间的数据序列预测未来的发展趋势，也称为时间序列趋势外推法;这种方法适合预测处于连续过程中的事物,它需要有若干年的数据资料，按时间排列成数据序列，其变化趋势和相互关系要明确和稳定;公预测用的历史数据资料的变化可以表现出比较强的规律性，由于它过去的变动趋势将会连续到未来，这样就可以直接利用过去的变动趋势预测未来;但多数的历史数据由于受偶然性因素的影响，其变化不太规则;利用这些资料时,要消除偶然性因素的影响，把时间序列作为随机变量序列，采用算术平均、加权平均和指数平均等来减少偶然因素，提高预测的准确性;常用的时间序列法有移动平均法加权移动平均法和指数平均法。
- 项目简介：零售行业的收益如何，取决于供应链能否良好的运转：没有库存的压力也没有缺货的现象、不同的商品都被储存在自己销售情况最好区域的仓库中、新商品的生产和旧商品的售卖能形成衔接;因此销售预测的重要性更加凸显。
- 作用：预测该公司在未来的一年中每个店铺、每个品类、每个月的销售情况;从而让公司对每个店铺、每个品类对配货提供强有力对指导。
- 数据说明: train文件中的数据是该公司所有零售商近四年所有的销售数据，该公司有10个店铺，50个品类。
- 实现思路：
- 1.对数据进行检查，确保可以使用时序算法;
- 2.使用arima()函数对该公司汇总的数据进行预测;
- 3.使用for循环对该企业所有对商品进行预测。

4、[电商的库存预测算法建模](https://github.com/Wat-999/sys/blob/main/%E9%94%80%E5%94%AE%E9%A2%84%E6%B5%8B/%E7%94%B5%E5%95%86%E7%9A%84%E5%BA%93%E5%AD%98%E9%A2%84%E6%B5%8B%E7%AE%97%E6%B3%95%E5%BB%BA%E6%A8%A1/%E7%94%B5%E5%95%86%E7%9A%84%E5%BA%93%E5%AD%98%E9%A2%84%E6%B5%8B%E7%AE%97%E6%B3%95%E5%BB%BA%E6%A8%A1.py)

- 算法原理: 
- 要预测商品的补货周期，我们要先算出上一个周期的销量，再将当前库存减去上一个周期的销量。当库存充足时，我们把当前库存除以上一个周期的销量，再乘补货周期的天数可以算出几个周期以后需要补货。当库存不足时，我们要进行补货，补货量的多少是上一个周期的销量减去当前库存量再加上一个补货周期的销量。
- 项目简介：给消费者推荐商品，提高转化率。
- 作用：给消费者推荐商品，提高转化率。
- 数据说明: 订单报表数据、商品报表数据、库存表数据。
- 实现思路：
- 1.计算每个商家编码近n天的销量，N为补货周期的日期;
- 2.计算多少天后需要补货，计算公式为：库存量/近N天销量*补货周期。

5、[基于业务逻辑的预测算法模型](https://github.com/Wat-999/sys/blob/main/%E9%94%80%E5%94%AE%E9%A2%84%E6%B5%8B/%E5%9F%BA%E4%BA%8E%E4%B8%9A%E5%8A%A1%E9%80%BB%E8%BE%91%E7%9A%84%E9%A2%84%E6%B5%8B%E7%AE%97%E6%B3%95%E6%A8%A1%E5%9E%8B/%E5%9F%BA%E4%BA%8E%E4%B8%9A%E5%8A%A1%E9%80%BB%E8%BE%91%E7%9A%84%E9%A2%84%E6%B5%8B%E7%AE%97%E6%B3%95%E6%A8%A1%E5%9E%8B.py)

- 项目简介：运营人员经常要预估店铺的销售额，用预估的销售额来做计划，一般运营人员会使用同比、环比的方式来预估销售额。
- 作用：预估第2天的销售额，以便做日计划率。
- 数据说明: 某类目下行业近3年的交易额数据和同比、环比的增长数据，数据都在一张表格中，表格的格式是xls。还有在该类目下某店铺近一个月每日的交易额数据，数据来自生意参谋后台导出的表格。
- 实现思路：
- 1.计算去年同期市场的增幅;
- 2.使用店铺的销售额乘去年同期市场增幅来预测近期数据。

# [客户价值分析](https://github.com/Wat-999/sys/tree/main/%E5%AE%A2%E6%88%B7%E4%BB%B7%E5%80%BC%E5%88%86%E6%9E%90)

1、[用户价值分析](https://github.com/Wat-999/sys/blob/main/%E5%AE%A2%E6%88%B7%E4%BB%B7%E5%80%BC%E5%88%86%E6%9E%90/%E7%94%A8%E6%88%B7%E4%BB%B7%E5%80%BC%E5%88%86%E6%9E%90.ipynb)

- 项目简介：零售行业遍布在我们的身边，无论是线上还是线下，在流量获客越来越贵的今天，已有用户价值的分析成为了每一个企业越来越重要的话题，此项目使用RFM模型来进行用户价值分析，将已有用户进行不同价值层级的划分，服务于个性化营销、增强用户体验等场景。


