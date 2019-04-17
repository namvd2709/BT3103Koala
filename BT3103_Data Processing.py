
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

data = pd.read_csv("Data.csv", parse_dates=['Offer Date'],dayfirst=True)


# In[3]:

data['Offer Date'].min()


# In[17]:

majors = pd.Series(data['Major'].unique())
majors = pd.DataFrame(majors, columns=['major_name'])
majors.dropna(inplace = True)

major_name
temporary = {}
for name in majors['major_name']:
    temporary[name] = 1
    
major_name['Business Analytics'] = temporary
major_name


# In[18]:

#major_industry
industry_count = data.groupby(['Major','Industry']).size()
industry_count


# In[19]:

industry = {}
for mjr in industry_count.index.levels[0]:
    test ={}
    for ind in industry_count[mjr].index:
        test[ind] =  industry_count[mjr][ind]
    industry[mjr]= test
    
industry


# In[20]:

#major_industry_roles
roles = data.groupby(['Major','Industry','Role']).size()
roles


# In[21]:

#roles_salary
min_salary = data.groupby(['Major','Industry','Role']).min()['Salary']
max_salary = data.groupby(['Major','Industry','Role']).max()['Salary']
ave_salary = data.groupby(['Major','Industry','Role']).mean()['Salary']


# In[22]:

jobs = {}
for mjr in roles.index.levels[0]:
    industry = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  roles[mjr][ind][rl]
        industry[ind] = test2
        jobs[mjr]=industry 
jobs


# In[23]:

salary_min = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  min_salary[mjr][ind][rl]
        salary[ind] = test2
        salary_min[mjr]=salary 
salary_min


# In[24]:

salary_ave = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  ave_salary[mjr][ind][rl]
        salary[ind] = test2
        salary_ave[mjr]=salary 
salary_ave


# In[25]:

salary_max = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  max_salary[mjr][ind][rl]
        salary[ind] = test2
        salary_max[mjr]=salary 
salary_max


# In[26]:

#companies
companies = data.groupby(['Major','Industry','Role'])['Company'].unique().agg(lambda x:", ".join(x))
#num interviews
num_interview = data.groupby(['Major','Industry','Role']).mean()['Number of Interviews']
#timeframes
offers = data.groupby(['Major','Industry','Role'])[['Offer Date']].quantile([0.9,0.5,0.1])
offers = pd.DataFrame(offers)


# In[27]:

num_interview


# In[28]:

np.datetime64(offers['Offer Date']['Business Analytics']['Healthcare']['Business Analyst'][0.9],'M').astype('int')%12 +1


# In[29]:

test = {'Information Security Officer': {'ave_salary': 4000.0,'count': 1,'max_salary': 4000, 'min_salary': 4000}}
test['Information Security Officer'].update({'new_date': '2017-06'})
print(test)


# In[30]:

import calendar


# In[31]:

print(companies)
print(num_interview)
print(offers)


# In[32]:

company = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  companies[mjr][ind][rl]
        salary[ind] = test2
        company[mjr]=salary 
company


# In[33]:

num_interviews = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  round(num_interview[mjr][ind][rl])
        salary[ind] = test2
        num_interviews[mjr]=salary 
num_interviews


# In[34]:

offer_date_90 = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  calendar.month_name[(np.datetime64(offers['Offer Date'][mjr][ind][rl][0.1],'M').astype('int')%12 +1)] + " " + ("sem 2" if (np.datetime64(offers['Offer Date'][mjr][ind][rl][0.9],'M').astype('int')%12 +1) <= 8 else "sem 1")
        salary[ind] = test2
        offer_date_90[mjr]=salary 
offer_date_90


# In[35]:

offer_date_50 = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  calendar.month_name[(np.datetime64(offers['Offer Date'][mjr][ind][rl][0.5],'M').astype('int')%12 +1)] + " " + ("sem 2" if (np.datetime64(offers['Offer Date'][mjr][ind][rl][0.5],'M').astype('int')%12 +1) <= 8 else "sem 1")
        salary[ind] = test2
        offer_date_50[mjr]=salary 
offer_date_50


# In[36]:

offer_date_10 = {}
for mjr in roles.index.levels[0]:
    salary = {}
    for ind in industry_count[mjr].index:
        test2 ={}
        for rl in roles[mjr][ind].index:
            test2[rl] =  calendar.month_name[(np.datetime64(offers['Offer Date'][mjr][ind][rl][0.9],'M').astype('int')%12 +1)] + " " + ("sem 2" if (np.datetime64(offers['Offer Date'][mjr][ind][rl][0.1],'M').astype('int')%12 +1) <= 8 else "sem 1")
        salary[ind] = test2
        offer_date_10[mjr]=salary 
offer_date_10


# In[37]:

