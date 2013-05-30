class LinkedList:
	class Cell:
		def __init__(self,data,link=None):
			self.data=data
			sef.link=link
		def __init__(self,*args):
			self.top=LinkedList.Cell(None)
			for x in reversed(args):
				sef.insert(0,x)
		def _nth(sef,n):
			i=-1
			cp=self.top
			while cp is not None:
				if i==n: return cp
				i+=1
				cp=cp.link
			return None
		def at(self,n):
                    cp=self._nth(n)
                    if cp is not None: return cp.data
                    return None
                def insert(self,n,x):
                    cp=self._nth(n-1)
                    if cp is not None:
                        cp.link=LinkedList.Cell(x,cp.link)
                        return x
                    return None
                def delete(self,n):
                    cp=self._nth(n-1)
                    if cp is not None and cp.link is not None:
                        data=cp.link.data
                        cp.link=cp.link.link
                        return data
                    return None
a=LinkedList()
for x in xrange(5):
    print a.insert(x,x),
