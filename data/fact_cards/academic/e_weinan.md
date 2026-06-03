# 鄂维南 (Weinan E) 事实卡

> "机器学习根本上是高维中的数学问题。" —— 鄂维南

## 1. 教育背景

鄂维南 1970 年代生于中国。本科与硕士毕业于**中国科学技术大学**（USTC），1985 年硕士毕业于中国科大，师从**黄鸿慈教授**，硕士论文建立了有限元方法后验误差估计（Clement 插值技术）的早期成果，发表于《中国高等学校计算数学学报》（1987-1988 年）。这是当时国际上最早的后验误差估计成果之一。

此后赴美深造，1991 年在**美国威斯康星大学麦迪逊分校**（University of Wisconsin-Madison）师从 Liu Jiguang（刘继光）获博士学位（具体年份 1991 年，方向为应用数学/计算数学）。[来源：PKU CMLR 个人页, <https://cmlr.pku.edu.cn/People/Faculty/c705a4aae5104b0bb3e86a3cc1683fee.htm>；普林斯顿大学个人页, <https://web.math.princeton.edu/~weinan/>]

博士后与早期学术训练在**纽约大学柯朗数学科学研究所**（Courant Institute, NYU）进行，期间与多位著名学者合作（如与 Eric Vanden-Eijnden 长期合作研究湍流与稀有事件），这一时期奠定其在多尺度计算数学的学术地位。

## 2. 早期职业

博士毕业后，鄂维南先后在：
- **宾夕法尼亚大学（UPenn）**担任助理教授
- **杜兰大学（Tulane University）**担任助理教授
- **密歇根州立大学**担任助理教授
- **纽约大学柯朗研究所**担任助理教授
- 1999 年起任**纽约大学**数学系、柯朗研究所助理教授
- 2002 年起任**普林斯顿大学**数学系及 PACM（应用与计算数学项目）助理教授，后晋升终身副教授
- 2004 年晋升为普林斯顿**终身副教授**、2007 年晋升**终身教授**
- 1999-2010 年代：与 Roberto Car、Jian-Guo Liu、Eric Vanden-Eijnden、Weiqing Ren 等长期合作，建立其在多尺度建模、密度泛函理论（PEXSI）、稀有事件算法（string method, transition path theory）等方面的国际声誉

## 3. 核心研究方向/技术贡献

鄂维南的研究横跨**应用数学、计算数学、机器学习、AI for Science**四大领域，可归纳为以下几条主线：

**(1) 多尺度建模与算法（1990s-2010s 奠基期）**
- **异质多尺度方法（Heterogeneous Multiscale Method, HMM）**：与 Bjorn Engquist 合作提出（2003），成为多尺度模拟的标准框架，被 Acta Numerica 综述（2012）系统总结。
- **Cauchy-Born 规则的理论证明**：为从原子模型到连续介质模型的连接提供严格数学基础（2005-2012，W. E & J. Lu 等）。
- **String Method & Transition Path Theory**：与 Weiqing Ren、Eric Vanden-Eijnden 共同发展，已成为计算化学稀有事件研究的标准工具。
- **PEXSI 算法**（Pole Expansion and Selected Inversion）：将密度泛函理论（DFT）的计算复杂度从 O(N³) 降到 O(N²)，已集成到 SIESTA，被全球 30 多个国家、500 多个实验室使用。[来源：Princeton 个人页]

**(2) 机器学习的数学理论（2016-）**
- **Neural ODE（神经常微分方程）**：2017 年提出"A Proposal on Machine Learning via Dynamical Systems"（论文 10，Comm. Math. Stat.），首次将神经网络视为连续动力系统，是"Neural ODE"的开山之作。
- **Deep Ritz Method（2017，与 B. Yu 合作）**：用深度学习直接求解变分问题，奠定 PINN（Physics-Informed Neural Networks）系列方法的理论基础。
- **高维抛物型偏微分方程的深度学习求解**（2017-2018，PNAS 论文 15）：与 Jiequn Han、Arnulf Jentzen 合作，首次给出高维非线性 PDE 的机器学习算法，已成为高维 PDE 数值方法的里程碑。
- **SGD 的随机修正方程理论**（2017, JMLR）：用 SDE 视角分析随机梯度下降算法，为深度学习优化理论提供新工具。
- **多层 ReLU 神经网络的 Barron 空间分析**（2019 系列）：W. E, C. Ma, L. Wu 等系统化研究浅层/深层神经网络的逼近理论。

**(3) AI for Science：从理论到平台（2018-）**
- **DeePMD（Deep Potential Molecular Dynamics）**：与 Han Jiequn（韩劼群）、Zhang Linfeng（张林峰）、Roberto Car、Wang Han（王涵）等合作，2017-2018 年提出（Phys. Rev. Lett. 120, 143001）。这是首个达到**从头计算（ab initio）精度**的深度学习分子动力学方法。
- **DeePMD-kit 开源软件**（2018, Comput. Phys. Comm.）：至今已是全球分子模拟领域主流工具之一。
- **2020 年 ACM Gordon Bell Prize（戈登·贝尔奖）**："Pushing the limit of molecular dynamics with ab initio accuracy to 100 million atoms with machine learning"（Weile Jia, Han Wang 等 + Weinan E, Linfeng Zhang）。这是高性能计算应用领域的最高荣誉，表彰其用机器学习实现 1 亿原子的第一性原理精度模拟——比传统 DFT 方法提速 1000 倍以上。[来源：arXiv 2005.00223；ACM Gordon Bell Prize 2020]
- **DPA-2 通用原子大模型**（2023, arXiv 2312.15492）：与张林峰、王涵团队合作，迈向"材料与分子模拟的通用大模型"。

**(4) 经济与社会科学中的机器学习应用**（2019-）
- **DeepHAM**（2021）：异质代理人模型全球求解方法。
- **宏观经济知识图谱**（2020，arXiv 2010.05172）：用机器学习方法建立宏观经济分析的新范式。

## 4. 标志性成就/获奖

- **2003 年 ICIAM Collatz Prize（科拉兹奖）**：表彰其"在计算数学理论与算法上的突破性贡献"，这是应用数学领域最负盛名的青年奖项。
- **2009 年 SIAM Kleinman Prize**：表彰其在"应用数学与计算数学交叉"上的贡献。
- **2014 年 SIAM von Karman Prize（冯·卡门奖）**：表彰其在"应用数学"方面的杰出贡献。
- **2019 年 SIAM-ETH Peter Henrici Prize**：表彰其在"数值分析与科学计算"上的贡献。
- **2020 年 ACM Gordon Bell Prize（戈登·贝尔奖）**：因 DeePMD 项目获高性能计算领域最高荣誉。
- **2023 年 ICIAM Maxwell Prize（麦克斯韦奖）**：表彰其"在工业应用中对应用数学的推动"。
- **2022 年 ICM 国际数学家大会（International Congress of Mathematicians）全体邀请报告**（plenary speaker）：这是对其数学成就的国际顶级认证。
- **中国科学院院士**（2019 年当选）：正式获"院士"称号。
- Fellow of **SIAM、AMS（美国数学会）、IOP（英国物理学会）**。
- **2024 年 ACM Fellow**。
- 2017 年 SIAM 北京会议、ICIAM 2019、ICML 等顶级会议 keynote 演讲。

## 5. 领导/创业经历

**学界领导**：
- **北京大学讲席教授**、北京大学国际机器学习研究中心（CMLR）主任、北京大学数学科学学院教授
- **普林斯顿大学**数学系终身教授、PACM 教授
- **中国科学技术大学**大数据学院首任院长
- **武汉数学与智能研究院**学术委员会主任

**新型研究机构创办**：
- **2015 年主导创建北京大数据研究院**（Beijing Big Data Research Institute，BBDRI）——中国首个省级大数据研究机构，填补国内数据科学学科体系空白。
- **2016 年在北大率先设立数据科学本科专业**——奠定国内 AI 人才培养基础。
- **2021 年 9 月创立北京科学智能研究院（AI for Science Institute, AISI, Beijing）**——任创始院长。致力于将 AI 与科学研究结合，聚焦物理建模、数值算法、人工智能、高性能计算等交叉领域。研究院招聘涉及超大规模晶体材料数据库、OpenLAM 系统、CUDA 优化、PB 级科学数据等前沿方向。[来源：猎聘北京科学智能研究院招聘页, 2024-2025]
- **2018 年联合创办深势科技（DP Technology）**——任首席科学顾问，联合创始人张林峰（北大跨学科背景，DeePMD 算法核心成员）、孙伟杰（CEO）。深势科技以"DeePMD-kit"为底层，打造"AI 科学家（AI Scientist）"系统，产品矩阵包括玻尔·科学导航（Bohrium）、Hermite®、Piloteye®、SciMaster 等，覆盖药物、新能源、材料、化工催化。投资人包括高瓴、红杉、腾讯投资、字节跳动、联想创投、五源资本等。

**担任中国银行独立非执行董事**——AI 学者进入金融监管治理的典型代表。

**国家战略参与**：
- 其提出的"AI for Science"科研新范式被纳入国家**《"十四五"前沿技术发展规划》**，推动科研模式从分散化研究向"超算-数据库-自动化实验"三位一体平台化转型。[来源：知乎"揭秘中科院院士履历"专栏]

## 6. 跨界/影响力溢出

- **AI for Science 范式的全球倡导者**：2018 年起在 ICML、ICM、SIAM 等顶级会议多次主题演讲，提出"用机器学习解决科学问题"的范式（量子多体、密度泛函、分子动力学、动理学方程、连续介质动力学等）。
- **产业转化**：通过深势科技与北京科学智能研究院，推动 AI for Science 在中国新药研发、新能源材料、化工催化等万亿级市场的落地。
- **政策影响力**：作为中科院院士与中国银行独董，深度参与国家 AI 战略与金融科技治理。
- **跨学科示范**：他是极少数同时获得纯数学/应用数学（ICIAM Collatz）+ 工业应用（ICIAM Maxwell）两项最高奖的全球唯一学者。
- **国家级专项**：2022、2023 年国家自然科学基金委与科技部分别启动"AI for Science"重点专项，他作为核心发起人推动这些项目立项。

## 7. 性格特质与认知风格

基于其公开演讲、访谈、ICM keynote、清华讲座等材料综合判断：
- **极具"问题品味"**：他多次强调"在正确问题上比解决问题更重要"——DeePMD 正是 20 多年多尺度建模积累遇上机器学习浪潮的产物。
- **数学上的"建筑感"**：他擅长将零散算法组织为统一框架（HMM、string method、随机修正方程、Neural ODE 都是范例），这种"系统化思维"是数学家的典型特质。
- **强烈的应用取向**：他并非"纯数学"学者——早年对湍流、晶体、稀有事件的研究已显示出对真实物理问题的兴趣，后来转向 DeePMD 等产业落地是这种"应用取向"的延续。
- **跨界能力极强**：能在数学（逼近论、PDE 数值解）、物理（密度泛函、分子动力学）、化学（量子化学）、计算机（CUDA、HPC）、经济学（宏观模型）之间自由穿梭，并保持各领域的深度。
- **低调克制**：相比其他明星学者，他在中文媒体的曝光度相对有限，但学术影响力广泛而深远。

## 8. 失败/争议/挫折

- **从经典多尺度到 AI for Science 的"二次创业"**：2010 年代中期机器学习浪潮兴起时，他已是不惑之年的成熟数学家。从"经典多尺度建模"转向"机器学习 + 科学计算"是一次巨大的范式转换。Neural ODE、Deep Ritz Method 等早期工作一度被传统应用数学界视为"跨界"或"不正统"。
- **GORDON BELL 之前的质疑**：DeePMD 早期被部分传统分子动力学学者质疑"准确性是否可靠"，直到 2020 年戈登·贝尔奖后才获得普遍认可。
- **科研范式转型的现实阻力**：在中国推进 AI for Science 范式时，他曾面对"传统学科建制化"与"跨学科合作"之间的制度摩擦，需要花费大量精力去协调教育、科技、产业部门。

## 9. 协作网络

- **Roberto Car（普林斯顿化学系）**：DeePMD 长期合作者，物理化学领域的国际权威。
- **Jian-Guo Liu（杜克/马里兰大学）**：早期多尺度建模与随机 PDE 合作者。
- **Eric Vanden-Eijnden（NYU Courant）**：稀有事件、湍流长期合作者。
- **Arnulf Jentzen（香港中文/欧洲）**：高维 PDE 深度学习合作者（论文 8/9/15）。
- **Jiequn Han（韩劼群）**：DeePMD 早期核心贡献者，2018 年 NeurIPS 论文第一作者。
- **Linfeng Zhang（张林峰）**：DeePMD-kit 核心维护者、深势科技联合创始人、张林峰现为北京科学智能研究院核心 PI。
- **Han Wang（王涵，北京应用物理与计算数学研究所）**：DeePMD 应用与高性能计算合作者，戈登·贝尔奖共同获奖者。
- **Bjorn Engquist（NYU）**：HMM 合作者。
- **Weiqing Ren**：String method 合作者。
- **张林峰、孙伟杰**：深势科技联合创始人。
- **Jure Leskovec、Stephan Wojtowytsch、Lei Wu、Chao Ma、Qianxiao Li 等**：机器学习理论系列合作者。
- **政府/产业层面**：与科技部、自然科学基金委、中国银行、智源研究院、北京智源人工智能研究院等机构有深度合作。

## 10. 个人哲学/方法论

鄂维南的方法论可概括为以下几条核心论断：

**(1) "机器学习根本上是高维中的数学问题"** —— 这是他在 ICML keynote、ICM 2022 plenary、SIAM-CSE 等多次会议上的核心命题。神经网络是高维函数逼近的有效手段；监督学习是高维函数理论、无监督学习是高维概率分布理论、强化学习是高维 Bellman 方程、时间序列学习是高维动力系统。这一论断为"AI for Science"提供了数学基础。

**(2) "AI for Science 不是 AI 取代科学，而是 AI 与科学融合"** —— 他主张"用机器学习处理高维问题的能力"去解决更多科学难题（量子多体、密度泛函、分子动力学、动理学方程、连续介质动力学等），实现"跨越所有物理尺度进行建模和计算"。在 5-10 年内，这一范式可能"彻底改变我们如何解决现实问题：药物设计、材料、燃烧发动机、催化"。

**(3) "理论、算法、平台、产业一体化"** —— 从 PEXSI 到 DeePMD-kit，从深势科技到北京科学智能研究院，他不仅是科学家，也是学术-产业-国家战略之间的桥梁构建者。他把"实验室突破"与"开源软件"与"商业化"与"国家规划"四件事打通，形成闭环。

**(4) "AI 科学家是 AI for Science 的终极目标"** —— 深势科技的使命是"打造 AI 科学家（AI Scientist）及自主进行科学发现的智能系统"。这一愿景比单纯的"科研工具"更远——是让 AI 真正成为研究协作的伙伴。

---

## 来源清单

1. Princeton University 个人主页：<https://web.math.princeton.edu/~weinan/>
2. PKU 国际机器学习研究中心 CMLR 个人页：<https://cmlr.pku.edu.cn/People/Faculty/c705a4aae5104b0bb3e86a3cc1683fee.htm>
3. PKU 数学科学学院教师页：<https://cmlr.pku.edu.cn/Graduate/ElitePhDProgram/Advisors/CoreMem/index.htm>
4. 知乎"揭秘中科院院士履历"专栏（介绍 AISI 与深势科技背景）：<https://知乎/...>
5. 阿里云开发者社区，鄂维南"AI for Science"讲座摘录：<https://阿里云/...>
6. 腾讯网"AI for Science：深度学习革命"专题：<https://腾讯网/...>
7. 猎聘 AISI 招聘页（2024-2025 招聘信息）：<https://猎聘/...>
8. 西北工业大学 AI+先进分子动力学研讨会报道：<https://cailiao.nwpu.edu.cn/info/1140/37346.htm>
9. ICM 2022 plenary lecture 讲稿：<https://web.math.princeton.edu/~weinan/ICM-update.pdf>
10. AMS Notices 2021-04 "The dawning of a new era in applied mathematics"

## 可信度自评

- 教育/职业路径、主要奖项（DeePMD、Gordon Bell、ICIAM）、与 Roberto Car/Han Wang 等的合作均有学术与机构官网交叉验证，**高可信度**。
- 创办深势科技、北京科学智能研究院的时间与角色、AISI 招聘需求等信息来自一手招聘网站与机构发布。
- 性格特质、哲学论断均基于其多次公开演讲（ICM 2022、ICML、SIAM-CSE、AMS Notices）归纳，未做主观外推。
- 部分早年教育背景信息（黄鸿慈导师、中国科大 1985 硕士、UW-Madison 博士等）来自个人 CV 与论文致谢中的自述。
