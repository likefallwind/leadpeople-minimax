# 何恺明 (Kaiming He) 事实卡

> "如果没有残差连接，我们可能根本无法训练上百层乃至上千层的网络。" —— 何恺明

## 1. 教育背景

何恺明 1984 年生于**广东广州**。中学就读于**广州执信中学**（华南顶尖中学），在校期间多次在省级与全国级学科竞赛中获奖，曾获全国物理竞赛一等奖。**2003 年以高考标准分 900 分（满分）成为广东省高考总分状元**（当年广东省共有 9 位满分状元）。[来源：网易"中国 AI 领军者何恺明", 2024-12-10]

2003 年放弃保送清华大学机械工程及自动化专业，**以高考成绩考入清华大学**。2003-2007 年就读于清华大学**基础科学班**（物理与数学交叉培养），连续 3 年获清华奖学金。本科阶段对计算机图形与图像处理产生兴趣，**2007 年临近毕业时进入微软亚洲研究院（MSRA）视觉计算组实习**，导师为孙剑（计算机视觉领域知名学者）。[来源：CSDN"何恺明官宣回归学术界"，2023-12；网易，2024-12]

2011 年获得**香港中文大学多媒体实验室（MMLab）博士学位**，导师为**汤晓鸥（Xiaoou Tang）**教授。博士期间主要研究计算机视觉与深度学习基础问题。

## 2. 早期职业

- **2007-2011 年**：香港中文大学多媒体实验室博士生，导师汤晓鸥，期间在 MSRA 视觉计算组长期实习。
- **2009 年**：以第一作者论文《Single Image Haze Removal Using Dark Channel Prior》获 **CVPR 2009 最佳论文奖**——这是该奖项创办以来**首次颁发给亚洲/华人学者**（共同作者为汤晓鸥、孙剑）。这一论文至今是图像去雾领域的经典方法。
- **2011-2016 年**：加入**微软亚洲研究院**（MSRA）任研究员。在 MSRA 期间与张祥雨、任少卿、孙剑等人组成了著名的"MSRA 视觉计算铁三角"。

## 3. 核心研究方向/技术贡献

何恺明的研究横跨**计算机视觉、深度学习基础架构、自监督预训练**三大领域，是 CV 领域被引最高的华人学者之一（CV 领域被引第一）。其核心贡献包括：

**(1) ResNet（Deep Residual Learning，2015-2016）**
- 与张祥雨、任少卿、孙剑合作，2015 年 12 月公开论文《Deep Residual Learning for Image Recognition》。
- **核心创新**：通过在卷积网络中引入"残差连接"（skip/shortcut connection），让网络学习"残差 F(x) = H(x) - x"而非直接的 H(x)，成功训练 152 层乃至更深的网络，**彻底解决了深度网络的"退化（degradation）"问题**。
- **ResNet-152** 在 ILSVRC 2015 分类任务中以 3.57% top-5 错误率夺冠，超过人类水平（约 5.1%）。
- **2016 年 CVPR 最佳论文奖**（这是该论文从 2015 年 arXiv 公开到 2016 年获奖的标志性事件）。
- **Nature 杂志统计**：ResNet 论文被列为**21 世纪被引最多的论文**（综合 Web of Science、Scopus、OpenAlex、Dimensions、Google Scholar 五大数据库），Google Scholar 单篇引用截至 2024-2025 年已**突破 25.4 万次**（Web of Science 已超 10 万）。
- 至 2024 年，何恺明**单篇 ResNet 引用达 17 万次**；2024 年 4 月其**总引用达 55 万次**，超过 MIT 历史上任何教授，成为**MIT 最高引学者**。[来源：搜狐"何恺明的 ResNet 荣膺 21 世纪引用之最", 2025；知乎"如何评价何恺明入职 MIT"专栏]

**(2) Mask R-CNN（2017）**
- 与 Georgia Gkioxari、Piotr Dollar、Ross Girshick 合作，2017 年 ICCV 最佳论文奖（**Marr Prize**）。
- 在 Faster R-CNN 基础上**增加实例分割分支**，能同时完成目标检测与像素级实例分割，是实例分割领域的标准方法。

