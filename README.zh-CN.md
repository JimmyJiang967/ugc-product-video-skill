# 基于证据的 UGC 产品视频 Skill

[English](README.en.md) | [仓库首页](README.md)

## 它解决什么问题

这个社区版 Skill 帮助 AI Agent 把经过授权的产品图片和已确认卖点，转化为一条经济、可信、由真人出镜讲解的 UGC 产品视频流程。默认目标是一条 15 秒竖屏视频，包括：

- 先分析产品，再设计动作；
- 提供两到三种真正不同的产品展示策略；
- 由用户选择直接展示或开箱到使用；
- 使用一张 2×2 四阶段锚点图保持故事连续；
- 按证据强度选择符合产品特征的动作；
- 口型、动作与台词共同生成或由授权录音驱动；
- 从最终媒体的真实 ASR 时间戳生成动态字幕；
- 使用确定性脚本校验策划和最终结果。

Skill 与具体平台解耦，不写死某个厂商的工具名、模型名、积分系统或私有 API。

## 为什么强调“基于证据”

产品看起来像某个品类，不代表按钮位置、使用方式、档位、材质或性能已经得到确认。每一个卖点必须使用以下一种证据路线：

| 路线 | 适用条件 | 可以展示什么 |
| --- | --- | --- |
| `mechanism_led` | 控件位置和操作方式都已确认 | 展示准确操作及可观察结果 |
| `state_led` | 使用状态明确，不依赖未知控件 | 展示穿戴、安装、装入或其他已确认状态 |
| `effect_led` | 功能已确认，但开关或操作顺序未知 | 不乱按按钮，只展示克制的可见效果 |
| `appearance_led` | 只确认了可见外观 | 只展示形状、纹理、颜色、表面和已提供细节 |

这样既能做出有用的视频，也不会为了“有动作”而捏造产品功能。

## 输入要求

必要输入：

- 至少一张有权使用的产品图片；
- 产品名称或中性描述；
- 一到三个已经确认的事实或卖点；
- 对图片、Logo、声音、肖像和包装设计的使用授权。

可选输入：

- 已授权的出镜者图片或录音；
- 官方产品资料及更多产品角度；
- 受众、目标市场、口播语言、语气、CTA、故事模式；
- 可用的平台适配器和用户批准的预算上限。

## 使用流程

1. 区分已确认事实、图片可见特征、未知信息和禁止表达。
2. 提出两到三种可执行的展示策略，并说明证据基础、遗漏未知项和取舍。
3. 在任何付费调用前确认出镜者、故事模式、场景和预算。
4. 生成一张 2×2 四阶段状态图，覆盖开场、核心动作、辅助证据和真实使用结果。
5. 在能力支持时，一次生成连续 15 秒的画面与同步口播。
6. 完整观看可播放草稿，做最小范围修正，再从最终媒体进行 ASR 字幕生成。
7. 完整回看成片，并校验策划与结果清单。

## 安装

把 [`create-evidence-led-ugc-product-video`](create-evidence-led-ugc-product-video/) 文件夹导入或复制到你的 AI Agent 运行环境所支持的 Skills 目录。该目录已经包含 `SKILL.md`、界面元数据、参考方法和校验脚本。

调用示例：

```text
请使用 $create-evidence-led-ugc-product-video 分析我有权使用的产品图片。已确认卖点是[卖点]，目标受众是[受众]，视频口播语言是[语言]，预算上限是[预算]。
```

当无法取得费用报价、报价超过预算、关键操作缺乏证据，或当前能力无法生成同步出镜口播时，Agent 应该在付费前停止并说明原因。

## 本地验证

```bash
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/apparel/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/wearable-device/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/personal-care/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_result.py examples/apparel/result.json
python3 tests/run_tests.py
```

## 社区版不包含什么

- 客户私有 Brief、SOP、截图和交付文档；
- 客户或第三方的产品图、测试视频和品牌素材；
- 特定厂商的付费生成适配器、内部参数和凭证；
- 对平台声音、口型、产品保真、ASR 或成本的能力保证；
- 把本地 JSON 校验通过表述为真实平台视听验收通过。

添加任何媒体前，请先阅读 [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md)。

## Apache-2.0 许可说明

Apache License 2.0 允许商业使用、修改、分发和私有使用，并提供明确的专利授权。再分发时需要保留许可证与相关声明。它不会自动授予第三方素材、客户资料、平台商标或人物肖像的使用权。

换句话说：你选择 Apache-2.0 后，其他人可以合法把这套社区版用于商业项目，只要遵守许可证条件。

完整条款见 [LICENSE](LICENSE)，项目声明见 [NOTICE](NOTICE)。

## 当前状态

Skill 结构、校验器、三个样例与负向回归已经在本地验证。实际视频质量、付费调用、口型同步、ASR 准确性和最终渲染，需要在各目标平台分别测试。当前不将本地验证等同于真实平台端到端验收。

