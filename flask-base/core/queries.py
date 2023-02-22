# from web_app import db

##for sqlite
# def get_user_info(user_id):
#     sql= f"""
#     SELECT client_id, office_id, username from users where client_id={user_id};
#     """
#     user_info=db.session.execute(sql).fetchall()
#     return user_info


##for postgress
# def login_credentials(username,password):
#     sql=f"""Select userid,username,passhash from auth.users where username='{username}' and passhash='{password}';"""
#     cur=conn.cursor()
#     cur.execute(sql)
#     row = cur.fetchall()
#     return row
