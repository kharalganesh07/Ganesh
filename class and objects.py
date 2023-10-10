#!/usr/bin/env python
# coding: utf-8

# In[4]:


#class and objects


# In[5]:


class phone:
    def make_call(self):
         print('i am making aa call')
    def play_games(self):
        print('playing game')


# In[6]:


p1=phone()


# In[7]:


p1.make_call()
p1.play_games()


# In[2]:


# def add(self,x,y):
   # self.sum = x+y
    #print('the sum is',self.sum)
class addition:
    def add(self, a,b):
        self.sum= a+b
        print('the sum is ',self.sum)


# In[4]:


ad= addition()
ad.add(2,3)


# In[10]:


class phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print('make a call')
    def play_game(self):
        print('play the game')
    


# In[11]:


ph=phone()


# In[12]:


ph.set_color('blue')


# In[13]:


ph.set_cost('200')


# In[14]:


ph.show_color()


# In[15]:


ph.show_cost()


# In[16]:


ph.make_call()


# In[17]:


# constructor


# In[18]:


class employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    
    
    def show_details(self):
        print('name:',self.name)
        print('age:',self.age)
        print('salary:',self.salary)
        print('gender:',self.gender)


# In[19]:


e1=employee('ganesh', 24, '50k', 'male')


# In[20]:


e1.show_details()


# In[21]:


class vechicle:
    def __init__ (self,milage,cost):
        self.m=milage
        self.c=cost
    def show_details(self):
        print('milage is',self.m)
        print('cost is',self.c)
    
    


# In[22]:


class car(vechicle):
    def show_car(self):
        print('this is a car')


# In[23]:


c1=car(55,230000)


# In[24]:


c1.show_details()


# In[25]:


c1.show_car()


# In[26]:


# overriding


# In[27]:


class car1(vechicle):
    def __init__(self,milage,cost,tyres,hp):
        super().__init__(milage,cost)
        self.tyres = tyres
        self.hp = hp
        
    def show_details(self):
        print('numberof tyresin car',self.tyres)
        print('hp is',self.hp)
                    
    
    


# In[28]:


c1= car1(55,1000,52,25)


# In[29]:


c1.show_details()


# In[30]:


class book:
    def __init__(self,author,price,publication):
        self.a=author
        self.p=price
        self.pn=publication
    def show_book(self):
        print('the author is',self.a)
        print('the price is',self.p,'and the publication is',self.pn)
        
    


# In[31]:


b1=book('ganesh', 200,2001)


# In[32]:


b1.show_book()


# In[86]:


class physics(book):
    def show_physics(self):
        print('show details of physics')
        
    def enter_physics(self,law):
        self.l=law
        
    def show_physics1(self):
        print('show the physics of law')
        print('also the law here,funny?',self.l)
        
    def show_law(self)  :
        print('actual law',self.l)
    


# In[87]:


phy1=physics('ganeshkharal',2255,'ekta')


# In[88]:


phy1.show_book()


# In[89]:


phy1.show_physics()


# In[90]:


phy1.enter_physics('1st law')


# In[91]:


phy1.show_physics1()


# In[92]:


phy1.show_law()


# In[93]:


p1= physics('gk',500,2020)
p1.show_book()


# In[94]:


p1.show_physics()


# In[95]:


class chemistry(book):
    def __init__(self,author,price,publication,pages,sales):
        super().__init__(author,price,publication)
        self.page=pages
        self.sale=sales
        
    def show_chemistry(self):
        print('this; is the page for chemistyt')
    


# In[96]:


ch= chemistry('ganeshkharal', 500,2023,125,1700)


# In[97]:


ch.show_chemistry()


# In[98]:


#inheritance multiple


# In[99]:


class parent1:
    def assign_one(self,str1):
        self.str1=str1
       
        
    def show_one(self):
         print('This is string 1')
    


# In[100]:


class parent2:
    def assign_two(self,str2):
        self.str2=str2
       
        
    def show_two(self):
         print('This is string 2')


# In[101]:


class derived(parent1,parent2):
    def assign_child(self,child):
        self.child=child
        
    def show_child(self):
        print('This is child')
        


# In[102]:


chi=derived()


# In[103]:


chi.assign_one(24)


# In[104]:


chi.show_one()


# In[105]:


chi.assign_two(50)
chi.show_two()


# In[106]:


chi.show_child()


# In[107]:


#multi-level inheritance
  


# In[108]:


# FIRST PRACTICE AND LEARN


# In[109]:


class school:
    def member(self,name,age):
        self.name= name
        self.age= age
        
    def staff(self, s_id):
        self.sid= s_id
        
    def show_details(self):
        print('the member is',self.name)
        print('the staff is ',self.sid)
        
    


# In[110]:


class teacher(school):
    def teacher_detail(self,t_id,qualifi):
        self.tid= t_id
        self.qualifi=qualifi
        
    def show_teacher(self):
        print('show details:',self.tid,'/n',self.qualifi)


# In[111]:


t1=teacher()


# In[112]:


t1.member('ganesh',24)
t1.staff(1124)
t1.teacher_detail(1100,'bachelors')


# 

# In[113]:


t1.show_details()
t1.show_teacher()


# In[124]:


class computer:
    def __init__(self,cname,cost,generation):
        self.name= cname
        self.cost=cost
        self.generation= generation
        
    def show_computer(self):
        print('show details')
        print('name is',self.name)
        print('cost is ',self.cost)
        print('generation is',self.generation)


# In[125]:


co=computer('dell', 11200, '11th')


# In[126]:


co.show_computer()


# In[139]:


class hp(computer):
    def __init__(self,cname,cost, generation,model,ram):
        super().__init__(cname, cost, generation)
        self.m=model
        self.ram=ram
        
    def show_hp(self):
        print('show details')
        print('model is',self.m)
        print('ram is ',self.ram)
        print('the above details are' ,self.name)
        print(self.cost)
        print(self.generation)
        
    


# In[140]:


hp1=hp('hp',10000, '13th','11escr5','8gb')


# In[141]:


hp1.show_hp()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




