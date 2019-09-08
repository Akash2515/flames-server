from flask import Flask,render_template,request

app = Flask(__name__)

def flame(l):
	res=['friends','love','affection','marriage','enemy','sister']
	while(len(res)>1):
	    s=(l%len(res))-1
        
	    if s>=0:
	        right=res[s+1:]
	        left=res[:s]
	        res=right+left
	    else:
	        res=res[:len(res)-1]
	return res[0]
def verify(name1,name2):
	l1=list(name1)
	l2=list(name2)
	a1=l1
	a2=l2
	ans=[]
	for i in range(len(l1)):
	    for j in range(len(l2)):
	        if l1[i]==l2[j]:
	            c=l1[i]
	            ans.append(c)
	            break
	for i in ans:
	    if i in a1 and i in a2:
	        a1.remove(i)
	        a2.remove(i)
	l=len(a1) + len(a2)
	ans=flame(l)
	return ans

@app.route('/')
def home():
    return render_template("index.html",action="Add")

@app.route('/flames',methods=['POST'])
def flames():
	if 'submit' in request.form:
		boyname=request.form['boy']
		boyname=str(boyname)
		girlname=request.form['girl']
		girlname=str(girlname)
		result=verify(boyname,girlname)
		resultflames='{} and {} are {}'.format(boyname,girlname,result)
		
		return render_template("index.html", action="Add", result=resultflames)
if __name__ == '__main__':
  app.run(host='0.0.0.0',port='8355',threaded=True)

# if result=='friends':
		# 	return render_template('friend.html')
		# elif result=='marriage':
		# 	return render_template('marriage.html')
		# elif result=='sister':
		# 	return render_template('sibling.html')
		# elif result=='love':
		# 	return render_template("LOVER.html")
		# elif result=='affection':
		# 	return render_template('affection.html')
		# elif result=='enemy':
		# 	return render_template('enemy.html')