import sys
import weechat

weechat.register("flash", "bverschueren", "1.0", "GPL3", "flash/highlight", "", "")

def flash_cb(data, signal, signal_data):
	tty = open('/dev/tty', 'w')
	tty.write('\a')
	tty.close()
	return weechat.WEECHAT_RC_OK

hook = weechat.hook_signal("weechat_highlight", "flash_cb", "")