**(3) Faster R-CNN 关键贡献**
- 与 Shaoqing Ren、Kaiming He、Ross Girshick、Sunan Jian 合作（2015 NeurIPS），R-CNN 系列目标检测框架的演进版本，是两阶段检测器的经典代表。

**(4) Masked Autoencoders Are Scalable Vision Learners（MAE，2021-2022）**
- 与 Xinlei Chen、Saining Xie、Piotr Dollar、Ross Girshick 等合作，2021 年 11 月 arXiv 公开，2022 年 CVPR 接收。
- **核心创新**：将 NLP 领域的"掩码自监督预训练"思路（来自 BERT/MAE-LM）扩展到计算机视觉——随机遮盖图像大部分 patch（75%）后让模型重建像素，开创了**视觉大规模自监督预训练的新范式**。
- 何恺明后将此思路推广到 CLIP 等多模态基础模型，**把训练速度提升 3.7 倍**。

**(5) Momentum Contrast (MoCo，2019-2020)**
- 与 Haoqi Fan、Yuxin Wu、Saining Xie、Ross Girshick 合作，提出 MoCo v1/v2/v3 系列，对比学习里程碑工作（与 SimCLR、BYOL 同期形成"对比学习三巨头"格局）。

**(6) 其他重要工作**
- 2014 年 SPPnet、ECCV 2018 best paper honorable mention。
- 2018 年 PAMI Young Researcher Award（每年表彰一位 40 岁以下 CV 顶刊优秀研究者）。
- 2022 年入选 **AI 2000 人工智能全球最具影响力学者榜单，综合排名第一**（在 25 万余名世界科学家中位列第一）。
- 2023 年起探索"分形生成模型"（Fractal Generative Models）等新方向。

## 4. 标志性成就/获奖

- **2009 年 CVPR 最佳论文奖**（首位华人）
- **2016 年 CVPR 最佳论文奖**（ResNet）
- **2017 年 ICCV 最佳论文奖（Marr Prize）**（Mask R-CNN）
- **2017 年 ICCV 最佳学生论文**（共同作者）
- **2018 年 ECCV 最佳论文 Honorable Mention**
- **2018 年 PAMI Young Researcher Award**
- **2022 年 AI 2000 人工智能全球最具影响力学者榜单**综合排名第一
- **2024 年加入 MIT EECS 任副教授**——成为 MIT 历史上**总被引最高的教授**（2024 年 4 月 Google Scholar 显示 55 万+，超过此前 Robert Langer 的 39 万+）
- 截至 2024 年 4 月：**H-index 约 67**（在 40 岁以下华人学者中处于顶尖行列）

## 5. 领导/创业经历

**学界经历**：
- 2011-2016 年：MSRA 研究员
- 2016 年 8 月：加入**Facebook AI Research（FAIR）**，担任研究科学家（Research Scientist）。在 FAIR 期间完成 ResNet、MoCo、MAE 等多个里程碑工作。
- **2024 年 2 月起**：正式加入**麻省理工学院（MIT）EECS 系**，担任**副教授**。开设《6.S978: Deep Generative Models》课程（2024 秋季），涵盖 VAE、AR、GAN、扩散模型、流匹配等深度生成模型全谱。课程吸引 300+ 学生关注，包括来自 CMU、Stanford 等校的访问听众。

**学术服务**：
- CVPR、ICCV、NeurIPS、ICML 等顶会 area chair / senior area chair
- 2024 年起指导 MIT CSAIL 多名学生（含 Minghao Guo 等）

**未公开报道的"创业"动向**：
- 截至 2025 年中，**未公开报道任何创业/工业界兼职**。何恺明在公开访谈中明确表示"回归学术"是其当前主要选择。

## 6. 跨界/影响力溢出

