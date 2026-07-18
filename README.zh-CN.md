# CollaborationOS

[English](README.md) | **简体中文**

<p>
  <a href="https://github.com/nickzhuchen66/collaborationos/releases"><img alt="Release" src="https://img.shields.io/github/v/release/nickzhuchen66/collaborationos?style=for-the-badge&label=release"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/nickzhuchen66/collaborationos?style=for-the-badge"></a>
  <a href="docs/gate-pack-v0.1/README.md"><img alt="Mode: manual and static" src="https://img.shields.io/badge/mode-manual%20%2F%20static-4f7cac?style=for-the-badge"></a>
  <a href="https://github.com/nickzhuchen66/collaborationos/discussions"><img alt="Discussions" src="https://img.shields.io/badge/discussions-open-2f855a?style=for-the-badge"></a>
</p>

**CollaborationOS（COS）** 是面向重要人类-AI协作的开源治理框架。它帮助团队恢复上下文、准入证据、绑定权限、形成决策、控制执行、独立验收、保留失败事实并沉淀学习，同时不把最终责任转交给 AI。

<p>
  <a href="#架构"><strong>了解架构</strong></a>
  ·
  <a href="#快速开始">快速开始</a>
  ·
  <a href="docs/adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md">接入手册</a>
  ·
  <a href="ROADMAP.md">路线图</a>
  ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

> COS v0.1.0 是一个**人工/静态治理基线**。它不是 Agent runtime、自动策略引擎、生产权限系统，也不声称已经完成跨 Host 验证。

## 为什么需要 CollaborationOS

AI 生成计划、代码、分析和操作指令的速度，已经快于多数团队检查其证据和权限的速度。真正危险的通常不只是生成错误，而是请求到执行之间的来源、权限和责任链条消失了。

COS 让这条链路可检查：

| 常见失控方式 | COS 的处理方式 |
|---|---|
| 从旧对话或不完整简报推断上下文 | 在后续工作前恢复并接受有边界的上下文包 |
| 把提交材料直接当成已接受证据 | 分离提交、准入、grounding 和排除 |
| 把参与者身份误当作权限 | 显式绑定功能角色和当前权限 |
| AI 建议悄悄变成执行指令 | 执行交接前必须有由人类负责的决策 |
| 把技术完成当作验收通过 | 分离执行证据与独立验收 |
| 清理失败现场或自动重试 | 保留失败事实，显式接管，禁止隐式重试 |
| 局部经验自动改写共享框架 | 学习候选必须经过独立的晋升权限 |

## 架构

COS 把稳定的治理核心与每个接入项目的业务系统分开。Host 项目继续拥有业务真相源、领域数据、权限、执行系统和最终决策；COS 提供协议、工件合同、Conformance 样例和接入指南。

```mermaid
flowchart TB
    H["Host 项目\n业务真相源"]

    subgraph COS["CollaborationOS 公开核心"]
        G["Governance\n宪法与不变量"]
        P["Protocols\nP01-P07"]
        A["Artifacts\nA01-A09 Schema 与模板"]
        C["Conformance\n126 个合成 Fixture 与 4 个 Matrix"]
        D["Adoption\nGate Pack 与 Host Adoption Kit"]

        G --> P
        P --> A
        A --> C
        C --> D
    end

    H <-->|"按引用接入，不转移业务 payload"| D
    D -.->|"仅提供有边界的治理指导"| H
```

### 七协议治理闭环

```mermaid
flowchart LR
    P01["P01 上下文恢复\nA01 Context Packet"]
    P02["P02 证据准入\nA02 Evidence Record"]
    P03["P03 权限绑定\nA03 Role/Authority Map"]
    P04["P04 决策先于指令\nA04 Decision + 可选 A05 Cost"]
    P05["P05 执行交接\nA06 Handoff"]
    P06["P06 独立验收\nA07 Acceptance + 可选 A08 Failure"]
    P07["P07 学习与晋升\nA09 Learning Candidate"]

    P01 --> P02 --> P03 --> P04 --> P05 --> P06 --> P07

    P05 -->|"legal stop"| STOP["不执行\n不隐式重试"]
    P06 -->|"失败或所有权歧义"| TAKEOVER["保留证据\n人工接管"]
    P07 -->|"独立人类权限"| PROMOTE["可选晋升决策"]
```

每个阶段都检查当前上游证据和权限。文件名、参与者身份、工具调用成功或后续结果，都不能反向创造权限。

## v0.1.0 包含什么

