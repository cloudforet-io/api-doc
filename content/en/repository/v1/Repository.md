---
title: "Repository"
linkTitle: "Repository"
weight: 3
bookFlatSection: true
---
# [Repository](#Repository)
A Repository is a repository storing data of deployable plugins.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Repository





**Repository Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./Repository#register) | [CreateRepositoryRequest](Repository#createrepositoryrequest) | [RepositoryInfo](Repository#repositoryinfo) |
| [**update**](./Repository#update) | [UpdateRepositoryRequest](Repository#updaterepositoryrequest) | [RepositoryInfo](Repository#repositoryinfo) |
| [**deregister**](./Repository#deregister) | [RepositoryRequest](Repository#repositoryrequest) | [Empty](Repository#empty) |
| [**get**](./Repository#get) | [GetRepositoryRequest](Repository#getrepositoryrequest) | [RepositoryInfo](Repository#repositoryinfo) |
| [**list**](./Repository#list) | [RepositoryQuery](Repository#repositoryquery) | [RepositoriesInfo](Repository#repositoriesinfo) |
| [**stat**](./Repository#stat) | [RepositoryStatQuery](Repository#repositorystatquery) | [Struct](Repository#struct) |



    
<br>

### register

Registers a Repository. The parameter `name` can only include alphabets, numbers, and hyphens(-). The parameter `repository_type` can be either `local` or `remote`. The parameter `endpoint` is needed if the `repository_type` is `remote`.



> **POST** /repository/v1/repository/register
>





 {{< tabs " register " >}}

 {{< tab "Request Example" >}}



[CreateRepositoryRequest](./Repository#createrepositoryrequest)

* **name** (string)   `Required` 


* **repository_type** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **endpoint** (string)  





{{< highlight json >}}
{
   "name": "Open Source Marketplace",
   "repository_type": "remote",
   "endpoint": "grpc+ssl://repository.portal.spaceone.megazone.io:443"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RepositoryInfo](#REPOSITORYINFO)
* **repository_id** (string)   `Required` 

* **name** (string)   `Required` 

* **repository_type** (string)   `Required` 

* **endpoint** (string)   `Required` 

* **version** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "repository_id": "repo-123456789012",
   "name": "Open Source Marketplace",
   "repository_type": "remote",
   "endpoint": "grpc+ssl://repository.portal.spaceone.megazone.io:443",
   "created_at": "2022-01-01T02:27:02.924Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Repository registered. You must specify the `repository_id` of the Repository to update. You can make changes in Repository settings, including `name`.



> **POST** /repository/v1/repository/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateRepositoryRequest](./Repository#updaterepositoryrequest)

* **repository_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  





{{< highlight json >}}
{
   "repository_id": "repo-123456789012",
   "name": "Changed Name"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RepositoryInfo](#REPOSITORYINFO)
* **repository_id** (string)   `Required` 

* **name** (string)   `Required` 

* **repository_type** (string)   `Required` 

* **endpoint** (string)   `Required` 

* **version** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "repository_id": "repo-123456789012",
   "name": "Open Source Marketplace",
   "repository_type": "remote",
   "endpoint": "grpc+ssl://repository.portal.spaceone.megazone.io:443",
   "created_at": "2022-01-01T02:27:02.924Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### deregister

Deregisters and deletes a specific Repository. You must specify the `repository_id` of the Repository to deregister.



> **POST** /repository/v1/repository/deregister
>





 {{< tabs " deregister " >}}

 {{< tab "Request Example" >}}



[RepositoryRequest](./Repository#repositoryrequest)

* **repository_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Repository. Prints detailed information about the Repository, including  `name`, `repository_type`, and `endpoint`.



> **POST** /repository/v1/repository/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetRepositoryRequest](./Repository#getrepositoryrequest)

* **repository_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RepositoryInfo](#REPOSITORYINFO)
* **repository_id** (string)   `Required` 

* **name** (string)   `Required` 

* **repository_type** (string)   `Required` 

* **endpoint** (string)   `Required` 

* **version** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "repository_id": "repo-123456789012",
   "name": "Open Source Marketplace",
   "repository_type": "remote",
   "endpoint": "grpc+ssl://repository.portal.spaceone.megazone.io:443",
   "created_at": "2022-01-01T02:27:02.924Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Repositories regardless of `domain`. You can use a query to get a filtered list of Repositories.



> **POST** /repository/v1/repository/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[RepositoryQuery](./Repository#repositoryquery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **repository_id** (string)  


* **name** (string)  


* **repository_type** (string)  





{{< highlight json >}}
{
   "query": {},
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RepositoriesInfo](#REPOSITORIESINFO)
* **results** (RepositoryInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "repository_id": "repo-123456789012",
           "name": "Open Source Marketplace",
           "repository_type": "remote",
           "endpoint": "grpc+ssl://repository.portal.spaceone.megazone.io:443",
           "created_at": "2022-01-01T02:26:29.081Z"
       }
   ],
   "total_count": 1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /repository/v1/repository/stat
>






    


<br>
<br>

## Message



### CreateRepositoryRequest
* **name** (string)   `Required` 

    
* **repository_type** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **endpoint** (string)  

    <br>

### GetRepositoryRequest
* **repository_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### RepositoriesInfo
* **results** (RepositoryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### RepositoryInfo
* **repository_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **repository_type** (string)   `Required` 

    
* **endpoint** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### RepositoryQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **repository_id** (string)  

    
* **name** (string)  

    
* **repository_type** (string)  

    <br>

### RepositoryRequest
* **repository_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### RepositoryStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateRepositoryRequest
* **repository_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    <br>
