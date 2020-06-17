from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response, render_template, session
import json, os, sys 
sys.path.append('./end')
from operator import itemgetter

mongodb_hostname = os.environ.get("MONGO_HOSTNAME","localhost")
client = MongoClient('mongodb://'+mongodb_hostname+':27017/')

# Choose InfoSys database
db = client['MovieFlix']
movies = db['Movies']
users = db['Users']


# Initiate Flask App
app = Flask(__name__)
app.secret_key ='mail'


@app.route('/')
def first():
   session['log']='no'
   return render_template('1.html')
       
@app.route('/', methods=['POST'])
def login():
      
   
   
    email =request.form['email']
    password =request.form['password']
   
    if users.find({"password":password,"email":email}).count() == 1 :
        session['em']=email;
        session['log']='yes'
        return render_template('3.html') 
    else:
        return render_template('1.html',error="email or password is wrong")


@app.route('/register')
def Index():
   return render_template('style.html')



@app.route('/register', methods=['POST'])
def register():
    
   
    name =request.form['name']
    email =request.form['email']
    password =request.form['password']
   
    if users.find({"email":email}).count() == 0 :
        user = {"name": name, "email": email,  "password":password , "category":'user' }
        
        users.insert_one(user)
        return render_template('1.html')
    else:
        return render_template('style.html',error="this email already exists")
       

@app.route('/menu')
def menu():
  if session['log'] == 'yes':
   return render_template('3.html')
  else:
   return render_template('1.html',error="You are not logged in")





@app.route('/search')
def search():
  if session['log'] == 'yes':
   return render_template('31.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/search', methods=['post'])
def get_all():
   title =request.form['title']
   year =request.form['year']
   actor =request.form['actor']
   actor={'name': actor}
   if title !="" and actor['name'] !="" and year !="":
        iterable = movies.find({"title":title,"year":{"$eq" :year,"$exists":True},"actors":actor})
        output = []
        for movie in iterable:
         movie['_id']=None
         if  "description" in movie and "year" in movie :
           dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if  "description" not in movie and "year" in movie :
           dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if  "description" in movie and "year"  not in movie :
           dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if  "description" not in movie and "year" not in movie :
           dic={'title' :movie['title'],'actors':movie['actors']}
                   
         output.append(dic)
        return jsonify(output)  
   if title !="" and actor['name'] !="" and year =="":
        iterable = movies.find({"title":title,"actors":actor})
        output = []
        for movie in iterable:
         movie ['_id'] = None
         if "description" in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if "description" in movie and "year"  not in movie :
            dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" not in movie :
            dic={'title' :movie['title'],'actors':movie['actors']}
            
         output.append(dic)
        return jsonify(output)  
   if title !="" and actor['name'] =="" and year !="":
        iterable = movies.find({"title":title,"year":{"$eq" :year,"$exists":True}})
        output = []
        for movie in iterable:
         movie ['_id'] = None
         if "description" in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if "description" in movie and "year"  not in movie :
            dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" not in movie :
            dic={'title' :movie['title'],'actors':movie['actors']}
            
         output.append(dic)
        return jsonify(output)  
   if title =="" and actor['name'] !="" and year !="":
        iterable = movies.find({"year":{"$eq" :year,"$exists":True},"actors":actor})
        output = []
        for movie in iterable:
         movie ['_id'] = None
         if "description" in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if "description" in movie and "year"  not in movie :
            dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" not in movie :
            dic={'title' :movie['title'],'actors':movie['actors']}
            
         output.append(dic)
        return jsonify(output)  
   if title !="" and actor['name'] =="" and year =="":
        iterable = movies.find({"title":title})
        output = []
        for movie in iterable:
         movie ['_id'] = None
         if "description" in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if "description" in movie and "year"  not in movie :
            dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" not in movie :
            dic={'title' :movie['title'],'actors':movie['actors']}
            
         output.append(dic)
        return jsonify(output)  
   if title =="" and actor['name'] !="" and year =="":
        iterable = movies.find({"actors":actor})
        output = []
        for movie in iterable:
         movie['_id'] = None
         if "description" in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if "description" in movie and "year"  not in movie :
            dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" not in movie :
            dic={'title' :movie['title'],'actors':movie['actors']}
            
         output.append(dic)
        return jsonify(output)  
   if title =="" and actor['name'] =="" and year !="":
        iterable = movies.find({"year":{"$eq" :year,"$exists":True}})
        output = []
        for movie in iterable:
         movie ['_id'] = None
         if "description" in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" in movie :
            dic={'title' :movie['title'],'year':movie['year'],'actors':movie['actors']}
         if "description" in movie and "year"  not in movie :
            dic={'title' :movie['title'],'description':movie['description'],'actors':movie['actors']}
         if "description" not in movie and "year" not in movie :
            dic={'title' :movie['title'],'actors':movie['actors']}
            
         output.append(dic)
        return jsonify(output)  
   else:
        return render_template('31.html',error="You must fill at least one field")

