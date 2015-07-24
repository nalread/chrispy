inv = []
vow = ['a', 'o', 'e', 'i', 'u', 'y']

def a_or_an(word):
	if word[1] in vow:
		return 'a'
	else:
		return 'an'

def inv_add(item):
	if item in inv:
		print "You've already got %s %s!" % (a_or_an(item), item)
	else:
		print "You got %s %s!" % (a_or_an(item), item)
		inv.append(item)
		
def inv_drop(item):
	if item in inv:
		print "You drop the %s!" % item
		inv.remove(item)
	else:
		print "You don't have that!"

def inv_use(item):
	if item in inv:
		print "You used the %s!" % item
		print "The %s broke!" % item
		inv.remove(item)
	else:
		print "You don't have that!"
		
inv_add('dagger')
inv_add('dagger')
inv_add('lockpick')
inv_add('axe')

print inv

inv_use('lockpick')
inv_use('sword')

print inv
