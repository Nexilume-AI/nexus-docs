# Real UI capture

**English** · [Chinese](capture-notes_zh.md)

## Environment and limits

- Date: October 1, 2026 (Asia/Shanghai).
- Edition: **Nexus Enterprise**, running through the existing Cloud launcher.
- Account: dedicated non-platform-admin demo identity in its own Organization.
- Agent: `Launch-notes-assistant`, private and unpublished, in the demo Project.
- Runtime: a real Docker container built through **Upload Python**. No mock API,
  injected UI state or preconstructed conversation was used.
- Workload: deterministic Python; no model inference, paid API, personal Computer,
  Browser, Mobile or OpenWrt operation is demonstrated in these images.
- Source: [readme_launch_agent.py](../../examples/readme_launch_agent.py).

The images are original browser screenshots at the browser's current viewport.
No labels, status indicators or results were painted over the UI. The responsive
layout uses Live / Context panels at this width. Captures exclude login forms,
tokens, device pairing codes, private endpoints and personal files.

Enterprise Organization, pricing and commercial navigation do not imply those
features ship in Community. A screenshot proves the displayed moment, not general
production readiness, model quality or performance. These files are **not video**.

## Reproduce

1. Configure the supported Python source-build profile, execution worker and
   private file storage for your installation. Use a fresh test account/project.
2. Create a private Agent and select **Nexus Container → Upload Python**.
3. Upload the linked file, without requirements or secrets. Build it, wait for the
   verified tool catalog, then explicitly deploy the candidate.
4. Open **Test Agent privately** and send:

   > Prepare a launch checklist for a self-hosted Python Agent. Include installation, a first private Run, permissions and troubleshooting.

5. Inspect the Plan, then answer **Self-hosting operators** in the inline question.
6. Wait for Run completion. In this installation, a new SDK-uploaded output stays
   scan-pending until explicitly scanned. As the demo Agent owner, open **Data
   Assets**, create a private collection, then choose **Import assets → Agent
   assets → Launch-notes-assistant → Output files & images**. Select the completed
   Run and `launch-checklist.md`, then choose **Scan output**. Wait for **scan
   passed / policy approved**. Do not bypass a failed scan.
7. Optionally choose **Capture approved output** to archive it to that private
   collection. This does not publish a Marketplace release.
8. Return to the original Private Run, open **Context → Files**, select
   `launch-checklist.md` and inspect its Markdown preview. It contains the brief
   and the chosen audience.

The example deliberately uploads a container-generated temporary file through
`output.upload_file()`. `output.write_text()` instead uses the Attached Computer
workspace and is not appropriate for this device-free example. The temporary
directory is cleaned by Python after upload; the Cloud output belongs to the Run.
