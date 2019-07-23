#!/usr/bin/env python
#-*- coding: utf-8 -*-

import inkex

class MyExtensionName(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option(
		"--x",
		dest='x',
		action='store',
		type='float',
                default=0,
		help='x coord'
	)
	self.OptionParser.add_option(
		"--y",
		dest='y',
		action='store',
		type='float',
                default=0,
		help='y coord'
	)

    def effect(self):
	docWidth = self.unittouu(self.document.getroot().xpath('@width', namespaces=inkex.NSS)[0])
	docHeight = self.unittouu(self.document.getroot().xpath('@height', namespaces=inkex.NSS)[0])
        optionX = self.options.x
	optionY = self.options.y

	#inkex.debug("docX: " + str(docWidth))
	#inkex.debug("docY: " + str(docHeight))
	#inkex.debug("optionX: " + str(optionX))
	#inkex.debug("optionY: " + str(optionY))

	for id, node in self.selected.iteritems():
		x = (180 + optionX) / 360 * docWidth - float(node.get("width")) / 2
		y = (90 + optionY) / 180 * docHeight - float(node.get("height")) / 2
		#inkex.debug("x: " + str(x))
		node.set("x", str(x))
		node.set("y", str(y))

if __name__ == '__main__':
    MyExtension = MyExtensionName()
    MyExtension.affect()
