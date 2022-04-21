# *-* encoding=utf-8 *-*
'''
just try to use *args and **kargs.
*argsè¡¨ç¤ºä»»ä½•å¤šä¸ªæ— åå‚æ•°ï¼Œå®ƒæ˜¯ä¸€ä¸ªtupleï¼›**kwargsè¡¨ç¤ºå…³é”®å­—å‚æ•°ï¼Œå®ƒæ˜¯ä¸€ä¸ªdictã€‚å¹¶ä¸”åŒæ—¶ä½¿ç”¨*argså’Œ**kwargsæ—¶ï¼Œå¿…é¡»*argså‚æ•°åˆ—è¦åœ¨**kwargså‰
'''

def foo(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
    print '---------------------------------------'

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)