@app.route('/comments')
def comments():
  if session['log'] == 'yes':
   return render_template('32.html')
  else:
   return render_template('1.html',error="You are not logged in")


@app.route('/comments', methods=['post'])
def comments1():
   title =request.form['title']
   year=request.form['year']
   
   if title !=""  and year !="":
        iterable = movies.find({"title":title,"year":year,"comments":{ "$exists":True}})
        output = []
        for movie in iterable:
         movie['_id'] = None
         dic={'comments':movie['comments']}
             
         output.append(dic)
        return jsonify(output)  
   else:
        return render_template('32.html',error="You must fill all fields")

@app.route('/rating')
def rating():
  if session['log'] == 'yes':
   return render_template('33.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/rating', methods=['post'])
def rating1():
   title =request.form['title']
   year=request.form['year']
   rating =request.form['rating']
   movies.find_one_and_update({"title":title,"year":year},{"$set": {"rating":{'email': session['em'],'rating':rating }}})
   return render_template('3.html')

@app.route('/delete_rating')
def delrating():
  if session['log'] == 'yes':
   return render_template('34.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/delete_rating', methods=['post'])
def delrating1():
    title =request.form['title']
    year=request.form['year']
    iterable =movies.find({"title":title,"year":year,"rating":{ "$exists":True}})
    output = []
    for movie in iterable:
     if movie['rating'].get('email') ==  session['em']:
           movies.update({"_id":movie['_id']},{"$unset":{'rating':""}})    
           return render_template('3.html')
        
    return render_template('34.html',error="Bad request")


@app.route('/comment')
def comment():
  if session['log'] == 'yes':
   return render_template('35.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/comment', methods=['post'])
def comment1():
   title =request.form['title']
   year=request.form['year']
   comment =request.form['comment']
   movies.find_one_and_update({"title":title,"year":year},{"$push": {"comments":{'email': session['em'],'content':comment }}})
   users.find_one_and_update({"email":session['em']},{"$push": {"comments":{'title': title,'content':comment }}})
   return render_template('3.html')

@app.route('/getusercomment', methods=['get'])
def getusercomment():
        iterable = users.find({'email':session['em'],'comments':{"$exists":True}})
        output = []
        for user in iterable:
         user['_id'] = None
         dic={'comments':user['comments']}
            
         output.append(dic)
        return jsonify(output)   

	   

@app.route('/getuserrating', methods=['get'])
def getuserrating():
        iterable = movies.find({'rating':{"$exists":True}})
        output = []
        for movie in iterable:
                if movie['rating'].get('email') ==  session['em']:
                 dic={'ratings':movie['rating'].get('rating'),'title':movie['title']}
            
                 output.append(dic)
        return jsonify(output)  


	  

@app.route('/delete_comment')
def delcomment():
  if session['log'] == 'yes':
   return render_template('36.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/delete_comment', methods=['post'])
def delcomment1():
    title =request.form['title']
    year=request.form['year']
    comment =request.form['comment']
    commentm={'email': session['em'],'content':comment }
    commentu={'title': title,'content':comment }
    iterable =movies.find({"title":title,"year":year,"comments":{ "$exists":True}})
    output = []
    for movie in iterable:
           movies.update({"title":title,"year":year},{"$pull":{'comments':commentm}})
	
    iterable =users.find({"email":session['em'],"comments":{ "$exists":True}})
    output = []
    for user in iterable:
           users.update({"email":session['em']},{"$pull":{'comments':commentu}})	
           return render_template('3.html')
        
    return render_template('36.html',error="Bad request")