- P01-P07 **7 个治理协议**；
- A01-A09 **9 个严格 JSON Schema** 与对应的人类可读模板；
- 覆盖上下文、权限、证据、决策、成本、执行、验收、失败和学习的 **126 个合成 Fixture**；
- **4 个人工 Conformance Matrix**；
- 面向操作者的 **Manual/Static Gate Pack**；
- **新 Host 接入手册**和 Host 侧模板；
- 一个合成端到端案例；
- Apache-2.0 许可证与公开协作规则。

## 快速开始

1. 阅读[宪法](00_Governance/COS_Constitution.md)、[方法论](01_Core/COS_Methodology.md)和[目标架构](01_Core/COS_Target_Architecture.md)。
2. 根据[协议系统图](02_Protocols/COS_Protocol_System_Map_v0.1.md)依次执行 P01-P07。
3. 使用[工件注册表](03_Schemas_and_Templates/COS_Gate_Pack_Artifact_Register_v0.1.md)选择必要的 A01-A09 工件。
4. 按照[人工操作流程](docs/gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md)和[Conformance 指南](docs/gate-pack-v0.1/MANUAL_CONFORMANCE_GUIDE.md)完成检查。
5. 先走一遍虚构的 [Northstar Docs](examples/synthetic/README.md) 正例、legal-stop 和 failure/takeover 分支。
6. 新项目通过[Host Adoption Manual](docs/adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md)按版本引用 COS，不把 Host payload 复制进 COS。

## 根据你的角色选择入口

| 你的目标 | 推荐入口 | 结果 |
|---|---|---|
| 评估 COS | [方法论](01_Core/COS_Methodology.md) | 理解运行模型与能力边界 |
| 设计受治理的 AI 流程 | [协议系统图](02_Protocols/COS_Protocol_System_Map_v0.1.md) | 映射 P01-P07 阶段 |
| 准备重要变更 | [人工操作流程](docs/gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md) | 组装有边界的人工 Gate Pack |
| 为新项目接入 COS | [Host Adoption Manual](docs/adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md) | 保留 Host 业务主权的引用式接入 |
| 检查协议或 Schema | [Conformance 指南](docs/gate-pack-v0.1/MANUAL_CONFORMANCE_GUIDE.md) | 覆盖正例、legal-stop 与失败分支 |
| 公开贡献 | [贡献指南](CONTRIBUTING.md) | 提交合成、可审查的改进 |

## 核心规则

1. 人类最终权限必须显式声明，不能从参与关系推断。
2. 证据提交与证据准入分离。
3. 决策先于可执行指令。
4. 权限默认 false，并绑定到具体行动。
5. 执行成功与独立验收分离。
6. 失败证据必须保留，重试不能隐式发生。
7. 学习候选不会自动修改 COS Core。
8. Host 项目保留自己的业务真相源。

## 仓库结构

```text
.
├── 00_Governance/              # 公开宪法
├── 01_Core/                    # 方法论与目标架构
├── 02_Protocols/               # P01-P07 与依赖关系
├── 03_Schemas_and_Templates/   # A01-A09 Schema 与模板
├── 05_Conformance/             # 4 个 Matrix 与 126 个 Fixture
├── docs/
│   ├── gate-pack-v0.1/         # 面向操作者的 Manual/Static Gate Pack
│   └── adoption-kit-v0.1/      # 新 Host 接入指南与模板
├── examples/synthetic/         # 虚构案例，不包含 Host payload
└── .github/                    # 公开协作入口
```

非自指的[包清单](PACKAGE_MANIFEST.json)用路径、字节数和 SHA-256 绑定当前分支的其他所有 tracked 文件。

## 项目状态与边界

稳定公开版本为 `v0.1.0`。`main` 上的工作优先改善公开可用性和仓库质量，不扩大 v0.1.0 的能力声明。

当前 COS **不包含**自动 validator、CLI、SDK、SaaS、Agent framework、可执行 Skill/Workflow、Host connector 或生产执行权限，也不声称完成跨 Host 验证。详见[公开路线图](ROADMAP.md)。历史实验和内部治理记录不会进入本公开仓库。

## 社区

- 提交前阅读[贡献指南](CONTRIBUTING.md)和[行为准则](CODE_OF_CONDUCT.md)。
- 在 [GitHub Discussions](https://github.com/nickzhuchen66/collaborationos/discussions) 讨论设计和接入问题。
- 在 [Issues](https://github.com/nickzhuchen66/collaborationos/issues) 提交有边界的问题、文档缺口和建议。
- 敏感问题按照[安全政策](SECURITY.md)报告。

如果 COS 对你的人类-AI协作有帮助，Star 可以帮助更多开发者发现它。

## 许可证与引用

CollaborationOS 采用 [Apache License 2.0](LICENSE)。归属说明见 [NOTICE](NOTICE)，引用信息见 [CITATION.cff](CITATION.cff)。