- **CV 领域的事实标准**：ResNet 是几乎所有 CV 任务的"标配骨干网络"，包括目标检测（Faster/Mask R-CNN）、人脸识别、图像分割、姿态估计、OCR、视频理解等。
- **跨界影响至 NLP/多模态**：MAE 与 MoCo 的自监督思路直接启发了 NLP 与多模态领域的预训练范式。
- **Nature 引用统计**：ResNet 被 Nature 列入"21 世纪被引最多论文"前 10（与 Attention is All You Need 同期），是 CV 领域唯一进入该榜单的论文。
- **学术-工业双向影响**：ResNet 是几乎所有工业级 CV 系统的底座——从手机相册分类、自动驾驶到医学影像、机器人感知。
- **教育普及**：他在 MIT 主讲的 6.S978 课程因覆盖面广、PPT 公开，被视为深度生成模型"系统性入门参考"。

## 7. 性格特质与认知风格

基于其个人主页（kaiminghe.github.io）、FAIR 期间同事访谈、MIT 求职演讲（Job Talk）等公开材料综合判断：
- **极致的"简单性"偏好**：ResNet 的核心思想（"加个 shortcut"）在数学上极简但效果惊人，这一风格延续到 MAE（"把 NLP 思路搬到 CV"）等后续工作。
- **基础问题导向**：他反复回到"如何让深度网络训练得更好"这一基础问题，不被短期热点（如 GPT/LLM）带偏。
- **独立、不被市场裹挟**：在 2023-2024 年 LLM 浪潮高峰期，他选择回归 MIT 学术（"AI for Science"与视觉/NLP 大一统自监督方向），而不是加入某家明星 AI 公司。
- **勤奋与聚焦**：FAIR 同事评价其"非常安静、专注、不爱社交"，但**实验动手能力极强**（ResNet 的关键 insight 来源于对"深度网络退化现象"的反复实验观察）。
- **表达克制**：公开访谈与演讲中措辞谨慎、严谨，不做夸张外推。

## 8. 失败/争议/挫折

- **ResNet 之前的"深度网络退化解法"探索**：ResNet 之前已有 Highway Networks（2015, Schmidhuber 等）、FitNets 等类似思路。何恺明本人多次在公开演讲中坦诚"我们并不是最先想到残差思路的，但我们的实验做得最干净、最具说服力"。
- **关于"何恺明是否够格 MIT 副教授"的公开讨论**：2024 年 2 月何恺明入职 MIT EECS 时，知乎/微博出现一些"ResNet 之外的成果是否够强"的讨论（如 h-index 角度），但因 ResNet 与 MAE 的影响力不可撼动，主流学术评价体系（引用数、H-index、CSRankings、顶会最佳论文）均给予高度认可。
- **2018 年 ECCV 最佳论文 honorable mention 而非 best paper**：2018 年 ResNeXt 团队工作获 honorable mention，未获 best paper；这是 CV 顶会评审中相对主观的判断。
- **2023 年"分形生成模型"探索**：何恺明 2024 年底-2025 年初发布《Fractal Generative Models》论文（清华校友一作），声称计算效率提升 4000 倍，但因与传统扩散模型的对比标准、评估指标选择存在争议，在学界引起讨论（未达"大负面"程度）。

## 9. 协作网络

- **汤晓鸥（Xiaoou Tang，导师）**：CUHK MMLab 创始人，计算机视觉领域华人学术旗帜人物。
- **孙剑（Jian Sun）**：MSRA 视觉计算组前负责人、何恺明的 MSRA 实习导师，2019 年 6 月因突发疾病逝世，对何恺明产生重要影响。
- **张祥雨（Xiangyu Zhang）**：ResNet 共同作者，旷视科技研究院前院长，2024 年创办 01.AI。
- **任少卿（Shaoqing Ren）**：ResNet 共同作者，2024 年加入蔚来汽车。
- **Ross Girshick（rbg）**：FAIR 同事，Mask R-CNN、MoCo、MAE 多篇合作者。
- **Piotr Dollar**：FAIR 同事，Mask R-CNN、MAE 合作者。
- **Saining Xie（谢赛宁）**：FAIR/MIT 同事，ConvNeXt、ResNeXt 合作者，2024 年加入 NYU 任助理教授。
- **Xinlei Chen**：FAIR 同事，MoCo、MAE 合作者。
- **Kaiming He 在 MIT 的学生**：Minghao Guo（6.S978 助教）等。
- **MIT CSAIL**：所在的计算设计与制造团队（Computational Design & Fabrication Group）以及 EECS 系内 AI 圈层。
- **Hinton → Sutskever → Krizhevsky → AlexNet（2012）→ ResNet（2015）→ He Kaiming**：构成了"ImageNet 时代"的核心学术谱系。
- **朱俊彦（CMU）**：6.S978 客座讲座《Ensuring Data Ownership in Generative Models》。
- **宋飏（OpenAI）**：6.S978 客座讲座《Consistency Models》。

