---
title: "ServiceAccount"
linkTitle: "ServiceAccount"
weight: 3
bookFlatSection: true
---
# [ServiceAccount](#ServiceAccount)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ServiceAccount





**ServiceAccount Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ServiceAccount#create) | [CreateServiceAccountRequest](ServiceAccount#createserviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**update**](./ServiceAccount#update) | [UpdateServiceAccountRequest](ServiceAccount#updateserviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**update_secret_data**](./ServiceAccount#update_secret_data) | [UpdateServiceAccountSecretRequest](ServiceAccount#updateserviceaccountsecretrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**delete_secret_data**](./ServiceAccount#delete_secret_data) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**delete**](./ServiceAccount#delete) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [Empty](ServiceAccount#empty) |
| [**get**](./ServiceAccount#get) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**list**](./ServiceAccount#list) | [ServiceAccountSearchQuery](ServiceAccount#serviceaccountsearchquery) | [ServiceAccountsInfo](ServiceAccount#serviceaccountsinfo) |
| [**stat**](./ServiceAccount#stat) | [ServiceAccountStatQuery](ServiceAccount#serviceaccountstatquery) | [Struct](ServiceAccount#struct) |



    
<br>

### create





> **POST** /identity/v2/service-account/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateServiceAccountRequest](./ServiceAccount#createserviceaccountrequest)

* **name** (string)   `Required` 


* **data** (Struct)   `Required` 


* **provider** (string)   `Required` 


* **project_id** (string)   `Required` 


* **secret_schema_id** (string)  


* **secret_data** (Struct)  


* **tags** (Struct)  


* **trusted_account_id** (string)  





{{< highlight json >}}
{
 "name": "woony-service-account",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "provider": "aws",
 "secret_schema_id": "aws-secret-access-key",
 "secret_data": {
   "aws_access_key_id": "a1b2c3d4e5f6",
   "aws_secret_access_key": "a1b2c3d4e5f6"
 },
 "project_id": "project-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ServiceAccountInfo](#SERVICEACCOUNTINFO)
* **service_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 

* **inactivated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T05:39:08.732Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "test-service-account",
 "project_id": "project-a1b2c3d4e5f6",
 "provider": "aws",
 "secret_id": "secret-a1b2c3d4e5f6",
 "secret_schema_id": "aws-secret-access-key",
 "service_account_id": "sa-a1b2c3d4e5f6",
 "state": "ACTIVE",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/service-account/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateServiceAccountRequest](./ServiceAccount#updateserviceaccountrequest)

* **service_account_id** (string)   `Required` 


* **name** (string)  


* **data** (Struct)  


* **tags** (Struct)  


* **project_id** (string)  





{{< highlight json >}}
{
 "service_account_id": "sa-a1b2c3d4e5f6",
 "project_id": "project-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ServiceAccountInfo](#SERVICEACCOUNTINFO)
* **service_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 

* **inactivated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T05:39:08.732Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "test-service-account",
 "project_id": "project-a1b2c3d4e5f6",
 "provider": "aws",
 "secret_id": "secret-a1b2c3d4e5f6",
 "secret_schema_id": "aws-secret-access-key",
 "service_account_id": "sa-a1b2c3d4e5f6",
 "state": "ACTIVE",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_secret_data





> **POST** /identity/v2/service-account/update-secret-data
>





 {{< tabs " update_secret_data " >}}

 {{< tab "Request Example" >}}



[UpdateServiceAccountSecretRequest](./ServiceAccount#updateserviceaccountsecretrequest)

* **service_account_id** (string)   `Required` 


* **secret_schema_id** (string)   `Required` 


* **secret_data** (Struct)   `Required` 


* **trusted_account_id** (string)  





{{< highlight json >}}
{
 "service_account_id": "sa-a1b2c3d4e5f6",
 "secret_schema_id": "aws-secret-access-key",
 "secret_data": {
   "aws_access_key_id": "a1b2c3d4e5f6",
   "aws_secret_access_key": "a1b2c3d4e5f6"
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ServiceAccountInfo](#SERVICEACCOUNTINFO)
* **service_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 

* **inactivated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T05:39:08.732Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "test-service-account",
 "project_id": "project-a1b2c3d4e5f6",
 "provider": "aws",
 "secret_id": "secret-a1b2c3d4e5f6",
 "secret_schema_id": "aws-secret-access-key",
 "service_account_id": "sa-a1b2c3d4e5f6",
 "state": "ACTIVE",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete_secret_data





> **POST** /identity/v2/service-account/delete-secret-data
>





 {{< tabs " delete_secret_data " >}}

 {{< tab "Request Example" >}}



[ServiceAccountRequest](./ServiceAccount#serviceaccountrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ServiceAccountInfo](#SERVICEACCOUNTINFO)
* **service_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 

* **inactivated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T05:39:08.732Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "test-service-account",
 "project_id": "project-a1b2c3d4e5f6",
 "provider": "aws",
 "secret_id": "secret-a1b2c3d4e5f6",
 "secret_schema_id": "aws-secret-access-key",
 "service_account_id": "sa-a1b2c3d4e5f6",
 "state": "ACTIVE",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/service-account/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ServiceAccountRequest](./ServiceAccount#serviceaccountrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/service-account/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[ServiceAccountRequest](./ServiceAccount#serviceaccountrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ServiceAccountInfo](#SERVICEACCOUNTINFO)
* **service_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 

* **inactivated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T05:39:08.732Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "test-service-account",
 "project_id": "project-a1b2c3d4e5f6",
 "provider": "aws",
 "secret_id": "secret-a1b2c3d4e5f6",
 "secret_schema_id": "aws-secret-access-key",
 "service_account_id": "sa-a1b2c3d4e5f6",
 "state": "ACTIVE",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/service-account/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ServiceAccountSearchQuery](./ServiceAccount#serviceaccountsearchquery)

* **query** (Query)  


* **service_account_id** (string)  


* **name** (string)  


* **state** (string)  


* **provider** (string)  


* **workspace_id** (string)  


* **project_id** (string)  


* **trusted_account_id** (string)  


* **secret_schema_id** (string)  


* **secret_id** (string)  





{{< highlight json >}}
{
 "provider": "aws",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [
     {
       "key": "created_at",
       "desc": true
     }
   ]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ServiceAccountsInfo](#SERVICEACCOUNTSINFO)
* **results** (ServiceAccountInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "created_at": "2024-11-18T06:03:09.191Z",
     "data": {
       "account_id": "a1b2c3d4e5f6"
     },
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "woony-service-account",
     "project_id": "project-a1b2c3d4e5f6",
     "provider": "aws",
     "service_account_id": "sa-a1b2c3d4e5f6",
     "state": "ACTIVE",
     "tags": {},
     "workspace_id": "workspace-a1b2c3d4e5f6"
   },
   {
     "created_at": "2024-11-18T05:48:49.783Z",
     "data": {
       "account_id": "g7h8i9j1k2l3"
     },
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "cloudforet-service-account",
     "project_id": "project-g7h8i9j1k2l3",
     "provider": "aws",
     "secret_id": "secret-g7h8i9j1k2l3",
     "secret_schema_id": "aws-secret-access-key",
     "service_account_id": "sa-g7h8i9j1k2l3",
     "state": "ACTIVE",
     "tags": {},
     "workspace_id": "workspace-g7h8i9j1k2l3"
   }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v2/service-account/stat
>






    


<br>
<br>

## Message



### CreateServiceAccountRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **secret_schema_id** (string)  

    
* **secret_data** (Struct)  

    
* **tags** (Struct)  

    
* **trusted_account_id** (string)  

    <br>

### ServiceAccountInfo
* **service_account_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **reference_id** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    
* **inactivated_at** (string)   `Required` 

    <br>

### ServiceAccountRequest
* **service_account_id** (string)   `Required` 

    <br>

### ServiceAccountSearchQuery
* **query** (Query)  

    
* **service_account_id** (string)  

    
* **name** (string)  

    
* **state** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **trusted_account_id** (string)  

    
* **secret_schema_id** (string)  

    
* **secret_id** (string)  

    <br>

### ServiceAccountStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ServiceAccountsInfo
* **results** (ServiceAccountInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateServiceAccountRequest
* **service_account_id** (string)   `Required` 

    
* **name** (string)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>

### UpdateServiceAccountSecretRequest
* **service_account_id** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **trusted_account_id** (string)  

    <br>