@app.route('/delete_account', methods=['post'])
def delaccount():
    iterable =movies.find({"rating":{ "$exists":True}})
    for movie in iterable:
     if movie['rating'].get('email') ==  session['em']:
           movies.update({"_id":movie['_id']},{"$unset":{'rating':""}})    
    commentm={'email': session['em'] }
    iterable =movies.find({"comments":{ "$exists":True}})
    output = []
    for movie in iterable:
           iterable2 =users.find({"email":session['em'],"comments":{ "$exists":True}})
           for user in iterable2:
               for i in range(len(user['comments'])):
                
                     commentm={'email': session['em'] ,'content':user['comments'][i].get('content')}
                     movies.update({"title":movie['title']},{"$pull":{'comments':commentm}})
    users.remove({'email':session['em']})
    return render_template('1.html')
  
   

@app.route('/admin_menu')
def adminmenu():
   iterable =users.find({'email':session['em']})
   for user in iterable:
    if user['category'] ==  "admin":
          return render_template('4.html')
    else:
          return render_template('3.html',error="You are not admin")


  
@app.route('/insert_movie')
def insert_movie():
  if session['log'] == 'yes':
   return render_template('41.html')
  else:
   return render_template('1.html',error="You are not logged in")




@app.route('/insert_movie', methods=['post'])
def insert_movie1():
   title =request.form['title']
   year =request.form['year']
   actor =request.form['actor']
   actor=actor.split(',')
   tactor=[None]*len(actor)
   description=request.form['description']
   iterable =movies.find({'title':title,'year':year})
   for movie in iterable:
       return render_template('41.html',error="This movie already exist")
   if description ==""  :
       for i in range(len(actor)):
         tactor[i]={'name':actor[i]}
       mv1 ={'title':title,'actors':tactor,'year':year}
       movies.insert_one(mv1)            
		
   if description !=""  :
       for i in range(len(actor)):
         tactor[i]={'name':actor[i]}
       mv1 ={'title':title,'actors':tactor, 'description': description}
       movies.insert_one(mv1)
		


   return render_template('4.html')


@app.route('/delete_movie')
def delete_movie():
  if session['log'] == 'yes':
   return render_template('42.html')
  else:
   return render_template('1.html',error="You are not logged in")




@app.route('/delete_movie', methods=['post'])
def delete_movie1():
   title =request.form['title']
   iterable =movies.find({"title":title})
    
   iterable=sorted(iterable,key=itemgetter('year'))
     

   movies.remove({'title':iterable[0].get('title'),'year':iterable[0].get('year')})
   		


   return render_template('4.html')


@app.route('/update_movie')
def update_movie():
  if session['log'] == 'yes':
   return render_template('43.html')
  else:
   return render_template('1.html',error="You are not logged in")




