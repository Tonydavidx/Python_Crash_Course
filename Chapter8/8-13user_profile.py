def build_profile(first,last,**user_info):
    """ Build a user profile """
    user_info['f_name'] = first
    user_info['l_name'] = last
    return user_info

user_profile = build_profile('Antony','David',location ='chennai',
                            age=25,skills='python')    

print(user_profile)