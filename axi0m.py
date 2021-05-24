from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 [link=https://kevindienst.blog]Kevin Dienst", guide_style="bold cyan")
python_tree = tree.add("🐍 Python", guide_style="green")
python_tree.add("Creator of [link=https://github.com/axi0m/violent_python]Violent Python")
secmon_tree = tree.add(":eyes: Security Monitoring", guide_style="purple")
secmon_tree.add("Contributor to [link=https://github.com/SigmaHQ/sigma]Sigma")
rto_tree = tree.add(":boom: Red Team Operations", guide_style="red")
rto_tree.add("Contributor to [link=https://github.com/redcanaryco/atomic-red-team]Atomic Red Team")

about = """\
:wave: I'm an information security professional who specializes in red team operations, security monitoring, and Python. 
[green]Read my blog [bold link=https://kevindienst.blog]kevindienst.blog[/]
[green]Follow me on twitter [bold link=https://twitter.com/kevindienst]@kevindienst[/]"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)