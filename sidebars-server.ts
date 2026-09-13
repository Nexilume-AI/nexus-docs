import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  serverSidebar: [
    'index',
    {
      type: 'category',
      label: '开始使用',
      collapsed: false,
      items: [
        'getting-started/quickstart',
        'getting-started/console-tour',
        'getting-started/first-workspace',
        'getting-started/first-agent',
      ],
    },
    {
      type: 'category',
      label: '执行环境',
      collapsed: false,
      link: {type: 'doc', id: 'environments/index'},
      items: ['environments/computer', 'environments/mobile'],
    },
    {
      type: 'category',
      label: '核心资源',
      collapsed: false,
      items: [
        'agents/index',
        'agents/private-runs',
        'data-assets/index',
        'providers/index',
        'model-pool/index',
        'routers/index',
        'marketplace/index',
      ],
    },
    {
      type: 'category',
      label: '场景教程',
      collapsed: false,
      items: [
        'tutorials/provider-router-api',
        'tutorials/team-access-lifecycle',
        'tutorials/marketplace-billing',
      ],
    },
    {
      type: 'category',
      label: '操作与可观测性',
      collapsed: false,
      link: {type: 'doc', id: 'operations/index'},
      items: [
        'operations/observability',
        'operations/inbox',
        'operations/production-readiness',
        'operations/backup-and-restore',
        'operations/upgrade-and-rollback',
      ],
    },
    {
      type: 'category',
      label: '访问与计费',
      items: ['access/index', 'billing/index', 'settings/index'],
    },
    {
      type: 'category',
      label: '管理',
      items: [
        'administration/plan-catalog',
        'guides/production-deployment',
      ],
    },
    {
      type: 'category',
      label: '概念',
      items: ['concepts/identity-and-request-path'],
    },
    {
      type: 'category',
      label: '指南',
      items: [
        'guides/connect-openwrt',
        'guides/api-keys',
      ],
    },
    {
      type: 'category',
      label: '参考',
      items: [
        'reference/user-surfaces',
        'reference/api',
        'reference/configuration',
        'reference/statuses-and-errors',
      ],
    },
    {
      type: 'category',
      label: '排错',
      items: ['troubleshooting/common'],
    },
  ],
};

export default sidebars;