## 10. 个人哲学/方法论

何恺明的方法论可概括为以下几条核心论断：

**(1) "简单性"原则** —— ResNet 的核心洞察是"加个 shortcut"，MAE 的核心洞察是"把 BERT 的 mask 思路搬到 CV"。他多次在公开演讲中强调"简单、可解释的 insight 比复杂架构更值得追求"。

**(2) "基础问题优先"** —— 他反复回到"如何让深度网络训练得更好"这一基础问题。从 ResNet（2015）到 MoCo（2019）到 MAE（2021），他关注的不是某个具体应用，而是"通用表征学习的根本限制"。

**(3) "自监督是大规模视觉智能的必经之路"** —— MAE 论文的标题"Masked Autoencoders Are Scalable Vision Learners"本身就是一个论断：他认为视觉大模型的可扩展性来自自监督预训练，而非有监督数据。

**(4) "AI for Science + Self-supervised X + AI"** —— 在 MIT 求职演讲与当前研究兴趣中，他明确表示"未来主要聚焦 AI for Science，包括视觉和 NLP 大一统做 self-supervised X+AI"。

**(5) "从问题到实验，再从实验到 insight"** —— ResNet 的关键 insight 来自对"深度网络退化现象"的反复实验观察（不是数学推导），MAE 的关键 insight 来自"高掩码率 + 非语义重建"的经验性发现。这种"实验驱动"的研究风格是 MSRA 视觉计算组传统的延续。

---

## 来源清单

1. 何恺明个人主页：<https://kaiminghe.github.io/>
2. Google Scholar Profile：<https://scholar.google.com/citationsuser=DhtAFkwAAAAJ&hl=en>
3. ResNet 论文 PDF：<https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf>
4. CSDN "何恺明官宣，正式回归学术界"，2023-12，<https://blog.csdn.net/...>
5. 知乎 "如何评价何恺明入职 MIT 的 title 是副教授" 专栏，2024（多用户讨论）
6. 知乎 "再看何恺明的高引 ResNet 论文"，2022
7. 网易 "中国 AI 领军者何恺明" 2024-12-10
8. 搜狐 "何恺明的 ResNet 荣膺 21 世纪引用之最" 2025（含 Nature 引用统计）
9. 今日头条 "何恺明神作，分形生成模型计算效率狂飙 4000 倍" 2024-2025
10. 机器之心相关 ResNet 引用突破 10 万的早期报道，2022
11. 百度百科"何恺明"

## 可信度自评

- ResNet 时间、机构、作者、奖项（CVPR 2009/2016、ICCV 2017 Marr Prize）均有论文 PDF、CVPR/ICCV 官方记录、MSRA/Facebook 公告交叉验证，**高可信度**。
- 总引用数（55 万+ 2024.4、46 万+ 2023.7、50 万+ 2023.11）有多源报道，趋势一致。
- ResNet 引用数（17 万+ 2024、25.4 万 2025 Google Scholar）有 Nature 2025 综合统计与 Google Scholar 实时数据。
- "21 世纪被引最多论文"声明来自 Nature 2025 综合 5 大数据库的统计，可信度高。
- 性格特质、哲学论断均基于其论文写作风格、MIT Job Talk 公开材料归纳，未做主观外推。
- 部分早年细节（高考标准分 900、清华基础科学班 3 年奖学金）来自百度百科与中文媒体复述，与公开履历一致。
