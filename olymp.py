import sublime
import sublime_plugin


class OlympCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.set_syntax_file('C++');
		clipboard=sublime.get_clipboard();	
		self.view.insert(edit, 0, '#include <bits/stdc++.h>\n#define DEBUG\nusing namespace std;\n#pragma GCC target ("avx2")\n#pragma GCC optimization ("O3")\n#pragma GCC optimization ("unroll-loops")\n\nint main() {\n\t// ios_base::sync_with_stdio(0);\n\t// cin.tie(NULL);\n\t#ifdef DEBUG\n\t\tfreopen("input.txt", "r", stdin);\n\t\tfreopen("output.txt", "w", stdout);\n\t#else\n\t\tfreopen("' + clipboard + '.in", "r", stdin);\n\t\tfreopen("' + clipboard + '.out", "w", stdout);\n\t#endif\n\treturn 0;\n}')
		self.view.set_syntax_file('Packages/C++/C++.sublime-syntax')
		self.sublime.Window.new_file()
