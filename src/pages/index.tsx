import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from '@site/src/pages/index.module.css';

type Journey = {title: string; text: string; to: string; action: string};

export default function Home(): React.ReactNode {
  const {i18n} = useDocusaurusContext();
  const en = i18n.currentLocale === 'en';
  const journeys: Journey[] = en
    ? [
        {title: 'Operate Nexus Server', text: 'Manage Environments, Agents, Providers, access, billing, and cloud operations from one Console.', to: '/server/', action: 'Open the Server guide'},
        {title: 'Run financial workflows', text: 'Use TokenBank desks for credit, funding, Agent finance, Provider finance, markets, and SLA protection.', to: '/tokenbank/getting-started/first-workflow', action: 'Start with TokenBank'},
        {title: 'Connect an OpenWrt edge', text: 'Pair a router, obtain a managed device certificate, publish IPv6 Agents, and avoid Docker hosting.', to: '/server/guides/connect-openwrt', action: 'Connect an edge node'},
        {title: 'Build an IPv6 Agent', text: 'Use the Python SDK to give each Agent an IPv6 address and expose HTTP, SSE, MCP, or A2A.', to: '/sdk/quickstart/first-agent', action: 'Open the SDK guide'},
      ]
    : [
        {title: '运行 Nexus Server', text: '在同一个 Console 中管理 Environment、Agent、Provider、访问控制、计费和云端运营。', to: '/server/', action: '打开 Server 指南'},
        {title: '处理 TokenBank 业务', text: '使用工作台处理授信、资金池、Agent 与 Provider 融资、内部市场和 SLA 保障。', to: '/tokenbank/getting-started/first-workflow', action: '开始 TokenBank 指南'},
        {title: '接入 OpenWrt 边缘节点', text: '配对路由器、签发托管设备证书并发布 IPv6 Agent，从而不必租用 Docker 主机。', to: '/server/guides/connect-openwrt', action: '接入边缘节点'},
        {title: '构建 IPv6 Agent', text: '使用 Python SDK 为每个 Agent 分配 IPv6，并发布 HTTP、SSE、MCP 或 A2A 服务。', to: '/sdk/quickstart/first-agent', action: '打开 SDK 指南'},
      ];

  return (
    <Layout
      title={en ? 'Documentation' : '用户文档'}
      description={en ? 'Documentation for Nexus Server, TokenBank, OpenWrt, and the Python SDK.' : 'Nexus Server、TokenBank、OpenWrt 与 Python SDK 的一体化用户文档。'}
    >
      <header className={`hero hero--primary ${styles.hero}`}>
        <div className="container">
          <div className={styles.badges}>
            <span>Nexus Server</span><span>TokenBank</span><span>OpenWrt 3.1</span><span>Python SDK 0.22.0</span>
          </div>
          <h1 className="hero__title">Nexus</h1>
          <p className={`hero__subtitle ${styles.subtitle}`}>
            {en
              ? 'One documentation site for the cloud control plane, financial workflows, OpenWrt edge network, and Agent SDK.'
              : '在同一个文档站中完成云端控制面、金融工作流、OpenWrt 边缘网络和 Agent SDK 的配置与使用。'}
          </p>
          <div className={styles.heroActions}>
            <Link className="button button--secondary button--lg" to="/server/getting-started/quickstart">
              {en ? 'Deploy Nexus Server' : '部署 Nexus Server'}
            </Link>
            <Link className="button button--outline button--secondary button--lg" to="/tokenbank/getting-started/first-workflow">
              {en ? 'Use TokenBank' : '使用 TokenBank'}
            </Link>
          </div>
        </div>
      </header>
      <main>
        <section className="container margin-vert--xl">
          <div className={styles.sectionHeading}>
            <span>{en ? 'START WITH AN OUTCOME' : '从目标开始'}</span>
            <h2>{en ? 'What do you need to do?' : '你要完成什么？'}</h2>
          </div>
          <div className="row">
            {journeys.map((journey) => (
              <div className="col col--3 margin-bottom--lg" key={journey.title}>
                <div className="docs-card">
                  <h3>{journey.title}</h3><p>{journey.text}</p><Link to={journey.to}>{journey.action} →</Link>
                </div>
              </div>
            ))}
          </div>
        </section>
        <section className={styles.firstResult}>
          <div className="container">
            <div className={styles.sectionHeading}>
              <span>{en ? 'ONE PLATFORM, FOUR SURFACES' : '一个平台，四个产品面'}</span>
              <h2>{en ? 'Move from cloud identity to an edge Agent and its settlement trail' : '从云端身份走到边缘 Agent，再追踪到结算记录'}</h2>
            </div>
            <ol className={styles.steps}>
              <li><strong>{en ? 'Server owns cloud identity.' : 'Server 管理云端身份。'}</strong><small>{en ? 'Users, tenants, projects, roles, API keys, and audit records share one control plane.' : '用户、租户、项目、角色、API Key 和审计记录共用一个控制面。'}</small></li>
              <li><strong>{en ? 'OpenWrt owns the edge runtime.' : 'OpenWrt 管理边缘运行时。'}</strong><small>{en ? 'A paired router publishes globally reachable IPv6 Agents without creating containers.' : '配对后的路由器发布全球可达的 IPv6 Agent，不创建容器。'}</small></li>
              <li><strong>{en ? 'TokenBank records controlled value movement.' : 'TokenBank 记录受控的价值流转。'}</strong><small>{en ? 'Balanced entries, approvals, product gates, and audit trails make every financial action explainable.' : '双分录、审批、产品门控和审计链让每笔金融操作都可解释。'}</small></li>
            </ol>
          </div>
        </section>
      </main>
    </Layout>
  );
}
