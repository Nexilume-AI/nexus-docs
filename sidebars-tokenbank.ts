import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tokenbankSidebar: [
    'index',
    {
      type: 'category',
      label: '开始使用',
      collapsed: false,
      items: [
        'getting-started/console-tour',
        'getting-started/first-workflow',
      ],
    },
    {
      type: 'category',
      label: '理解 TokenBank',
      collapsed: false,
      items: [
        'concepts/ledger-and-controls',
        'concepts/money-and-rights-flow',
      ],
    },
    {
      type: 'category',
      label: '八个工作台',
      collapsed: false,
      items: [
        'desks/credit',
        'desks/funding',
        'desks/derivatives',
        'desks/agent-finance',
        'desks/agent-market',
        'desks/provider-finance',
        'desks/provider-market',
        'desks/sla',
      ],
    },
    {
      type: 'category',
      label: '操作指南',
      items: [
        'guides/use-desks',
        'guides/financial-flows',
        'guides/admin-operations',
      ],
    },
    {
      type: 'category',
      label: '参考',
      items: [
        'reference/desks-and-products',
        'reference/permissions-and-api',
        'reference/statuses-and-errors',
        'reference/automation-and-settlement',
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
