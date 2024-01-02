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
| [**verify_email**](./User#verify_email) | [VerifyUserEmailRequest](User#verifyuseremailrequest) | [Empty](User#empty) |
| [**disable_mfa**](./User#disable_mfa) | [DisableUserMFARequest](User#disableusermfarequest) | [UserInfo](User#userinfo) |
| [**set_required_actions**](./User#set_required_actions) | [SetRequiredActionsRequest](User#setrequiredactionsrequest) | [UserInfo](User#userinfo) |
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






    
<br>

### update

Update user info by given user_id



> **POST** /identity/v2/user/update
>






    
<br>

### verify_email





> **POST** /identity/v2/user/verify-email
>






    
<br>

### disable_mfa

Disable MFA for user. If this api is called, send email to user.



> **POST** /identity/v2/user/disable-mfa
>





 {{< tabs " disable_mfa " >}}

 {{< tab "Request Example" >}}



[DisableUserMFARequest](./User#disableusermfarequest)

* **user_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com",
 "force": false,
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### set_required_actions





> **POST** /identity/v2/user/set-required-actions
>






    
<br>

### enable





> **POST** /identity/v2/user/enable
>






    
<br>

### disable





> **POST** /identity/v2/user/disable
>






    
<br>

### delete





> **POST** /identity/v2/user/delete
>






    
<br>

### get





> **POST** /identity/v2/user/get
>






    
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

### DisableUserMFARequest
* **user_id** (string)   `Required` 

    <br>

### MFA
* **state** (State)   `Required` 

    
* **mfa_type** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    <br>

### SetRequiredActionsRequest
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

### VerifyUserEmailRequest
* **user_id** (string)   `Required` 

    
* **email** (string)  

    <br>
