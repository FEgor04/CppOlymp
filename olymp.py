import sublime
import sublime_plugin


class OlympCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.set_syntax_file('C++');
		clipboard=sublime.get_clipboard();	
		self.view.insert(edit, 0, '#include <bits/stdc++.h>\nusing namespace std;\nint main() {\n\tios_base::sync_with_stdio(0);\n\tcin.tie(NULL)\t\tfreopen("' + clipboard + '.in", "r", stdin);\n\tfreopen("' + clipboard + '.out", "w", stdout);\n\treturn 0;\n}')
		self.view.set_syntax_file('Packages/C++/C++.sublime-syntax')
		self.sublime.Window.new_file()