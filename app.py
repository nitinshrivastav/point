#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle



# In[2]:


file=open('apunkamodel.pkl','rb')
model=pickle.load(file)


# In[9]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fkjfkjf():
    return render_template('apnatimeaayega.html')
@app.route('/info',methods=['GET','POST'])
def fkjfk():
    if(request.method=='POST'):
        research=int(request.form['r'])
        admin=int(request.form['a'])
        market=int(request.form['m'])
        res=model.predict([[research,admin,market]])
        return render_template('apnatimeaayega.html',ans=res)
if __name__=='__main__':
    app.run()



