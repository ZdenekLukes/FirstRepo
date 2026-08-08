---
title: "15. MCP, Skills, Plugins, and Connectors"
part: "VII — Tools: When the LLM Stops Only Writing"
status: release-candidate
version: "0.8-eng"
updated: 2026-08-08
snapshot: "2026-08-08"
---

# 15. MCP, Skills, Plugins, and Connectors

<!-- visual:15-mcp-architecture.svg -->

![MCP architecture](assets/diagrams/15-mcp-architecture.svg)

*Figure: A standardized layer between an AI host and external tools or resources.*

The previous chapter connected an LLM to tools. That immediately creates a new engineering problem: every tool speaks a different language.

```text
GitHub → REST / GraphQL
Slack → Slack API
Google Calendar → Google API
filesystem → local OS
PostgreSQL → SQL
Cadence → scripts / proprietary interfaces
```

If every AI application integrates every system independently, the number of one-off adapters grows quickly.

```text
5 AI applications
×
20 enterprise systems
=
100 separate integrations
```

Each integration has to handle authentication, schemas, errors, permissions, data formats, and updates.

**MCP — Model Context Protocol** addresses this integration problem by defining a common interface between AI hosts and external capabilities.

Before going further, separate the vocabulary:

```text
MCP       = protocol
Tool      = executable capability
Skill     = reusable instruction/workflow package
Plugin    = platform-specific extension bundle
Connector = integration with a service or data source
API       = interface exposed by a particular service
```

These concepts may be packaged together, but they are not interchangeable.

---

## 15.1 Why an Integration Standard Matters

Without a standard layer, an AI application tends to look like this:

```text
AI application
│
├── custom GitHub integration
├── custom Slack integration
├── custom database integration
├── custom filesystem wrapper
└── custom calendar integration
```

Then another AI application rebuilds much of the same work.

A standard changes the shape of the problem:

```text
             AI application
                   ↓
                 MCP
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     GitHub      Slack     Database
      server      server      server
```

The underlying APIs still exist. MCP creates a standardized **AI-facing layer** above them.

A useful analogy is USB-C. USB-C does not define how a monitor or SSD works internally. It defines a common way to connect devices. MCP plays a similar role for AI applications.

---

## 15.2 What MCP Is — and Is Not

MCP is an open protocol for connecting AI applications to external systems.

It can standardize how a host discovers and uses:

- tools,
- resources,
- reusable prompts,
- structured inputs and outputs.

A simplified architecture is:

```text
LLM / agent
    ↓
AI host application
    ↓
MCP client
    ↓
MCP protocol
    ↓
MCP server
    ↓
API / filesystem / database / application
```

MCP is **not**:

- a model,
- an agent framework,
- a database,
- or a security policy by itself.

It is a communication and capability-discovery protocol.

That distinction matters because standards can reduce integration cost without automatically solving authorization, trust, or governance.

---

## 15.3 MCP Server

An **MCP server** exposes capabilities in a standardized form.

It may wrap:

```text
filesystem
GitHub API
internal database
simulation service
enterprise application
```

An internal simulation server, for example, could expose:

```text
TOOLS
- run_simulation
- get_simulation_status
- extract_measurements

RESOURCES
- available_testbenches
- simulator_documentation
```

Internally, the server may use a proprietary API, command-line interface, or existing service. The AI host does not need to know those implementation details.

### Local and remote servers

A server may run locally:

```text
AI app
  ↓
local MCP server
  ↓
filesystem
```

or remotely:

```text
AI app
  ↓ HTTPS
remote MCP server
  ↓
cloud or enterprise service
```

This is useful in hybrid architectures. A sensitive filesystem integration can stay inside the company network while a public search integration remains external.

---

## 15.4 MCP Client and Host

The **host** is the application the human interacts with: a desktop AI app, coding agent, IDE, or internal agent platform.

The **client** is the protocol implementation inside the host that communicates with a particular MCP server.

```text
HOST
│
├── MCP client → GitHub server
├── MCP client → filesystem server
└── MCP client → simulation server
```

From the user’s point of view, these can appear as one coherent toolbox.

The architectural benefit is modularity. A server can be changed or replaced without redesigning the entire agent.

---

## 15.5 Tools

A **tool** is an executable capability:

```text
search_files(query)
run_simulation(testbench, corner)
create_issue(title, body)
get_calendar_events(date)
```

A tool definition usually includes a name, description, and input schema. It may also define a structured output schema.

The model can then select a tool when the task requires it:

```text
user:
“Run the TT gain simulation.”
   ↓
LLM
   ↓
run_simulation(test="gain", corner="TT")
   ↓
MCP server
   ↓
simulator
   ↓
result
   ↓
LLM interprets result
```

A tool is an **action surface**, which makes it the most security-sensitive primitive in many agentic systems.

---

## 15.6 Resources

A **resource** is something the AI application can read.

Examples:

```text
file:///project/spec.md
database://projects/A17/specification
simulation://run/204/results
```

A useful mental split is:

```text
TOOL
→ do something

RESOURCE
→ read something
```

Resources may represent documents, configuration, logs, database records, or current state from an external system.

This distinction helps reduce authority. A host can expose read-only resources without exposing write-capable tools.

---

## 15.7 Skills

A **skill** is not the same thing as a tool.

