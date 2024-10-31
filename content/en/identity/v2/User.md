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
 "email": "example@cloudforet.com",
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



{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/user/list
>






    
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
