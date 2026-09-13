// Public documentation for all four Nexus products; contains no application server source.
import type {Config} from '@docusaurus/types';
import core from './site-config';

const classic = core.presets![0] as [string, Record<string, unknown>];
const theme = core.themeConfig as any;

const config: Config = {
  ...core,
  tagline: 'Build, connect, operate, and finance AI Agents',
  presets: [[classic[0], {...classic[1], pages: {path: 'src/pages'}}]],
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'server',
        path: 'docs-server',
        routeBasePath: 'server',
        sidebarPath: './sidebars-server.ts',
        showLastUpdateAuthor: false,
        showLastUpdateTime: false,
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'tokenbank',
        path: 'docs-tokenbank',
        routeBasePath: 'tokenbank',
        sidebarPath: './sidebars-tokenbank.ts',
        showLastUpdateAuthor: false,
        showLastUpdateTime: false,
      },
    ],
    ...core.plugins!,
  ],
  themeConfig: {
    ...theme,
    navbar: {
      ...theme.navbar,
      items: [
        {type: 'docSidebar', docsPluginId: 'server', sidebarId: 'serverSidebar', label: 'Server', position: 'left'},
        {type: 'docSidebar', docsPluginId: 'tokenbank', sidebarId: 'tokenbankSidebar', label: 'TokenBank', position: 'left'},
        ...theme.navbar.items,
      ],
    },
    footer: {
      ...theme.footer,
      links: [
        {
          title: 'Documentation',
          items: [
            {label: 'Nexus Server', to: '/server/'},
            {label: 'TokenBank', to: '/tokenbank/'},
            ...theme.footer.links[0].items,
            {label: 'Server diagnostics', to: '/server/troubleshooting/common'},
          ],
        },
        ...theme.footer.links.slice(1),
      ],
    },
  },
};

export default config;
