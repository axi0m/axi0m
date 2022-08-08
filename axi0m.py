from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

# Tree class
# https://rich.readthedocs.io/en/stable/tree.html

tree = Tree(f"[link=https://kevindienst.blog]Kevin Dienst",
    guide_style="bold cyan",
    )
python_tree = tree.add("🐍 Python")
secmon_tree = tree.add(":eyes: Security Monitoring")
rto_tree = tree.add(":boom: Red Team Operations")

# Define bbcode text, supports emoji shortcodes
about = """\
:wave: I'm an information security practitioner who specializes in red team operations, security monitoring, and Python. 
[green]Read my blog [link=https://kevindienst.blog]kevindienst.blog[/]
[green]Follow me on twitter [link=https://twitter.com/kevindienst]@kevindienst[/]"""

# Panel class
# Used to generate border for about content
# https://rich.readthedocs.io/en/stable/panel.html

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="purple", title="[b]Hi there", width=60
)

# Print to console our panel and tree in columnar form
# https://rich.readthedocs.io/en/stable/columns.html
console.print(Columns([panel, tree]))

# Pre-format our HTML output
CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

# Save the console output to README.html
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)