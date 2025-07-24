from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged

class CommandNode(nodes.literal):
    pass

class CommandDirective(Directive):
    has_content = False
    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        command_text = self.arguments[0]
        node = CommandNode(command_text, command_text)
        node['classes'] += ['command-directive']
        return [node]

def setup(app):
    app.add_node(CommandNode, html=(visit_command_node, depart_command_node))
    return {'version': '1.0'}

def visit_command_node(self, node):
    self.body.append(self.starttag(node, 'code', '', CLASS='command-directive'))
    self.body.append(node.astext())
    self.body.append('</code><br><span class="subheading">')  # Add subheading style

def depart_command_node(self, node):
    self.body.append('</span>')
