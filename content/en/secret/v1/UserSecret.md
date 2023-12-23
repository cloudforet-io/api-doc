---
title: "UserSecret"
linkTitle: "UserSecret"
weight: 3
bookFlatSection: true
---
# [UserSecret](#UserSecret)
UserSecret is a service that stores and manages credentials.
UserSecret is used to store credentials for a specific user.


>  **Package : spaceone.api.user_secret.v1**

<br>
<br>

## UserSecret





**UserSecret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserSecret#create) | [CreateUserSecretRequest](UserSecret#createusersecretrequest) | [UserSecretInfo](UserSecret#usersecretinfo) |
| [**update**](./UserSecret#update) | [UpdateUserSecretRequest](UserSecret#updateusersecretrequest) | [UserSecretInfo](UserSecret#usersecretinfo) |
| [**delete**](./UserSecret#delete) | [UserSecretRequest](UserSecret#usersecretrequest) | [Empty](UserSecret#empty) |
| [**update_data**](./UserSecret#update_data) | [UpdateUserSecretDataRequest](UserSecret#updateusersecretdatarequest) | [Empty](UserSecret#empty) |
| [**get_data**](./UserSecret#get_data) | [GetUserSecretDataRequest](UserSecret#getusersecretdatarequest) | [UserSecretDataInfo](UserSecret#usersecretdatainfo) |
| [**get**](./UserSecret#get) | [UserSecretRequest](UserSecret#usersecretrequest) | [UserSecretInfo](UserSecret#usersecretinfo) |
| [**list**](./UserSecret#list) | [UserSecretQuery](UserSecret#usersecretquery) | [UserSecretsInfo](UserSecret#usersecretsinfo) |
| [**stat**](./UserSecret#stat) | [UserSecretStatQuery](UserSecret#usersecretstatquery) | [Struct](UserSecret#struct) |



    
<br>

### create

Create a new user secret.
Created user secret is encrypted and stored securely.



> **POST** /secret/v1/user-secret/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateUserSecretRequest](./UserSecret#createusersecretrequest)

* **name** (string)   `Required` 


* **data** (Struct)   `Required` 


* **schema_id** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "Cloudforet AWS Dev",
   "data": "********",
   "schema_id": "aws_access_key",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserSecretInfo](#USERSECRETINFO)
* **user_secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "user_secret_id": "user_secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema_id": "aws_access_key",
   "provider": "aws",
   "user_id": "whdalsrnt@gmail.com",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific user secret's information.
You can only change the 'name' and 'tags', and to change the data you must use the update_data API.



> **POST** /secret/v1/user-secret/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateUserSecretRequest](./UserSecret#updateusersecretrequest)

* **user_secret_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "user_secret_id": "user-secret-123456789012",
   "name": "aws-dev2",
   "tags": { "a": "b"}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserSecretInfo](#USERSECRETINFO)
* **user_secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "user_secret_id": "user_secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema_id": "aws_access_key",
   "provider": "aws",
   "user_id": "whdalsrnt@gmail.com",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific user secret.



> **POST** /secret/v1/user-secret/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[UserSecretRequest](./UserSecret#usersecretrequest)

* **user_secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "user_secret_id": "user-secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_data

Updates a specific user secret's data.
Updated user_secret is encrypted and stored securely.



> **POST** /secret/v1/user-secret/update-data
>





 {{< tabs " update_data " >}}

 {{< tab "Request Example" >}}



[UpdateUserSecretDataRequest](./UserSecret#updateusersecretdatarequest)

* **user_secret_id** (string)   `Required` 


* **schema_id** (string)   `Required` 


* **data** (Struct)   `Required` 





{{< highlight json >}}
{
   "user_secret_id": "user-secret-123456789012",
    "data": "********"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get_data

Get a specific user secret's data.
This API is for internal system use only.







 {{< tabs " get_data " >}}

 {{< tab "Request Example" >}}



[GetUserSecretDataRequest](./UserSecret#getusersecretdatarequest)

* **user_secret_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "user_secret_id": "user-secret-123456789012",
   "domain_id": "domain-12345abcde"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Get a specific user secret's information.



> **POST** /secret/v1/user-secret/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[UserSecretRequest](./UserSecret#usersecretrequest)

* **user_secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "user_secret_id": "user-secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserSecretInfo](#USERSECRETINFO)
* **user_secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "user_secret_id": "user_secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema_id": "aws_access_key",
   "provider": "aws",
   "user_id": "whdalsrnt@gmail.com",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Queries a list of user secrets.
You can use a query to get a filtered list of user secrets.



> **POST** /secret/v1/user-secret/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[UserSecretQuery](./UserSecret#usersecretquery)

* **query** (Query)  


* **user_secret_id** (string)  


* **name** (string)  


* **schema_id** (string)  


* **provider** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserSecretsInfo](#USERSECRETSINFO)
* **results** (UserSecretInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
          "user_secret_id": "user_secret-123456789012",
          "name": "aws-dev",
          "tags": {},
          "schema": "aws_access_key",
          "provider": "aws",
          "user_id": "whdalsrnt@gmail",
          "domain_id": "domain-123456789012",
          "created_at": "2022-01-01T06:10:14.851Z"
       },
       {
           "user_secret_id": "user_secret-987654321098",
           "name": "plugin-credentials",
           "tags": {},
           "user_id": "whdalsrnt@gmail.com",
           "domain_id": "domain-123456789012",
           "created_at": "2022-01-01T02:31:01.709Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /secret/v1/user-secret/stat
>






    


<br>
<br>

## Message



### CreateUserSecretRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **schema_id** (string)  

    
* **tags** (Struct)  

    <br>

### GetUserSecretDataRequest
* **user_secret_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateUserSecretDataRequest
* **user_secret_id** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### UpdateUserSecretRequest
* **user_secret_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UserSecretDataInfo
* **encrypted** (bool)   `Required` 

    
* **encrypt_options** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### UserSecretInfo
* **user_secret_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### UserSecretQuery
* **query** (Query)  

    
* **user_secret_id** (string)  

    
* **name** (string)  

    
* **schema_id** (string)  

    
* **provider** (string)  

    <br>

### UserSecretRequest
* **user_secret_id** (string)   `Required` 

    <br>

### UserSecretStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UserSecretsInfo
* **results** (UserSecretInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
