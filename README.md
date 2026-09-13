Getting Started with Claude Code
What Is Vibe Coding?
Vibe coding means describing what you want in plain English and letting an AI coding agent build it for you. You don't need to know how to code — you guide the process by explaining what you need, reviewing what the AI creates, and asking for changes.

Think of it like working with a very fast assistant: you describe the goal, the assistant builds it, and you steer the result. The skill is in communicating clearly and evaluating the output — not in writing code yourself.

What You Need
Claude Max plan subscription (~$20/month), which gives you access to Claude Code.
A terminal application: Terminal.app on Mac or Windows Terminal on Windows.
Node.js and npm installed from nodejs.org.
A folder where you'll work, such as ~/csp-vibe-code.
Quick Start (5 Minutes)
1. Subscribe to Claude Max
Go to claude.ai and subscribe to the Max plan ($20/month). This gives you access to Claude Code.

2. Open Your Terminal
Mac: Open the Terminal app (search "Terminal" in Spotlight).
Windows: Open Windows Terminal or Command Prompt.
Chromebook: Enable Linux (Settings > Advanced > Developers > Linux), then open the Terminal app.
3. Install Claude Code
Type this command and press Enter:

npm install -g @anthropic-ai/claude-code
If you see npm: command not found, install Node.js first from nodejs.org (download the LTS version), then try again.

4. Start Your First Session
Create a folder for your project, navigate to it, and launch Claude Code:

mkdir my-project
cd my-project
claude
Claude Code will open an interactive session. Describe what you want to build in plain English.

Example Prompts
Try these prompts:

"Build me a simple Python script that reads a CSV and prints summary statistics."
"Create an HTML page with a form that takes a name and shows a personalized greeting."
"Write a function that takes a list of numbers and returns the median."
Start simple, then add complexity. If something isn't right, tell Claude Code what to change.

Troubleshooting
"command not found": Make sure Node.js is installed (node --version should show a number). Restart your terminal after installing.
"permission denied": On Mac/Linux, try sudo npm install -g @anthropic-ai/claude-code.
Claude Code shows errors: Describe the error to Claude Code itself: "I'm getting this error: [paste error]. How do I fix it?" This is part of the learning process.
Need help? Ask your instructor or post in the course discussion board. Include a screenshot of your terminal.
