import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import imageDimensionsGuard from './scripts/image-dimensions.cjs';

const normalizeBaseUrl = (value: string): string => {
  const trimmed = value.trim().replace(/^\/+|\/+$/g, '');
  return trimmed ? `/${trimmed}/` : '/';
};

const useJieba = process.env.DOCS_SEARCH_JIEBA === '1';
const siteUrl = (process.env.DOCS_URL || 'http://localhost:3000').replace(/\/$/, '');
const baseUrl = normalizeBaseUrl(process.env.DOCS_BASE_URL || '/');

const searchOptions: Record<string, unknown> = {
  indexDocs: true,
  indexBlog: false,
  indexPages: true,
  language: useJieba ? ['zh', 'en'] : 'en',
};

if (!useJieba) {
  searchOptions.lunr = {
    tokenizerSeparator: /[\s\-]+|(?=[\u3400-\u9fff])|(?<=[\u3400-\u9fff])/,
  };
}

const config: Config = {
  title: 'Nexus',
  tagline: 'Build and connect AI Agents',
  favicon: 'img/favicon.svg',
  url: siteUrl,
  baseUrl,
  trailingSlash: false,
  organizationName: process.env.ORGANIZATION_NAME || 'Nexilume-AI',
  projectName: process.env.PROJECT_NAME || 'nexus-docs',
  deploymentBranch: process.env.DEPLOYMENT_BRANCH || 'gh-pages',
  onBrokenLinks: 'throw',
  markdown: {
    mermaid: true,
    hooks: {onBrokenMarkdownLinks: 'throw'},
  },
  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans', 'en'],
    localeConfigs: {
      'zh-Hans': {label: '简体中文', htmlLang: 'zh-CN'},
      en: {label: 'English', htmlLang: 'en-US'},
    },
  },
  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs-openwrt',
          routeBasePath: 'openwrt',
          sidebarPath: './sidebars-openwrt.ts',
          showLastUpdateAuthor: false,
          showLastUpdateTime: false,
        },
        blog: false,
        theme: {customCss: './src/css/custom.css'},
      } satisfies Preset.Options,
    ],
  ],
  plugins: [
    imageDimensionsGuard,
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'sdk',
        path: 'docs-sdk',
        routeBasePath: 'sdk',
        sidebarPath: './sidebars-sdk.ts',
        showLastUpdateAuthor: false,
        showLastUpdateTime: false,
      },
    ],
    ['@cmfcmf/docusaurus-search-local', searchOptions],
  ],
  themes: ['@docusaurus/theme-mermaid'],
  themeConfig: {
    colorMode: {respectPrefersColorScheme: true},
    navbar: {
      title: 'Nexus',
      items: [
        {type: 'docSidebar', sidebarId: 'openwrtSidebar', label: 'OpenWrt', position: 'left'},
        {type: 'docSidebar', docsPluginId: 'sdk', sidebarId: 'sdkSidebar', label: 'Python SDK', position: 'left'},
        {type: 'localeDropdown', position: 'right'},
        {
          type: 'dropdown',
          label: 'GitHub',
          position: 'right',
          items: [
            'nexus-cloud-community',
            'nexus-mobile',
            'nexus-docs',
            'nexus-agent-sdk-python',
            'nexus-openwrt',
          ].map((repository) => ({
            label: repository,
            href: `https://github.com/Nexilume-AI/${repository}`,
          })),
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentation',
          items: [
            {label: 'OpenWrt', to: '/openwrt/'},
            {label: 'Python SDK', to: '/sdk/'},
          ],
        },
        {
          title: 'Project',
          items: [{label: 'GitHub', href: 'https://github.com/Nexilume-AI/nexus-docs'}],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Nexus`,
    },
    prism: {additionalLanguages: ['bash', 'json', 'python', 'powershell', 'yaml']},
  } satisfies Preset.ThemeConfig,
};

export default config;
