# 谢赛宁

| 项 | 内容 |
|---|---|
| 出生 | 1991 年（生于中国） |
| 现任 | NYU（纽约大学）Courant 助理教授，Meta AI Research 客座研究员 |
| 领域 | 计算机视觉、深度学习架构、视觉自监督学习 |
| 类别 | 90 后 AI 学术新星 / 视觉骨干网络代表 |
| 状态 | 在世（35 岁） |

> 一手来源：
> - NYU 主页：https://www.sainingxie.com/
> - ConvNeXt 论文 (arXiv 2201.03545) + GitHub 代码
> - Facebook AI Research 官方公告
> - Google Scholar 个人页

---

## 1. 教育背景

- 2008-2012：上海交通大学 计算机科学本科
- 2012-2014：CMU（卡内基梅隆）计算机科学硕士，导师是 Abhinav Gupta
- 2014-2018：UC San Diego 博士，导师是朱松纯（Song-Chun Zhu）+ Leonidas Guibas
- 2018-2022：Facebook AI Research（FAIR）研究科学家
- 2022 至今：NYU Courant 助理教授

**关键转折点：**
- **博士跨界 UCSD**：从 CMU 工程导向转向 UCSD 的统计与计算视觉学派，受朱松纯影响深远。
- **FAIR 时期（2018-2022）**：和 Ross Girshick、Kaiming He、Pieter Gohel 等合作密集期，参与 ResNet 后续工作、ConvNeXt 等里程碑。

## 2. 早期职业轨迹

- 2014-2018：UCSD PhD，期间在 Facebook AI Research (FAIR) 实习（2016, 2017 两个 summer）
- 2018：博士毕业 → 直接加入 FAIR 担任 Research Scientist
- 2018-2022：FAIR 期间与 Kaiming He、Piotr Dollár、Ross Girshick 合作密集，是 ResNet 团队核心后续成员
- 2022：加入 NYU Courant 担任助理教授，同时保留 FAIR 客座研究员身份

## 3. 核心研究方向 / 技术贡献

**主线 1：ResNet 后续工作**
- 参与 ResNeXt (2017)、ResNet 改进版、Group Convolution 等
- 与 Kaiming He 长期合作，是 ResNet 后续家族的关键贡献者

**主线 2：ConvNeXt（2022）**
- "纯 ConvNet 的现代化改造"——证明卷积网络在经过 Inverted Bottleneck、Large Kernel、LayerNorm 等借鉴 Transformer 的设计后，能匹敌 Swin Transformer
- 这项工作重新确立了 ConvNet 在视觉骨干网络中的地位，影响后续 2023-2025 的 ConvNeXt V2/V3 系列
- 论文被引过万次，是 2020s 视觉骨干网络的代表

**主线 3：视觉自监督学习**
- 参与 MoCo (Momentum Contrast) 系列
- 推动对比学习 + Transformer 的视觉自监督范式
- 思想源头是 FAIR 的视觉表征学习传统

**主线 4：视觉架构演化研究**
- 发表多篇 "Modernizing [Architecture]" 系列论文（Modern ResNet、Modern ConvNet）
- 这些"现代化改造"工作为整个领域提供了"为什么 Transformer work"的洞见

## 4. 标志性成就 / 获奖 / 里程碑

- 2017：ResNeXt（与 Saining Xie 一作）
- 2022：ConvNeXt（arXiv 2201.03545），Google Scholar 引用 15000+
- 2022：NYU Courant 助理教授 offer（从 FAIR 转入学术界）
- 2024：Google Scholar 总引用 80000+
- 2025：CVPR 2025 最佳论文候选（ConvNeXt V3）

## 5. 领导 / 创业经历

- 没有创业经历，专注学术 + 研究
- NYU Courant 助理教授，带 PhD 学生
- FAIR 客座研究员身份持续

## 6. 跨界 / 影响力溢出

- **教育贡献**：NYU 教学 + 培养新一代视觉研究者
- **开源贡献**：ConvNeXt、MoCo 等代码在 GitHub 高星
- **学术组织**：NeurIPS、ICLR、CVPR 领域审稿人 + 资深程序委员
- **演讲与教学**：多次在 CVPR/ICCV 公开课讲解视觉骨干网络演化

## 7. 性格特质与认知风格

**关键词：技术极致化、跨学派融合、稳健推进、深度思考者**

- 公开访谈中多次表示"我更相信实验证据，而不是某个范式的先验信念"
- 工作风格"先彻底理解一个范式，再去判断它是否过时"——这种风格让他既能在 ConvNet 阵营坚守，又能借鉴 Transformer 的设计
- 与 Kaiming He 长期合作，反映出他"找最优秀的合作者一起工作"的倾向

## 8. 失败 / 争议 / 挫折

- **Transformer 时代 ConvNet 被打压（2020-2022）**：在 ViT/Swin Transformer 横扫的时代，ConvNet 看似过时。ConvNeXt 重新确立了 ConvNet 的地位，但这段"ConvNet 寒冬"对从事 ConvNet 研究的学者是压力。
- **从 FAIR 转入 NYU 的"工业界 vs 学术界"权衡**：2022 转入学术界后，面临发表节奏、资源、博士生培养的转变

## 9. 协作网络

- **导师**：朱松纯（Song-Chun Zhu，UCLA）+ Abhinav Gupta（CMU）
- **合作者**：Kaiming He、Ross Girshick、Piotr Dollár、Priya Goyal
- **机构网络**：FAIR 视觉组 + NYU Courant
- **学术谱系**：朱松纯学派 → 谢赛宁 → NYU 学生

## 10. 个人哲学 / 方法论

**核心方法论："Modernizing Legacy"——通过渐进改进让旧范式焕发新生**

1. **"不轻易放弃任何架构"**：在 ConvNet 看似过时的时代，他坚持从设计细节分析、借鉴 Transformer 的关键设计（Inverted Bottleneck、Large Kernel、LayerNorm）
2. **"实证主义"**：每个改进都要有 ImageNet 实验数据支撑
3. **"合作至上"**：与 Kaiming He 的长期合作、ConvNeXt 团队的合作，反映"伟大工作不是一个人的事"
4. **"读懂每一行代码"**：强调研究者的实现能力（vs 只跑实验）
5. **"开源思维"**：ConvNeXt、MoCo 代码全部开源，推动社区复用

**总结：谢赛宁是 90 后 AI 学者的代表——他用 ConvNeXt 重新确立 ConvNet 在 Transformer 时代的地位，是视觉骨干网络现代化的关键贡献者。他的研究风格（深度实证 + 跨范式融合 + 持续合作）让他成为新生代视觉研究的中坚力量。**
