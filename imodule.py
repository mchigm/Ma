import lib

class m_error:
	msg = f"Error log ge"
	def __init__(path, file, line, index, self, error=DeBug):
		self.p = path
		self.file = file
		self.l = line
		self.I = index
		self.emsg = f" {error} error, in {self.file}, line {self.l}: \n code forced to exit due to {error} at index {self.I}."
class m_warning:
	def __init__(self):
		pass