role_industry = data.groupby(['Industry','Role','Major']).count()['ID']


# In[38]:

type(role_industry)


# In[39]:

role_industry


# In[40]:

competitions = {}
for ind in role_industry.index.levels[0]:
    test ={}
    for role in  role_industry.index.levels[1]:
        test2 ={}
        for mjr in role_industry.index.levels[2]:
            if role_industry[ind][role][mjr] is None :
                break
            else:
                test2[mjr]= role_industry[ind][role][mjr]
        test[role] = test2
        competitions[ind]=test
    
competitions


# In[41]:

majors = {}
all_majors = data['Major'].unique()

for mjr in all_majors:
    print(mjr)
majors    


# In[42]:


all_majors


# In[43]:

job_description = {}
job_description['Business Analyst'] = 'Business analysts work with organisations to help them improve their processes and systems. They conduct research and analysis in order to come up with solutions to business problems and help to introduce these systems to businesses and their clients.'
job_description['Data Analyst'] = 'A data analyst collects and stores data on sales numbers, market research, logistics, linguistics, or other behaviours. They bring technical expertise to ensure the quality and accuracy of that data, then process, design and present it in ways to help people, businesses, and organizations make better decisions.'
job_description['IT Consultant'] = 'Your role as an IT consultant will be to work in partnership with clients, advising them how to use information technology in order to meet their business objectives or overcome problems. You will work to improve the structure and efficiency of IT systems in various organisations.'
job_description['Information Security Officer'] = 'An Information Security Officer (ISO) provides the vision and strategies necessary to ensure the confidentiality, integrity, and availability of University electronic information by communicating risk to senior administration, creating and maintaining enforceable policies and supporting processes, and ensuring compliance with regulatory requirements.'
job_description['Software Engineer'] = 'A Software Engineer determines operational feasibility by evaluating analysis, problem definition, requirements, solution development, and proposed solutions. Documents and demonstrates solutions by developing documentation, flowcharts, layouts, diagrams, charts, code comments and clear code.'
job_description


# In[44]:

data.head()


# In[45]:

industry = {}
for mjr in industry_count.index.levels[0]:
    test ={}
    for ind in industry_count[mjr].index:
        test[ind] =  industry_count[mjr][ind]
    industry[mjr]= test
    
industry


# In[46]:

bt3103 = {}
bt3103['industry'] = industry
bt3103['jobs'] = jobs
bt3103['min_salary'] = salary_min
bt3103['ave_salary'] = salary_ave
bt3103['max_salary'] = salary_max
bt3103['companie'] = company
bt3103['num_interviews'] = num_interviews
bt3103['offer_date_10']  = offer_date_10
bt3103['offer_date_50']  = offer_date_50
bt3103['offer_date_90']  = offer_date_90


# In[48]:

bt3103['competition'] = competitions
bt3103['job_description'] = job_description
bt3103['major'] = major_name


# In[49]:

df = pd.DataFrame(bt3103)
df


# # not used
# import calendar
# for mjr in companies.index.levels[0]:
#     for ind in industry_count[mjr].index:
#         test2 ={}
#         for rl in roles[mjr][ind].index:
#             test2[rl] = {'companies': companies[mjr][ind][rl]
#                         , 'num_interviews': round(num_interview[mjr][ind][rl])
#                         , 'offer_date_90': calendar.month_name[(np.datetime64(offers['Offer Date'][mjr][ind][rl][0.1],'M').astype('int')%12 +1)] + " " + ("sem 2" if (np.datetime64(offers['Offer Date'][mjr][ind][rl][0.9],'M').astype('int')%12 +1) <= 8 else "sem 1")
#                         , 'offer_date_50':  calendar.month_name[(np.datetime64(offers['Offer Date'][mjr][ind][rl][0.5],'M').astype('int')%12 +1)] + " " + ("sem 2" if (np.datetime64(offers['Offer Date'][mjr][ind][rl][0.5],'M').astype('int')%12 +1) <= 8 else "sem 1")
#                         , 'offer_date_10':  calendar.month_name[(np.datetime64(offers['Offer Date'][mjr][ind][rl][0.9],'M').astype('int')%12 +1)] + " " + ("sem 2" if (np.datetime64(offers['Offer Date'][mjr][ind][rl][0.1],'M').astype('int')%12 +1) <= 8 else "sem 1")
#                         , 'count': roles[mjr][ind][rl]
#                         , 'min_salary': min_salary[mjr][ind][rl]
#                         , 'max_salary': max_salary[mjr][ind][rl]
#                         , 'ave_salary': ave_salary[mjr][ind][rl]
#                          }
#         result[mjr][ind]['roles'] = test2
# 
# result

# In[50]:

df.to_json('outputv4.json')


# In[ ]:



