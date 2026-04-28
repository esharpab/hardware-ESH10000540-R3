# SharpMES in Claude Code

SharpMES is our Manufacturing Execution System. It tracks parts, products, inventory, serial numbers, work orders, and manufacturing processes. You can query it conversationally through Claude Code once the MCP server is connected.

## Part number prefixes

| Prefix | Stands for | Used for |
|---|---|---|
| **EGP** | E-Sharp Goods Purchased | Bought components — resistors, capacitors, ICs, connectors, etc. |
| **ESH** | E-Sharp (in-house) | Manufactured items — PCBAs, assemblies, finished products |
| **EPN** | E-Sharp Part N… | Purchased non-components — cables, screws, mechanical parts |

Format is always prefix + 8 digits, e.g. `EGP10000898`, `ESH10000121`.

**Serial numbers** track individual manufactured units: format `Axxxxxxx`, e.g. `A000801`.

**Manufacturer part numbers** (e.g. `BAT54C`, `STM32F407`) are separate from internal part numbers — use the manufacturer part number to look something up if you don't know the EGP/ESH number yet.

## Example queries

**Finding a part**
> "Find BAT54C"
> "Search for STM32F407"
> "Look up EGP10000898"

**Inventory**
> "How much stock do we have of EGP10000898?"
> "Show inventory for BAT54C"
> "Are there any consigned parts with low stock?"

**Products and BOMs**
> "Show the BOM for ESH10000121"
> "Which products use EGP10000898?"
> "List revisions for ESH10000121"

**Serial numbers**
> "What's the status of serial number A000801?"
> "Show the build history for A000801"
> "What are the child serial numbers of A000801?"

**Work orders**
> "Show open work orders"
> "Find work orders for ESH10000121"
> "What are the details of work order [ID]?"

**Manufacturing steps and testing**
> "What steps have been performed on A000801?"
> "Show test stations"
> "Get step details for [step ID]"

**Locations and sites**
> "Where is BAT54C stored?"
> "List manufacturing sites"
> "Find location [name]"

## Tips

- If you know the internal part number (EGP/ESH/EPN), use it — searches are faster and unambiguous.
- If you only know the manufacturer part number, just paste it in and Claude will find the internal number first.
- ESH numbers are both parts *and* products — you can ask for BOM, inventory, and product details on the same number.
- Serial numbers start with `A`, not `ESH` or `EGP` — if you're tracking a specific unit off the line, that's what you want.

## Adding the MCP server to Claude Code

Run this once in your terminal:

```bash
claude mcp add sharpmes --transport http https://sharpmes-mcp-server-d4ceatb7chbge3eq.swedencentral-01.azurewebsites.net/mcp
```

Then verify it connected:

```bash
claude mcp list
```

You should see `sharpmes: ... - ✓ Connected`. You only need to do this once — it persists across sessions.

If you want it available in all your projects (not just the current one), add the `-s user` flag:

```bash
claude mcp add sharpmes --transport http https://sharpmes-mcp-server-d4ceatb7chbge3eq.swedencentral-01.azurewebsites.net/mcp -s user
```
