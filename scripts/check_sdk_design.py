"""Exercise the downloadable design example against the real local SDK/FastMCP.

Requires the SDK's fastmcp extra. No Router, model credentials or Cloud required.
This verifies local tools and feedback; it does not certify Cloud resources.
"""
import asyncio
import importlib.util
import os
from pathlib import Path
import os
import sys

SITE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(os.environ.get('NEXUS_SDK_SOURCE', 'sdk-source/src'))))
os.environ['NEXUS_AGENT_RUNTIME_MODE'] = 'hosted'
from fastmcp import Client
from nexus_agent import NexusRunContext

spec = importlib.util.spec_from_file_location('sdk_design_example', SITE/'static/downloads/sdk/document-agent.py')
example = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example)

async def main():
    expected = {'characters': 23, 'words': 4, 'lines': 2}
    assert example.analyze_text('hello nexus\nsecond line') == expected
    for invalid in ('', None, 'x'*20001):
        try:
            example.analyze_text(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid input accepted')
    events=[]
    # A test sink exercises feedback without fabricating a trusted Cloud token.
    def sink(event):
        events.append(event)
        return True
    ctx=NexusRunContext(run_id='docs-design-test', _event_sink=sink)
    try:
        assert example.inspect_document({'text':'hello nexus\nsecond line'},ctx)==expected
        ctx.flush()
        assert events, 'Expected Run feedback'
    finally:
        ctx.close()
    async with Client(example.agent.as_mcp_server().fastmcp) as client:
        tools=await client.list_tools()
        assert [tool.name for tool in tools]==['inspect_document']
        result=await client.call_tool('inspect_document', {'text':'hello nexus\nsecond line'})
        assert result.structured_content==expected, result
        invalid=await client.call_tool('inspect_document', {'text':''},raise_on_error=False)
        assert invalid.is_error, 'Expected schema rejection'
    print('PASS: business bounds, Run feedback, MCP discovery/invoke/schema rejection')

if __name__=='__main__':
    asyncio.run(main())
