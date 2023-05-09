---
title: "User"
linkTitle: "User"
weight: 3
bookFlatSection: true
---
# [User](#User)
desc: User API which allows member management within project, company, and domain
note: Administrator must register User first.


>  **Package : spaceone.api.identity.v1**

<br>
<br>

## User





**User Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./User#create) | [CreateUserRequest](User#createuserrequest) | [UserInfo](./User#userinfo) |
| [**update**](./User#update) | [UpdateUserRequest](User#updateuserrequest) | [UserInfo](./User#userinfo) |
| [**verify_email**](./User#verify_email) | [VerifyEmailRequest](User#verifyemailrequest) | [Empty](./User#empty) |
| [**confirm_email**](./User#confirm_email) | [ConfirmEmailRequest](User#confirmemailrequest) | [UserInfo](./User#userinfo) |
| [**reset_password**](./User#reset_password) | [UserRequest](User#userrequest) | [Empty](./User#empty) |
| [**set_required_actions**](./User#set_required_actions) | [SetRequiredActionsRequest](User#setrequiredactionsrequest) | [UserInfo](./User#userinfo) |
| [**enable**](./User#enable) | [UserRequest](User#userrequest) | [UserInfo](./User#userinfo) |
| [**disable**](./User#disable) | [UserRequest](User#userrequest) | [UserInfo](./User#userinfo) |
| [**delete**](./User#delete) | [UserRequest](User#userrequest) | [Empty](./User#empty) |
| [**get**](./User#get) | [GetUserRequest](User#getuserrequest) | [UserInfo](./User#userinfo) |
| [**list**](./User#list) | [UserQuery](User#userquery) | [UsersInfo](./User#usersinfo) |
| [**stat**](./User#stat) | [UserStatQuery](User#userstatquery) | [Struct](./User#struct) |
| [**find**](./User#find) | [FindUserQuery](User#finduserquery) | [FindUsersInfo](./User#findusersinfo) |
| [**sync**](./User#sync) | [UserRequest](User#userrequest) | [UserInfo](./User#userinfo) |



    
<br>

### create





> **POST** /identity/v1/user/create
>






    
<br>

### update

desc: Update user info by given user_id
note:
request_example: >-
{
"user_id": "dkang@mz.co.kr",
"tags": [{
"key": "user1",
"value": "Reuters"
}, {
"key": "user2",
"value": "Bloomberg"
}],
"domain_id": "{{DOMAIN_ID}}"
}
response_example: >-
{
"user_id": "dkang@mz.co.kr",
"name": "Dong Yoo kang",
"state": "ENABLED",
"email": "dkang@mz.co.kr",
"language": "en",
"timezone": "UTC",
"tags": [{
"key": "user1",
"value": "Reuters"
}, {
"key": "user2",
"value": "Bloomberg"
}],
"last_accessed_at": {
"seconds": "1593161630",
"nanos": 79000000
},
"created_at": {
"seconds": "1593161630",
"nanos": 79000000
},
"domain_id": "domain-fd6e23a5ae36"
}



> **POST** /identity/v1/user/update
>






    
<br>

### verify_email





> **POST** /identity/v1/user/verify-email
>






    
<br>

### confirm_email





> **POST** /identity/v1/user/confirm-email
>






    
<br>

### reset_password





> **POST** /identity/v1/user/reset-password
>






    
<br>

### set_required_actions





> **POST** /identity/v1/user/set-required-actions
>






    
<br>

### enable





> **POST** /identity/v1/user/enable
>






    
<br>

### disable





> **POST** /identity/v1/user/disable
>






    
<br>

### delete





> **POST** /identity/v1/user/delete
>






    
<br>

### get





> **POST** /identity/v1/user/get
>






    
<br>

### list





> **POST** /identity/v1/user/list
>






    
<br>

### stat





> **POST** /identity/v1/user/stat
>






    
<br>

### find





> **POST** /identity/v1/users/find
>






    
<br>

### sync





> **POST** /identity/v1/user/sync
>






    


<br>
<br>

## Message



### ConfirmEmailRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **verify_code** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CreateUserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **password** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **user_type** (UserType)  `Required` 

  *is_required: false*

    
* **backend** (UserBackend)  `Required` 

  *is_required: true*

    
* **language** (string)  `Required` 

  *is_required: false*

    
* **timezone** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **reset_password** (bool)  `Required` 

  *is_required: false*

    <br>

### FindUserInfo
* **user_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **email** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    <br>

### FindUserQuery
* **search** (FindUserSearch)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### FindUserSearch
* **user_id** (string)  `Required` 

    
* **keyword** (string)  `Required` 

    <br>

### FindUsersInfo
* **results** (FindUserInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetUserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### SetRequiredActionsRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **actions** (UserRequiredAction)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateUserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **password** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **language** (string)  `Required` 

  *is_required: false*

    
* **timezone** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **reset_password** (bool)  `Required` 

  *is_required: false*

    <br>

### UserInfo
* **user_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **email** (string)  `Required` 

    
* **user_type** (UserType)  `Required` 

    
* **backend** (UserBackend)  `Required` 

    
* **language** (string)  `Required` 

    
* **timezone** (string)  `Required` 

    
* **required_actions** (UserRequiredAction)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **last_accessed_at** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **email_verified** (bool)  `Required` 

    <br>

### UserQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **user_type** (UserType)  `Required` 

  *is_required: false*

    
* **backend** (UserBackend)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### UserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UsersInfo
* **results** (UserInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### VerifyEmailRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **force** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
