import sublime
import sublime_plugin


class OlympCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		clipboard=sublime.get_clipboard();	
		self.view.insert(edit, 0, '/*\n█████████████.....██████....██.........█....██████████....██.........██.\n██.........██.......██......█.█........█....██......██.....██.......██..\n██.........██.......██......█..█.......█....██......██......██.....██...\n██.........██.......██......█...█......█....██......██.......██...██....\n██.........██.......██......█....█.....█....██......██........██.██.....\n██.........██.......██......█.....█....█....██......██.........███......\n█████████████.......██......█.....█....█....██████████.........███......\n██..................██......█......█...█....██......██.........███......\n██..................██......█......█...█....██......██.........███......\n██..................██......█.......█..█....██......██.........███......\n██..................██......█.......█..█....██......██.........███......\n██..................██......█........█.█....██......██.........███......\n██..................██......█........█.█....██......██.........███......\n██................██████....█.........██....██......██.........███......\n*/\n#include <bits/stdc++.h>\n#define DEBUG\nusing namespace std;\ntypedef long long ll;\ntypedef long double ld;\ntypedef vector<ll> vll;\ntypedef vector<int> vi;\ntypedef pair<int, int> pii;\ntypedef pair<ll, ll> pll;\n#define FF first\n#define SS second\n#define watch(x) cerr << (#x) << " is " << x << endl\n\nint main() {\n\t// ios_base::sync_with_stdio(0);\n\t// cin.tie(NULL);\n\t#ifdef DEBUG\n\t\tfreopen("input.txt", "r", stdin);\n\t\tfreopen("output.txt", "w", stdout);\n\t#else\n\t\tfreopen("' + clipboard + '.in", "r", stdin);\n\t\tfreopen("' + clipboard + '.out", "w", stdout);\n\t#endif\n\treturn 0;\n}')
		self.view.set_syntax_file('Packages/C++/C++.sublime-syntax')
		self.sublime.Window.new_file()
