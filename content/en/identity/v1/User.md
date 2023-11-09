---
title: "User"
linkTitle: "User"
weight: 3
bookFlatSection: true
---
# [User](#User)
User API which allows member management within project, company, and domain
note: Administrator must register User first.


>  **Package : spaceone.api.identity.v1**

<br>
<br>

## User





**User Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./User#create) | [CreateUserRequest](User#createuserrequest) | [UserInfo](User#userinfo) |
| [**update**](./User#update) | [UpdateUserRequest](User#updateuserrequest) | [UserInfo](User#userinfo) |
| [**verify_email**](./User#verify_email) | [VerifyEmailRequest](User#verifyemailrequest) | [Empty](User#empty) |
| [**confirm_email**](./User#confirm_email) | [ConfirmEmailRequest](User#confirmemailrequest) | [UserInfo](User#userinfo) |
| [**reset_password**](./User#reset_password) | [UserRequest](User#userrequest) | [Empty](User#empty) |
| [**set_required_actions**](./User#set_required_actions) | [SetRequiredActionsRequest](User#setrequiredactionsrequest) | [UserInfo](User#userinfo) |
| [**enable_mfa**](./User#enable_mfa) | [EnableMFARequest](User#enablemfarequest) | [UserInfo](User#userinfo) |
| [**disable_mfa**](./User#disable_mfa) | [DisableMFARequest](User#disablemfarequest) | [UserInfo](User#userinfo) |
| [**confirm_mfa**](./User#confirm_mfa) | [ConfirmMFARequest](User#confirmmfarequest) | [UserInfo](User#userinfo) |
| [**enable**](./User#enable) | [UserRequest](User#userrequest) | [UserInfo](User#userinfo) |
| [**disable**](./User#disable) | [UserRequest](User#userrequest) | [UserInfo](User#userinfo) |
| [**delete**](./User#delete) | [UserRequest](User#userrequest) | [Empty](User#empty) |
| [**get**](./User#get) | [GetUserRequest](User#getuserrequest) | [UserInfo](User#userinfo) |
| [**list**](./User#list) | [UserQuery](User#userquery) | [UsersInfo](User#usersinfo) |
| [**stat**](./User#stat) | [UserStatQuery](User#userstatquery) | [Struct](User#struct) |
| [**find**](./User#find) | [FindUserQuery](User#finduserquery) | [FindUsersInfo](User#findusersinfo) |
| [**sync**](./User#sync) | [UserRequest](User#userrequest) | [UserInfo](User#userinfo) |



    
<br>

### create

You can create user.



> **POST** /identity/v1/user/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateUserRequest](./User#createuserrequest)

* **user_id** (string)   `Required` 


* **backend** (UserBackend)   `Required` 


* **domain_id** (string)   `Required` 


* **password** (string)  

  *When backend is LOCAL, password is required.*


* **name** (string)  


* **email** (string)  


* **user_type** (UserType)  


* **language** (string)  


* **timezone** (string)  


* **tags** (Struct)  


* **reset_password** (bool)  

  *If reset_password is true, send email*





{{< highlight json >}}
{}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Update user info by given user_id



> **POST** /identity/v1/user/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateUserRequest](./User#updateuserrequest)

* **user_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **password** (string)  


* **name** (string)  


* **email** (string)  


* **language** (string)  


* **timezone** (string)  


* **tags** (Struct)  


* **reset_password** (bool)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### verify_email





> **POST** /identity/v1/user/verify-email
>






    
<br>

### confirm_email





> **POST** /identity/v1/user/confirm-email
>





 {{< tabs " confirm_email " >}}



 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### reset_password

+noauth



> **POST** /identity/v1/user/reset-password
>






    
<br>

### set_required_actions





> **POST** /identity/v1/user/set-required-actions
>





 {{< tabs " set_required_actions " >}}



 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable_mfa

Enable MFA for user. If this api is called, send email to user.



> **POST** /identity/v1/user/enable-mfa
>





 {{< tabs " enable_mfa " >}}

 {{< tab "Request Example" >}}



[EnableMFARequest](./User#enablemfarequest)

* **user_id** (string)   `Required` 


* **mfa_type** (string)   `Required` 

  *EMAIL*


* **options** (Struct)   `Required` 

  *If mfa_type is EMAIL, email is required in options.*


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com",
 "mfa_type": "EMAIL",
 "options": {"email": "wonny@cloudforet.com"},
 "domain_id": "domain-xxxxxxxxxxxx"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable_mfa

Disable MFA for user. If this api is called, send email to user.



> **POST** /identity/v1/user/disable-mfa
>





 {{< tabs " disable_mfa " >}}

 {{< tab "Request Example" >}}



[DisableMFARequest](./User#disablemfarequest)

* **user_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **force** (bool)  

  *If this value true, disable MFA without verification for user.*





{{< highlight json >}}
{
 "user_id": "example@cloudforet",
 "force": false,
 "domain_id": "domain-xxxxxxxxxxxx"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### confirm_mfa

Confirm MFA for user by given verify_code which is sent by your authentication method.



> **POST** /identity/v1/user/confirm-mfa
>





 {{< tabs " confirm_mfa " >}}

 {{< tab "Request Example" >}}



[ConfirmMFARequest](./User#confirmmfarequest)

* **user_id** (string)   `Required` 


* **verify_code** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet",
 "verify_code": "123456",
 "domain_id": "domain-xxxxxxxxxxxx"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable





> **POST** /identity/v1/user/enable
>





 {{< tabs " enable " >}}



 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable





> **POST** /identity/v1/user/disable
>





 {{< tabs " disable " >}}



 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v1/user/delete
>






    
<br>

### get





> **POST** /identity/v1/user/get
>





 {{< tabs " get " >}}



 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
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





> **POST** /identity/v1/user/find
>






    
<br>

### sync





> **POST** /identity/v1/user/sync
>





 {{< tabs " sync " >}}



 {{< tab "Response Example" >}}

[UserInfo](#USERINFO)
* **user_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **email** (string)   `Required` 

* **user_type** (UserType)   `Required` 

* **backend** (UserBackend)   `Required` 

* **language** (string)   `Required` 

* **timezone** (string)   `Required` 

* **required_actions** (UserRequiredAction)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **last_accessed_at** (string)   `Required` 

* **created_at** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **email_verified** (bool)   `Required` 

* **mfa** (Struct)   `Required` 



{{< highlight json >}}
{
   "user_id": "dkang@mz.co.kr",
   "name": "Dong Yoo kang",
   "state": "ENABLED",
   "email": "dkang@mz.co.kr",
   "email_verified" : true,
   "mfa": {
      "mfa_type": "EMAIL",
      "state" : "ENABLED",
      "options": {
         "email": "example@cloudforet.com"
      }
   },
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### ConfirmEmailRequest
* **user_id** (string)   `Required` 

    
* **verify_code** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ConfirmMFARequest
* **user_id** (string)   `Required` 

    
* **verify_code** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CreateUserRequest
* **user_id** (string)   `Required` 

    
* **backend** (UserBackend)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **password** (string)  

  *When backend is LOCAL, password is required.*

    
* **name** (string)  

    
* **email** (string)  

    
* **user_type** (UserType)  

    
* **language** (string)  

    
* **timezone** (string)  

    
* **tags** (Struct)  

    
* **reset_password** (bool)  

  *If reset_password is true, send email*

    <br>

### DisableMFARequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **force** (bool)  

  *If this value true, disable MFA without verification for user.*

    <br>

### EnableMFARequest
* **user_id** (string)   `Required` 

    
* **mfa_type** (string)   `Required` 

  *EMAIL*

    
* **options** (Struct)   `Required` 

  *If mfa_type is EMAIL, email is required in options.*

    
* **domain_id** (string)   `Required` 

    <br>

### FindUserInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **email** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    <br>

### FindUserQuery
* **search** (FindUserSearch)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### FindUserSearch
* **user_id** (string)   `Required` 

    
* **keyword** (string)   `Required` 

    <br>

### FindUsersInfo
* **results** (FindUserInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetUserRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### SetRequiredActionsRequest
* **user_id** (string)   `Required` 

    
* **actions** (UserRequiredAction)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateUserRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
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

    
* **user_type** (UserType)   `Required` 

    
* **backend** (UserBackend)   `Required` 

    
* **language** (string)   `Required` 

    
* **timezone** (string)   `Required` 

    
* **required_actions** (UserRequiredAction)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **email_verified** (bool)   `Required` 

    
* **mfa** (Struct)   `Required` 

    <br>

### UserQuery
* **query** (Query)  

    
* **user_id** (string)  

    
* **name** (string)  

    
* **state** (string)  

    
* **email** (string)  

    
* **user_type** (UserType)  

    
* **backend** (UserBackend)  

    
* **domain_id** (string)  

    <br>

### UserRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UserStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UsersInfo
* **results** (UserInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### VerifyEmailRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **email** (string)  

    
* **force** (bool)  

    <br>