@app.route('/update_movie', methods=['post'])
def update_movie1():
   utitle =request.form['utitle']
   uyear =request.form['uyear']
   title =request.form['title']
   year =request.form['year']
   actor =request.form['actor']
   description=request.form['description']
  
   if title !="" and actor !="" and year !="" and description !="":
        actor=actor.split(',')
        tactor=[None]*len(actor) 
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'description':description,'year':year,'actor':tactor}})
        return render_template('4.html')
   if title !="" and actor !="" and year ==""  and description !="":
        actor=actor.split(',')
        tactor=[None]*len(actor) 
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'description':description,'actor':tactor}})   
        return render_template('4.html')
   if title !="" and actor =="" and year !="" and description !="":
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'description':description,'year':year}}) 
        return render_template('4.html')
   if title =="" and actor !="" and year !="" and description !="":
        actor=actor.split(',')
        tactor=[None]*len(actor) 
        movies.update({"title":utitle,'year':uyear},{"$set":{'description':description,'year':year,'actor':tactor}})
        return render_template('4.html')
   if title !="" and actor =="" and year =="" and description !="":
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'description':description}})
        return render_template('4.html')
   if title =="" and actor !="" and year =="" and description !="":
        actor=actor.split(',')
        tactor=[None]*len(actor) 
        movies.update({"title":utitle,'year':uyear},{"$set":{'description':description,'actor':tactor}})
        return render_template('4.html')
   if title =="" and actor =="" and year !="" and description !="":
        movies.update({"title":utitle,'year':uyear},{"$set":{'description':description,'year':year}})
        return render_template('4.html')
   if title !="" and actor !="" and year !="" and description =="": #dddd
        actor=actor.split(',')
        tactor=[None]*len(actor)
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'year':year,'actor':tactor}}) 
        return render_template('4.html')
   if title !="" and actor !="" and year ==""  and description =="":
        actor=actor.split(',')
        tactor=[None]*len(actor) 
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'actor':tactor}})
        return render_template('4.html')
   if title !="" and actor =="" and year !="" and description =="":
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title,'year':year}})  
        return render_template('4.html')   
   if title =="" and actor !="" and year !="" and description =="":
        actor=actor.split(',')
        tactor=[None]*len(actor) 
        movies.update({"title":utitle,'year':uyear},{"$set":{'year':year,'actor':tactor}})
        return render_template('4.html')
   if title !="" and actor =="" and year =="" and description =="":
        movies.update({"title":utitle,'year':uyear},{"$set":{'title':title}})
        return render_template('4.html')
   if title =="" and actor !="" and year =="" and description =="":
        actor=actor.split(',')
        tactor=[None]*len(actor)
        movies.update({"title":utitle,'year':uyear},{"$set":{'actor':tactor}}) 
        return render_template('4.html')
   if title =="" and actor =="" and year !="" and description =="":  
        movies.update({"title":utitle,'year':uyear},{"$set":{'year':year}})
        return render_template('4.html')
   if title =="" and actor =="" and year =="" and description !="": 
        movies.update({"title":utitle,'year':uyear},{"$set":{'description':description}})
        return render_template('4.html')
   else:
        return render_template('43.html',error="You must fill at least one field")

@app.route('/logout')
def logout():
 session.clear()
 return render_template('1.html')

@app.route('/delete_any_comments')
def delanycomment():
  if session['log'] == 'yes':
   return render_template('44.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/delete_any_comments', methods=['post'])
def delanycomment1():
    title =request.form['title']
    year=request.form['year']
    comment =request.form['comment']
    email=request.form['email']
    commentm={'email': email,'content':comment }
    commentu={'title': title,'content':comment }
    iterable =movies.find({"title":title,"year":year,"comments":{ "$exists":True}})
    output = []
    for movie in iterable:
           movies.update({"title":title,"year":year},{"$pull":{'comments':commentm}})
	
    iterable =users.find({"email":email,"comments":{ "$exists":True}})
    output = []
    for user in iterable:
           users.update({"email":email},{"$pull":{'comments':commentu}})	
           return render_template('4.html')
        
    return render_template('44.html',error="Bad request")

@app.route('/category')
def category():
  if session['log'] == 'yes':
   return render_template('45.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/category', methods=['post'])
def category1():
    email=request.form['email']
    iterable =users.find({"email":email})
    for user in iterable:
         if user['category']=='user':
           users.update({"email":email},{"$set":{'category':'admin'}})	
           return render_template('4.html')
         else:
             return render_template('45.html',error="User already be an admin")
  
    return render_template('45.html',error="Bad request")


@app.route('/delete_user_account')
def deluaccount():
  if session['log'] == 'yes':
   return render_template('46.html')
  else:
   return render_template('1.html',error="You are not logged in")



@app.route('/delete_user_account', methods=['post'])
def deluaccount1():
    email=request.form['email']
    iterable2 =users.find({"email":email})
    for user in iterable2:
         if user['category']=='admin':
                return render_template('46.html',error="User be an admin")
    iterable =movies.find({"rating":{ "$exists":True}})
    for movie in iterable:
     if movie['rating'].get('email') ==  email:
           movies.update({"_id":movie['_id']},{"$unset":{'rating':""}})    
    commentm={'email': email }
    iterable =movies.find({"comments":{ "$exists":True}})
    output = []
    for movie in iterable:
           iterable2 =users.find({"email":email,"comments":{ "$exists":True}})
           for user in iterable2:
               for i in range(len(user['comments'])):
                
                     commentm={'email': email ,'content':user['comments'][i].get('content')}
                     movies.update({"title":movie['title']},{"$pull":{'comments':commentm}})
    users.remove({'email':email})
    return render_template('4.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
