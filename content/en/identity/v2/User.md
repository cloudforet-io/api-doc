---
title: "User"
linkTitle: "User"
weight: 3
bookFlatSection: true
---
# [User](#User)
User API which allows member management within project, company, and domain
note: Administrator must register User first.


>  **Package : spaceone.api.identity.v2**

<br>
<br>

## User





**User Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./User#create) | [CreateUserRequest](User#createuserrequest) | [UserInfo](User#userinfo) |
| [**update**](./User#update) | [UpdateUserRequest](User#updateuserrequest) | [UserInfo](User#userinfo) |
| [**verify_email**](./User#verify_email) | [VerifyEmailUserRequest](User#verifyemailuserrequest) | [Empty](User#empty) |
| [**disable_mfa**](./User#disable_mfa) | [DisableMFAUserRequest](User#disablemfauserrequest) | [UserInfo](User#userinfo) |
| [**set_required_actions**](./User#set_required_actions) | [SetRequiredActionsUserRequest](User#setrequiredactionsuserrequest) | [UserInfo](User#userinfo) |
| [**set_refresh_timeout**](./User#set_refresh_timeout) | [SetRefreshTimeout](User#setrefreshtimeout) | [UserInfo](User#userinfo) |
| [**enable**](./User#enable) | [UserRequest](User#userrequest) | [UserInfo](User#userinfo) |
| [**disable**](./User#disable) | [UserRequest](User#userrequest) | [UserInfo](User#userinfo) |
| [**delete**](./User#delete) | [UserRequest](User#userrequest) | [Empty](User#empty) |
| [**get**](./User#get) | [UserRequest](User#userrequest) | [UserInfo](User#userinfo) |
| [**list**](./User#list) | [UserSearchQuery](User#usersearchquery) | [UsersInfo](User#usersinfo) |
| [**stat**](./User#stat) | [UserStatQuery](User#userstatquery) | [Struct](User#struct) |



    
<br>

### create

You can create user. after create user you have to binding role to user.
See role-binding create api.
External type user do not need password.



> **POST** /identity/v2/user/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateUserRequest](./User#createuserrequest)

* **user_id** (string)   `Required` 


* **auth_type** (AuthType)   `Required` 


* **reset_password** (bool)   `Required` 

  *If reset_password is true, send email*


* **password** (string)  

  *When auth_type is LOCAL, password is required.*


* **name** (string)  


* **email** (string)  


* **language** (string)  

  *en,ko*


* **timezone** (string)  

  *UTC, Asia/Seoul*


* **tags** (Struct)  





{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "reset_password": false,
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Update user info by given user_id



> **POST** /identity/v2/user/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateUserRequest](./User#updateuserrequest)

* **user_id** (string)   `Required` 


* **password** (string)  


* **name** (string)  


* **email** (string)  


* **language** (string)  


* **timezone** (string)  


* **tags** (Struct)  


* **reset_password** (bool)  





{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!!",
 "reset_password": false,
 "name": "Cloudforet",
 "email": "cloudforet@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### verify_email





> **POST** /identity/v2/user/verify-email
>





 {{< tabs " verify_email " >}}

 {{< tab "Request Example" >}}



[VerifyEmailUserRequest](./User#verifyemailuserrequest)

* **user_id** (string)   `Required` 


* **email** (string)  





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com",
 "email": "example@cloudforet.com"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### disable_mfa

Disable MFA for user. If this api is called, send email to user.



> **POST** /identity/v2/user/disable-mfa
>





 {{< tabs " disable_mfa " >}}

 {{< tab "Request Example" >}}



[DisableMFAUserRequest](./User#disablemfauserrequest)

* **user_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### set_required_actions





> **POST** /identity/v2/user/set-required-actions
>





 {{< tabs " set_required_actions " >}}

 {{< tab "Request Example" >}}



[SetRequiredActionsUserRequest](./User#setrequiredactionsuserrequest)

* **user_id** (string)   `Required` 


* **required_actions** (UserRequiredAction)  `Repeated`    `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com",
 "required_actions": ["UPDATE_PASSWORD"]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### set_refresh_timeout

Sets the user's refresh token timeout. This API can only be used by users with the `DOMAIN_ADMIN` role.
Min value is `1800` seconds and max value is `2592000` seconds



> **POST** /identity/v2/user/set-refresh-timeout
>





 {{< tabs " set_refresh_timeout " >}}

 {{< tab "Request Example" >}}



[SetRefreshTimeout](./User#setrefreshtimeout)

* **user_id** (string)   `Required` 


* **refresh_timeout** (int32)   `Required` 





{{< highlight json >}}
{
  "user_id": "wonny@cloudforet.io",
  "refresh_token_timout": 10800
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable





> **POST** /identity/v2/user/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[UserRequest](./User#userrequest)

* **user_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable





> **POST** /identity/v2/user/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[UserRequest](./User#userrequest)

* **user_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/user/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[UserRequest](./User#userrequest)

* **user_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/user/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[UserRequest](./User#userrequest)

* **user_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **auth_type** (AuthType)   `Required` 

* **role_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **mfa** (MFA)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **refresh_timeout** (int32)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password1234!",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/user/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[UserSearchQuery](./User#usersearchquery)

* **query** (Query)  


* **user_id** (string)  


* **name** (string)  


* **state** (State)  


* **email** (string)  


* **auth_type** (AuthType)  





{{< highlight json >}}
{
 "auth_type": "LOCAL",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [{
     "key": "created_at",
     "desc": true
   }]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UsersInfo](#USERSINFO)
* **results** (UserInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "auth_type": "LOCAL",
     "created_at": "2024-11-14T01:53:19.224Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "email": "wonny@cloudforet.io",
     "language": "en",
     "name": "Wonny",
     "role_type": "USER",
     "state": "PENDING",
     "timezone": "UTC",
     "user_id": "wonny@cloudforet.io"
   },
   {
     "auth_type": "LOCAL",
     "created_at": "2024-11-12T04:46:41.209Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "email": "cloudforet@cloudforet.io",
     "language": "ko",
     "last_accessed_at": "2024-11-13T07:42:46.511Z",
     "name": "Cloudforet Admin",
     "role_id": "managed-domain-admin",
     "role_type": "DOMAIN_ADMIN",
     "state": "ENABLED",
     "timezone": "UTC",
     "user_id": "cloudforet@cloudforet.io"
   }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v1/user/stat
>






    


<br>
<br>

## Message



### CreateUserRequest
* **user_id** (string)   `Required` 

    
* **auth_type** (AuthType)   `Required` 

    
* **reset_password** (bool)   `Required` 

  *If reset_password is true, send email*

    
* **password** (string)  

  *When auth_type is LOCAL, password is required.*

    
* **name** (string)  

    
* **email** (string)  

    
* **language** (string)  

  *en,ko*

    
* **timezone** (string)  

  *UTC, Asia/Seoul*

    
* **tags** (Struct)  

    <br>

### DisableMFAUserRequest
* **user_id** (string)   `Required` 

    <br>

### MFA
* **state** (State)   `Required` 

    
* **mfa_type** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    <br>

### SetRefreshTimeout
* **user_id** (string)   `Required` 

    
* **refresh_timeout** (int32)   `Required` 

    <br>

### SetRequiredActionsUserRequest
* **user_id** (string)   `Required` 

    
* **required_actions** (UserRequiredAction)  `Repeated`    `Required` 

    <br>

### UpdateUserRequest
* **user_id** (string)   `Required` 

    
* **password** (string)  

    
* **name** (string)  

    
* **email** (string)  

    
* **language** (string)  

    
* **timezone** (string)  

    
* **tags** (Struct)  

    
* **reset_password** (bool)  

    <br>

### UserInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **email** (string)   `Required` 

    
* **email_verified** (bool)   `Required` 

    
* **auth_type** (AuthType)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **mfa** (MFA)   `Required` 

    
* **language** (string)   `Required` 

    
* **timezone** (string)   `Required` 

    
* **required_actions** (UserRequiredAction)  `Repeated`    `Required` 

    
* **refresh_timeout** (int32)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    <br>

### UserRequest
* **user_id** (string)   `Required` 

    <br>

### UserSearchQuery
* **query** (Query)  

    
* **user_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **email** (string)  

    
* **auth_type** (AuthType)  

    <br>

### UserStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### UsersInfo
* **results** (UserInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### VerifyEmailUserRequest
* **user_id** (string)   `Required` 

    
* **email** (string)  

    <br>