A skill usually describes **how to perform a class of work**. It can package instructions, domain knowledge, checklists, references, and reusable workflow steps.

Example:

```text
skill: review-pull-request

1. inspect diff
2. run tests
3. look for security risks
4. separate blocking from non-blocking issues
5. write structured review
```

The skill may use tools such as:

```text
get_diff()
read_file()
run_tests()
post_comment()
```

So:

```text
SKILL
= how to do the job

TOOL
= an action available while doing the job
```

Keeping these concepts separate makes agent architecture much easier to reason about.

---

## 15.8 Plugins

A **plugin** is a broader, platform-dependent package.

It may contain:

- tools,
- skills,
- an MCP server,
- UI components,
- configuration,
- permissions,
- documentation.

Different products use the word *plugin* differently, so never infer architecture from the label alone.

When evaluating a plugin, ask:

> What code does it run, what systems can it access, what permissions does it receive, and how is it updated?

The packaging term is less important than the actual security and execution model.

---

## 15.9 Connectors

A **connector** is usually an adapter to a particular external service or data source:

```text
Google Drive connector
Slack connector
GitHub connector
SharePoint connector
```

A connector may handle:

- authentication,
- authorization,
- synchronization,
- search,
- format conversion,
- source-specific metadata.

It may be implemented directly against an API or exposed through an MCP server.

The term describes the **purpose of the integration**, not necessarily the protocol used underneath.

---

## 15.10 API vs. MCP

A service API might expose endpoints such as:

```text
POST /repos/{owner}/{repo}/issues
GET  /repos/{owner}/{repo}/commits
```

An MCP server can wrap the same API as AI-friendly capabilities:

```text
create_issue(...)
search_commits(...)
```

The stack becomes:

```text
AI agent
   ↓
MCP
   ↓
MCP server
   ↓
service API
   ↓
service
```

MCP does not replace APIs. It often **adapts them into a standardized interface that AI hosts can discover and use consistently**.

---

## 15.11 The Security Boundary Is Still Outside the Model

A standardized tool protocol makes integration easier. It does not make every integration safe.

For every server, tool, connector, or plugin, we still need to know:

```text
Who authenticated?
What can they read?
What can they change?
Which credentials are used?
What leaves the system?
What is logged?
Can the action be reversed?
```

The protocol describes communication. Authorization must still be enforced by deterministic software.

A model should not be able to grant itself broader permissions by producing persuasive text.

---

## 15.12 Capability Discovery Can Expand the Attack Surface

Automatic discovery is convenient: the host asks a server what tools or resources are available.

But more discoverable capabilities mean a larger action space.

If an agent can see 100 tools when it needs 3, we increase:

- selection errors,
- prompt-injection opportunities,
- accidental side effects,
- and debugging complexity.

A strong system therefore exposes only the capabilities required for the current role or task.

> **Least privilege applies to tool discovery as well as to credentials.**

---

## 15.13 Why MCP Matters for Enterprise AI

The long-term value of a protocol is not that it makes a demo easier. It is that it can decouple components.

An enterprise AI platform may want to swap:

- the model,
- the user interface,
- the agent runtime,
- or the orchestration framework

without rewriting every integration to GitHub, documents, simulation systems, and databases.

That creates a more durable architecture:

```text
models change
hosts change
agent frameworks change

integration boundary remains stable
```

This is one of the reasons standards matter in a market where the model layer changes every few months.

---

## 15.14 A Constrained MCP Example: AI-Assisted Analog Design

Consider an agent connected to an analog-design environment. Giving it an unrestricted shell would make the integration powerful, but it would also make the security boundary unnecessarily broad.

A safer MCP server can expose only the operations the workflow actually needs:

```text
TOOLS

run_spectre_simulation(
    testbench,
    corner,
    temperature
)

get_measurement(
    run_id,
    measurement
)

list_available_testbenches()
```

The agent cannot execute:

```text
rm -rf project/
```

because no such tool exists. Its action space is defined by the host, not by what the model can imagine.

Above those tools, a skill can encode the engineering procedure:

```text
SKILL: verify-LDO-design

1. read the specification
2. select the required testbenches
3. run the required corners
4. extract measurements
5. compare results with the specification
6. produce a verification report
```

This separation is useful beyond analog design:

- **MCP tools provide the hands.**
- **The skill provides the workflow.**
- **The LLM provides interpretation and bounded decision-making.**
- **Host software defines permissions and the security boundary.**

The result is more useful than a generic shell and easier to audit.

---

## Key Takeaways

1. **MCP is a protocol, not a model or agent framework.**
2. **It standardizes how AI hosts connect to external tools and resources.**
3. **An MCP server adapts an underlying system into an AI-facing interface.**
4. **A tool is an action; a resource is something to read.**
5. **A skill describes how to perform work; it may use many tools.**
6. **Plugins and connectors are packaging/integration concepts whose exact meaning depends on the platform.**
7. **MCP usually wraps existing APIs rather than replacing them.**
8. **Standardization reduces integration cost but does not replace authentication or authorization.**
9. **Capability discovery should still follow least privilege.**
10. **A stable integration layer can outlive individual models and agent frameworks.**

Once a model has instructions, context, state, and tools, it becomes possible to repeat a decision-and-action loop toward a goal.

That is the point where the word **agent** becomes useful.