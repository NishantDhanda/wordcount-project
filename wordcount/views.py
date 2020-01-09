from django.shortcuts import render
import operator
import re

def home(request):
	return render(request,'home.html')

def count(request):
	fulltext=request.GET['fulltext']
	count=len(re.findall(r'\w+',fulltext))
	words1=re.findall(r'\w+',fulltext)
	words2={}
	for i in words1:
		if i in words2:
			words2[i]+=1
		else:
			words2[i]=1
	words=sorted(words2.items(),key=operator.itemgetter(1),reverse=True)			
	return render(request,'count.html',{'fulltext':fulltext,'count':count,'words':words})	

def about(request):
	return render(request,'about.html')