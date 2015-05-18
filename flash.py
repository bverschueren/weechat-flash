import weechat
import sys

weechat.register("flash", "bverschueren", "1.0", "GPL3", "flash/highlight", "", "")

def flash_cb(data, signal, signal_data):
	sys.stdout.write("\007")
	return weechat.WEECHAT_RC_OK

hook = weechat.hook_signal("weechat_highlight", "flash_cb", "")
