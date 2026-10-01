---
sidebar_position: 3
title: Connect Computer Runtime
---

# Connect Computer Runtime

Computer Runtime runs as your operating-system user and connects outbound to Nexus Cloud over WSS. It does not require an inbound SSH port or a public IP address.

1. Install the `computer` extra, plus `browser` if you want browser control.
2. Create a Computer pairing link in your Nexus Cloud workspace.
3. Run the following commands as your normal user:

```sh
python -m pip install "nexilume[computer,browser]==0.47.0"
nexus-computer setup "<pairing-url-from-nexus-cloud>"
nexus-computer status
```

Wait for the registration to report `connected`. Attach the Computer to a Run and grant the required scopes before an agent uses its files, terminal or browser. Each registration has its own workspace root and identity.

Useful commands:

```sh
nexus-computer logs
nexus-computer restart
nexus-computer repair
nexus-computer unpair --registration <registration-id>
```

`repair` repairs autostart for an existing pairing. `unpair` revokes the selected registration. You can pair the same computer with more than one workspace by running `setup` for each pairing link.

### Linux browser setup

Install a supported Chrome/Chromium browser, or download Chromium with Playwright:

```sh
python -m playwright install chromium
```

On a minimal Linux installation, Playwright may also need system libraries; `python -m playwright install-deps chromium` installs them and can request administrator privileges.

For a Playwright-downloaded browser or a custom browser location, configure the Runtime service explicitly:

```sh
systemctl --user edit nexus-computer.service
```

Add the following, replacing the executable path with the actual installed browser path:

```ini
[Service]
Environment="NEXUS_BROWSER_EXECUTABLE=/absolute/path/to/chrome"
Environment="NEXUS_BROWSER_HEADLESS=true"
```

Then restart:

```sh
systemctl --user daemon-reload
nexus-computer restart
```

Installing the Playwright Python package alone does not install a browser. An environment variable set only in an interactive shell does not update an already running systemd service.
